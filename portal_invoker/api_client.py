import base64
import json
import os
from base64 import b64decode, standard_b64encode
from xml.dom import minidom

import requests
from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Util import number

from .AES_Crypto import (decrypt_cipher_text_using_symmetric_key,
                         encrypt_msg_using_symmetric_key)

# global variable
site_url = None


def set_site_url(url):
    """Set server URL.

    Parameters
    ----------
    url : str, required
        The server URL

    """
    global site_url
    site_url = url


def get_site_url():
    """Get server URL.

    Returns
    -------
    str
        site url of the server
    """
    global site_url
    return site_url


def get_asymmetric_public_key_from_server():
    """Perform API call to server to get server's RSA public key.

    Returns
    -------
    dict object
        response json object containing public key from server
    """
    url = get_site_url() + "/Data/GetPublicKey"
    response = requests.post(url, data=None)
    if response.status_code == 200:
        try:
            return json.loads(response.text)
        except Exception as e:
            raise Exception("EncryptionProcessError")
    else:
        raise Exception("InternalServerError:", response.status_code)


def get_long(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
    string = ''.join(rc) 
    return number.bytes_to_long(b64decode(string))


def get_key_from_xml_string(xml_string):
    """Converts RSA public key xml string to RSA key object.

    Parameters
    ----------
    xml_string : str, required
        The rsa public key xml string
    
    Returns
    -------
    object
        RSA key object    
    """
    rsa_key_value = minidom.parseString(xml_string)
    modulus = get_long(rsa_key_value.getElementsByTagName('Modulus')[0].childNodes)
    exponent = get_long(rsa_key_value.getElementsByTagName('Exponent')[0].childNodes)
    pub_key = RSA.construct((modulus, exponent))
    return pub_key


def public_key_to_xml(pem_public_key):
    """Converts RSA public key to xml string.

    Parameters
    ----------
    pem_public_key : object, required
        The RSA public ley PEM
    
    Returns
    -------
    str
        The rsa public key xml string
        
    """
    public_key = RSA.importKey(pem_public_key)
    xml = '<RSAKeyValue>'
    xml += '<Modulus>'
    xml += str(standard_b64encode(number.long_to_bytes(public_key.n)), 'utf-8')
    xml += '</Modulus>'
    xml += '<Exponent>'
    xml += str(standard_b64encode(number.long_to_bytes(public_key.e)), 'utf-8')
    xml += '</Exponent>'
    xml += '</RSAKeyValue>'
    return xml


def generate_rsa_asymmetric_keys():
    """Generates 1024 bit RSA key object.
    
    Returns
    -------
    tuple
        RSA decoded public key,RSA key pair object
    """
    key_pair = RSA.generate(1024)
    pub_key = key_pair.publickey()
    pub_key_PEM = pub_key.exportKey()
    rsa_asymmetric_public_key = pub_key_PEM.decode('ascii')
    return rsa_asymmetric_public_key, key_pair


def combine_client_symmetric_key_client_rsa_public_key(client_symmetric_key_part, rsa_asymmetric_public_key):   
    """Combines two byte array
    
    Parameters
    ----------
    client_symmetric_key_part : byte array, required
        The client side symmetric key first part
    rsa_asymmetric_public_key : byte array, required
        The client side asymmetric public key

    Returns
    -------
    bytes
        The combination of both keys in bytes
    """     
    encoded_symmetric_key = list(client_symmetric_key_part)
    encoded_client_public_key = list(rsa_asymmetric_public_key)
    return bytes(encoded_symmetric_key + encoded_client_public_key)


def encrypt_msg_with_public_key(msg, pubkey):
    """Encrypt bytes message with RSA public key 
    
    Parameters
    ----------
    msg : bytes, required
        The message to be encrypted
    pubkey : RSA key object
        The RSA key for encryption process

    Returns
    -------
    str
        The encrypted base64 message
    """     
    encryption = PKCS1_v1_5.new(pubkey)
    encrypted_byte_array = encryption.encrypt(msg)
    return str(base64.b64encode(encrypted_byte_array), "utf-8")


def decrypt_msg_with_private_key(cipher_text, key_pair):
    """Decrypt bytes message with RSA private key 
    
    Parameters
    ----------
    cipher_text : bytes, required
        The message to be decrypted
    key_pair : RSA key object
        The RSA key for decryption process

    Returns
    -------
    list of bytes
        The decrypted symmetric key from server
    """     
    digest_size = SHA.digest_size
    sentinel = Random.new().read(16 + digest_size)      # Let's assume that average data length is 16
    cipher = PKCS1_v1_5.new(key_pair)
    message = cipher.decrypt(cipher_text, sentinel)
    return list(message)


def perform_key_exchange(call_node, key_token, combined_key_encrypted_base64):
    """Perform key exchange with server
    
    Parameters
    ----------
    call_node : str, required
        The node having answered on the step #1
    key_token : str, required
        Identification of the key returned by the server at step #1
    combined_key_encrypted_base64 : str
        Encrypted combined key
    
    Returns
    -------
    dict
        Response of key exchange API
    """     
    request_payload = {
        'key':
            {
                'CallNode': call_node,
                'KeyToken': key_token,
                'AsymetricClientPublicKeyAndClientSymetricXmlBase64': combined_key_encrypted_base64
            }
    }
    url = get_site_url() + "/Data/ExecuteKeyExchange"
    response = requests.post(url, json=request_payload)
    if response.status_code == 200:
        try:
            return json.loads(response.text)
        except Exception as e:
            raise Exception("EncryptionProcessError")
    else:
        raise Exception("InternalServerError:", response.status_code)


def make_api_call_with_encrypted_body(method_name, request_body):
    """Perfom encrypted API call with server
    
    Parameters
    ----------
    method_name : str, required
        The API name
    request_body : dict, required
        Encrypted request body
    
    Returns
    -------
    dict
       Encrypted response from server
    """     
    url = get_site_url() + "/Data/"+method_name
    response = requests.post(url, json=request_body)
    if response.status_code == 200:
        if response.text is None or response.text == '':
            return None
        else:
            try:
                return json.loads(response.text)
            except Exception as e:
                raise Exception("EncryptionProcessError")
    else:
        raise Exception("InternalServerError:", response.status_code)


def call_tib_api(method_name, api_request_body):
    """Perform encryption and decryption of request body and response.

    Parameters
    ----------
    method_name : str, required
        The method name for which encryption is to be done
    
    api_request_body : dict, required
        Request body for the method API

    Returns
    -------
    dict object
        Decrypted response from the API in json format
    
    Raises
    ------
    InvalidSiteURLError
        If server is not set then it will throw an Error
    
    EncryptionProcessError In encryption there are some issues with padding or data length is incorrect for
    encryption then server will refuse the API request and this error will be raised
    
    InternalServerError
        Error in API call from server
    """
    # check if server URL is set or not
    if get_site_url() is None:
        raise Exception("InvalidSiteURLError")

    # 1) Request asymmetric key.
    get_public_key_api_response = get_asymmetric_public_key_from_server()
    server_public_key_xml_string = get_public_key_api_response.get('PublicKeyXmlString')
    node_answered = get_public_key_api_response.get('NodeAnswered')
    key_token = get_public_key_api_response.get('KeyToken')
    
    # - public key is in xml string that need to converted to rsa key object
    server_public_key = get_key_from_xml_string(server_public_key_xml_string)
    
    # 2) Generate the client-side 16 bytes symmetric key.
    client_symmetric_key_part = bytearray(os.urandom(16))

    # 3) Generate the client-side RSA asymmetric key.
    rsa_asymmetric_public_key, key_pair = generate_rsa_asymmetric_keys()
    pub_key = key_pair.publickey()
    pub_key_PEM = pub_key.exportKey()
    # - public key needs to be converted to xml string
    rsa_asymmetric_public_key = public_key_to_xml(pub_key_PEM)
    # - then xml string to bytes array
    rsa_asymmetric_public_key = bytes(rsa_asymmetric_public_key, 'utf-8')
    
    # 4) Combines client-side symmetric key and asymmetric key.
    combined_client_symmetric_key_client_public_key = combine_client_symmetric_key_client_rsa_public_key(
        client_symmetric_key_part, rsa_asymmetric_public_key)

    # 5) Encrypt the combined keys.
    combined_key_encrypted_base64 = encrypt_msg_with_public_key(combined_client_symmetric_key_client_public_key,
                                                                server_public_key)

    # 6) Transmit the key to the server.
    key_exchange_api_response = perform_key_exchange(node_answered, key_token, combined_key_encrypted_base64)
    full_symmetric_key_token = key_exchange_api_response.get('FullSymetricKeyToken')
    symmetric_host_half_key = key_exchange_api_response.get('SymetricHostHalfKey')

    # 7) Decrypt the server-side received key.
    # -  first decode it from base64 then to byte array
    symmetric_host_half_key = base64.b64decode(symmetric_host_half_key)
    decoded_symmetric_host_half_key = bytes(symmetric_host_half_key)

    # - decrypt data with client side RSA key
    decrypted_server_side_generated_symmetric_key = decrypt_msg_with_private_key(decoded_symmetric_host_half_key,
                                                                                 key_pair)
    
    # 8) Combine symmetric keys.
    combined_symmetric_keys = list(client_symmetric_key_part) + decrypted_server_side_generated_symmetric_key
    combined_symmetric_keys = bytes(combined_symmetric_keys)
    
    # 9) Perform the desired call.
    # -  Encrypt the request payload using full symmetric key 
    base64_iv, base64_cipher_text = encrypt_msg_using_symmetric_key(combined_symmetric_keys, api_request_body)

    # - Prepared Encrypted request body
    encrypted_request_body = {
        "data": {
            "CallNode": node_answered,
            "KeyToken": full_symmetric_key_token,
            "Base64IV": base64_iv,
            "Base64CryptedData": base64_cipher_text
        }
    }
    api_response_encrypted = make_api_call_with_encrypted_body(method_name, encrypted_request_body)

    if api_response_encrypted is not None:
        # 10) Decrypt the returned result from the server.
        encrypted_base64_data = api_response_encrypted.get('CryptedBase64Data')
        encrypted_base64_data = base64.b64decode(encrypted_base64_data)
        iv = api_response_encrypted.get('IV')
        iv = bytes(iv)
        
        decrypted_response = decrypt_cipher_text_using_symmetric_key(combined_symmetric_keys, iv, encrypted_base64_data)
        return decrypted_response
    else:
        return None

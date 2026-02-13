from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64
import os
import json

import re
import itertools
import sys

all_chars = (chr(i) for i in range(sys.maxunicode))
categories = {'Cc'}
control_chars = ''.join(map(chr, itertools.chain(range(0x00, 0x20), range(0x7f, 0xa0))))

control_char_re = re.compile('[%s]' % re.escape(control_chars))


def remove_control_chars(s):
    return control_char_re.sub('', s)


def encrypt_msg_using_symmetric_key(key, msg):
    """Encrypt text using AES algorithm  with padding
    
    Parameters
    ----------
    key : bytes, required
        The symmetric key for AES
    msg : dict, required
        Request payload which needs to be encrypted
    
    Returns
    -------
    tuple
       IV (initialization vector, which is a 16-byte value) base64 encoded , cipher text base64 encoded 
    """     
    iv = os.urandom(16)
    aes_enc = AES.new(key, AES.MODE_CBC, iv)
    msg = json.dumps(msg).encode('utf8')
    cipher_text = aes_enc.encrypt(pad(msg, AES.block_size))
    base64_iv = base64.b64encode(bytes(iv)).decode("utf-8") 
    base64_cipher_text = base64.b64encode(bytes(cipher_text)).decode("utf-8") 
    return base64_iv, base64_cipher_text


def decrypt_cipher_text_using_symmetric_key(key, iv, cipher_text):
    """Decrypt text using AES algorithm 
    
    Parameters
    ----------
    key : bytes, required
        The symmetric key for AES
    iv : bytes, required
        Initialization vector used for encryption
    cipher_text : bytes, required
        Cipher text which needs to be decrypted
    
    Returns
    -------
    dict
       Decrypted API response in json
    """     
    aes_dec = AES.new(key, AES.MODE_CBC, iv)
    message = aes_dec.decrypt(cipher_text)
    message = str(message.decode('utf-8'))
    # after decryption there are some unprintable chars in the message , need to remove that
    message = remove_control_chars(message)
    return json.loads(message)

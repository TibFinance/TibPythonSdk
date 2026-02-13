

from .api_client import call_tib_api, set_site_url
from .method_documentation import METHOD_DOC
from .utility import *
from .responses import *


class Portal:
    

    @staticmethod
    def createSession(createSessionArgs):
        """
            The CreateSession function is purposed to establish a fresh session, thereby ensuring a secure and distinct environment for user activities.
            Parameters
            ----------
            createSessionArgs : CreateSessionArgs, required

            Returns
            -------
            CreateSessionResponse : CreateSessionResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(createSessionArgs)
        api_response = call_tib_api(method_name='CreateSession', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = CreateSessionResponse(api_response)
        return api_response

    @staticmethod
    def listServices(listServicesArgs):
        """
            Retrieves the full list of services that are available to the authenticated client.
            Parameters
            ----------
            listServicesArgs : ListServicesArgs, required

            Returns
            -------
            ListServicesResponse : ListServicesResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(listServicesArgs)
        api_response = call_tib_api(method_name='ListServices', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = ListServicesResponse(api_response)
        return api_response

    @staticmethod
    def getService(getServiceArgs):
        """
            Retrieves the details of a specified service within the TIB Finance API. This function is essential for accessing service-related information, which is crucial for managing contracts and determining applicable limits and fees.
            Parameters
            ----------
            getServiceArgs : GetServiceArgs, required

            Returns
            -------
            GetServiceResponse : GetServiceResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(getServiceArgs)
        api_response = call_tib_api(method_name='GetService', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = GetServiceResponse(api_response)
        return api_response

    @staticmethod
    def getWalletInformationsByService(getWalletInformationsArgs):
        """
            Gets the service.
            Parameters
            ----------
            getWalletInformationsArgs : GetWalletInformationsArgs, required

            Returns
            -------
            GetWalletInformationsResponse : GetWalletInformationsResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(getWalletInformationsArgs)
        api_response = call_tib_api(method_name='GetWalletInformationsByService', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = GetWalletInformationsResponse(api_response)
        return api_response

    @staticmethod
    def listMerchants(listMerchantsArgs):
        """
            Retrieves a list of all merchants associated with the client's account. This function is essential for managing and accessing merchant-specific data within the API.
            Parameters
            ----------
            listMerchantsArgs : ListMerchantsArgs, required

            Returns
            -------
            ListMerchantsResponse : ListMerchantsResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(listMerchantsArgs)
        api_response = call_tib_api(method_name='ListMerchants', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = ListMerchantsResponse(api_response)
        return api_response

    @staticmethod
    def getServiceBoardingStatus(getServiceBoardingStatusArgs):
        """
            Retrieves a list of merchants who have completed the boarding process. This function is essential for monitoring and managing merchant onboarding statuses within the system.
            Parameters
            ----------
            getServiceBoardingStatusArgs : GetServiceBoardingStatusArgs, required

            Returns
            -------
            GetServiceBoardingStatusResponse : GetServiceBoardingStatusResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(getServiceBoardingStatusArgs)
        api_response = call_tib_api(method_name='GetServiceBoardingStatus', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = GetServiceBoardingStatusResponse(api_response)
        return api_response

    @staticmethod
    def createMerchant(createMerchantArgs):
        """
            Initiates the creation of a new merchant account within the TIB Finance system. This function is essential for setting up a merchant's basic and account information, which is a prerequisite for conducting transactions.
            Parameters
            ----------
            createMerchantArgs : CreateMerchantArgs, required

            Returns
            -------
            CreateMerchantResponse : CreateMerchantResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(createMerchantArgs)
        api_response = call_tib_api(method_name='CreateMerchant', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = CreateMerchantResponse(api_response)
        return api_response

    @staticmethod
    def getMerchant(getMerchantArgs):
        """
            Retrieves detailed information about a specific merchant using the provided merchant ID. This function is essential for accessing the merchant's basic and account information necessary for transaction processing.
            Parameters
            ----------
            getMerchantArgs : GetMerchantArgs, required

            Returns
            -------
            GetMerchantResponse : GetMerchantResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(getMerchantArgs)
        api_response = call_tib_api(method_name='GetMerchant', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = GetMerchantResponse(api_response)
        return api_response

    @staticmethod
    def saveMerchant(saveMerchantArgs):
        """
            Persists a merchant entity to the TIB Finance system.
            Parameters
            ----------
            saveMerchantArgs : SaveMerchantArgs, required

            Returns
            -------
            SaveMerchantResponse : SaveMerchantResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(saveMerchantArgs)
        api_response = call_tib_api(method_name='SaveMerchant', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = SaveMerchantResponse(api_response)
        return api_response

    @staticmethod
    def saveMerchantBasicInfo(saveMerchantBasicInfoArgs):
        """
            This function saves the basic information of a merchant. It is used to update or create the initial details associated with a merchant account within the TIB Finance API system.
            Parameters
            ----------
            saveMerchantBasicInfoArgs : SaveMerchantBasicInfoArgs, required

            Returns
            -------
            SaveMerchantResponse : SaveMerchantResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(saveMerchantBasicInfoArgs)
        api_response = call_tib_api(method_name='SaveMerchantBasicInfo', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = SaveMerchantResponse(api_response)
        return api_response

    @staticmethod
    def saveMerchantAccountInfo(saveMerchantAccountInfoArgs):
        """
            Stores the merchant's account details securely in the system.
            Parameters
            ----------
            saveMerchantAccountInfoArgs : SaveMerchantAccountInfoArgs, required

            Returns
            -------
            SaveMerchantResponse : SaveMerchantResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(saveMerchantAccountInfoArgs)
        api_response = call_tib_api(method_name='SaveMerchantAccountInfo', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = SaveMerchantResponse(api_response)
        return api_response

    @staticmethod
    def deleteMerchant(deleteMerchantArgs):
        """
            Removes a specified merchant from the system. This operation is irreversible and will permanently delete the merchant's data, including all associated accounts and transactions.
            Parameters
            ----------
            deleteMerchantArgs : DeleteMerchantArgs, required

            Returns
            -------
            DeleteMerchantResponse : DeleteMerchantResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(deleteMerchantArgs)
        api_response = call_tib_api(method_name='DeleteMerchant', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = DeleteMerchantResponse(api_response)
        return api_response

    @staticmethod
    def getMerchantsByExternalId(getMerchantsByExternalIdArgs):
        """
            Retrieves merchant information using an external identifier. This function is essential for accessing merchant details that are linked to a specific external ID, facilitating seamless integration with external systems.
            Parameters
            ----------
            getMerchantsByExternalIdArgs : GetMerchantsByExternalIdArgs, required

            Returns
            -------
            GetMerchantsByExternalIdResponse : GetMerchantsByExternalIdResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(getMerchantsByExternalIdArgs)
        api_response = call_tib_api(method_name='GetMerchantsByExternalId', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = GetMerchantsByExternalIdResponse(api_response)
        return api_response

    @staticmethod
    def adjustWallet(adjustWalletArgs):
        """
            Retrieves a list of customers associated with a merchant account.
            Parameters
            ----------
            adjustWalletArgs : AdjustWalletArgs, required

            Returns
            -------
            AdjustWalletResponse : AdjustWalletResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(adjustWalletArgs)
        api_response = call_tib_api(method_name='AdjustWallet', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = AdjustWalletResponse(api_response)
        return api_response

    @staticmethod
    def listCustomers(listCustomersArgs):
        """
            Generates a comprehensive list of all customers based on specified criteria, providing a complete overview of the customer base.
            Parameters
            ----------
            listCustomersArgs : ListCustomersArgs, required

            Returns
            -------
            ListCustomersResponse : ListCustomersResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(listCustomersArgs)
        api_response = call_tib_api(method_name='ListCustomers', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = ListCustomersResponse(api_response)
        return api_response

    @staticmethod
    def createCustomer(createCustomerArgs):
        """
            Creates a new customer entity within the system. This function initializes a customer object, which serves as a container for identifying the individual and associating payment methods.
            Parameters
            ----------
            createCustomerArgs : CreateCustomerArgs, required

            Returns
            -------
            CreateCustomerResponse : CreateCustomerResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(createCustomerArgs)
        api_response = call_tib_api(method_name='CreateCustomer', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = CreateCustomerResponse(api_response)
        return api_response

    @staticmethod
    def getCustomer(getCustomerArgs):
        """
            Retrieves detailed information about a specific customer based on the provided customer identifier. This function is essential for accessing customer data necessary for transaction processing and account management.
            Parameters
            ----------
            getCustomerArgs : GetCustomerArgs, required

            Returns
            -------
            GetCustomerResponse : GetCustomerResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(getCustomerArgs)
        api_response = call_tib_api(method_name='GetCustomer', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = GetCustomerResponse(api_response)
        return api_response

    @staticmethod
    def saveCustomer(saveCustomerArgs):
        """
            Persists the customer data to the database, ensuring that all necessary customer information is stored for future transactions.
            Parameters
            ----------
            saveCustomerArgs : SaveCustomerArgs, required

            Returns
            -------
            SaveCustomerResponse : SaveCustomerResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(saveCustomerArgs)
        api_response = call_tib_api(method_name='SaveCustomer', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = SaveCustomerResponse(api_response)
        return api_response

    @staticmethod
    def deleteCustomer(deleteCustomerArgs):
        """
            Removes a customer from the system based on the provided customer ID. This operation is irreversible and ensures that all associated data with the customer is permanently deleted.
            Parameters
            ----------
            deleteCustomerArgs : DeleteCustomerArgs, required

            Returns
            -------
            DeleteCustomerResponse : DeleteCustomerResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(deleteCustomerArgs)
        api_response = call_tib_api(method_name='DeleteCustomer', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = DeleteCustomerResponse(api_response)
        return api_response

    @staticmethod
    def getCustomersByExternalId(getCustomersByExternalIdArgs):
        """
            Retrieves customer information using an external identifier. This function is essential for accessing customer data linked to a specific external ID, which is useful for integration with external systems.
            Parameters
            ----------
            getCustomersByExternalIdArgs : GetCustomersByExternalIdArgs, required

            Returns
            -------
            GetCustomersByExternalIdResponse : GetCustomersByExternalIdResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(getCustomersByExternalIdArgs)
        api_response = call_tib_api(method_name='GetCustomersByExternalId', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = GetCustomersByExternalIdResponse(api_response)
        return api_response

    @staticmethod
    def listPaymentMethods(listPaymentMethodsArgs):
        """
            Retrieves a list of available payment methods associated with a customer. This function is essential for accessing and managing the various financial accounts linked to a customer, such as credit cards, bank accounts, and Interac. It is particularly useful for applications that need to display or process customer payment options.
            Parameters
            ----------
            listPaymentMethodsArgs : ListPaymentMethodsArgs, required

            Returns
            -------
            ListPaymentMethodsResponse : ListPaymentMethodsResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(listPaymentMethodsArgs)
        api_response = call_tib_api(method_name='ListPaymentMethods', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = ListPaymentMethodsResponse(api_response)
        return api_response

    @staticmethod
    def createCreditCardPaymentMethod(createCreditCardPaymentMethodArgs):
        """
            Initializes a new credit card payment method for a customer. This function is essential for enabling transactions using a customer's credit card within the TIB Finance API. It securely stores the credit card details and associates them with the customer's account.
            Parameters
            ----------
            createCreditCardPaymentMethodArgs : CreateCreditCardPaymentMethodArgs, required

            Returns
            -------
            CreateCreditCardPaymentMethodResponse : CreateCreditCardPaymentMethodResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(createCreditCardPaymentMethodArgs)
        api_response = call_tib_api(method_name='CreateCreditCardPaymentMethod', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = CreateCreditCardPaymentMethodResponse(api_response)
        return api_response

    @staticmethod
    def createDirectAccountPaymentMethod(createDirectAccountPaymentMethodArgs):
        """
            Initializes a new direct account payment method for a customer. This function facilitates the creation of a payment method linked directly to a customer's bank account, allowing for seamless transactions.
            Parameters
            ----------
            createDirectAccountPaymentMethodArgs : CreateDirectAccountPaymentMethodArgs, required

            Returns
            -------
            CreateDirectAccountPaymentMethodResponse : CreateDirectAccountPaymentMethodResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(createDirectAccountPaymentMethodArgs)
        api_response = call_tib_api(method_name='CreateDirectAccountPaymentMethod', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = CreateDirectAccountPaymentMethodResponse(api_response)
        return api_response

    @staticmethod
    def createInteracPaymentMethod(createInteracPaymentMethodArgs):
        """
            This function initializes and creates a new Interac payment method for a customer. It allows the merchant to facilitate transactions using the Interac network, which is a popular method for electronic funds transfers in Canada.
            Parameters
            ----------
            createInteracPaymentMethodArgs : CreateInteracPaymentMethodArgs, required

            Returns
            -------
            CreateInteracPaymentMethodResponse : CreateInteracPaymentMethodResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(createInteracPaymentMethodArgs)
        api_response = call_tib_api(method_name='CreateInteracPaymentMethod', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = CreateInteracPaymentMethodResponse(api_response)
        return api_response

    @staticmethod
    def getPaymentMethod(getPaymentMethodArgs):
        """
            Retrieves the details of a specific payment method associated with a customer. This function is essential for accessing payment method information, which can include credit cards, bank accounts, or Interac details.
            Parameters
            ----------
            getPaymentMethodArgs : GetPaymentMethodArgs, required

            Returns
            -------
            GetPaymentMethodResponse : GetPaymentMethodResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(getPaymentMethodArgs)
        api_response = call_tib_api(method_name='GetPaymentMethod', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = GetPaymentMethodResponse(api_response)
        return api_response

    @staticmethod
    def deletePaymentMethod(deletePaymentMethodArgs):
        """
            Removes a specified payment method from the system. This function is typically used to delete a customer's payment method that is no longer needed or valid.
            Parameters
            ----------
            deletePaymentMethodArgs : DeletePaymentMethodArgs, required

            Returns
            -------
            DeletePaymentMethodResponse : DeletePaymentMethodResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(deletePaymentMethodArgs)
        api_response = call_tib_api(method_name='DeletePaymentMethod', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = DeletePaymentMethodResponse(api_response)
        return api_response

    @staticmethod
    def setDefaultPaymentMethod(setDefaultPaymentMethodArgs):
        """
            Sets the default payment method for a customer. This function assigns a specified payment method as the primary option for transactions, ensuring that it is used by default unless another method is specified.
            Parameters
            ----------
            setDefaultPaymentMethodArgs : SetDefaultPaymentMethodArgs, required

            Returns
            -------
            SetDefaultPaymentMethodResponse : SetDefaultPaymentMethodResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(setDefaultPaymentMethodArgs)
        api_response = call_tib_api(method_name='SetDefaultPaymentMethod', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = SetDefaultPaymentMethodResponse(api_response)
        return api_response

    @staticmethod
    def listBills(listBillsArgs):
        """
            Retrieves a list of all bills associated with the client's account. This function is essential for managing and reviewing billing information within the system.
            Parameters
            ----------
            listBillsArgs : ListBillsArgs, required

            Returns
            -------
            ListBillsResponse : ListBillsResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(listBillsArgs)
        api_response = call_tib_api(method_name='ListBills', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = ListBillsResponse(api_response)
        return api_response

    @staticmethod
    def createBill(createBillArgs):
        """
            Initiates the creation of a bill within the system. This function generates a unique Bill ID, which can be used for subsequent operations related to the bill.
            Parameters
            ----------
            createBillArgs : CreateBillArgs, required

            Returns
            -------
            CreateBillResponse : CreateBillResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(createBillArgs)
        api_response = call_tib_api(method_name='CreateBill', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = CreateBillResponse(api_response)
        return api_response

    @staticmethod
    def getBill(getBillArgs):
        """
            Retrieves a bill based on the provided criteria. This function is essential for accessing detailed billing information within the API, facilitating further operations such as payment processing or bill management.
            Parameters
            ----------
            getBillArgs : GetBillArgs, required

            Returns
            -------
            GetBillResponse : GetBillResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(getBillArgs)
        api_response = call_tib_api(method_name='GetBill', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = GetBillResponse(api_response)
        return api_response

    @staticmethod
    def deleteBill(deleteBillArgs):
        """
            Removes a specified bill from the system. This operation is typically used when a bill is no longer needed or was created in error. Ensure that the bill ID is valid and corresponds to an existing bill before attempting to delete.
            Parameters
            ----------
            deleteBillArgs : DeleteBillArgs, required

            Returns
            -------
            DeleteBillResponse : DeleteBillResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(deleteBillArgs)
        api_response = call_tib_api(method_name='DeleteBill', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = DeleteBillResponse(api_response)
        return api_response

    @staticmethod
    def listTransfers(listTransfersArgs):
        """
            Retrieves a list of all transfer operations available within the system. This function provides details about each transfer, including status and associated metadata.
            Parameters
            ----------
            listTransfersArgs : ListTransfersArgs, required

            Returns
            -------
            ListTransfersResponse : ListTransfersResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(listTransfersArgs)
        api_response = call_tib_api(method_name='ListTransfers', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = ListTransfersResponse(api_response)
        return api_response

    @staticmethod
    def listTransfersFast(listTransfersFastArgs):
        """
            Lists the transfers.
            Parameters
            ----------
            listTransfersFastArgs : ListTransfersFastArgs, required

            Returns
            -------
            ListTransfersFastResponse : ListTransfersFastResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(listTransfersFastArgs)
        api_response = call_tib_api(method_name='ListTransfersFast', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = ListTransfersFastResponse(api_response)
        return api_response

    @staticmethod
    def listTransfersForBillFast(listTransfersForBillFastArgs):
        """
            Lists the transfers of a bill.
            Parameters
            ----------
            listTransfersForBillFastArgs : ListTransfersForBillFastArgs, required

            Returns
            -------
            ListTransfersFastResponse : ListTransfersFastResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(listTransfersForBillFastArgs)
        api_response = call_tib_api(method_name='ListTransfersForBillFast', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = ListTransfersFastResponse(api_response)
        return api_response

    @staticmethod
    def getRecuringTransfers(getRecuringTransfersArgs):
        """
            Retrieves a list of recurring transfer operations associated with the client's account. This function is essential for clients who need to manage or review their scheduled transfers.
            Parameters
            ----------
            getRecuringTransfersArgs : GetRecuringTransfersArgs, required

            Returns
            -------
            GetRecuringTransfersResponse : GetRecuringTransfersResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(getRecuringTransfersArgs)
        api_response = call_tib_api(method_name='GetRecuringTransfers', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = GetRecuringTransfersResponse(api_response)
        return api_response

    @staticmethod
    def deleteRecuringTransfer(deleteRecuringTransferArgs):
        """
            Deletes a recurring transfer from the system.
            Parameters
            ----------
            deleteRecuringTransferArgs : DeleteRecuringTransferArgs, required

            Returns
            -------
            DeleteRecuringTransferResponse : DeleteRecuringTransferResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(deleteRecuringTransferArgs)
        api_response = call_tib_api(method_name='DeleteRecuringTransfer', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = DeleteRecuringTransferResponse(api_response)
        return api_response

    @staticmethod
    def createPayment(createPaymentArgs):
        """
            Initiates a new payment transaction within the system. This function processes the payment details provided and returns a response indicating the success or failure of the operation.
            Parameters
            ----------
            createPaymentArgs : CreatePaymentArgs, required

            Returns
            -------
            CreatePaymentResponse : CreatePaymentResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(createPaymentArgs)
        api_response = call_tib_api(method_name='CreatePayment', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = CreatePaymentResponse(api_response)
        return api_response

    @staticmethod
    def getPayment(getPaymentArgs):
        """
            Retrieves the details of a specific payment using the provided payment identifier.
            Parameters
            ----------
            getPaymentArgs : GetPaymentArgs, required

            Returns
            -------
            GetPaymentResponse : GetPaymentResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(getPaymentArgs)
        api_response = call_tib_api(method_name='GetPayment', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = GetPaymentResponse(api_response)
        return api_response

    @staticmethod
    def deletePayment(deletePaymentArgs):
        """
            Removes a specified payment from the system. This function is essential for managing and rectifying payment records, ensuring that erroneous or obsolete payments are efficiently deleted.
            Parameters
            ----------
            deletePaymentArgs : DeletePaymentArgs, required

            Returns
            -------
            DeletePaymentResponse : DeletePaymentResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(deletePaymentArgs)
        api_response = call_tib_api(method_name='DeletePayment', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = DeletePaymentResponse(api_response)
        return api_response

    @staticmethod
    def createDirectInteracTransaction(createDirectInteracTransactionArgs):
        """
            Initiates a direct Interac transaction, enabling the transfer of funds using a recipient's email or mobile phone number. This method facilitates seamless money transfers without requiring detailed customer account information.
            Parameters
            ----------
            createDirectInteracTransactionArgs : CreateDirectInteracTransactionArgs, required

            Returns
            -------
            CreateDirectInteracTransactionResponse : CreateDirectInteracTransactionResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(createDirectInteracTransactionArgs)
        api_response = call_tib_api(method_name='CreateDirectInteracTransaction', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = CreateDirectInteracTransactionResponse(api_response)
        return api_response

    @staticmethod
    def createTransactionFromRaw(createTransactionFromRawArgs):
        """
            Initiates a transaction using raw data input. This function processes the raw transaction details to create a valid transaction entry within the system.
            Parameters
            ----------
            createTransactionFromRawArgs : CreateTransactionFromRawArgs, required

            Returns
            -------
            CreateTransactionFromRawResponse : CreateTransactionFromRawResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(createTransactionFromRawArgs)
        api_response = call_tib_api(method_name='CreateTransactionFromRaw', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = CreateTransactionFromRawResponse(api_response)
        return api_response

    @staticmethod
    def listExecutedOperations(listExecutedOperationsArgs):
        """
            Retrieves a list of operations that have been executed within the system. This function provides detailed information about each operation, allowing users to track and analyze completed transactions.
            Parameters
            ----------
            listExecutedOperationsArgs : ListExecutedOperationsArgs, required

            Returns
            -------
            ListExecutedOperationsResponse : ListExecutedOperationsResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(listExecutedOperationsArgs)
        api_response = call_tib_api(method_name='ListExecutedOperations', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = ListExecutedOperationsResponse(api_response)
        return api_response

    @staticmethod
    def forcePaymentProcess(forcePaymentProcessArgs):
        """
            Triggers the payment processing workflow for a specific payment, overriding the default automatic selection mechanism.
            Parameters
            ----------
            forcePaymentProcessArgs : ForcePaymentProcessArgs, required

            Returns
            -------
            ForcePaymentProcessResponse : ForcePaymentProcessResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(forcePaymentProcessArgs)
        api_response = call_tib_api(method_name='ForcePaymentProcess', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = ForcePaymentProcessResponse(api_response)
        return api_response

    @staticmethod
    def getDropInPublicToken(getDropInPublicTokenArgs):
        """
            Retrieves the public token necessary for initiating a drop-in session. This token is used to authenticate and authorize the session within the API framework.
            Parameters
            ----------
            getDropInPublicTokenArgs : GetDropInPublicTokenArgs, required

            Returns
            -------
            GetDropInPublicTokenResponse : GetDropInPublicTokenResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(getDropInPublicTokenArgs)
        api_response = call_tib_api(method_name='GetDropInPublicToken', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = GetDropInPublicTokenResponse(api_response)
        return api_response

    @staticmethod
    def createFreeOperation(createFreeOperationArgs):
        """
            Initiates a free operation within the TIB Finance API, allowing for transactions not directly linked to a specific bill. This function is typically used to either collect payments from a customer's payment method or deposit funds into it, with the exception of credit card deposits.
            Parameters
            ----------
            createFreeOperationArgs : CreateFreeOperationArgs, required

            Returns
            -------
            CreateFreeOperationResponse : CreateFreeOperationResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(createFreeOperationArgs)
        api_response = call_tib_api(method_name='CreateFreeOperation', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = CreateFreeOperationResponse(api_response)
        return api_response

    @staticmethod
    def createFreeOperationBatch(createFreeOperationBatchArgs):
        """
            Initiates a batch of free operations, allowing for transactions not tied to a specific bill. This function is essential for handling payments or deposits directly linked to customer payment methods.
            Parameters
            ----------
            createFreeOperationBatchArgs : CreateFreeOperationBatchArgs, required

            Returns
            -------
            CreateFreeOperationBatchResponse : CreateFreeOperationBatchResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(createFreeOperationBatchArgs)
        api_response = call_tib_api(method_name='CreateFreeOperationBatch', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = CreateFreeOperationBatchResponse(api_response)
        return api_response

    @staticmethod
    def revertTransfer(revertTransferArgs):
        """
            Reverts a previously executed transfer operation, restoring the original state of the involved accounts.
            Parameters
            ----------
            revertTransferArgs : RevertTransferArgs, required

            Returns
            -------
            RevertTransferResponse : RevertTransferResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(revertTransferArgs)
        api_response = call_tib_api(method_name='RevertTransfer', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = RevertTransferResponse(api_response)
        return api_response

    @staticmethod
    def changeInteracPaymentMethodQuestionAndAnswer(changeInteracPaymentMethodQuestionAndAnswerArgs):
        """
            Modifies the security question and answer for an Interac payment method associated with a customer account.
            Parameters
            ----------
            changeInteracPaymentMethodQuestionAndAnswerArgs : ChangeInteracPaymentMethodQuestionAndAnswerArgs, required

            Returns
            -------
            ChangeInteracPaymentMethodQuestionAndAnswerResponse : ChangeInteracPaymentMethodQuestionAndAnswerResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(changeInteracPaymentMethodQuestionAndAnswerArgs)
        api_response = call_tib_api(method_name='ChangeInteracPaymentMethodQuestionAndAnswer', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = ChangeInteracPaymentMethodQuestionAndAnswerResponse(api_response)
        return api_response

    @staticmethod
    def initBoarding(initBoardingArgs):
        """
            Initializes the boarding process for a new client within the TIB Finance API.
            Parameters
            ----------
            initBoardingArgs : InitBoardingArgs, required

            Returns
            -------
            InitBoardingResponse : InitBoardingResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(initBoardingArgs)
        api_response = call_tib_api(method_name='InitBoarding', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = InitBoardingResponse(api_response)
        return api_response

    @staticmethod
    def createSubClient(createSubClientArgs):
        """
            Creates a new sub-client within the TIB Finance system.
            Parameters
            ----------
            createSubClientArgs : CreateSubClientArgs, required

            Returns
            -------
            CreateSubClientResponse : CreateSubClientResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(createSubClientArgs)
        api_response = call_tib_api(method_name='CreateSubClient', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = CreateSubClientResponse(api_response)
        return api_response

    @staticmethod
    def resendPaymentEmail(resendPaymentEmailArgs):
        """
            Resends the payment notification email to the specified recipient.
            Parameters
            ----------
            resendPaymentEmailArgs : ResendPaymentEmailArgs, required

            Returns
            -------
            ResendPaymentEmailResponse : ResendPaymentEmailResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(resendPaymentEmailArgs)
        api_response = call_tib_api(method_name='ResendPaymentEmail', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = ResendPaymentEmailResponse(api_response)
        return api_response

    @staticmethod
    def relaunchMerchantFailedTransfer(relaunchMerchantFailedTransferArgs):
        """
            Initiates a retry process for a merchant's failed transfer operation.
            Parameters
            ----------
            relaunchMerchantFailedTransferArgs : RelaunchMerchantFailedTransferArgs, required

            Returns
            -------
            RelaunchMerchantFailedTransferResponse : RelaunchMerchantFailedTransferResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(relaunchMerchantFailedTransferArgs)
        api_response = call_tib_api(method_name='RelaunchMerchantFailedTransfer', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = RelaunchMerchantFailedTransferResponse(api_response)
        return api_response

    @staticmethod
    def createSupplierTransfer(createSupplierTransferArgs):
        """
            
            Parameters
            ----------
            createSupplierTransferArgs : CreateSupplierTransferArgs, required

            Returns
            -------
            CreateSupplierTransferResponse : CreateSupplierTransferResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(createSupplierTransferArgs)
        api_response = call_tib_api(method_name='CreateSupplierTransfer', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = CreateSupplierTransferResponse(api_response)
        return api_response

    @staticmethod
    def getSuppliers(getSuppliersArgs):
        """
            
            Parameters
            ----------
            getSuppliersArgs : GetSuppliersArgs, required

            Returns
            -------
            GetSuppliersResponse : GetSuppliersResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(getSuppliersArgs)
        api_response = call_tib_api(method_name='GetSuppliers', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = GetSuppliersResponse(api_response)
        return api_response

    @staticmethod
    def createSupplier(createSupplierArgs):
        """
            
            Parameters
            ----------
            createSupplierArgs : CreateSupplierArgs, required

            Returns
            -------
            CreateSupplierResponse : CreateSupplierResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(createSupplierArgs)
        api_response = call_tib_api(method_name='CreateSupplier', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = CreateSupplierResponse(api_response)
        return api_response

    @staticmethod
    def getWalletOperations(getWalletOperationsArgs):
        """
            
            Parameters
            ----------
            getWalletOperationsArgs : GetWalletOperationsArgs, required

            Returns
            -------
            GetWalletOperationsResponse : GetWalletOperationsResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(getWalletOperationsArgs)
        api_response = call_tib_api(method_name='GetWalletOperations', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = GetWalletOperationsResponse(api_response)
        return api_response


    @staticmethod
    def initialize_portal(site_url):
        """Set server URL.

        Parameters
        ----------
        site_url : str, required
            The server URL

        """
        set_site_url(site_url)

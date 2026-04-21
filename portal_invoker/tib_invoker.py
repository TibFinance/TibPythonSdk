

from .api_client import call_tib_api, set_site_url
from .method_documentation import METHOD_DOC
from .utility import *
from .responses import *


class Portal:
    

    @staticmethod
    def createSession(createSessionArgs):
        """
            Creates an authenticated session for a TIB Finance client.
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
            Retrieves the list of service contracts associated with the authenticated merchant.
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
            Retrieves the details of a specific Service (contract) for the authenticated client.
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
            Retrieves the wallet state for a specific service.
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
            Retrieves a list of merchant accounts accessible to the authenticated session.
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
            Retrieves the boarding status of all merchants associated with a specific service.
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
            Creates a new merchant (bank account) for the client.
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
            Retrieves the details of a merchant by its GUID.
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
            Updates or creates a merchant record in TIB Finance.
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
            Updates the basic profile data of an existing merchant.
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
            Saves or updates a merchant's bank account information.
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
            Deletes a merchant (bank account) identified by its GUID.
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
            Retrieves TIB merchant records that match a given external system identifier.
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
            Adjusts the merchant's wallet balance by the specified amount.
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
            Retrieves a list of customer objects associated with the specified merchant.
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
            Creates a new Customer object in TIB Finance.
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
            Retrieves details of a specific customer.
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
            Creates or updates a customer record in TIB Finance.
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
            Deletes a customer record from the TIB Finance system.
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
            Retrieves one or more TIB Finance customers matching a given external identifier.
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
            Retrieves all payment methods associated with a specific customer under a given merchant.
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
            Creates a new credit‑card payment method for a specified customer.
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
            Creates a bank‑account payment method linked directly to a customer.
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
            Creates an Interac payment method for a specified customer.
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
            Retrieves the details of a specific payment method.
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
            Deletes a specific payment method from a customer profile.
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
            Sets the default payment method for a specified customer.
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
            Retrieves a collection of bills created within a specified time range.
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
            Creates a new bill record in TIB Finance.
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
            Retrieves details of a specific bill.
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
            Deletes a previously created bill.
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
            Retrieves a paginated list of transfer records matching the supplied filters.
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
            Retrieves a filtered, summarized list of transfer records for a specified service.
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
            Retrieves all transfer records associated with a specific bill.
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
            Retrieves all active recurring transfers for a specified service.
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
            Deletes a recurring transfer and cancels all its future scheduled executions.
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
            Creates a payment associated with a specific bill.
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
            Gets the payment.
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
            Deletes the payment.
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
            Creates the direct Interac transaction
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
            Creates the transaction from raw.
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
            Lists the executed operations.
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
            Forces the payment process.
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
            Gets the drop in public token.
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
            Creates the free operation.
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
            Creates a batch of free operations (deposits or collections) in a single call. Validates that client onboarding (KYC) is completed before allowing free deposit operations.
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
            Reverts (cancels or reverses) a transfer. For pending gateway payments, deletes the transfer and its public token. For processed payments, creates reversal operations for each non-fee operation. Rejects transfers over $5,000 or wallet-type transfers.
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
            Updates the security question and answer on an existing Interac payment method. Creates a replacement payment method with the new credentials and deletes the old one. The answer is encrypted via the external data vault, and both question and answer are obfuscated in logs.
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
            Initializes the merchant onboarding (boarding) process for a service. Generates a public access token and returns a redirect URL to either the direct login page (if a service-level login exists) or the boarding sign-up wizard.
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
            Creates a new sub-client (child service) under the authenticated client's account. The sub-client is represented as a service entity with its own name, language, and currency.
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
            Resends the payment notification email to the customer associated with a specific payment.
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
            Relaunches (retries) a previously failed transfer for a merchant. Resets the failed payment in the database for reprocessing and sends an internal notification email with the transfer details.
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
            Creates a payment transfer from the calling merchant to a supplier. Validates both merchants, runs business rules on the sending merchant's limits, creates the transfer as a free collection, and optionally creates a bill. Notifies the supplier unless client approval is required.
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
            Retrieves the list of suppliers associated with a merchant, returning each supplier's name and identifier.
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
            Creates or registers a supplier for a merchant. If a supplier with the given email already exists, reuses that supplier; otherwise provisions a new client, service, merchant, and login. Links the supplier to the calling merchant and creates a reciprocal customer record in the supplier's service.
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
    def listSuppliers(listSuppliersArgs):
        """
            Lists suppliers linked to the specified merchant, including detailed information such as supplier name, email address, and creation date. For a lightweight name-and-ID-only list, use GetSuppliers instead.
            Parameters
            ----------
            listSuppliersArgs : ListSuppliersArgs, required

            Returns
            -------
            ListSuppliersResponse : ListSuppliersResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(listSuppliersArgs)
        api_response = call_tib_api(method_name='ListSuppliers', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = ListSuppliersResponse(api_response)
        return api_response

    @staticmethod
    def updateSupplierAlias(updateSupplierAliasArgs):
        """
            Updates the display name (alias) that the payer uses to identify a supplier. The alias is a payer-side label and does not affect the supplier's own merchant name.
            Parameters
            ----------
            updateSupplierAliasArgs : UpdateSupplierAliasArgs, required

            Returns
            -------
            UpdateSupplierAliasResponse : UpdateSupplierAliasResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(updateSupplierAliasArgs)
        api_response = call_tib_api(method_name='UpdateSupplierAlias', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = UpdateSupplierAliasResponse(api_response)
        return api_response

    @staticmethod
    def deleteSupplier(deleteSupplierArgs):
        """
            Soft-deletes a supplier link for the specified merchant. The supplier's merchant account is not affected â€” only the payer-to-supplier association is removed.
            Parameters
            ----------
            deleteSupplierArgs : DeleteSupplierArgs, required

            Returns
            -------
            DeleteSupplierResponse : DeleteSupplierResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(deleteSupplierArgs)
        api_response = call_tib_api(method_name='DeleteSupplier', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = DeleteSupplierResponse(api_response)
        return api_response

    @staticmethod
    def listSupplierTransfers(listSupplierTransfersArgs):
        """
            Lists supplier transfers initiated by the calling merchant (identified via FeeMerchantId). Returns transfers where the caller is the fee-payer, with optional datestatus filters.
            Parameters
            ----------
            listSupplierTransfersArgs : ListSupplierTransfersArgs, required

            Returns
            -------
            ListSupplierTransfersResponse : ListSupplierTransfersResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(listSupplierTransfersArgs)
        api_response = call_tib_api(method_name='ListSupplierTransfers', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = ListSupplierTransfersResponse(api_response)
        return api_response

    @staticmethod
    def getSupplierTransfer(getSupplierTransferArgs):
        """
            Retrieves a single supplier transfer by ID. Accessible to both the fee-payer and the supplier. Returns the transfer details along with the counterparty name and the caller's role.
            Parameters
            ----------
            getSupplierTransferArgs : GetSupplierTransferArgs, required

            Returns
            -------
            GetSupplierTransferResponse : GetSupplierTransferResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(getSupplierTransferArgs)
        api_response = call_tib_api(method_name='GetSupplierTransfer', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = GetSupplierTransferResponse(api_response)
        return api_response

    @staticmethod
    def listSupplierRecurringTransfers(listSupplierRecurringTransfersArgs):
        """
            Lists recurring supplier transfers initiated by the calling merchant. Returns recurring transfer configurations where the caller is the fee-payer.
            Parameters
            ----------
            listSupplierRecurringTransfersArgs : ListSupplierRecurringTransfersArgs, required

            Returns
            -------
            ListSupplierRecurringTransfersResponse : ListSupplierRecurringTransfersResponse

            Raises ------ InvalidSiteURLError If server is not set then it will throw an Error EncryptionProcessError In
            encryption there are some issues with padding or data length is incorrect for encryption then server will
            refuse the API request and this error will be raised
        
            InternalServerError
                Error in API call from server
        """
        api_request_body = object2dict(listSupplierRecurringTransfersArgs)
        api_response = call_tib_api(method_name='ListSupplierRecurringTransfers', api_request_body=api_request_body)
        if api_response is not None:
            api_response = dict2obj(api_response)
            api_response = ListSupplierRecurringTransfersResponse(api_response)
        return api_response

    @staticmethod
    def getWalletOperations(getWalletOperationsArgs):
        """
            Retrieves wallet operation history for a service within a specified date range. Returns the list of daily operations, the wallet balance as of the start date, and the configured delay buffer amount.
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

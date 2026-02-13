METHOD_DOC = {
    'CreateSession':
        """
            API call to the server.
            Parameters
            ----------
            api_request_body : dict, required
                The API request payload 
                Call Example:
                {
                    ClientId: "0651af61-ae9e-41a7-898e-8ec775c6f8a1",
                    Username: "User",
                    Password: "Password"
                }

            Returns
            -------
            dict
                The server's response for the API
                Response example
                {
                    SessionId: "46a84f3f-c4fb-4d00-b3ff-caf6c85d06d4"
                }
        """
    ,
    'ListCustomers': """
            API call to the server.
            Parameters
            ----------
            api_request_body : dict, required
                The API request payload 
                Call Example:
                {
                    SessionToken: "0651af61-ae9e-41a7-898e-8ec775c6f8a1",
                    ServiceId: "862b96b1-85d4-406f-b55c-8f48f895f68e"
                }

            Returns
            -------
            dict
                The server's response for the API
                Response example
                Customers: [{
                    CustomerId: "05880372-5c30-4f17-8796-c353bfaece3f",
                    CustomerName: "Jackie Tester",
                    CustomerExternalId: "c123-55",
                    Language: 1,
                    CustomerDescription: "VIP Customer",
                    PaymentMethods: []
                    },{
                    CustomerId: "0d38bce8-b4d1-445b-acf1-a921ab0eee4c",
                    CustomerName: "Jackie Tester2",
                    CustomerExternalId: "c123-56",
                    Language: 1,
                    CustomerDescription: "VIP Customer",
                    PaymentMethods: []
                }]
        """
    ,
    'CreateCustomer': """
            API call to the server.
            Parameters
            ----------
            api_request_body : dict, required
                The API request payload 
                Call Example
                {
                    SessionToken: "0651af61-ae9e-41a7-898e-8ec775c6f8a1",
                    ServiceId: "862b96b1-85d4-406f-b55c-8f48f895f68e",
                    CustomerInfo: {
                    CustomerName: "Jackie Tester",
                    CustomerExternalId: "c123-55",
                    Language: 1,
                    CustomerDescription: "VIP Customer"}
                }

            Returns
            -------
            dict
                The server's response for the API
                Response example
                {
                    CustomerId: "46a84f3f-c4fb-4d00-b3ff-caf6c85d06d4"
                }
        """
    ,
    'GetCustomer': """
            API call to the server.
            Parameters
            ----------
            api_request_body : dict, required
                The API request payload 
                Call Example:
                {
                    SessionToken: "0651af61-ae9e-41a7-898e-8ec775c6f8a1",
                    CustomerId: "05880372-5c30-4f17-8796-c353bfaece3f",
                }

            Returns
            -------
            dict
                The server's response for the API
                Response example
                Customer: {CustomerId: "05880372-5c30-4f17-8796-c353bfaece3f",
                    CustomerName: "Jackie Tester",
                    CustomerExternalId: "c123-55",
                    Language: 1,
                    CustomerDescription: "VIP Customer",
                    PaymentMethods: [{
                    PaymentMethodId: "b96d8827-5e57-4698-ab57-5601a9b973a2",
                    IsCustomerAutomaticPaymentMethod: false,
                    PaymentMethodType: 3,
                    PaymentMethodDescription: "Compete principal",
                    AccountPreview: "***-*****-***1234"}]
                }
        """
    ,
    'SaveCustomer': """
            API call to the server.
            Parameters
            ----------
            api_request_body : dict, required
                The API request payload 
                Call Example:
                {
                    SessionToken: "0651af61-ae9e-41a7-898e-8ec775c6f8a1",
                    ServiceId: "862b96b1-85d4-406f-b55c-8f48f895f68e",
                    CustomerInfo: {
                        CustomerId: "05880372-5c30-4f17-8796-c353bfaece3f",
                        CustomerName: "Jackie Tester",
                        CustomerExternalId: "c123-55",
                        Language: 1,
                        CustomerDescription: "VIP Customer"
                    }
                }
        """
    ,
    'DeleteCustomer': """
            API call to the server.
            Parameters
            ----------
            api_request_body : dict, required
                The API request payload 
                Call Example:
                {
                    SessionToken: "0651af61-ae9e-41a7-898e-8ec775c6f8a1",
                    CustomerId: "05880372-5c30-4f17-8796-c353bfaece3f",
                }
        """
    ,
    'ListBills': """
            API call to the server.
            Parameters
            ----------
            api_request_body : dict, required
                The API request payload 
                Call Example:
                {
                    SessionToken: "86ee144e-9c27-4039-aa1f-43be0042aecf",
                    ServiceId: "ae18de50-74c0-4fac-bee1-fbda4c6b8355",
                    MerchantId: "122c2650-6418-469a-a2ce-4fdc02c601ac ",
                    FromDateTime: "2021-02-16T13:45:00.000Z",
                    ToDateTime: "2021-02-16T21:00:00.000Z"
                }

            Returns
            -------
            dict
                The server's response for the API
                Response example
                {
                    Bills: [{
                        BillId: "45c35985-2b94-4abd-a608-8685aeb75226",
                        CreatedDate: "2021-01-28T13:47:27.443-05:00",
                        MerchantId: "122c2650-6418-469a-a2ce-4fdc02c601ac",
                        BillTitle: "test interact",
                        BillDescription: "test interact",
                        BillAmount: 1,
                        ExternalSystemBillNumber1: "",
                        ExternalSystemBillNumber2: "",
                        ExternalSystemBillNumber3: "",
                        BillCurrency: 2,
                        Language: 1,
                        RelatedCustomerId: "986cec31-be7a-4d7c-a703-0f4c67791362"
                    }]
                }
        """
    ,    
    'CreateBill': """
            API call to the server.
            Parameters
            ----------
            api_request_body : dict, required
                The API request payload 
                Call Example:
                {
                    SessionToken: "0651af61-ae9e-41a7-898e-8ec775c6f8a1",
                    BreakIfMerchantNeverBeenAuthorized: true,
                    BillData: {
                        MerchantId: "122c2650-6418-469a-a2ce-4fdc02c601ac",
                        BillTitle: "test interact",
                        BillDescription: "test interact",
                        BillAmount: 1,
                        ExternalSystemBillNumber1: "",
                        ExternalSystemBillNumber2: "",
                        ExternalSystemBillNumber3: "",
                        BillCurrency: 2,
                        Language: 1,
                        RelatedCustomerId: "986cec31-be7a-4d7c-a703-0f4c67791362"
                    }
                }

            Returns
            -------
            dict
                The server's response for the API
                Response example
                {
                    BillId: "45c35985-2b94-4abd-a608-8685aeb75226"
                }
        """
    ,
    'GetBill' : """
            API call to the server.
            Parameters
            ----------
            api_request_body : dict, required
                The API request payload 
                Call Example:
                {
                    SessionToken: "86ee144e-9c27-4039-aa1f-43be0042aecf",
                    BillId: "45c35985-2b94-4abd-a608-8685aeb75226"
                }

            Returns
            -------
            dict
                The server's response for the API
                Response example
                {
                    Bill: {
                        BillId: "45c35985-2b94-4abd-a608-8685aeb75226",
                        CreatedDate: "2021-01-28T13:47:27.443-05:00",
                        MerchantId: "122c2650-6418-469a-a2ce-4fdc02c601ac",
                        BillTitle: "test interact",
                        BillDescription: "test interact",
                        BillAmount: 1,
                        ExternalSystemBillNumber1: "",
                        ExternalSystemBillNumber2: "",
                        ExternalSystemBillNumber3: "",
                        BillCurrency: 2,
                        Language: 1,
                        RelatedCustomerId: "986cec31-be7a-4d7c-a703-0f4c67791362"
                    }
                }
        """
    ,  
    'DeleteBill': """
            API call to the server.
            Parameters
            ----------
            api_request_body : dict, required
                The API request payload 
                Call Example:
                {
                    SessionToken: "0651af61-ae9e-41a7-898e-8ec775c6f8a1",
                    PaymentMethodId: "06e45951-b19c-4001-8e00-d6257ef1ac1c"
                }
        """
    ,
    'ListPaymentMethods': """
            API call to the server.
            Parameters
            ----------
            api_request_body : dict, required
                The API request payload 
                Call Example:
                {
                    SessionToken: "0651af61-ae9e-41a7-898e-8ec775c6f8a1",
                    CustomerId: "986cec31-be7a-4d7c-a703-0f4c67791362"
                }

            Returns
            -------
            dict
                The server's response for the API
                Response example
                {
                    PaymentMethods: [{
                    PaymentMethodId: "b96d8827-5e57-4698-ab57-5601a9b973a2",
                    Owner: "Fanny Tester",
                    PaymentMethodDescription: "Compete principal",
                    IsCustomerAutomaticPaymentMethod: false,
                    PaymentMethodType: 3,
                    AccountPreview: "***-*****-***1234",
                    },{
                    PaymentMethodId: "886fe591-bb09-4442-84d4-509293044d90",
                    Owner: "Kelly Carlson",
                    PaymentMethodDescription: "Test Credit Card",
                    IsCustomerAutomaticPaymentMethod: true,
                    PaymentMethodType: 1,
                    AccountPreview: "***************4242",
                    ExpirationDate: "2024-12-01T00:00:00",
                    }]
                }
        """
    ,
    'SetDefaultPaymentMethod': """
            API call to the server.
            Parameters
            ----------
            api_request_body : dict, required
                The API request payload 
                Call Example:
                {
                    SessionToken: "0651af61-ae9e-41a7-898e-8ec775c6f8a1",
                    PaymentMethodId: "06e45951-b19c-4001-8e00-d6257ef1ac1c",
                    CustomerId: "986cec31-be7a-4d7c-a703-0f4c67791362"
                }
        """
    ,
    'CreateDirectAccountPaymentMethod': """
            API call to the server.
            Parameters
            ----------
            api_request_body : dict, required
                The API request payload 
                Call Example:
                {
                    SessionToken: "0651af61-ae9e-41a7-898e-8ec775c6f8a1",
                    CustomerId: "986cec31-be7a-4d7c-a703-0f4c67791362",
                    IsCustomerAutomaticPaymentMethod: "true",
                    Account: {
                        Owner: "Jeff Testing",
                        AccountName: "Personal bank account",
                        BankNumber: "003",
                        InstitutionNumber: "12345",
                        AccountNumber: "9876543"
                    }
                }

            Returns
            -------
            dict
                The server's response for the API
                Response example
                {
                    PaymentMethodId: "06e45951-b19c-4001-8e00-d6257ef1ac1c"
                }
        """
    ,
    'GetPaymentMethod': """
            API call to the server.
            Parameters
            ----------
            api_request_body : dict, required
                The API request payload 
                Call Example:
                {
                    SessionToken: "0651af61-ae9e-41a7-898e-8ec775c6f8a1",
                    PaymentMethodId: "06e45951-b19c-4001-8e00-d6257ef1ac1c"
                }

            Returns
            -------
            dict
                The server's response for the API
                Response example
                {
                    PaymentMethod: {
                        PaymentMethodId: "b96d8827-5e57-4698-ab57-5601a9b973a2",
                        Owner: "Fanny Tester",
                        PaymentMethodDescription: "Compete principal",
                        IsCustomerAutomaticPaymentMethod: false,
                        PaymentMethodType: 3,
                        AccountPreview: "***-*****-***1234",
                    }
                }
        """
    ,
    'DeletePaymentMethod': """
            API call to the server.
            Parameters
            ----------
            api_request_body : dict, required
                The API request payload 
                {
                    SessionToken: "0651af61-ae9e-41a7-898e-8ec775c6f8a1",
                    PaymentId: "c9a521d5-60a1-4398-8f6c-7462797d584c"
                }
        """
    ,
    'CreatePayment': """
            API call to the server.
            Parameters
            ----------
            api_request_body : dict, required
                The API request payload 
                Call Example 1:
                {
                    SessionToken: "86ee144e-9c27-4039-aa1f-43be0042aecf",
                    BillId: "45c35985-2b94-4abd-a608-8685aeb75226"
                    SetPaymentCustomerFromBill: true,
                    PaymentInfo: {
                        PaymentFlow: 7
                    }
                }

                Call Example 2:
                {
                    SessionToken: "4840fe52-5ab2-43be-8a07-4354f263431b",
                    BillId: "45c35985-2b94-4abd-a608-8685aeb75226",
                    SetPaymentCustomerFromBill: "false",
                    PaymentInfo: {
                        PaymentFlow: 6,
                        RelatedCustomerId: "986cec31-be7a-4d7c-a703-0f4c67791362",
                        DueDate: "2021-02-16T16:10:19.000Z",
                        PaymentAmount: 1.22
                    }
                }

            Returns
            -------
            dict
                The server's response for the API
                Response example 1:
                {
                    PaymentId: "c9a521d5-60a1-4398-8f6c-7462797d584c",
                    AutoSelectPaymentFlowResult: 5,
                    PaymentFlowParsingResult: 1
                }
        """
    ,
    'CreateDirectDeposit': """
            API call to the server.
            Parameters
            ----------
            api_request_body : dict, required
                The API request payload 
                Call Example:
                {
                    SessionToken: "86ee144e-9c27-4039-aa1f-43be0042aecf",
                    OriginMerchantId: "122c2650-6418-469a-a2ce-4fdc02c601ac ",
                    DestinationAccount: {
                        Owner: "Jeff Testing",
                        AccountName: "Personal bank account",
                        BankNumber: "003",
                        InstitutionNumber: "12345",
                        AccountNumber: "9876543"
                    },
                    DepositDueDate: "2021-02-16T16:10:19.000Z",
                    Currency: 1
                    Language: 1,
                    ReferenceNumber: "C12343-324",
                }
        """
    ,
    'CreateTransactionFromRaw': """
            API call to the server.
            Parameters
            ----------
            api_request_body : dict, required
                The API request payload 
                Call Example:
                {
                    SessionToken: "0651af61-ae9e-41a7-898e-8ec775c6f8a1",
                    MerchantId: "122c2650-6418-469a-a2ce-4fdc02c601ac",
                    RawAcpFileContent: "[THE ACP FILE CONTENT TEXT]"
                }

            Returns
            -------
            dict
                The server's response for the API
                Response example
                {
                    TransactionsGroupId: "TIBGID-132162625479516834"
                }
        """
    ,
    'GetCustomersByExternalId': """
            API call to the server.
            Parameters
            ----------
            api_request_body : dict, required
                The API request payload 
                Call Example:
                {
                    SessionToken: "0651af61-ae9e-41a7-898e-8ec775c6f8a1",
                    ExternalCustomerId: "c123-55",
                }

            Returns
            -------
            dict
                The server's response for the API
                Response example
                Customers: [{CustomerId: "05880372-5c30-4f17-8796-c353bfaece3f",
                    CustomerName: "Jackie Tester",
                    CustomerExternalId: "c123-55",
                    Language: 1,
                    CustomerDescription: "VIP Customer",
                    PaymentMethods: [{
                    PaymentMethodId: "b96d8827-5e57-4698-ab57-5601a9b973a2",
                    IsCustomerAutomaticPaymentMethod: false,
                    PaymentMethodType: 3,
                    PaymentMethodDescription: "Compete principal",
                    AccountPreview: "***-*****-***1234"}]
                }]
        """
    ,
    'ListExecutedOperations': """
            API call to the server.
            Parameters
            ----------
            api_request_body : dict, required
                The API request payload 
                Call Example:
                {
                    SessionToken: "0651af61-ae9e-41a7-898e-8ec775c6f8a1",
                    ServiceId: "862b96b1-85d4-406f-b55c-8f48f895f68e"
                }

            Returns
            -------
            dict
                The server's response for the API
                Response example
                {
                    RecuringTransfers: [{
                        RecuringTransferId: "89d720f2-78ae-4816-8fda-0099aa867c38",
                        RecuringMode: 2,
                        RecuringRefDate: "2021-02-12T13:47:27.443-05:00",
                        CreatedDate: "2021-01-28T13:47:27.443-05:00",
                        RelatedMerchantId: "122c2650-6418-469a-a2ce-4fdc02c601ac",
                        RelatedMerchantName: "Company merchant",
                        CustomerName: "Client",
                        RelatedCustomerId: "986cec31-be7a-4d7c-a703-0f4c67791362"
                        Amount: 98.6
                    }]  
                }
        """
    ,
    'Login': """
            API call to the server.
            Parameters
            ----------
            api_request_body : dict, required
                The API request payload 

            Returns
            -------
            dict
                The server's response for the API
        """
    ,
    'CreateFreeOperation': """
            API call to the server.
            Parameters
            ----------
            api_request_body : dict, required
                The API request payload 
                Call Example:
                {
                    SessionToken: "0651af61-ae9e-41a7-898e-8ec775c6f8a1",
                    MerchantId: "122c2650-6418-469a-a2ce-4fdc02c601ac",
                    PaymentMethodId: "b96d8827-5e57-4698-ab57-5601a9b973a2",
                    TransferType: 1,
                    ReferenceNumber: "C123-01312",
                    Amount: 12.44,
                    Language: 1,
                    TransactionDueDate: "2021-02-16T16:10:19.000Z",
                    GroupId: "HT123123",
                    TransferFrequency: 0
                }

            Returns
            -------
            dict
                The server's response for the API
                Response example
                {
                    PaymentId: "c9a521d5-60a1-4398-8f6c-7462797d584c"
                }
        """
    ,
    'RevertTransfer': """
            API call to the server.
            Parameters
            ----------
            api_request_body : dict, required
                The API request payload 
                Call Example:
                {
                    SessionToken: "0651af61-ae9e-41a7-898e-8ec775c6f8a1",
                    TransferId: "c9a521d5-60a1-4398-8f6c-7462797d584c"
                }
        """
    ,
    'GetRecuringTransfers': """
            API call to the server.
            Parameters
            ----------
            api_request_body : dict, required
                The API request payload 
                Call Example:
                {
                    SessionToken: "0651af61-ae9e-41a7-898e-8ec775c6f8a1",
                    ServiceId: "862b96b1-85d4-406f-b55c-8f48f895f68e"
                }

            Returns
            -------
            dict
                The server's response for the API
                Response example
                {
                    RecuringTransfers: [{
                        RecuringTransferId: "89d720f2-78ae-4816-8fda-0099aa867c38",
                        RecuringMode: 2,
                        RecuringRefDate: "2021-02-12T13:47:27.443-05:00",
                        CreatedDate: "2021-01-28T13:47:27.443-05:00",
                        RelatedMerchantId: "122c2650-6418-469a-a2ce-4fdc02c601ac",
                        RelatedMerchantName: "Company merchant",
                        CustomerName: "Client",
                        RelatedCustomerId: "986cec31-be7a-4d7c-a703-0f4c67791362"
                        Amount: 98.6
                        }]
                    }
        """
    ,
    'DeleteRecuringTransfer': """
            API call to the server.
            Parameters
            ----------
            api_request_body : dict, required
                The API request payload 
                Call Example:
                {
                    SessionToken: "0651af61-ae9e-41a7-898e-8ec775c6f8a1",
                    RecuringTransferId: "89d720f2-78ae-4816-8fda-0099aa867c38"
                }
        """
    ,
    'CreateInteracPaymentMethod': """
            API call to the server.
            Parameters
            ----------
            api_request_body : dict, required
                The API request payload 
                Call Example:
                {
                SessionToken: "0651af61-ae9e-41a7-898e-8ec775c6f8a1",
                CustomerId: "986cec31-be7a-4d7c-a703-0f4c67791362",
                IsCustomerAutomaticPaymentMethod: "true",
                InteracInformation: {
                    Description: "interact Test",
                    Owner: "Kelly interact",
                    TargetEmailAddress: "kinterac@dummytest.com",
                    TargetMobilePhoneNumber: "888-123-4567",
                    InteracQuestion: "Remember the fruit",
                    InteracAnswer: "Orange"
                    }
                }

            Returns
            -------
            dict
                The server's response for the API
                Response example
                {
                    PaymentMethodId: "06e45951-b19c-4001-8e00-d6257ef1ac1c"
                }
        """
    ,
    'CreateDirectInteracTransaction': """
            API call to the server.
            Parameters
            ----------
            api_request_body : dict, required
                The API request payload 
                Call Example:
                {
                    SessionToken: "86ee144e-9c27-4039-aa1f-43be0042aecf",
                    MerchantId: "122c2650-6418-469a-a2ce-4fdc02c601ac",
                    InteracInformation: {
                        "Description": "Interac Test",
                        "Owner": "Kelly interact",
                        "TargetEmailAddress": "kinterac@dummytest.com",
                        "TargetMobilePhoneNumber": "888-123-4567",
                        "InteracQuestion": "Remember the fruit",
                        "InteracAnswer": "Orange"
                    },
                    DueDate: "2021-02-16T16:10:19.000Z",
                    Currency: 1
                    Language: 1,
                    ReferenceNumber: "C12343-324",
                }
        """
}

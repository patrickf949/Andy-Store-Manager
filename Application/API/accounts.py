"""
This module deals with manipulation of accounts
"""
class Accounts:
    admin = { 
        1 : {
            "username":"admin",
            "password":"pass"
        }
    }
    
    attendants = {
        1 : {
            'username' : 'mchwezi',
            'password' : 'pass',
            '' : ''
        },
        2 : {
            'username' : 'mhombi',
            'password' : 'pass'
        },
        3 : {
            'username' : 'angy',
            'pass' : 'pass'
        },
        4 : {
            'username' : 'adele',
            'password' : 'pass'
        },
        5 : {
            'username' : 'alicia',
            'password' : 'pass'
        }
    }

    activeuser=[]

    def Accounts(self):
        
        #print(attendants)
        pass


    def loginAdmin(self, dict):
        """
        Verifies admin details to allow admin login
        params: dictionary with key as username, value as password
        return: id,True if verified else false
        """
        pass

    
    def login(self,dict):
        """
        Verifies Store Attendant login
        params: dictionary with key as username, and value as the password entered by the user
        return: id,True if verified else false
        """
        pass


    def addNewAccount(self, dict):
        """
        Adds New Store Attendant account to inventory
        params: dictionary containing key as username, value as password
        return: true if added
        """
        pass
    

    def updateExistingAccount(self, dict):
        """
        Updates information of existing account
        params: dictionary with key as id, value as dictionary containing updated information
        return: true if added
        """
        pass


    def deleteAccount(self, id):
        """
        Deletes selected user from the system
        params: user id
        return: true if deleted
        """
        pass


    def deleteAllAccounts(self):
        """
        Deletes all Store Attendant Accounts in inventory
        params: n/a
        returns: true if all Store attendant accounts are deleteds
        """
        pass


    def checkIfAccountExists(self, dict):
        """
        Checks the existing account details based on user input
        params: dictionary containing with key as username, value as password
        returns: id,true if exists else false
        """
        pass
    pass
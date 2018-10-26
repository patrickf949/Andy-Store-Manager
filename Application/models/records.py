"""
This module deals with manipulation of records
"""
from Application.models.products import Products

class Records:

    records = {
                1 : {'user': 'angy',
                    'Fresh Diary milk' : {'no' :12, 'price' : 2000, 'subtotal': 24000 },
                    'French Toasts' : {'no' :12, 'price' : 100, 'subtotal': 1200 },
                    'Total' :  25200},
                2 : {'user': 'mhombi',
                    'Fresh Diary milk' : {'no' :12, 'price' : 2000, 'subtotal': 24000 },
                    'French Toasts' : {'no' :12, 'price' : 100, 'subtotal': 1200 },
                    'Total' :  25200}                
            }

    def __init__(self, dict):
        self.attendant= dict['user']
        self.items = dict['items']
        self.created_at = dict['created_at']
        

    
        
    def createSaleRecord(self, ):
        """
        Creates a sale record and stores it for 
        """
        id = self.getId()       
        Records.records[id]["attendant"] = self.attendant
        Records.records[id]["created_at"] = self.created_at
        Records.records["total_sales"] += self.total_sales
        Records.records["total_products_sold"] += self.total_items
    

    def deleteSaleRecord(self, saleId):
        """
        Deletes a sale record
        Params: n/a
        returns: n/a
        """
        pass

    def deletesAllRecords(self): 
        """
        Deletes all sale records:

        """
        pass

    def getId(self):
        """
        This method provids an id for a new product
        params: n/a
        returns:id for new product.
        """
        id = len(Products.products)+1
        return id
    
    def calculateTotals(self):
        """
        Calculates the total got from a sale
        params: n/a
        returns: all subtotals and total and arranges final sale record
        """
        # for i in self.items:
        pass
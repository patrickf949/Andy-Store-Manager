
"""
This module manages the products available in the inventory
"""

class Products:
    products = { 1 :{
            "name" : "French Toasts",
            "quantity" : 500,
            "min_quantity" : 20,
            "price" : 100
        },
        2 :{
            "name" : "Fresh Diary Milk 500mls",
            "quantity" : 400,
            "min_quantity" : 20,
            "price" : 2000

        },
        3 :{
            "name" : "Dog Supplements 40kgs",
            "quantity" : 400,
            "min_quantity" : 10,
            "price" : 5000

        },
        4 :{
            "name" : "Dog Supplements 40kgs",
            "quantity" : 400,
            "min_quantity" : 10,
            "price" : 5000

        },
        5 :{
            "name" : "Dog Supplements 40kgs",
            "quantity" : 400,
            "min_quantity" : 10,
            "price" : 5000

        },
        6 :{
            "name" : "Dog Supplements 40kgs",
            "quantity" : 400,
            "min_quantity" : 10,
            "price" : 5000

        },
        7 :{
            "name" : "Dog Supplements 40kgs",
            "quantity" : 400,
            "min_quantity" : 10,
            "price" : 5000

        },
        8 :{
            "name" : "Dog Supplements 40kgs",
            "quantity" : 400,
            "min_quantity" : 10,
            "price" : 5000

        },
        9 :{
            "name" : "Ting Supplements",
            "quantity" : 400,
            "min_quantity" : 10,
            "price" : 50000

        },
        10 :{
            "name" : "Thick Yoghurt",
            "quantity" : 400,
            "min_quantity" : 10,
            "price" : 5000

        },
        11 :{
            "name" : "Chicken salads",
            "quantity" : 400,
            "min_quantity" : 10,
            "price" : 500

        }

    }
    
    def addProduct(self, list):
        """
        Adds A new product to inventory
        params: list of the information of the new product
        return: True if object is added
        """
        pass
    

    def deleteProduct(self, id):
        """
        deletes a selected product from the inventory
        params: id of the product to be deleted
        return: true if deleted
        """
        pass
    

    def reduceAfterProductSale(self, list):
        """
        reduces the products in the inventory after a sale
        params: list of dictionaries with key as the item id and 
        value as the number of pieces of that particular item were purchased
        return: True if all have been added
        """
        pass
    

    def deleteAllProducts(self):
        """
        Deletes all products from the inventory
        params: n/a
        returns: true if succcessfully deleted all products
        """
        pass


    def addStockForExistingProduct(self,dict):
        """
        Adds Quantity of an existing product in stock
        params: dictionary with key as item id and value as the added stock
        return: True if addedd
        """
        pass


    def updateExistingProduct(self, dict):
        """
        Updates the records of an existing product in stock
        params: dictionary with key as item id, value as dictionary of updated info
        """
        pass


    




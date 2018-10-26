
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

    def __init__(self, name='', qty=0, min_qty=0, price=0):
        if name!='':
            self.name=name
            self.qty = qty
            self.min_qty = qty
            self.price= price

        
    def addProduct(self):
        """
        Adds A new product to inventory
        params: n/a
        return: tuple of True, and All Products in inventory if object is added
        """
        if self.checkIfProductExists(self.name) or self.checkIfProductExists(self.name)=='There are no items in the store':
            newId = self.getId()
            Products.products[newId]={
                                        "name" : self.name,
                                        "quantity" : self.qty,
                                        "min_quantity" : self.min_qty,
                                        "price" : self.price
                                    }
            return True, Products.products
        return 'The Product is already in inventory'
        

    def deleteProduct(self, id):
        """
        deletes a selected product from the inventory
        params: id of the product to be deleted
        return: true if deleted
        """
        if self.checkIfProductExists(id):
            del Products.products[id]
            return True
        else:
            return False
    

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


    def addStockForExistingProduct(self,id, amount):
        """
        Adds Quantity of an existing product in stock
        params: product id and amount to be added
        return: True if addedd
        """
        if self.checkIfProductExists(id):
            id['quantity']+=amount


    def updateExistingProduct(self, dict):
        """
        Updates the records of an existing product in stock
        params: dictionary with key as item id, value as dictionary of updated info
        """
        pass

    def checkIfProductExists(self, productId=0, name=''):
        """
        This method checks whether a product exists
        params:either an ID or a name
        returns: true if exists
        """
        if len(Products.products)==0:#
            return "There are no items in the store"

        elif productId==0:
            for i in Products.products:
                if name == i['name']:
                    return True
            return False
        
        elif name=='':
            if productId in Products.products.keys():
                return True
            return False

    def getId(self):
        """
        This method provids an id for a new product
        params: n/a
        returns:id for new product.
        """
        id = len(Products.products)+1
        return id
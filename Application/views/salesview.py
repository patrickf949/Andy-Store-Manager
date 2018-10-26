from flask import jsonify, Blueprint, request
from datetime import datetime
from Application.models.products import Products
from Application.models.records import Records


blue_print = Blueprint("sales", __name__)

#working cart
newCart = {"total_price":0, "total_items_in_cart":0}


@blue_print.route('/v1/sales/shopping_cart', methods = ['GET', 'POST'])
def shopping_cart():
    """
    create carts
    """        
    if request.method == 'POST':
        
        product_id = int(request.form.get('product_id'))
        quantity = int(request.form.get('quantity'))

        if product_id > len(Products.products):
            response = "Product not in Inventory"
            return jsonify ({"Response":response})

        elif Products.products[product_id]["quantity"] < quantity:
            response = "Not enough stock available in store"
            return jsonify ({"Response":response})
        else: 
            id_in_cart = len(current_shopping_cart)
                                                     
            newCart[str(id_in_cart)] = {
                "product_name":Products.products[product_id]["product_name"]
                ,"quantity_ordered":quantity
                ,"price": quantity*Products.products[product_id]["unit_price"]
            }           
            current_shopping_cart["total_price"] += quantity*Products.products[product_id]["unit_price"]
            current_shopping_cart["total_items_in_cart"] += quantity         

            Products.products[product_id]["quantity"] -= quantity # reduce quantity of product in products

            response = "Product added to cart successfully!"
            return jsonify ({"Response":response, "Items in Cart":current_shopping_cart}), 200

    if len(current_shopping_cart) > 0:        
        return jsonify ({"Items in Cart": current_shopping_cart}), 200  

    response = "Cart is empty!"
    return jsonify ({"Response":response, "Items in Cart": current_shopping_cart})  

@blue_print.route('/v1/sales/create_record')
def createSalesRecord():
    global current_shopping_cart
    attendant = ""
    time = datetime.now()            
    details = current_shopping_cart            
    total_price = current_shopping_cart["total_price"]
    items= current_shopping_cart["total_items_in_cart"]
    dict = {'user':attendant,
            'items': items,
            'nos_of_items': details,
            'total': total_price,
            'time': time
        }
    sale = Records(dict)
    sale.createSaleRecord()
    current_shopping_cart = {}

    response = "Sales Record Created Successfully"  
    
    return jsonify({"Response": response}), 200

@blue_print.route('/v1/sales/allrecords')
def getAllRecords():
    """
    Get all sales records
    params: n/a
    returns: all records
    """
    if len(Records.records)<=0:
        response = "There are no sales records to show!"
        return jsonify({"Response":response, "Sales Records":Records.records})

    response = "All sales records are shown"
    return jsonify({"Response":response, "Sales Records":Records.records}), 200

@blue_print.route('/v1/sales/<sale_id>')
def getRecordbyId(sale_id): 
    """
    Get individual sale record
    params: sale id
    returns: individual sale record information
    """
    if  len(Records.records) == 0:
        response = "You are yet to receive your first customer. No sales records yet"
        return jsonify({"response":response})

    elif sale_id not in Records.records.keys():
        response = "Why you lying, that sale was not made" 
        return jsonify({'Response':response})
    else:
        response = "Sales record found!" 
        return jsonify({"response":response, "Record details":Records.records[sale_id]})

    
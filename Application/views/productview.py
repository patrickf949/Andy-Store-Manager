from flask import  request, Blueprint, jsonify
from Application.models.products import Products

blue_print = Blueprint('products', __name__)


@blue_print.route('/v1/products/<int:productId>')
def get_product_by_id(productId):
    """
    View an item in the store
    params: product id
    returns: json for infor on object
    """
    if  len(Products.products) == 0:
        response = "There are no products in inventory"
        return jsonify({"response":response})

    elif int(productId) not in Products.products.keys():
        #checks if product id provided exists in the store
        response = "No such product" 
        return jsonify({'Response':response}), 401
    else:
        response = "Product found!" 
        return jsonify({"response":response, "Product details":Products.products[productId]})


@blue_print.route('/v1/products')
def getAllProducts():
    if len(Products.products) == 0:
        response = "There are no products in inventory"
        return jsonify({"response":response})
    else:
        response = "All available products!" 
        return jsonify({"response":response, "Products details":Products.products})

    
@blue_print.route('/v1/products/create', methods = ['GET','POST'])
def addItem():
    """
    This method adds a new item to the store
    params:n/a
    returns: json
    """
    if request.method == 'POST':
        name = request.form.get('name')
        price = int(request.form.get('price'))
        qty = int(request.form.get('quantity'))
        min_qty = int(request.form.get('minimum_quantity'))
        newItem = Products(name,qty,min_qty,price)

        if newItem.addProduct():
            response = "Product already exists! Choose edit instead"
            return jsonify({'Response':response}), 401

        else:
            response = "Product added successfully!"    
            return jsonify({"response":response, "Products in inventory":Products.products}), 200

    return jsonify({"Products in inventory: inventory":Products.products}), 200



        


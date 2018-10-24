from flask import Flask, request,jsonify
from accounts import Accounts
from records import Records
from products import Products


app = Flask(__name__)

action = store_manager.Product_Operation("Yivanna Biles")

@app.route('/')
def home_page():
    return "Store Manager welcomes you!\nThis is a web application to enable store owners manage sales and product inventory records. This "

@app.route('/products/create', methods = ['GET','POST'])
def create_product():
    """
    This Method adds a product to the inventory
    params: n/a
    returns:n/a
    """
    if request.method == 'POST':
        name = request.form.get('name')
        unit = request.form.get('unit')
        quantity = int(request.form.get('quantity'))
        min_quantity = int(request.form.get('min_quantity'))      
        price = int(request.form.get('unit_price'))
        action.admin_create_product(name, unit, price, quantity, min_quantity)  
        return action.response
        # return jsonify(store_manager.inventory)

@app.route('/products/<int:productId>')
def get_product_by_id(productId):    
    return jsonify(action.get_product_by_id(productId))


@app.route('/products')
def get_all_products():
    return jsonify(store_manager.inventory)

@app.route('/sales/shopping_cart', methods = ['GET', 'POST'])
def shopping_cart():
    if request.method == 'POST':
        product_id = int(request.form.get('product_id'))
        quantity = int(request.form.get('quantity'))
        action.add_to_cart_by_id(product_id,quantity)
        return action.response       

    return jsonify(store_manager.shopping_cart) 

@app.route('/v1/sales/create_record')
def create_sales_record():
    action.create_sales_record()
    return action.response
   

@app.route('/v1/sales/get_all_records')
def get_all_records():
    return jsonify(store_manager.sales_records)


@app.route('/v1/sales/<saleId>')
def get_record_by_id(saleId):    
    return jsonify(action.get_record_by_id(saleId))


if __name__ == "__main__":
    app.run(debug=True)
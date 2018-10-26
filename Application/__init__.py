from flask import jsonify,Flask

app = Flask(__name__)

def create_app():

    app = Flask(__name__)

    @app.route("/")
    def kingslanding():
        return jsonify([
            "Store Manager!"
            ,"Store Manager is a web application that enables store owners manage sales and inventory records",{
                "/v1/products/create":"Create new product"
                ,"/v1/products": "Fetch all products"
                ,"/v1/products/<int:productId>": "Fetch product by Id"
                ,"/v1/sales/shopping_cart":"Add item to shopping cart"
                ,"/v1/sales/create_record": "Post sale record from shopping cart"
                ,"/v1/sales/allrecords": "Fetch all sales records"
                ,"/v1/sales/<sale_id>":"Fetch sale record by Id"
            }            
        ]), 200

    
    from Application.views import salesview
    app.register_blueprint(salesview.blue_print)
    
    
    from Application.views import productview
    app.register_blueprint(productview.blue_print)

    
    

    return app 
from yourapplication import app

@app.route('/')
def index():
    return 'Store Manager!\nStore Manager is a web application that enables store owners manage their attendants and their inventories'
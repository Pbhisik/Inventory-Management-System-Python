from flask import Blueprint,request,jsonify
from models.inventory import Inventory
from models.product import Product

bp = Blueprint('prodcuts',__name__)

inventory = Inventory()

@bp.route('/products',methods = ['GET'])
def get_all_prodcuts():
    products = [products.__dict__ for prodcut in inventory.product.values()]
    return jsonify(products)

@bp.route('/products',methods = ['POST'])
def create_product():
    data = request.get_json()
    product = Product(**data)
    inventory.add_product(product)
    return jsonify(product.__dict__),201

@bp.route('/products/<int:product_id>',methods = ['GET'])
def get_product(product_id):
    product = inventory.get_product(product_id)
    if product:
        return jsonify(product.__dict__)
    else:
        return jsonify({"error":"Product not found "}), 404
    
@bp.route('/products/<int:product_id>',methods = ['PUT'])
def update_product(product_id):
    data = request.json()
    product = inventory.get_product(product_id)
    if product:
        product.name = data.get('name',product.name)
        product.price = data.get('price',product.price)
        product.category = data.get('category',product.category)
        product.quantity = data.get('quantity',product.quantity)
        return jsonify(product.__dict__)
    else:
        return jsonify({"error":"Prodcut not found"}),404
    
@bp.route('/product/<int:product_id>',methods= ['DELETE'])
def remove_product(product_id):
    inventory.remove_product(product_id)
    return jsonify({"message":"product removed"})



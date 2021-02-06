from flask import Flask, jsonify, request # jsonify: convierte un objeto a un json

app = Flask(__name__)

from products import products
from products import persons

@app.route("/ping")
def ping():
    return jsonify({"message": "Hola noa"})


@app.route('/products', methods=['GET'])
def getProducts():
    return jsonify({"products":products, "message": "Lista de Productos"})


@app.route('/products/<string:product_name>')
def getProduct(product_name):
    # for p in products:
    #     if p["name"] == product_name:
    #         productFound = p

    productFound = [product for product in products if product["name"]==product_name]

    if len(productFound)>0:
        return jsonify({"product": productFound[0]})
    return jsonify({"message":"Producto no encontrado"})


@app.route('/products', methods=["POST"])
def addProduct():
    new_product ={
        "name": request.json["name"],
        "price": request.json["price"],
        "quantity": request.json["quantity"]
    }

    products.append(new_product)
    return jsonify({"message":"Producto Agregado satisfactoriamente", "products":products})


@app.route('/persons', methods=['GET'])
def getPersons():
    return jsonify({"persons": persons})


@app.route('/persons', methods=['POST'])
def addPerson():
    new_person ={
        "name": request.json['name'],
        "lastname": request.json['lastname'],
        "age": request.json['age']
    }
    persons.append(new_person)
    return jsonify({"persons":persons})

@app.route('/persons/<string:f_person>')
def getPerson(f_person):
    personFound = [person for person in persons if person["name"]== f_person]

    if len(personFound)>0:
        return jsonify({"person":personFound[0]})


if __name__=='__main__':
    app.run(debug=True, port=4000)
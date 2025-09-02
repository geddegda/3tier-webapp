from flask import Flask,render_template, request, jsonify
from flask_cors import CORS
from db_connection import get_connection

app = Flask(__name__)
CORS(app)

@app.route("/update_product", methods=["POST"])
def update_product():

    data = request.json

    id = data.get('id')
    product_name = data.get('product_name')
    product_price = data.get('product_price')
    product_quantity = data.get('product_quantity')

    if not id:
        return jsonify(error="an ID is required"), 400

    conn = get_connection()
    cursor = conn.cursor(dictionary = True)

    cursor.execute(
            "UPDATE products SET product_name= %s, product_price= %s, product_quantity=%s WHERE id= %s",
            (product_name, product_price, product_quantity,id)
    )

    conn.commit()

    if cursor.rowcount == 0:
        cursor.close()
        conn.close()
        return jsonify(error="Product not found"), 404

    cursor.close()
    conn.close()

    return jsonify(message="Product updated successfully")


@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route('/show_product', methods=['GET'])
def show_product():
    conn = get_connection()
    cursor = conn.cursor(dictionary = True)

    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(result=rows)


@app.route('/product', methods=['POST'])
def product():
    data = request.get_json()

    product_name = data.get('product_name')
    product_price = data.get('product_price')
    product_quantity = data.get('product_quantity')

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
            "INSERT INTO products (product_name, product_price, product_quantity) VALUES (%s, %s, %s)",
            (product_name, product_price, product_quantity)
    )

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify(message="New product successfully inserted!"), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)

from flask import Flask, jsonify

app = Flask(__name__)

purchase_orders = [
    {
        'id': 1,
        'description': 'Order purchase 1',
        'items': [
            {
                'id': 1,
                'description': 'Order item 1',
                'price': 20.99
            }
        ]
    }
]


@app.route('/')
def home():
    return "Hello World"


@app.route('/purchase_orders')
def get_purchase_orders():
    return jsonify(purchase_orders)


@app.route('/purchase_orders/<int:id>')
def get_purchase_orders_by_id(id):
    for purchase in purchase_orders:
        if not purchase.get("id") == id:
            return jsonify({"message": "Item not found"}), 404

        return jsonify(purchase)


app.run(port=5000, debug=True)
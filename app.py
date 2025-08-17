from flask import Flask, jsonify, request

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
        if purchase.get("id") == id:
            return jsonify(purchase)

    return jsonify({"message": "Item not found"}), 404


@app.route('/purchase_orders', methods=['POST'])
def create_purchase_orders():
    request_data = request.get_json()
    purchase_order = {
        'id': request_data['id'],
        'description': request_data['description'],
        'items': []
    }

    purchase_orders.append(purchase_order)
    return jsonify(purchase_order)


@app.route('/purchase_orders/<int:id>/items')
def get_purchase_orders_items(id):
    for purchase in purchase_orders:
        if purchase.get("id") == id:
            return jsonify(purchase['items'])

    return jsonify({"message": "Item not found"}), 404


@app.route('/purchase_orders/<int:id>/items', methods=['POST'])
def create_purchase_orders_items(id):
    payload = request.get_json()
    for purchase in purchase_orders:
        if purchase.get("id") == id:
            purchase['items'].append(
                {
                    'id': payload['id'],
                    'description': payload['description'],
                    'price': payload['price']
                }
            )
        return jsonify(purchase['items'])


app.run(port=5000, debug=True)
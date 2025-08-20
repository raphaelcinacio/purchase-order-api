from flask_restful import Resource, reqparse
from repository.Purchase import purchase_orders


class PurchaseOrders(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument(
        'id',
        type=int,
        required=True,
        help="Parameter is missing"
    )

    parser.add_argument(
        'description',
        type=str,
        required=True,
        help="Parameter is missing"
    )

    def get(self):
        return purchase_orders

    def post(self):
        request_data = PurchaseOrders.parser.parse_args()

        purchase_order = {
            'id': request_data['id'],
            'description': request_data['description'],
            'items': []
        }
        purchase_orders.append(purchase_order)
        return purchase_order


class PurchaseOrdersById(Resource):

    def get(self, id):

        for purchase in purchase_orders:
            if purchase.get("id") == id:
                return purchase

        return {"message": "Item not found"}, 404

    
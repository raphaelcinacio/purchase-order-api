from flask_restful import Resource
from flask import jsonify
from repository.Purchase import purchase_orders


class PurchaseOrdersItems(Resource):

    def get(self, id):
        for purchase in purchase_orders:
            if purchase.get("id") == id:
                return (purchase['items'])

        return {"message": "Item not found"}, 404
from flask import Flask, jsonify, request

app = Flask(__name__)
ORDERS = [
    {"id": 1, "drink": "latte", "size": "medium", "status": "ready"},
    {"id": 2, "drink": "cappuccino", "size": "large",  "status": "pending"},
    {"id": 3, "drink": "espresso", "size": "small",  "status": "brewing"},
    {"id": 4, "drink": "mocha", "size": "large",  "status": "ready"},
]

@app.get("/health")
def health():
    return jsonify(status="ok")

@app.get("/orders")
def list_orders():
    status = request.args.get("status")
    rows = [o for o in ORDERS if o["status"] == status] if status else ORDERS
    return jsonify(count=len(rows), orders=rows)

@app.get("/orders/<int:order_id>")
def one_order(order_id):
    for o in ORDERS:
        if o["id"] == order_id:
            return jsonify(o)
    return jsonify(error="no order with that id", id=order_id), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

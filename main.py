from fastapi import FastAPI, Header
from typing import Optional
from models import Order
import persistence as db

app = FastAPI()


@app.get("/")
async def root():
    return {
        "message": "Sample store api written in FastAPI. "
                   "For documentation, go to /docs"
    }


@app.get("/products/")
async def list_products(accepts_version: Optional[str] = Header('1.0')):
    products = db.get_products()

    return products


@app.get("/orders/")
async def list_orders():
    orders = db.get_orders()
    return orders


@app.post("/orders/")
async def create_order(order: Order):
    db.save_order(order)
    return {"message": "Order created", **order.dict()}


@app.put("/orders/")
async def update_order(order: Order):
    db.update_order(order)
    return {"message": "Order updated", **order.dict()}


@app.delete("/orders/")
async def delete_order(order: Order):
    db.delete_order(order)
    return {"message": "Order deleted", "order id": order.id}

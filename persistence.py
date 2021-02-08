import sqlite3
import pandas as pd
from models import Order, Product

conn = sqlite3.connect('store.db')


def save_order(order: Order):
    try:
        orders_df = pd.read_sql('select * from orders', con=conn).set_index('id')
    except pd.io.sql.DatabaseError:
        orders_df = pd.DataFrame()
    order_df = pd.DataFrame.from_records([order.dict()]).set_index('id')
    orders_df = order_df.append(orders_df)
    orders_df.to_sql('orders', con=conn, if_exists='replace')


def get_orders():
    orders = pd.read_sql('select * from orders', con=conn).set_index('id')

    return orders.to_dict('records')


def update_order(order: Order):
    # TODO: change this garbage
    orders = pd.read_sql('select * from orders', con=conn)
    if order.id not in orders['id']:
        return {'error': "this order doesn't exists"}
    else:
        sql = '''UPDATE orders
                    SET customer_name = ?,
                    shipping_address = ?,
                    order_date = ?,
                    order_total = ?
                WHERE id=?
        '''
        cur = conn.cursor()
        try:
            cur.execute(
                sql,
                (
                    order.customer_name,
                    order.shipping_address,
                    order.order_date,
                    order.order_total,
                    order.id
                )
            )
            conn.commit()
        except sqlite3.Error as e:
            return {'error': "found issues updating your order"}


def delete_order(order: Order):
    sql = 'DELETE FROM orders WHERE id=?'
    cur = conn.cursor()
    try:
        cur.execute(sql, (order.id,))
        conn.commit()
    except sqlite3.Error as e:
        return {'error': "this order doesn't exists"}


def get_products():
    products = pd.read_sql('select * from products', con=conn).set_index('id')

    return products.to_dict('records')

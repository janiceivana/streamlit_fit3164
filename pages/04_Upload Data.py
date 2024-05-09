
import streamlit as st
import pandas as pd
import pyodbc
from streamlit_cookies_controller import CookieController

controller = CookieController()

# Set a cookie
controller.set('user-cred', 'testing')

# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};SERVER="
        + st.secrets["server"]
        + ";DATABASE="
        + st.secrets["database"]
        + ";UID="
        + st.secrets["username"]
        + ";PWD="
        + st.secrets["password"]
        + ";Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"
    )

conn = init_connection()




df = pd.read_csv()



with conn.cursor() as cur:
    seen = []
    for records in df:
        if records['store_id'] not in seen:
            seen.append(records['store_id'])
            insert_stmt1 = 'INSERT INTO STORE (store_id, cookie) VALUES (?, ?)'
            cur.execute(insert_stmt1, {"store_id": records['store_id'], "cookie": controller.get("user-cred")})
            conn.commit()
        insert_stmt2 = 'INSERT INTO SALE (store_id, price, date,  item_id, dept_id, qty_sold, cost) VALUES (?,?,?,?,?,?,?,?)'
        cur.execute(insert_stmt2, {"store_id" : records['store_id'] , "cookie" : controller.get("user-cred"), "price" : records['price'] , "date" : records['date'] , "item_id": records["item_id"] ,"dept_id" : records['dept_id'], "qty_sold" : records['qty_sold'], "cost" : records['cost']})
        conn.commit()



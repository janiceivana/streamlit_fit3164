
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




uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)


    with conn.cursor() as cur:
        seen = []
        for i in range(len(df)):
            if df.loc[i,'store_id'] not in seen:
                seen.append(df.loc[i, 'store_id'])
                insert_stmt1 = 'INSERT INTO STORE (store_id, cookie) VALUES (?, ?)'
                cur.execute(insert_stmt1, {"store_id": df.loc[i,'store_id']}, {"cookie": controller.get("user-cred")})
                conn.commit()
            insert_stmt2 = 'INSERT INTO SALE (store_id, price, date,  item_id, dept_id, qty_sold, cost) VALUES (?,?,?,?,?,?,?,?)'
            cur.execute(insert_stmt2, {"store_id" : df.loc[i,'store_id']} , {"cookie" : controller.get("user-cred")}, {"price" : df.loc[i,'price']} , {"date" : df.loc[i,'date'] }, {"item_id":df.loc[i,'item_id']} ,{"dept_id" : df.loc[i,'dept_id']}, {"qty_sold" : df.loc[i,'qty_sold']},{ "cost" : df.loc[i,'cost']})
            conn.commit()




import streamlit as st
import pandas as pd
import os
# Upload file command for use to upload there file
import sqlalchemy
from google.oauth2 import service_account
import google.auth

import json
from google.cloud.sql.connector import Connector, IPTypes
import pyodbc
#from streamlit_cookies_controller import CookieController




# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 18 for SQL Server};SERVER="
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



'''
controller = CookieController()

# Set a cookie
controller.set('user-cred', 'testing')
'''







data_cvs = st.file_uploader("choose a csv file")

'''
if data_cvs is not None:
    # read file using pandas
    df = pd.read_csv(data_cvs.path)
    # check file format
    #add file format check here ************ IMPORTANT ***************

    #add quit exit condition if file is not correct
    with pool.connect() as db_conn:

        for records in df:
            
            
            insert_stmt1= 'INSERT INTO STORE (store_id, cookie) VALUES (?, ?)'
    
    
            insert_stmt2= 'INSERT INTO SALE (store_id, cookie, price, date,  item_id, dept_id, qty_sold,) VALUES (?,?,?,?,?,?,?)'
    
    
            cnxn.execute(insert_stmt1, {"store_id" : records['store_id'], "cookie" :controller.get("user-cred")})
            cnxn.execute(insert_stmt2, {"store_id" : records['store_id'] , "cookie" : controller.get("user-cred"), "price" : records['price'] , "date" : records['date'] , "item_id": records["item_id"] ,"dept_id" : records['dept_id'], "qty_sold" : records['qty_sold']})
            








            # inserting file into sqlserver
            insert_stmt1 = sqlalchemy.text(
                "INSERT INTO STORE (store_id, cookie) VALUES (:store_id, :cookie)",
            )

            insert_stmt2 = sqlalchemy.text(
                "INSERT INTO SALE (store_id, cookie, price, date, qty_sold, item_id, dept_id) VALUES (:store_id, :cookie, :price, :date, :qty_sold, :item_id, :dept_id)",
            )



            conn.execute (insert_stmt1, parameters={"store_id" : records['store_id'] , "cookie" : controller.get("user-cred") })
            conn.execute (insert_stmt2, parameters={"store_id" : records['store_id'] , "cookie" : controller.get("user-cred"), "price" : records['price'] , "date" : records['date'] , "item_id": records["item_id"], "dept_id" : records['dept_id'], "qty_sold" : records['qty_sold']})

            db_conn.commit()
'''
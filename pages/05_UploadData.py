
import streamlit as st
import pandas as pd
import os
# Upload file command for use to upload there file

from google.oauth2 import service_account
import json
from google.cloud.sql.connector import Connector, IPTypes
import pyodbc
from streamlit_cookies_controller import CookieController






controller = CookieController()

# Set a cookie
controller.set('user-cred', 'testing')


# Create credential for oauth flow


credentials = service_account.Credentials.from_service_account_info( st.secrets.service_acc
  , scopes=["https://www.googleapis.com/auth/sqlservice.admin"]
 )




'''
# initialize connector
connector = Connector()

# getconn now set to private IP
def getconn():
    conn = connector.connect(
      "stellar-sunrise-421203:australia-southeast2:client", # <PROJECT-ID>:<REGION>:<INSTANCE-NAME>
      "pytds",
      user= 'sqlserver',
      password= 'eZZ+6]E9(xN*}7',

      db='34.129.166.10',
      ip_type= IPTypes.PRIVATE
    )
    return conn

# create connection pool
pool = sqlalchemy.create_engine(
    "mssql+pytds://",
    creator=getconn,
)
'''


@st.cache_resource
def init_connection():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};SERVER="
        + "34.129.166.10"
        + ";DATABASE="
        + "stellar-sunrise-421203:australia-southeast2:client"
        + ";UID="
        + "sqlserver"
        + ";PWD="
        + "eZZ+6]E9(xN*}7"
    )


conn = init_connection()


# streamlit code to upload file and insert them into database


@st.cache_data(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()



data_cvs = st.file_uploader("choose a csv file")


if data_cvs is not None:
    # read file using pandas
    df = pd.read_csv(data_cvs.path)
    # check file format
    #add file format check here ************ IMPORTANT ***************

    #add quit exit condition if file is not correct

    for records in df:

        insert_stmt1= 'INSERT INTO STORE (store_id, cookie) VALUES (?, ?)'


        insert_stmt2= 'INSERT INTO SALE (store_id, cookie, price, date,  item_id, dept_id, qty_sold,) VALUES (?,?,?,?,?,?,?)'

        for records in df:
            conn.execute(insert_stmt1,
                         [records['store_id'], controller.get("user-cred")])
            conn.execute(insert_stmt2,
                          [records['store_id'], controller.get("user-cred"),
                                     records['price'],records['date'], records['item_id'], records['dept_id'],
                                     records['qty_sold']])








'''
    # inserting file into sqlserver
    insert_stmt1 = sqlalchemy.text(
        "INSERT INTO STORE (store_id, cookie) VALUES (:store_id, :cookie)",
    )

    insert_stmt2 = sqlalchemy.text(
        "INSERT INTO SALE (store_id, cookie, price, date, qty_sold, item_id, dept_id) VALUES (:store_id, :cookie, :price, :date, :qty_sold, :item_id, :dept_id)",
    )

    for records in df:

        conn.execute (insert_stmt1, parameters={"store_id" : records['store_id'] , "cookie" : controller.get("user-cred") })
        conn.execute (insert_stmt2, parameters={"store_id" : records['store_id'] , "cookie" : controller.get("user-cred"), "price" : records['price'] , "date" : records['date'] , "dept_id" : records['dept_id'], "qty_sold" : records['qty_sold']})

    db_conn.commit()'''

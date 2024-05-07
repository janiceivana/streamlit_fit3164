
import streamlit as st
import pandas as pd
import os
# Upload file command for use to upload there file
import sqlalchemy
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





# initialize connector
connector = Connector()

# getconn now set to private IP
def getconn():
    conn = connector.connect(
      "stellar-sunrise-421203:australia-southeast2:client", # <PROJECT-ID>:<REGION>:<INSTANCE-NAME>
      "pyodbc",
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

conn = connector.connect()

server = "34.129.166.10"
database = "stellar-sunrise-421203:australia-southeast2:client"
username = "sqlserver"
password = "eZZ+6]E9(xN*}7"

'''
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};\
                      SERVER='+server+';\
                      DATABASE='+database+';\
                      UID='+username+';\
                      PWD='+ password)



# streamlit code to upload file and insert them into database


@st.cache_data(ttl=600)
def run_query(query):
    with cnxn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

'''



data_cvs = st.file_uploader("choose a csv file")


if data_cvs is not None:
    # read file using pandas
    df = pd.read_csv(data_cvs.path)
    # check file format
    #add file format check here ************ IMPORTANT ***************

    #add quit exit condition if file is not correct
    with pool.connect() as db_conn:

        for records in df:
            '''
            insert_stmt1= 'INSERT INTO STORE (store_id, cookie) VALUES (?, ?)'
    
    
            insert_stmt2= 'INSERT INTO SALE (store_id, cookie, price, date,  item_id, dept_id, qty_sold,) VALUES (?,?,?,?,?,?,?)'
    
    
            cnxn.execute(insert_stmt1, {"store_id" : records['store_id'], "cookie" :controller.get("user-cred")})
            cnxn.execute(insert_stmt2, {"store_id" : records['store_id'] , "cookie" : controller.get("user-cred"), "price" : records['price'] , "date" : records['date'] , "item_id": records["item_id"] ,"dept_id" : records['dept_id'], "qty_sold" : records['qty_sold']})
            '''








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

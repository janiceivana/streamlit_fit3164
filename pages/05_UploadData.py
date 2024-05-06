
import streamlit as st
import pandas as pd
import os
# Upload file command for use to upload there file

from google.oauth2 import service_account
import json
from google.cloud.sql.connector import Connector, IPTypes
import sqlalchemy
from streamlit_cookies_controller import CookieController



st.write(st.secrets["key"])


st.set_page_config('Cookie QuickStart', '🍪', layout='wide')

controller = CookieController()

# Set a cookie
controller.set('user-cred', 'testing')





# Create credential for oauth flow
info1= json.loads( st.secrets)

credentials = service_account.Credentials.from_service_account_info( info = info1
  , scopes=["https://www.googleapis.com/auth/sqlservice.admin"]
 )


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




# streamlit code to upload file and insert them into database



data_cvs = st.file_uploader("choose a csv file")
if data_cvs is not None:
    # read file using pandas
    df = pd.read_csv(data_cvs.path)
    # check file format
    #add file format check here ************ IMPORTANT ***************

    #add quit exit condition if file is not correct

    # inserting file into sqlserver
    insert_stmt1 = sqlalchemy.text(
        "INSERT INTO STORE (store_id, cookie) VALUES (:store_id, :cookie)",
    )

    insert_stmt2 = sqlalchemy.text(
        "INSERT INTO SALE (store_id, cookie, price, date, qty_sold, item_id, dept_id) VALUES (:store_id, :cookie, :price, :date, :qty_sold, :item_id, :dept_id)",
    )
    with pool.connect() as db_conn:
        for records in df:

            db_conn.execute(insert_stmt1, parameters={"store_id" : records['store_id'] , "cookie" : controller.get("user-cred") })
            db_conn.execute(insert_stmt2, parameters={"store_id" : records['store_id'] , "cookie" : controller.get("user-cred"), "price" : records['price'] , "date" : records['date'] , "dept_id" : records['dept_id'], "qty_sold" : records['qty_sold']})

    db_conn.commit()


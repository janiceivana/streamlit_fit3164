
import streamlit as st
import pandas as pd
import os
# Upload file command for use to upload there file

data_cvs = st.file_uploader("", type=None, accept_multiple_files=["csv"], key=None, help=" click here to upload file into database", on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")
if data_cvs is not None:
    # read file using pandas
    df = pd.read_csv(data_cvs.path)

    # check file format
    #add file format check here ************ IMPORTANT ***************

    #add quit exit condition if file is not correct

    #set default credential:
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path_to_your_.json_credential_file"

    #inserting file into sqlserver

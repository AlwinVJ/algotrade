import gspread as gs
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

def authorize_google_sheets(creds_path):
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name(creds_path, scope)
    client = gs.authorize(creds)
    
    return client

def upload_dataframe(sheet, df, tab_name):
    try:
        try:
            worksheet = sheet.worksheet(tab_name)
            worksheet.clear()
        except gs.exceptions.WorksheetNotFound:
            worksheet = sheet.add_worksheet(title = tab_name, rows="100", cols="20")
        
        data = [df.columns.values.tolist()] + df.values.tolist()
        worksheet.update("A1",data)
        
    except Exception as e:
        print(f"Error uploading to tab {tab_name}: ", e)
        

def upload_summary(sheet, summary_dict, tab_name="Summary"):
    df_summary = pd.DataFrame([summary_dict])
    upload_dataframe(sheet, df_summary, tab_name)
    
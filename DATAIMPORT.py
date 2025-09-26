#IMPORTS PACKAGES
import arcpy
import urllib.request
import zipfile
import os
import sys
import pandas as pd
from datetime import datetime
import tempfile

arcpy.env.overwriteOutput = True

#DEFINES VARIABLES
current_year = datetime.now().strftime("%Y")
today_date = datetime.now().strftime("%m%d%Y")
url = "http://www.muskingumcountyauditor.org/api/Document/GISExtract.zip"


#USES TEMP DIR TO MAKE PORTABLE 
download_folder = tempfile.gettempdir()
arcpy.AddMessage(f"Using download folder: {download_folder}")


#CHECKS THAT NETWORK PATH EXISTS
network_extract_folder = rf"\\MCGIS\Data\MapData\Parcel\{current_year}\{today_date}"
local_extract_folder = os.path.join(download_folder, f"ParcelExtract_{today_date}")


#TRYS NETWORK PATH FIRST, LOCAL IF NETWORK IS UNAVAILABLE
if os.path.exists(r"\\MCGIS\Data\MapData\Parcel"):
    extract_folder = network_extract_folder
    arcpy.AddMessage(f"Using network storage: {extract_folder}")
else:
    extract_folder = local_extract_folder
    arcpy.AddMessage(f"Network path unavailable, using local: {extract_folder}")

outputtable=os.path.join(extract_folder, "ParcelGIS_ExcelToTable")    

#CREATES FOLDER IF DOESNT EXIST
try:
    os.makedirs(extract_folder, exist_ok=True)
    arcpy.AddMessage(f"Extract folder created/verified: {extract_folder}")
except Exception as e:
    arcpy.AddError(f"Cannot create extract folder: {e}")
    sys.exit()

#DEFINES THE ZIP FILE PATH
zip_file_path = os.path.join(download_folder, "GISExtract.zip")


#DOWNLOADS & EXTRACTS 
try:
    arcpy.AddMessage(f"Downloading file from {url}...")
    urllib.request.urlretrieve(url, zip_file_path)
    arcpy.AddMessage(f"File downloaded successfully to {zip_file_path}")

    arcpy.AddMessage(f"Extracting file to {extract_folder}...")
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_folder)
    arcpy.AddMessage("Extraction complete.")
    
except Exception as e:
    arcpy.AddError(f"Error downloading/extracting the file: {e}")
    sys.exit()


#DEFINES EXCEL FILE
excel_file_path = os.path.join(extract_folder, "Parcel GIS.xlsx")


#ADDS EXCEL ERROR
try:
    arcpy.AddMessage(f"Processing Excel file: {excel_file_path}")
    
    #9.1 CHECK IF FILE EXISTS
    if not os.path.exists(excel_file_path):
        arcpy.AddError(f"Excel file not found: {excel_file_path}")
        #LIST FILES IN DIRECTORY TO SEE WHAT'S THERE
        arcpy.AddMessage("Files in extract folder:")
        for file in os.listdir(extract_folder):
            arcpy.AddMessage(f"  - {file}")
        sys.exit()


    #READS EXCEL FILE
    df = pd.read_excel(excel_file_path, sheet_name="Sheet 1")
    arcpy.AddMessage("Excel file read successfully")


    #9REMOVES SPACES FROM FIELD NAMES
    df.columns = df.columns.str.replace(' ', '')
    arcpy.AddMessage(f"Cleaned column names: {list(df.columns)}")

    #SAVSE MODIFIED FILE AS XLSX
    modified_file_path = os.path.join(extract_folder, "ParcelGIS.xlsx")
    df.to_excel(modified_file_path, sheet_name="Sheet1", index=False)
    arcpy.AddMessage(f"Modified XLSX file saved to: {modified_file_path}")

except Exception as e:
    arcpy.AddError(f"Error processing Excel file: {e}")
    sys.exit()

#SETS THE OUTPUT PARAMETER
arcpy.SetParameterAsText(0, modified_file_path)
arcpy.AddMessage("Script completed successfully!")


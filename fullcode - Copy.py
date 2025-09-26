#0. IMPORT PACKAGES
import arcpy
import urllib.request
import zipfile
import os
import sys
import pandas as pd
from datetime import datetime
import tempfile

arcpy.env.overwriteOutput = True

#1.0 DEFINE VARIABLES
current_year = datetime.now().strftime("%Y")
today_date = datetime.now().strftime("%m%d%Y")

#3.0 CHECK IF NETWORK PATH EXISTS
extract_folder = rf"\\MCGIS\Data\MapData\Parcel\{current_year}\{today_date}"
ISSG_file_unconverted= os.path.join(extract_folder, "ParcelGIS.xlsx")
outtable= os.path.join(extract_folder, "ParcelGIS")

# Check if input exists
if arcpy.Exists(ISSG_file_unconverted):
    arcpy.AddMessage("ISSG unconverted Excel File found successfully")

    #Create table
    arcpy.AddMessage("Converting Excel to table...")
    arcpy.conversion.ExcelToTable(
        Input_Excel_File=ISSG_file_unconverted,
        Output_Table=outtable,
        Sheet="Sheet1",
        field_names_row=1,
        cell_range=""
    )
    arcpy.AddMessage("Excel to Table conversion complete!")

# SET THE OUTPUT PARAMETER
arcpy.SetParameterAsText(0, outtable)
arcpy.AddMessage("Script completed successfully!")








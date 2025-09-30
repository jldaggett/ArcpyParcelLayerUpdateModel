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

#CHECKS IF NETWORK PATH EXISTS
extract_folder = rf"\\MCGIS\Data\MapData\Parcel\{current_year}\{today_date}"
ISSG_file_unconverted= os.path.join(extract_folder, "ParcelGIS.xlsx")
outtable= os.path.join(extract_folder, "ParcelGIS")

#CHECKS IF INPUT EXISTS
if arcpy.Exists(ISSG_file_unconverted):
    arcpy.AddMessage("ISSG unconverted Excel File found successfully")

    #CREATES DBTABLE
    arcpy.AddMessage("Converting Excel to table...")
    arcpy.conversion.ExcelToTable(
        Input_Excel_File=ISSG_file_unconverted,
        Output_Table=outtable,
        Sheet="Sheet1",
        field_names_row=1,
        cell_range=""
    )
    arcpy.AddMessage("Excel to Table conversion complete!")

#SETS OUTPUT PARAMETER
arcpy.SetParameterAsText(0, outtable)
arcpy.AddMessage("Script completed successfully!")









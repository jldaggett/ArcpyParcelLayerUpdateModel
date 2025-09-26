#IMPORT PACKAGES
import arcpy
import sys

# GET INPUT TABLE PARAMETER FROM MODEL BUILDER (JOINED TABLE)
input_table = arcpy.GetParameterAsText(0)

#CALCULATE FIELDS (MULTIPLE)
try:
    arcpy.management.CalculateFields(
        in_table=input_table,
        expression_type="PYTHON3",
        fields=[
            ["SCANLINK", r'"\\mcgis\Data\SCANS\SURVEY 2\\" + !TOWNSHIP! + "\\" + !TOWNSHIP! + "-" + !MAP_NUM! + "\\" + !OLDPARCEL! + ".tif"'],
            ["AUDLINK", r'"https://www.muskingumcountyauditor.org//detail.aspx?number=" + !PARCELNUM!'],
            ["TAXMAPLINK", r'"\\mcgis\data\SCANS\TAX MAPS\TAX MAPS 2004 PDF\\" + !TOWNSHIP! + "\\" + !MAP_NUM! + ".pdf"'],
            ["ISSG", r'"https://muskingum-real.issg.io/RealEstate/Appraisal?ParcelNumber=" + !OLDPARCEL!'],
            ["SCANLINK_P", r'"\\mcgis\Data\SCANS\SURVEY 2\\" + !TOWNSHIP! + "\\" + !TOWNSHIP! + " " + !MAP_NUM! + "\\" + !OLDPARCEL! + ".pdf"'],
            ["DBRef", "!DeedVolume!"],
            ["DPRef", "!DeedPage!"],
            ["DeedVolume", "str(!DBRef!)"],
            ["DeedPage", "str(!DPRef!)"],
            ["RecLink", r'"https://cotthosting.com/ohmuskingum/LandRecords/protected/SrchBookPage.aspx?bAutoSearch=true&bk=" + !DeedVolume! + "&pg=" + !DeedPage! + "&idx=OFF"']
        ],
        code_block="",
        enforce_domains="NO_ENFORCE_DOMAINS"
    )
    arcpy.AddMessage("Export Complete!")
    
except Exception as e:
    arcpy.AddError(f"Error during export: {e}")
    sys.exit()

# SET OUTPUT PARAMETER
arcpy.SetParameterAsText(0, input_table)

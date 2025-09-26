#IMPORTS PACKAGES
import arcpy
import os
import sys
import tempfile
from datetime import datetime


#GETS INPUT TABLE PARAMETER FROM MODEL BUILDER (JOINED TABLE)
input_table = arcpy.GetParameterAsText(0)

# GET OUTPUT LOCATION OF EXPORTED JOIN FILE
network_export_file = arcpy.GetParameterAsText(1)

#DEFINES VARIABLES
current_year = datetime.now().strftime("%Y")
today_date = datetime.now().strftime("%m%d%Y")

#SETS UP FOLDER PATHS
network_export_folder = rf"\\MCGIS\Data\MapData\Parcel\{current_year}\{today_date}"
network_export_file = os.path.join(network_export_folder, "TAXPARCEL")

#EXPORTS JOINED TABLE
try:
    arcpy.AddMessage("Exporting Joined Table...")
    arcpy.conversion.ExportFeatures(
        in_features = input_table,
        out_features = network_export_file,
        where_clause = "",
        use_field_alias_as_name ="NOT_USE_ALIAS",
        field_mapping="",
        sort_field=""
    )
    arcpy.AddMessage("Export Complete!")
except Exception as e:
    arcpy.AddError(f"Error during export: {e}")
    sys.exit()
    
#SETS OUTPUT PARAMETER
arcpy.SetParameterAsText(1, network_export_file)
arcpy.AddMessage(f"Export complete! Output saved to: {network_export_file}")

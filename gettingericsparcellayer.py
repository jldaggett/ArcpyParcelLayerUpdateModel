import arcpy

# Hardcoded path - no input parameter needed
parcels_fc = r"\\mcgis\Data\MapData\Parcel\Parcel Fabric\Live\Live.gdb\Parcel_live\Parcels"

# Create the feature layer
output_layer_name = "EricsParcelLayer"

# Check if input exists
if arcpy.Exists(parcels_fc):
    arcpy.AddMessage("Eric's Parcel Feature Class found successfully")
    
    # Create the feature layer
    arcpy.management.MakeFeatureLayer(parcels_fc, output_layer_name)
    arcpy.AddMessage(f"Created feature layer: {output_layer_name}")
    
    # Set the output parameter so Model Builder can use it
    arcpy.SetParameterAsText(0, output_layer_name)  # Output: Feature Layer
    
else:
    arcpy.AddError(f"Parcel feature class not found: {parcels_fc}")

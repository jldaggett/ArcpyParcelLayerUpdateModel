import arcpy

#GRABS PARCEL LAYER VIA HARDCODED PATH & ASSIGNS VARIABLE
parcels_fc = r"\\mcgis\Data\MapData\Parcel\Parcel Fabric\Live\Live.gdb\Parcel_live\Parcels"

#CREATES OUTPUT VARIABLE
output_layer_name = "EricsParcelLayer"

#CHECKS THAT INPUT EXISTS
if arcpy.Exists(parcels_fc):
    arcpy.AddMessage("Eric's Parcel Feature Class found successfully")
    
    #CREATES FEATURE LAYER
    arcpy.management.MakeFeatureLayer(parcels_fc, output_layer_name)
    arcpy.AddMessage(f"Created feature layer: {output_layer_name}")
    
    #SETS THE OUTPUT LAYER
    arcpy.SetParameterAsText(0, output_layer_name)
    
else:
    arcpy.AddError(f"Parcel feature class not found: {parcels_fc}")


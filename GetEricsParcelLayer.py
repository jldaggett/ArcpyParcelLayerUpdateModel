import arcpy

#GRABS PARCEL LAYER VIA HARDCODED PATH & ASSIGNS VARIABLE
parcels_fc = r"\\mcgis\Data\MapData\Parcel\Parcel Fabric\Live\Live.gdb\Parcel_live\Parcels"

#CREATES OUTPUT VARIABLE
output_layer_name = "EricsParcelLayer"

#CHECKS THAT INPUT EXISTS
if arcpy.Exists(parcels_fc):
    arcpy.AddMessage("Eric's Parcel Feature Class found successfully")
    
    #CREATES FEATURE LAYER
    arcpy.management.MakeFeatureLayer(
    in_features= parcels_fc,
    out_layer= output_layer_name,
    where_clause="RetiredByRecord IS NULL",
    workspace=None,
    field_info="OBJECTID OBJECTID VISIBLE NONE;Shape Shape VISIBLE NONE;Name Name VISIBLE NONE;CreatedByRecord CreatedByRecord VISIBLE NONE;RetiredByRecord RetiredByRecord VISIBLE NONE;StatedArea StatedArea VISIBLE NONE;StatedAreaUnit StatedAreaUnit VISIBLE NONE;CalculatedArea CalculatedArea VISIBLE NONE;MiscloseRatio MiscloseRatio VISIBLE NONE;MiscloseDistance MiscloseDistance VISIBLE NONE;IsSeed IsSeed VISIBLE NONE;created_user created_user VISIBLE NONE;created_date created_date VISIBLE NONE;last_edited_user last_edited_user VISIBLE NONE;last_edited_date last_edited_date VISIBLE NONE;Shape_Length Shape_Length VISIBLE NONE;Shape_Area Shape_Area VISIBLE NONE;GlobalID GlobalID VISIBLE NONE;VALIDATIONSTATUS VALIDATIONSTATUS VISIBLE NONE;OLDPARCEL OLDPARCEL VISIBLE NONE;ACODE ACODE VISIBLE NONE;SUBREF SUBREF VISIBLE NONE;SUBCODE SUBCODE VISIBLE NONE;CALC_ACR CALC_ACR VISIBLE NONE;PBOOK PBOOK VISIBLE NONE;PPAGE PPAGE VISIBLE NONE;SCH_DIST SCH_DIST VISIBLE NONE;TOWNSHIP TOWNSHIP VISIBLE NONE;MAP_NUM MAP_NUM VISIBLE NONE;BLOCK_SECT BLOCK_SECT VISIBLE NONE;PARCEL PARCEL VISIBLE NONE;SPLIT SPLIT VISIBLE NONE;PARCELNUM PARCELNUM VISIBLE NONE;DATEUPDATE DATEUPDATE VISIBLE NONE;SURVEYOR SURVEYOR VISIBLE NONE;StampDate StampDate VISIBLE NONE;Approved Approved VISIBLE NONE;NOTES NOTES VISIBLE NONE;SCANLINK SCANLINK VISIBLE NONE;AUDLINK AUDLINK VISIBLE NONE;TAXMAPLINK TAXMAPLINK VISIBLE NONE;DBRef DBRef VISIBLE NONE;DPRef DPRef VISIBLE NONE;RecLink RecLink VISIBLE NONE;PicLin PicLin VISIBLE NONE;Shape_Leng Shape_Leng VISIBLE NONE;SCANLINK_P SCANLINK_P VISIBLE NONE;ISSG ISSG VISIBLE NONE"
)
    arcpy.AddMessage(f"Created feature layer: {output_layer_name}")
    
    #SETS THE OUTPUT LAYER
    arcpy.SetParameterAsText(0, output_layer_name)
    
else:
    arcpy.AddError(f"Parcel feature class not found: {parcels_fc}")



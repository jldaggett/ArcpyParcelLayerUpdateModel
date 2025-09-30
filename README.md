These are scripts that were inputted into Script tools which I placed in a model I built for in ArcGIS Pro for Muskingum County Auditor's GIS Department. It was created to help streamline our parcel layer updating process.

BELOW ARE EXPLANATIONS FOR WHAT EACH PART OF THE MODEL DOES:

  #DataImport
      This tool:
          - pulls the Parcel Layer zip file from an api
          - downloads the zip from the api into a temporary folder
          - creates a permanent folder on our server with the {current year} and then a folder inside of that with the {today's date}
          - in that {today's date} folder, it extracts the contents of the zip file
          - removes spaces from the field names in the excel file that was extracted from the zip file
          - saves table and makes that file path the output [ISSG_Data]


#ConversionTool
      This tool:
          - grabs the excel file from the output of the previous tool (this is in .xlsx format)
          - runs the ArcGIS Pro geoprocessing tool called "ExcelToTable" which convert the .xlsx to a .dbf
          - saves the table and makes it the output for this tool [ConvertedTable]


#GetEricsParcelLayer
      This tool:
          - grabs the parcel layer whose geometry is edited/updated by the Map Dept's Engineer
          - makes that a feature layer and sets it as the output [EricParcel]


#"AddJoin"
    //I did not script this tool. It is a geoprocessing tool on ArcGIS Pro and I simply pulled it into my model and set the parameters as my two outputs from previous script tools: [ConvertedTable] and [EricParcel]


#ExportJoin
      This tool:
          - finds the folder path using the folders we created in the DataImport.py tool: {current year}/{today's date}
          - exports the joined table (the output of AddJoin: [JoinedTable]) to the file path above
          - makes the exported join the output parameter, [Output_ExportedFC]


#MultipleFieldCalc
      This tool:
          - calculates fields of the output from the previous tool
          - we do this because, for example some of our fields contain hyperlinks which are calculated using deed book and page or parcel numbers. when a new parcel gets created or a piece of property is sold, these fields that calculate the links are either 
            updated/changed or are new additions to the database.
          - my coworker Jacob Smelker, another GIS Analyst, helped write some of this code for the field calculations

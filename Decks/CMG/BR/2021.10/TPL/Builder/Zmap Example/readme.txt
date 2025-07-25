This foldercontains files that will help the user get more familiar with importing different types of files into a dataset that uses ZMAP contour maps. 
Note: This example does not produce a completed dataset for simulation.

Files for Dataset Setup:
====================================
dev_well.dat - Builder dataset which can be opened before opening the other files in the folder


Map Files
-------------------------------------------------------------------
zmapcntr.dat - Top of structure map file in ZMAP CNTR format

zmapflt.dat - ZMAP fault file that can be used for CNTR or GRID format

zmapgrid.dat - Top of structure map file in ZMAP GRID format 

porosity.msh - Map file used for the specification of porosity

porosity picks.xls - Data can be used to re-create porosity.msh


Trajectory Files
-------------------------------------------------------------------
output.wdb - Trajectory file in Table format which can be used

zmapwell3.dat - Trajectory file in ZMAP format


Perf File
--------------------------------------------------------------------
zmap5.perf - Perforation location file for the Dev_well dataset.  After the trajectory information is imported, 
             perforation information can be imported through the "Trajectory Perforation Intervals" dialog.


Other Properties
---------------------------------------------------------------------
PVT.xls - After setting the Model type in dev_well.dat, data in this Excel file can be used for the PVT Region table

RelPermTable1.xls & RelPermTable2.xls - Data can be used for the specification of two rock types.  





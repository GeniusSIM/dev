This directory contains map, well trajectory and well log template files for use with Builder, as well as some RESCUE sample files.


A break down of these folders is as follows:

(1) Maps - Examples of different geological map types that can be opened in Builder
(2) RESCUE - Examples of RESCUE format files that can be opened in Builder
(3) Trajectories - Examples of different well trajectory formats that can be imported in Builder by using the "Import Well Trajectory Wizard".
(4) Waterflood Example - Example dataset that can be opened in Builder.  A top of structure map and a thickness map are included in WINDIG format.
(5) Well Logs - Example Log data in different formats that can be imported.
(6) Zmap Example - Contains the components for working with a dataset that uses ZMAP contour maps

There are three main sets of data, in addition to some extra map files, trajectories, logs and RESCUE files:

(1) 'Waterflood Example' folder - Example of WINDIG contour maps and a corresponding dataset.  The folder is located under the Builder folder.   
        watfldTop.dig    - Top of structure map in WINDIG format
        watfldThick.dig  - Thickness map in WINDIG format

     Some additional files that can be used with the Waterflood dataset are located in other folders:        
        
        watfld.dev       - PA format deviated well trace.  Located in Builder\Trajectories\Production Analyst.
        watfld.xy        - PA format surface locations.  Located in Builder\Trajectories\Production Analyst.  
        watfld.perf      - perforation locations.  Located in Builder\Trajectories\Production Analyst.
        watfldtb.wlg    - Multiple well log format file.  Located in Builder\Well Logs\CMG\MultipleWells.
        watfld.las       - LAS format log file.  Located in Builder\WellLogs\LAS.


(2) 'Zmap Example' folder - Examples of geological data in ZMAP format.  Folder is located under the Builder folder.

        dev_well.dat     - Builder dataset which can be opened before opening the other files in the folder.
        zmapgrid.dat    - Top of structure map file in ZMAP GRID format 
        zmapcntr.dat    - Top of structure map file in ZMAP CNTR format
        zmapflt.dat       - ZMAP fault file that can be used for CNTR or GRID format
        zmapdwel3.dat - Trajectory file in ZMAP format
        zmap5.perf       - Perforation location file for the Dev_well dataset.  After the trajectory information is imported, 
                                 perforation information can be imported through the "Trajectory Perforation Intervals" dialog.


(3) 'EarthVision' folder - Example of a zone with sloping faults.  Folder is located under the Builder\Maps folder.  
        evbottom.dat      - EarthVision grid export format for bottom of structure
        evbottom.vflt      - EarthVision fault export format giving fault locations on bottom
        evporosity.dat    - EarthVision grid export format for zone porosity
        evporosity.vflt     - EarthVision fault export format giving fault locations on top
        evtop.dat           - EarthVision grid export format for top of structure
        evtop.vflt            - EarthVision fault export format giving fault locations on top



PTubeCalculator
=================

The PTubeCalculator directory contains three wellbore calculator input files that can be used with the Tubing Tables feature in Builder.

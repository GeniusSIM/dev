~VERSION INFORMATION       
 VERS.                 3.0:   CWLS LOG ASCII STANDARD - VERSION 2.0 
 WRAP.                  NO:   ONE LINE PER DEPTH STEP
 DLM .               SPACE: DELIMITING CHARACTER BETWEEN DATA COLUMNS 
~WELL INFORMATION BLOCK
#MNEM.UNIT        DATA              DESCRIPTION OF MNEMONIC    
#---------    -------------         ------------------------
 STRT .M              1670.0000                : First Index Value
 STOP .M               713.2500                : Last Index Value 
 STEP .M              -0.1250                  : STEP 
 NULL .               -999.25                  : NULL VALUE
 COMP .       ANY OIL COMPANY INC.             : COMPANY
 WELL .       W-12                            :WELL NAME  
 FLD  .       WILDCAT                          : FIELD
 LOC  .       12-34-12-34W5M                   : LOCATION
 PROV .       ALBERTA                          : PROVINCE 
 SRVC .       ANY LOGGING COMPANY INC.         : SERVICE COMPANY
 DATE .       01-JAN-1988                      : LOG DATE  {DD/MMM/YYYY}
 UWI  .       W-12		               : UNIQUE WELL ID
 API  .       12345678                         : API NUMBER
# LAT .DEG                             34.56789 : Latitude  {DEG}
# LONG.DEG                           -102.34567 : Longitude  {DEG}
# Lat & Long can also be presented as:
# LAT .DEG                           34/34/4.4 : Latitude  {DEG/MIN/SEC}
# LONG.DEG                        -102/20/44.4 : Longitude  {DEG/MIN/SEC}
 UTM  .                                        : UTM LOCATION
 X    .M       1448.2                          : X LOCATION
 Y    .M       1715                            : Y LOCATION
~CURVE INFORMATION      
#MNEM.UNIT      API CODE      CURVE DESCRIPTION
#---------    -------------   ------------------------------
 DEPT.M                      :  1  DEPTH
 DT2 .US/M                   :  2  SONIC TRANSIT TIME
 RHOB.K/M3                   :  3  BULK DENSITY
 NPHI.V/V                    :  4  NEUTRON POROSITY
 SFLU.OHMM                   :  5  RXO RESISTIVITY
 SFLA.OHMM                   :  6  SHALLOW RESISTIVITY
 ILM .OHMM                   :  7  MEDIUM RESISTIVITY
 ILD .OHMM                   :  8  DEEP RESISTIVITY
 SP  .OHMM                   :  9  SPONTANEOUS POTENTIAL
 GR  .GAPI                   : 10  GAMMA RAY
 CALI.MM                     : 11  CALIPER
 DRHO.K/M3                   : 12  DENSITY CORRECTION
~PARAMETER INFORMATION       
#MNEM.UNIT        VALUE       DESCRIPTION OF MNEMONIC
#---------    -------------   ------------------------------
 BHT .DEGC         35.5000:   BOTTOM HOLE TEMPERATURE
 BS  .MM          200.0000:   BIT SIZE
 FD  .K/M3       1000.0000:   FLUID DENSITY
 MATR.           SANDSTONE:   NEUTRON MATRIX
 MDEN.              2650.0:   LOGGING MATRIX DENSITY
 RMF .OHMM          0.2160:   MUD FILTRATE RESISTIVITY
 DFD .K/M3       1525.0000:   DRILL FLUID DENSITY
~A  DEPTH      DT2        RHOB       NPHI       SFLU       SFLA       ILM        ILD        SP         GR         CALI       DRHO
1929.0000   406.0000  2334.7658     0.3948     2.5262     2.5262     2.4769         2.0758    -0.5005    78.1250   328.9724     5.9473
1928.1150   406.0000  2323.4088     0.3492     2.5262     2.5262     2.4769         2.0742    -0.0930    78.1250   336.1309     6.4924
1927.9050   406.0000  2329.4088     0.3892     2.5262     2.5262     2.4769         2.0742    -0.0930    78.1250   336.1309     6.4924
1926.7500   406.0000  2319.4548     0.3839     2.5262     2.5262     2.4769         2.0752    -0.0005    78.1250   329.6516     6.7535
1925.6250   406.0000  2314.5724     0.3918     2.5262     2.5262     2.4769         2.0783     0.2272    78.1250   322.2677     8.9939
1925.2000   406.0000  2315.0783     0.4009     2.5262     2.5262     2.4769         2.0810     0.4995    78.1250   319.6201    11.0514
1924.3750   406.0000  2316.9758     0.3927     2.5262     2.5262     2.4754         2.0811     0.4516    78.1250   321.2740     9.7426
1923.2500   406.0000  2325.6233     0.3957     2.5262     2.5262     2.4625         2.0848     0.0415    78.1250   321.4790    10.3931
~Inclinometry_Definition
MD.  M                                  : Measured Depth        {F}
AZIM.DEG                                : Borehole Azimuth      {F}
DEVI.DEG                                : Borehole Deviation    {F}
~Inclinometry | Inclinometry_Definition
1896 300.00 0.00
1929 300.00 0.00
~Perforations_Definition
 PERFT.M                                : Perforation Top Depth    {F}
 PERFB.M                                : Perforation Bottom Depth {F}
 PERFD.SHOTS/M                          : Shots per meter          {F}
 PERFT.                                 : Charge Type              {S}
~Perforations | Perforations_Definition
1925 1926 12 big
1927 1928 12 big




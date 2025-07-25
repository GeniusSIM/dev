
                   User Notes for STARS 2021.10
                   ============================

Purpose of 2021.10 Release
--------------------------

STARS 2021.10 is the general STARS release for 2021.

What's New in STARS Version 2021.10
-----------------------------------

1) The description of new and improved features is available in "What's_New_in_STARS_2021.10.pdf".
   This release also includes bug fixes and code improvements implemented since STARS 2020.10.

2) Information about the compiler version and runtime libraries is available in
   "Linux_x64_runtime_environment_2021.pdf" and "Readme_Linux_libs_2021.pdf".


*************************************************************************************************************

                   User Notes for STARS 2020.10
                   ============================

Purpose of 2020.10 Release
--------------------------

STARS 2020.10 is the general STARS release for 2020.

What's New in STARS Version 2020.10
-----------------------------------

1) The description of new and improved features is available in "What's_New_in_STARS_2020.10.pdf".
   This release also includes bug fixes and code improvements implemented since STARS 2019.10.

2) Information about the compiler version and runtime libraries is available in
   "Linux_x64_runtime_environment_2020.pdf" and "Readme_Linux_libs_2020.pdf".


*************************************************************************************************************
                 
                   User Notes for STARS 2019.10
                   ============================

Purpose of 2019.10 Release
--------------------------

STARS 2019.10 is the general STARS release for 2019.

What's New in STARS Version 2019.10
-----------------------------------

1) The description of new and improved features is available in "What's New in STARS 2019_10.pdf".
   This release also includes bug fixes and code improvements implemented since STARS 2018.11.

2) Information about the compiler version and runtime libraries is available in
   "Linux_x64_runtime_environment_2019.pdf" and "Readme_Linux_libs_2019.pdf".


*************************************************************************************************************
                   
                   User Notes for STARS 2018.11
                   ============================

STARS 2018.11 is the general release update 1 for 2018. STARS 2018.11 has
many new and improved features detailed in "What's_New_in_STARS_2018.11.doc".
New and modified manual fragments and templates are available in
"doc\Other_Manual_Pages".


*************************************************************************************************************

                   User Notes for STARS 2018.10
                   ============================

Purpose of 2018.10 Release
--------------------------

STARS 2018.10 is the general STARS release for 2018.

What's New in STARS Version 2018
--------------------------------

SIMULATOR CHANGES
=================

Injection Options Enhancements

  New *INCOMP sub-keyword *MIXTURE-Z makes it possible to inject an arbitrary
  stream of components.  The operating constraint must be either the summed-phase
  rate specified with *OPERATE *STF or a pressure-type constraint. This option is
  general in nature and can handle the component/phase scenarios of all the other
  *INCOMP options (*WATER, *OIL, *GAS, *WATER-GAS-Z, *WATER-OIL-Z, and *WATER-GAS-OIL-Z).
  Unlike any other option, it can inject a two-phase mixture without aqueous components.
  *MIXTURE-Z must be used together with *PINJW and new keyword *HINJW (which specifies
  the molar enthalpy of the injected fluid).
  The *MIXTURE-Z option uses global mole fractions z1 . . . znumy, pressure and enthalpy
  as input and performs an isenthalpic flash to obtain the temperature, phase splits and
  phase compositions. Unlike the other *INCOMP options, this method makes no assumption
  for the existence of phases and therefore will always provide consistent result. 
  Therefore, the *MIXTURE-Z option is recommended for multi-phase mixtures over a wide
  temperature range. For example, it is best for steam injected with an engineered solvent
  comprised of several components of various volatilities, especially at temperatures
  outside the water saturation range at injection pressure. See template "stwwm150.dat"
  
Heater Cable Enhancements

  New *HEATER_CABLE sub-keyword *SECTIONS allows the user to define segmented heater cables
  with variable heat conduction rates along the well. New sub-keyword *CBL_PROP can be used
  to specify the diameter and number of cables. See template "stwwm096.dat"

Flow Control Device Table Enhancements

  New optional dependency *SUBCOOL is available for keyword *FCDTABLE. *SUBCOOL is defined
  as temperature difference between the saturation temperature of steam at inlet pressure
  and the inlet temperature. For example, if flow direction is from reservoir grid block
  to the wellbore grid block, *SUBCOOL is calculated by deducting the reservoir grid block
  temperature from the saturation temperature of steam at reservoir grid block pressure.
  See template "stwwm151.dat"

Wellbore Shear Effects

  New keyword *WELLSHEAR enables a modified form of radial inflow model which incorporates
  the shear effects in wellbore. The standard radial inflow model, used to couple the
  pressure in the wellbore to the average grid block pressure, is based on a steady-state
  Newtonian flow. However, experimental results have shown that for applications such as
  polymer flooding, the velocity dependence of viscosity must be taken into account for
  accurate modeling of wellbore flow. These effects are particularly important near the
  wellbore where shear has the strongest effect on viscosity. In the past users had to use
  local grid refinement around wells to capture the effects of non-Newtonian flow behaviors.
  With the new keyword, the use of fine grid could be avoided. See template "stflu072.dat"

Well Polymer Viscosity Adjustment 

  The effective aqueous phase viscosity in wellbore can now be adjusted using new keyword
  *WPLYFAC to account for the efficiency reduction during polymer injection. For wells
  perforated in relatively large blocks, the non-Newtonian rheological behavior of polymer
  may result in a very different water phase viscosity compared to block averaged value.
  In such a case, *WPLYFAC can also be applied as a history matching parameter to achieve
  the shear thinning ( factor < 1.0 ) or thickening effect (factor > 1.0 )near wellbore.
  See template "stflu073.dat"

Numerical Tuning Enhancements

  It's now possible to enable/disable *AUTOTUNE option in the recurrent section. *AUTOTUNE
  monitors variables such the maximum change of primary variables, number of iterations,
  number of cuts, etc. for previous time steps to determine the next time step size. For
  some operating scenarios, e.g. starting a new injection cycle, turning the tool *ON or
  *OFF might improve the numerical performance. See template "stsmo084.dat"

  To provide better control of material balance error and convergence algorithms, new
  *MATBALTOL sub-keywords *RMBE_STALL and *RMBE_RATIO can be used to prevent unnecessary
  extra Newton iterations while *MAX_REPEAT specifies the maximum allowed number of failures.
  See template "stwwm064.dat"
  
Incomplete Mixing

  New keyword *OMEGA_PW enables the Todd-Longstaff incomplete mixing algorithm for polymer
  injection. To model partially mixed polymer solutions, the mobility of aqueous phase and
  polymer solution must be modified. This can be achieved by using effective viscosity values
  in aqueous and polymer fluid flow equations. The legacy implementation, known to cause
  unphysical polymer buildup when injecting at a concentration less than the maximum reference
  (tapering), is also available for comparison with other commercial simulators.
  See template "stflu071.dat"

Adsorption Options Enhancements

  New keyword *SWIPV specifies the inaccessible water saturation volume of the selected rock
  type. Since a grid block's inaccessible water saturation volume should not exceed its water
  saturation, each block uses the minimum of Swipv and 0.999 × water saturation. Consequently,
  each block will use the specified Swipv value as long as its water saturation is high enough.
  See template "stflu071.dat"

  With new keywords *RRFTW, *RRFTO and *RRFTG, residual resistance factor of the adsorbing
  component can be defined separately for water, oil and gas phases, i.e. polymer/surfactant
  adsorption can impact the oil and water flows differently. See template "stflu071.dat"

Change of Default

  Extensive testing has demonstrated that over-relaxation of accumulation terms improves the
  Flexible Wellbore convergence for majority of models. Therefore *FW-RELAX-ACC *ON has become
  the default.

  *INTERP_SCAL *ON has become the default to avoid the need for manual adjustment of the
  endpoints of interpolation sets. Keyword *INTERP_ENDS is no longer required but will be
  supported for backward compatibility.

Output Enhancements

  New keywords *BLOCKP5 and *BLOCKP9 under *OUTSRF *WELL provide the pore-volume weighted
  average well block pressure. The average can be done for a 5-point pattern (well block
  plus four immediate neighboring blocks), or a 9-point pattern (by adding four more diagonal
  neighboring blocks on the same plane). See template "stwwm075.dat"

  New keywords *GGASIPn (n = 1, 2, or 3) under *OUTSRF *WELL allow the user to optionally
  output group(field) gas delivery capacity, when all well constraints are used, or only
  well pressure constraints are used, or when the wells are operated on a minimum BHP control
  of 1 atm. See template "stwwm075.dat"

  New keywords *DWN, *DWA, or *DWB under *OUTSRF *WELL allow the user to optionally output
  well-drawdown pressure. See template "stwwm075.dat"

  Oil, gas, and water stream mole fractions for individual wells and groups are now available
  for visualization using RESULTS. No keywords other when *OUTSRF *WELL *MOLE are required.

  When *WELLSHEAR is enabled, following outputs will be available with *OUTSRF *WELL *LAYER *ALL:
  - Well equivalent viscosity: average viscosity from wellbore radius to Peaceman radius,
    which could be compared with layer water Newtonian viscosity.
  - Well viscosity at reference radius to show the radial dependency of shear effects.

Obsolete Keyword
 
  Keyword *NEXTSEG is obsolete and will no longer be supported. The required functionality is
  available through trigger options. 


GEOMECHANICS CHANGES
====================

Parallel Solver for Geomechanics

  Geomechanics stiffness matrix for 3D strain problems (keyword *GEOM3D) can now be solved using
  parallel linear solver PARASOL which is activated automatically for models using PARASOL for
  flow calculations. Control parameters for Geomechanics solution can be specified by new
  keywords *SOLVERG *PARASOL, *PPATTERNG, *SDEGREEG, etc. in the Geomechanics section.
  Substantial improvement in run time is expected for coupled Geomechanics and fluid flow models
  especially in models with a large number of grid blocks. 

Shear Fracture Modeling 

  New keywords *USHEARST, *BBTENSH, *PERMODULUS, *SHPERMAX and *SHPERMRES are added to enhance
  the Barton-Bandis (BB) fracture modeling option. When shear failure occurs on a grid block,
  the tensile threshold used in the BB model can now be increased to facilitate fracturing.
  This allows the grid block to experience fracturing (due to tensile stress) much easier than
  a grid block without shear-failure. Further, the shear fracturing option also allows changing
  fracture permeability of a grid block. See templates "stgro093/95.dat"

  New keyword *USTRESTOT allows specification of fracturing threshold in the BB model as the total
  stress instead of the default effective stress. New optional keyword *GULIMPERM restricts
  reduction of fracture permeability upon fracture closure. See template "stgeo095.dat"

Initial Total Stress

  New keyword *UTSTRESS indicates that the input of initial stress is the total stress instead of
  the effective stress as default. See template "stgeo095.dat"

Pressure for Fracture Initiation

  New keyword *GPSCALING allows the user to define pressure for fracture initiation, by weighting
  between the matrix and collocated grid-block fracture pressures from the flow simulation. See
  templates "stgeo093/94/95.dat"

Improved Boundary conditions on Fracture Surface

  The definition of boundary conditions on the fracture surface are improved by introduction of
  two new keywords, *GBCPFACT and *GBCUFACT. With *GBCPFACT both fracturing pressure and total
  stress are taken into account in determining the loading and unloading pressures. In absence
  of this keyword, fracturing pressure at two consecutive time steps is used to determine the
  loading-unloading pressures. The input associated with *GBCUFACT is used to control the
  fracture closure. See template "stgeo094.dat"

Stress Dependent Transmissibility Multiplier for Dilation-Recompaction

  Support for transmissibility multipliers is added for keyword *GROCKTAB. Dilation-recompaction
  can now be modeled through stress dependent permeability and transmissibility tables.
  See template "stgeo092.dat"


GRID CHANGES
============

Preconditioned *DYNAGRID

  New *DYNAGRID sub-keywords *SATO_P, *SATG_P, or *SATW_P are used as saturation thresholds
  for grid amalgamation or de-refinement. This amalgamation or de-refinement is a preprocessing
  step to grid definition and cannot be reversed by dynamic criteria. The option is useful when
  a number of grid blocks can be easily amalgamated without compromising the accuracy of the results
  (e.g. aquifer regions), thereby reducing the simulation time. See template "stgro079.dat"

Directional Inter-Regional Transmissibility Multipliers

  Optional direction specification is available for the inter-regional transmissibility multipliers
  (*INTER_REGION_TM). When specified, the multipliers will be applied only for the connections having
  the same directions. See template "stgro074.dat"

New Shape Functions for Matrix-Fracture Transfer

  New shape functions *KX and *K-AV2 are implemented under the primary keyword *SHAPE to provide
  the user with more flexibility in calculating the matrix-fracture transmissibility. See templates
  "stgro080/81.dat"

Recurrent *SCONNECT and *IRCONNECT

  Special connections (*SCONNECT) or irregular connections (*IRCONNECT) can now be redefined in the
  Well and Recurrent Data section. See template "verify79.dat"

PINCHVGAP Default Change

  Corner point grid blocks are defined via coordinates. Ideally two neighboring blocks should have
  four shared corners, i.e., there should be no gap between the corresponding blocks. If pinched
  out blocks are creating gaps between vertical corner point blocks, it is necessary to decide
  whether the simulator should consider a connection between the corner point blocks. The previous
  default (i.e., in absence of keyword *PINCHVGAP) was *SKIP, i.e. not making connection, has now
  been changed to making connection between the grid blocks, i.e. *CONNECT.

Aquifer Options
 
  New option for keyword *AQPINIT allows the user to specify the datum depth corresponding to the
  initial aquifer pressure. See template "sttst25.dat"

Grid Refinement Options

  New sub-keywords *WF1 and *K1INT, available with primary keywords *REFINE, *PLNR_REFINE and
  *PLNRFRAC_TEMPLATE, re-define the intrinsic fracture width and intrinsic matrix (or fracture)
  permeability of the primary fracture network within fracture zone of the SRV or planar fracture
  region. These sub-keywords must be defined together. See template "stgro071.dat"

Obsolete Keyword

  Keyword *MDPLNRBK, used to specify the maximum number of fundamental grid blocks that each planar
  fracture may fully or partially cover, is no longer required.


WELL MANAGEMENT CHANGES
=======================

Parallelization of Well Management

  Most of the calculations in the well management module have been parallelized which will be
  beneficial to models with a large number of wells (and well perforations) when run in parallel
  processing mode, especially on machines with a large number of cores. The well management
  parallelization is activated automatically as long as *PARASOL and/or one of the parallel Jacobian
  decomposition options (e.g. *DPLANES) are in effect. The number of threads used by the well
  management is adjusted internally but can be overwritten by command-line argument '-wmthrds n'
  where n denotes the desired number of threads.

Well-List Feature

  New keyword *WELLIST creates and maintains a list of wells that can be collectively referred
  to by any well-related keyword (e.g. *SHUTIN) that reads a list of well numbers or well names.
  See template "stwwm014.dat"

Trigger Enhancements

  Following new variables are added on which Trigger conditions may be applied to wells:
  ROIL-RP	Oil production rate at reservoir condition
  ROIL-RI	Oil injection rate at reservoir condition
  RGAS-RP	Gas production rate at reservoir condition
  RGAS-RI	Gas injection rate at reservoir condition
  RWAT-RP	Water production rate at reservoir condition
  RWAT-RI	Water injection rate at reservoir condition
  GORRC	        Production gas-oil ratio reservoir condition
  GLRRC	        Production gas-liquid ratio at reservoir condition
  TEMP	        Maximum temperature of all completions of a well (producer only)
  O2CONC        Oxygen component mole fraction - maximum of all completions of a well
  RSTM-RP       For Producers: Steam production rate at reservoir conditions in cold water
                equivalent terms. Production rate of aqueous components in reservoir gas
                phase expressed as CWE volume.
  Cumulatives related to the above rates can also be used as Trigger conditions. Similarly,
  reservoir oil, gas, and water phase compositions at specific well perforations can also be
  used as Trigger conditions. See template "stwwm045.dat"

Simplification of Trigger Variable Format

  The format of trigger variables is further simplified to make it more intuitive. The older
  format continues to be supported for backward compatibility. An equal sign (=) is permitted
  in trigger variable definition.  In such a case for mathematical expressions involving trigger
  variables quotes are not used.

Default Action on Constraint Violation

  New keyword *ACT-DEFAULT sets / resets the default action globally for all wells defined
  afterwards. Note that this is the only way to specify the action for new constraints introduced
  via the *TARGET keyword. See template "stwwm014.dat"

Group Injection Control on Total Fluid
 
  The group control has been extended to include the total fluid as an injection stream, either
  as stock-tank fluid (*STF) or bottom-hole fluid (*BHF).  Under keyword *GCONI, the total fluid
  control includes the maximum constraint (*MAX), fixed target (*GTARGET), voidage replacement
  (*VREP) and recycling (*RECYCLE).  Note that once a total fluid injection constraint is
  specified, any other single-phase injection group control is disallowed for the same group.  
  For the stock-tank fluid target, it is also recommended to specify the volumetric equivalency
  for apportionment between liquid and vapor phases using either the user guide rates (*GUIDE),
  or the internal guide rates (*INGUIDE) with priority formula (*PRIOR-FORM). 
  See template "stwwm093.dat"

 
New Template Data Sets
======================

stflu071.dat	Verify/Illustrate *SWIPV, *OMEGA_PW, *RRFTW(O/G)
stflu072.dat	Verify/Illustrate *WELLSHEAR with Shear Thinning
stflu073.dat	Verify/Illustrate *WPLYFAC with Shear Thinning
stgeo067.dat	Test/Illustrate contracting and expanding grids
stgeo092.dat	Verify/Illustrate *GROCKTAB with Stress-Dependent Trans. Multipliers
stgeo093.dat	Illustrate Shear and Tensile Fractures
stgeo094.dat	Four Stages of 3D Hydraulic Fracturing
stgeo095.dat	Total Tensile Threshold in BB Model
stgro080.dat	Test/Illustrate *SHAPE *K-AV2 with *DUALPERM
stgro081.dat	Test/Illustrate *SHAPE *KX with *DUALPERM
stsmo096.dat	Verify/Illustrate *INTERP_SCAL for Double Interpolation
stsmo097.dat	Verify/Illustrate *INTERP_SCAL with *CP_IMBIB and *PCOW_CRV
stsmo098.dat	Verify/Illustrate *INTER_SCAL with Hysteresis
stwwm150.dat 	General Injection Option with *INCOMP *MIXTURE-Z and *HINJW
stwwm151.dat	FlexWell, *FCDTABLE with *SUBCOOL Dependency


Changed Template Data Sets
==========================

stflu024.dat	Remove obsolete keyword *NEXTSEG 
stflu025.dat	Remove obsolete keyword *NEXTSEG 
stflu032.dat	Remove obsolete keyword *NEXTSEG 
stflu033.dat	Remove obsolete keyword *NEXTSEG 
stflu070.dat	Additional *MATBALTOL options are used to reduce the material balance error
stgch003.dat	Remove keyword *INTERP_ENDS *ON which is no longer needed with
                *INTERP_SCAL *ON (default) 
stgch007.dat	Remove keyword *INTERP_ENDS *ON which is no longer needed with
                *INTERP_SCAL *ON (default) 
stgch009.dat	Additional *MATBALTOL options are used for better numerical performance
stgro071.dat	Add *PLNRFRAC_TEMPLATE sub-keywords *K1INT and *WF1 for defining intrinsic
                fracture width and matrix/fracture intrinsic permeability
stgro074.dat	Add direction sub option to *INTER_REGION_TM
stgro079.dat	Add *DYNAGRID sub-keyword *SATO_P as a threshold condition for amalgamation
stsmo080.dat	Add *INTERP_SCAL *OFF (*ON will overwrite *INTERP_ENDS *ON, i.e. the default)
stsmo084.dat	Verify/Illustrate Automatic Tuning *AUTOTUNE
stsmo091.dat	Remove obsolete *AMG-ROW-SCALED *OFF; use *AMG-DRS *FI
stsmo092.dat	Remove obsolete *AMG-ROW-SCALED *OFF; use *AMG-DRS *RSCAL
stsmo093.dat	Replace *AMG-DRS *ALL with *AMG-DRS *ON
stsmo094.dat	Replace *AMG-DRS *ALL with *AMG-DRS *ON
sttst07.dat 	Add *NOLISTLIM to override the limited echo of long grid-array data. The
                last lines of *VATYPE data are cut off at 20 lines, but enabling *NOLISTLIM
                in the IO Control data section removes that limit.
sttst25.dat	Add datum depth option to *AQPINIT
verify22.dat	Remove obsolete keyword *NEXTSEG
verify79.dat	Demonstrate that *SCONNECT may appear in recurrent data
verify97.dat	Demonstrate the use of *KRTYPE from *OUTBOARD software
stwwm014.dat	Miscible Flood with Group Control, Autodrill, *WELLIST and *ACT-DEFAULT
stwwm021.dat	Remove obsolete keyword *NEXTSEG
stwwm027.dat	Add *FW-RELAX-ACC  ON
stwwm028.dat	Remove obsolete keyword *NEXTSEG
stwwm031.dat	Remove obsolete keyword *NEXTSEG
stwwm045.dat	Add various *TRGVAR options
stwwm051.dat	Remove obsolete keyword *NEXTSEG
stwwm063.dat	Remove obsolete keyword *NEXTSEG
stwwm064.dat	Add new *MATBALTOL options: *MAX_REPEAT, *RMBE_STALL, *RMBE_RATIO
stwwm072.dat	Remove obsolete keyword *NEXTSEG
stwwm075.dat	Add new outputs *OUTSRF *WELL *BLOCKP5 *DWN *GGASIP1
stwwm086.dat	Remove obsolete keyword *NEXTSEG
stwwm093.dat	Use general keywords *PRIOR-FORM *FLDI under *GCONI
stwwm096.dat	Remove obsolete keyword *NEXTSEG
stwwm099.dat	Remove obsolete keyword *NEXTSEG
stwwm104.dat	Remove obsolete keyword *NEXTSEG; add new sub-keyword *SECTIONS for *HEATER_CABLE
stwwm122.dat	Remove obsolete keyword *NEXTSEG
stwwm127.dat	Remove obsolete keyword *NEXTSEG

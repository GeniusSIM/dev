@echo off
echo.
echo This batch file runs simulator using all the *.dat files that it
echo finds in the current directory
echo.
if $%1==$ goto error
for %%i in (*.dat) do call runall1.bat %%i %1
goto end
:error
echo proper syntax :
echo.
echo         runall program_name
echo.
echo                e.g.
echo.
echo           runall st9700
:end

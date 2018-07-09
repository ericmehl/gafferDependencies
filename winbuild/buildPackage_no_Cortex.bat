SETLOCAL

if not defined VERSION set VERSION=0.47.0.0

set ROOT_DIR=%~dp0%\..

cd %BUILD_DIR%
%ROOT_DIR%\winbuild\7zip\7za.exe a -tzip %ROOT_DIR%\gafferDependencies-%VERSION%-noCortex-windows-msvc2017.zip @%ROOT_DIR%\winbuild\packageList_no_Cortex.txt
if %ERRORLEVEL% NEQ 0 (exit /b %ERRORLEVEL%)

ENDLOCAL

@echo off
set driveLetter=S:
set networkPath=\\192.168.1.60\SRV-ATEngine-02
set username=%USERNAME%

:: Disconnect the network drive if it's already mapped
net use %driveLetter% /delete

:: Map the network drive using the "net use" command
net use %driveLetter% %networkPath% /user:ATENGINE\%username% password

set driveLetter=U:
set networkPath=\\192.168.1.60\Users\Usuarios

:: Disconnect the network drive if it's already mapped
net use %driveLetter% /delete

:: Map the network drive using the "net use" command
net use %driveLetter% %networkPath% /user:ATENGINE\%username% password

set driveLetter=P:
set networkPath=\\192.168.1.60\Public

:: Disconnect the network drive if it's already mapped
net use %driveLetter% /delete

:: Map the network drive using the "net use" command
net use %driveLetter% %networkPath% /user:ATENGINE\%username% password

@echo off
set "source=\\192.168.1.60\SRV-ATEngine-02\IT$\APPs\Baseline"
set "destination=%userprofile%\Desktop\Baseline"

xcopy /E /I "%source%" "%destination%"

echo Copia completada.

echo Ejecutando los archivos en la carpeta Baseline...

start "" "%userprofile%\Desktop\Baseline\Adobe\Acrobat_2017_Web_WWMUI.exe"
start "" "%userprofile%\Desktop\Baseline\GlobalProtect64.msi"
start "" "%userprofile%\Desktop\Baseline\OfficeSetup.exe"
start "" "%userprofile%\Desktop\Baseline\TeamsSetup_c_w_.exe"
start "" "%userprofile%\Desktop\Baseline\Windows_791_x64.msi"

echo Archivos ejecutados.

pause

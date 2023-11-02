@echo off
set driveLetter=S:
set networkPath=\\192.168.1.60\SRV-ATEngine-02
set username=%USERNAME%

:: Disconnect the network drive if it's already mapped
net use %driveLetter% /delete

:: Map the network drive using the "net use" command
net use %driveLetter% %networkPath% /user:ATENGINE\%username% password

set driveLetter=U:
set networkPath=\\192.168.1.60\Users\Usuarios\%USERNAME%

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

echo  Favor  de confirmar  que los discos funcionen, de lo contrario levantar ticket con recorte de pantalla de este mensaje.
pause

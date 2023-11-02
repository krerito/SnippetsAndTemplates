@echo off
setlocal enabledelayedexpansion

:: Identificar el nombre del adaptador de Ethernet
for /f "tokens=4*" %%i in ('netsh interface show interface ^| findstr /C:"Ethernet"') do set AdapterName=%%j

if not defined AdapterName (
    echo No se pudo encontrar el adaptador de Ethernet.
    echo Por favor, manda esta información a IT. Se requiere atención personal.
    exit /b
)
echo Renovando dirección IP para el adaptador: %AdapterName%...
:: Liberar IP
ipconfig /release "%AdapterName%"
if ERRORLEVEL 1 (
    echo Ocurrió un error al liberar la IP: !ERRORLEVEL!
    echo Por favor, manda esta información a IT. Se requiere atención personal.
    exit /b
)
:: Renovar IP
ipconfig /renew "%AdapterName%"
if ERRORLEVEL 1 (
    echo Ocurrió un error al renovar la IP: !ERRORLEVEL!
    echo Por favor, manda esta información a IT. Se requiere atención personal.
    exit /b
)
echo Hecho.
endlocal
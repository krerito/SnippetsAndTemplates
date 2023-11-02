
from pyrfc import Connection

# Mandar a llamar una funcion RFC
def bapicall(p_matnr):
    conn = Connection(ashost='',    #servidor al que te conectas, ej: dev, pruebas, prd
                      sysnr='',     #normalmente es 00
                      client='',    #tu cliente, cuando seleccionas un ambiente te sale arriba del sap logon
                      user='',      #usuario
                      passwd=''     #contraseña del usuario
                      )
    
    # Llamar a una función RFC
    result = conn.call(
                        'ZIT_TEST',         #transaccion
                        P_MATNR=p_matnr     #parametros a meter
                        )
    
    return result

de pysnmp import hlapi
de . importar quicksnmp
# Usando SNMPv2c, establecemos el nombre de host del dispositivo remoto en 'SNMPHost'
quicksnmp set ( '192 .168.100.22 ' , { ' 1.3.6.1.2.1.1.5.0 ' : ' SNMPHost ' } , hlapi. CommunityData ( ' ICTSHORE ' ))
# Usando SNMPv2c, recuperamos el nombre de host del dispositivo remoto
print ( get ( '192 .168.100.22 ' , [ ' 1.3.6.1.2.1.1.5.0 ' ] , hlapi. CommunityData ( ' ICTSHORE ' )))
# Obtenemos el nombre de la interfaz y la descripción de la interfaz de Cisco para todas las interfaces
# ¡El último parámetro es el OID que contiene el número de interfaces, por lo que podemos hacer un bucle con todos ellos!
its = get_bulk_auto ( '192 .168.100.22 ' , [
    «1.3.6.1.2.1.2.2.1.2» ,
    '1.3.6.1.2.1.31.1.1.1.18'
    ] , hlapi. CommunityData ( 'ICTSHORE' ) , '1.3.6.1.2.1.2.1.0' )
# Imprimimos los resultados en formato OID = valor
para ello en su:
    para k, v en ella. artículos () :
        print ( "{0} = {1}" . formato ( k, v ))
    # Dejamos una línea en blanco entre la salida de cada interfaz
    imprimir ( '' )
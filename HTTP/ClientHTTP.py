import os
import argparse
import http.client

REMOTE_SERVER_HOST = '127.0.0.1'
REMOTE_SERVER_PATH = '/'


def menu():
    print("Request Methods")
    print("\t1 - GET")
    print("\t2 - HEAD")
    print("\t3 - POST")
    print("\t4 - PUT")
    print("\t5 - DELETE")
    print("\t6 - CONNECT")
    print("\t7 - OPTIONS")
    print("\t8 - TRACE")


conn = http.client.HTTPConnection(REMOTE_SERVER_HOST, 8080)
menu()
print("Seleccione un request method a probar.")
opcionMenu = int(input())
os.system('cls')
if opcionMenu == 1:
    print("Prueba del request method GET")
    conn.request("GET", "/")
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    while True:
        chunk = r1.read(200)  # 200 bytes
        if not chunk:
            break
        print(repr(chunk))
if opcionMenu == 2:
    print("Prueba del request method HEAD")
    conn.request("HEAD", "/")
    res = conn.getresponse()
    print(res.status, res.reason)
    data = res.read()
    print(len(data))
if opcionMenu == 3:
    print("Prueba del request method POST")
    conn.request("POST", "/")
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    while True:
        chunk = r1.read(200)  # 200 bytes
        if not chunk:
            break
        print(repr(chunk))
if opcionMenu == 4:
    print("Prueba del request method PUT")
    BODY = "***filecontents***"
    conn.request("PUT", "/test.txt", BODY)
    response = conn.getresponse()
    print(response.status, response.reason)
    data = response.read()
if opcionMenu == 5:
    print("Prueba del request method DELETE")
    conn.request("DELETE", "C:/Users/giolo/PycharmProjects/CapaAplicacionProt/HTTP/test.txt")
    response = conn.getresponse()
    print(response.status, response.reason)
    data = response.read()
if opcionMenu == 6:
    print("Prueba del request method CONNECT")
    conn.request("CONNECT", "/")
    response = conn.getresponse()
    print(response.status, response.reason)
if opcionMenu == 7:
    print("Prueba del request method OPTIONS")
    conn.request("OPTIONS", "/")
    response = conn.getresponse()
    print(response.status, response.reason)
    data = response.getheaders()
    print(data)
if opcionMenu == 8:
    print("Prueba del request method TRACE")
    conn.request("TRACE", "/")
    response = conn.getresponse()
    print(response.status, response.reason)
    data = response.read()
    print(data)
conn.close()

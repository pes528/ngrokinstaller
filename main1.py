import os
import time
import random
try:
    from pyngrok import ngrok, conf
except:
    os.system("!pip install pyngrok > /dev/null 2>&1")
    print("ngrok instalado con exito")
    from pyngrok import ngrok, conf

#colors------
barra="\033[1;101m"
green="\033[1;32m"
red="\033[1;31m"
finColor="\033[0m"
#-------



def escribe(nombre, datoss):
    r=open(nombre, "w")
    r.write(datoss)
    r.close()
def lee():
    r=open("ngrok_token", "r")
    tok=r.read()
    r.close()
    return (str(tok))

REGIONES={
    
    "us": "< United States",
    "eu": "< Europe",
    "ap": "< Asia",
    "au": "< Australia",
    "sa": "< South America",
    "jp": "< Japan"
}
def isNum(dato):
    try:
        str(dato)
        return True
    except:
        return False
def verifica():

    if os.path.isfile("ngrok_token"):
        return True
    else:
        return False
def creatoken(token):
    to=open("ngrok_token", "w")
    to.write(token)
    to.close()


def fin():
    os.system("clear")
    print("SELECCIONA LOS PUERTOS")
    print("1 < Puerto automatico\n2 < Puerto personalizado\n0 < Volver")
    opcion=input("OPCION: ")
    if opcion == "1":
        ran=random.randint(500, 9001)
        tun=ngrok.connect(ran, bind_tls=True)
        print(f"TUNEL: {tun.get_tunnels()}")
        escribe("tunnels.txt", tun)
        print("DATOS GUARDADOS EN TUNELS.TXT")
    elif opcion=="2":
        op=int(input("ESCRIBE EL PUERTO: "))
        if isNum(op)== False :

            tunelPer=ngrok.connect(op, bind_tls=True)
            print(f"TUNEL: {tunelPer.get_tunnels()}")
            escribe("tunnels.txt", tunelPer)
            print("DATOS GUARDADOS EN TUNELS.TXT")
        else:
            print("PUERTO INCORRECTO")
            fin()
    elif opcion == "0":
        menu()
    else:
        print("opcion incorrecta")
        menu()
    

def puertos():
    os.system("clear")
    print("Verificando Token...", end="")
    for i in range(0,10):
        print(".", end="")
    if verifica() == True:
        print("TOKEN VERIFICADO CON EXITO")
        ngrok.set_auth_token(lee())
        fin()

    else:
        print("TOKEN NO ENCONTRADO, VE A NGROK.COM Y COPIA EL TOKEN DE AUTENTICACION A CONTINUACION.")
        token=input("INSERTE EL TOKEN: ")
        creatoken(token)
        print("TOKEN ALAMCENADO CON EXITO")
        ngrok.set_auth_token(lee())
        fin()
        
        



def init_tunnel():

    """< INICIAR TUNEL NGROK"""
    os.system("clear")
    conf.get_default().conf_path="./ngrok_conf.yml"
    print("SELECCIONA UNA REGION")
    for i, j in REGIONES.items():
        print(i, j)
    regi=input("ESCRIBE LA REGION [ejemplo(sa)]:  ")
    if isNum(regi)==True and len(regi)>2:
        print("ERROR")
        init_tunnel()
    else:
        re=REGIONES.get(regi)
        conf.get_default().region=re
        print("REGION SELECCIONADA CON EXITO")
        puertos()
    
def config():
    """< CAMBIAR CONFIGURACIONES"""

def salir():
    """< SALIR"""
    print("FINALIZADO")
    os.system("clear")
    return exit()
def menu():
    print(f"{green}—{finColor}"*41, f"\n{barra}        instalador ngrok by @pes528       {finColor}")
    print(f"{green}—{finColor}"*41)
    options={"1)":init_tunnel, "2)":config, "0)": salir}
    for opcion, funcion in options.items():
        print(opcion, f"{green}{funcion.__doc__}{finColor}")
    opt=input("OPCION: ")
    r=options.get(opt+")", None)
    if r:
        r()
    else:
        print("ELIGE UNA OPCION VALIDA")
        time.sleep(2)
        menu()


if __name__ == "__main__":
    
    menu()

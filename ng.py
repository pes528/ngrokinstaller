import os
import time
import random
try:
    from pyngrok import ngrok, conf
except:
    os.system("pip install pyngrok > /dev/null 2>&1")
    print("ngrok instalado con exito")
    from pyngrok import ngrok, conf

#colors------
barra="\033[1;101m"
green="\033[1;32m"
red="\033[1;31m"
finColor="\033[0m"
#-------
region=["us", "eu", "ap", "au", "sa", "jp"]
REGIONES={
    
    "us": "< United States",
    "eu": "< Europe",
    "ap": "< Asia",
    "au": "< Australia",
    "sa": "< South America",
    "jp": "< Japan"
}
#CONFIGURACIONES EXTRAS
def newToken():
    """< CONFIGURAR TOKEN"""
    print("INSERTA EL NUEVO TOKEN")
    token=input("TOKEN: ")
    creatoken(token)
    print("TOKEN ALMACENADO CON EXITO")

def newRegion():
    """< CAMBIAR REGION"""
    print("SELECCIONA UNA REGION")
    for i, j in REGIONES.items():
        print(i, j)
    regi=input("ESCRIBE LA REGION [ejemplo(sa)]:  ")
    
    if isNum(regi)==True and len(regi)>2:
        print("ERROR")
        init_tunnel()
    else:
        
        if regi in region:

          conf.get_default().region=regi
          print("REGION SELECCIONADA CON EXITO")
          time.sleep(3)
          config()
          
        else:
          print("region incorrecta")
          config()
    

def volverMenu():
    """< VOLVER AL MENU""" 
    return menu()
#FIN CONFIGURACIONES EXTRAS

#funciones utilitarias
def escribe(nombre, datoss):
    r=open(nombre, "w")
    r.write(datoss+"\n")
    r.close()
def lee():
    r=open("ngrok_token", "r")
    tok=r.read()
    r.close()
    return (str(tok))


def isNum(dato):
    try:
        int(dato)
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
#fin funciones utilitarias

def fin():
    os.system("clear")
    print("SELECCIONA LOS PUERTOS")
    ngrok.set_auth_token(lee())
    print("1 < Puerto automatico\n2 < Puerto personalizado\n0 < Volver")
    opcion=input("OPCION: ")
    try:
        if opcion == "1":
            os.system("clear")
            ran=random.randint(500, 9001)
            tun=ngrok.connect(int(ran), bind_tls=True)
            datos=f"{red}LINK NGROK{finColor}: {tun.public_url}\n{red}PUERTO ALEATORIO{finColor}: {ran}"
            print(f"{red}LINK NGROK{finColor}: {tun.public_url}\n{red}PUERTO ALEATORIO{finColor}: {ran}")
            escribe("tunnel.txt", datos)
            print("DATOS GUARDADOS EN tunnel.txt\nPara cerrar el tunel ngrok, solo debes salir del programa con la opcion 0 en el menu")
            input("PRECIONA 0 PARA VOLVER: ")
            menu()
        elif opcion=="2":
            ngrok.set_auth_token(lee())
            op=input("ESCRIBE EL PUERTO: ")
            if isNum(op)== True :

                tunelPer=ngrok.connect(int(op), bind_tls=True)
                os.system("clear")
                datos=f"{red}LINK NGROK{finColor}: {tunelPer.public_url}\n{red}PUERTO SELECCIONADO{finColor}: {op}"
                print(f"{red}LINK NGROK{finColor}: {tunelPer.public_url}\n{red}PUERTO SELECCIONADO{finColor}: {op}")
                escribe("tunnel.txt", datos)
                print("DATOS GUARDADOS EN tunel.txt\nPara cerrar el tunel ngrok, solo debes salir del programa con la opcion 0 en el menu")
                input("PRECIONA 0 PARA VOLVER: ")
                menu()
            else:
                print("PUERTO INCORRECTO")
                fin()
        elif opcion == "0":
            menu()
        else:
            print("opcion incorrecta")
            menu()
    
    except :
        os.system("clear")
        for i in range(0,5):
            time.sleep(1)
            print(f"{red}TOKEN ERRONEO!!!{finColor}")
        menu()


def puertos():
    os.system("clear")
    print("Verificando Token...", end="")
    for j in range(0,10):
        print(".", end="")
    
    if verifica() == True:
        print("TOKEN VERIFICADO CON EXITO")
        ngrok.set_auth_token(lee())
        fin()

    else:
        print("TOKEN NO ENCONTRADO, VE A NGROK.COM Y COPIA EL TOKEN DE AUTENTICACION A CONTINUACION.")
        token=input("INSERTE EL TOKEN: ")
        creatoken(token)
        print("TOKEN ALMACENADO CON EXITO")
        ngrok.set_auth_token(lee())
        fin()
        
        


#PRINCIPAL-----------------
def init_tunnel():

    """< INICIAR TUNEL NGROK"""
    os.system("clear")
    
    print("SELECCIONA UNA REGION")
    for i, j in REGIONES.items():
        print(i, j)
    regi=input("ESCRIBE LA REGION [ejemplo(sa)]:  ")
    
    if isNum(regi)==False and len(regi)>2:
        print("ERROR")
        time.sleep(2)
        init_tunnel()
    else:
        
        if regi in region:


            conf.get_default().region=regi
            print("REGION SELECCIONADA CON EXITO")
            puertos()
        else:
          print("REGION INCORRECTA")
          time.sleep(2)
          init_tunnel()



def config():
    """< CAMBIAR CONFIGURACIONES"""
    os.system("clear")
    print(f"{barra}       MENU DE CONFIGURACIONES       {finColor}")
    opcionConfig = {"1)":newToken, "2)":newRegion, "0)": volverMenu}
    for option, function in opcionConfig.items():
        print(option, function.__doc__)
    option=input("OPCION: ")
    o=opcionConfig.get(option+")", None)
    if o:
        o()
    else:
        print("OPCION INCORRECTA")
        config()

def viewTunnels():
    """< VER TÚNELES ABIERTOS"""
    
    if ngrok.get_tunnels():

        for link in ngrok.get_tunnels():
            print(link)
            input(f"{red}PRECIONA 0 PARA VOLVER{finColor}: ")
            time.sleep(2)
            menu()
                        
    else:
        print("NO HAY SERVICIOS ACTIVOS")
        time.sleep(2)
        menu()

def ayuda():
    """< AYUDA"""
    os.system("clear")
    print(f"{barra}         CONSEJOS            {finColor}\n\n1: Si copiaste mal el token, ngrok no funcionara")
    print("2: No debes SALIR el script si ya iniciaste un tunel ngrok o el tunel se cerrara")
    print("")
    input("PRECIONA UNA TECLA PARA VOLVER ATRAS: ")
    menu()
def salir():
    """< SALIR"""
    print("FINALIZADO")
    os.system("clear")
    return exit()

#FIN PRINCIPAL-----------------------------


def menu():
    os.system("clear")
    print(f"{green}—{finColor}"*41, f"\n{barra}       MINI NGROK MANAGER by @pes528     {finColor}")
    print(f"{green}—{finColor}"*41)
    options={"1)":init_tunnel, "2)":config,"3)":viewTunnels,"4)":ayuda, "0)": salir}
    for opcion, funcion in options.items():
        print(opcion, f"{red}{funcion.__doc__}{finColor}")
    opt=input("OPCION: ")
    r=options.get(opt+")", None)
    if r:
        r()
    else:
        print("ELIGE UNA OPCION VALIDA")
        time.sleep(2)
        menu()


if __name__ == "__main__":
    
    conf.get_default().config_path="./ngrok_conf.yml"
    menu()

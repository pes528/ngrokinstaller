#!/bin/python3


from pyngrok import ngrok, conf
import os
from time import sleep
import random
#colors------
barra="\033[1;101m"
green="\033[1;32m"
red="\033[1;31m"
fin="\033[0m"
#-------

#regiones__
#by @pes528
#regiones
#[us] United States
#[eu] Europe
#[ap] Asia
#[au] Australia
#[sa] South America
#[jp] Japan
#[in] India


def crearFile(name, content):
    tok=open(name, "w")
    tok.write(content)
    tok.close()

def region():
    try:

        if conf.get_default().region:
          menu()
        print(f"{barra}SELECCION DE REGIONES{fin}")
        regiones = {1:"UNITED STATES", 2:"EUROPE", 3:"ASIA", 4:"AUSTRALIA", 5:"SOUTH AMERICA", 6:"JAPAN", 7:"INDIA"}
    
        for opcion, region in regiones.items():
            print(opcion, region)
        reg=regiones.get(int(input("opcion:")), None)
        if reg:
            conf.get_default().region=reg
            
            menu()
        else:
            print("selecciona una opcion valida")
            return region()
    except:
        print("Opcion no valida")
        return region()



class tunel:
    def __init__(self):
        self.instalado=True
        self.config = conf.get_default().config_path="./ngrokconfig.yml"
    
    def verifica(self):
        try:
            if os.path.isfile("ngrok_token"):

                return region()
            else:
                print("Necesitas un token de ngrok para continuar\nConsigue tu token en ngrok.io\nO preciona Ctrl+c para salir")
                print("LLamando a la funcion para almacenar tu token", end="")
                for i in range(0,10):
                    sleep(1)
                    print(".", end="")
                ngroktoken=input("Pega tu token aqui:  ")
                crearFile("ngrok_token", ngroktoken)
                return tunel.verifica(self)
        except KeyboardInterrupt:
            print("")
            print("Saliste del script")



    def install_ngrok(self):
        """INSTALAR NGROK"""
        print("INSTALANDO NGROK", end="")
        try:
            for i in range(0,10):
                sleep(1)
                print(".", end="")
            os.system("pip install pyngrok > /dev/null 2>&1")
            print("Ngrok instalado con exito")
            sleep(3)
            os.system("clear")
            return menu()
        except:
            print("algo saloio mal")
            self.instalado = False

    def iniciar_tunel(self):
        """INICIAR TUNEL NGROK"""
        try:
            if self.instalado:
                op_puerto = input("1:PUERTO ALEATORIO\n2:ELEGIR PUERTO\nSELECCIONA UNA OPCION:")
                if op_puerto == "1":
                    portRandom=random.randint(500, 6000)
                    ngrok_tunnel=ngrok.connect(portRandom, bind_tls=True)
                    print(f"URL NGROK: {ngrok_tunnel.public_url}\nSe guardo en el archivo url.txt")
                    crearFile("url.txt", ngrok_tunnel.public_url)

                elif op_puerto == "2":
                    SelPort=input("Selecciona el puerto:")
                    ngrok_tunnel=ngrok.connect(SelPort, bind_tls=True)
                    print(f"URL NGROK: {ngrok_tunnel.public_url}")
                else:
                    print("Selecciona una opcion valida")
                    sleep(1)
                    return menu()
        except:
              print("algo salio mal")



tunnel = tunel()

def menu():

    print(f"{green}—{fin}"*41, f"\n{barra}        instalador ngrok by @pes528       {fin}")
    print(f"{green}—{fin}"*41)
    options = {"a)":tunnel.install_ngrok, "b)":tunnel.iniciar_tunel }
    
    for opcion, funcion in options.items():
        
        print(f"{red}{opcion}{fin}", funcion.__doc__)
    op=input("\nopcion:")
    op=op+")"
    me=options.get(op, None)
    if me:
        me()
    else:
        print("Elige una opcion valida")
        sleep(4)
        os.system("clear")
        return menu()  
        
def main():
    tunnel.verifica()      
              
          
if __name__ == "__main__":
    
    main()

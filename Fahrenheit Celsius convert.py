#Fahrenheit en Celsius, Celsius en Fahrenheit

def affiche_menu():
    print('1. Celsius en Fahrenheit')
    print('2. Fahrenheit en Celsius')
def celsius_fahrenheit():
    C=float(input('Entrer la température en Celsius : '))
    F=C*1.8+32
    print('Température en Fahrenheit : {0}'.format(F))
def fahrenheit_celsius():
    F=float(input('Entrer la température en fahrenheit : '))
    C=(F-32)/1.8
    print('Température en Celsius : {0}'.format(C))
if __name__=='__main__':
    affiche_menu()
    choix=int(input('Quelle conversion voudriez vous effectuez ? '))
    if choix==1:
        celsius_fahrenheit()
    if choix==2:
        fahrenheit_celsius()
    

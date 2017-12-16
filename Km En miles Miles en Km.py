#Test convertisseur km en miles et inversement

def affiche_menu():
    print('1. Kilomètre en Miles')
    print('2. Miles en kilomètre')
def km_miles():
    km=float(input('Entrer la distance en kilometre : '))
    miles=km/1.609
    print('Distance en miles : {0}'.format(miles))
def miles_km():
    miles=float(input('Entrer la distance en miles : '))
    km=miles*1.609
    print('Distance en kilomètre : {0}'.format(km))
if __name__=='__main__':
    affiche_menu()
    choix=input('Quelle conversion voudriez vous effectuer ? ')
    if choix=='1':
        km_miles()
    if choix=='2':
        miles_km()
    

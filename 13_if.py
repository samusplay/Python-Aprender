if True:
    print('deberia ejecutarse')
    # estructura booleanos
    if False:
        print('nunca se ejecuta')# no puede entrar
''''''
pet=input('¿Cual es tu mascota favorita?')

if pet=='perro':
    print('Genial los perros son geniales')


if pet=='Gato':
    print('los gatos son muy chismosos')
elif pet=='pez':
    print('eres muy nadador')
else:
    print('no tienes mascota')
''''''

stock= int(input('Digita el stock=>'))

if stock>=100 and stock<=1000:
    print('el stcok es correcto')
else:#es si no se cumple la primera condicion
    print('el stock es incorrecto')    

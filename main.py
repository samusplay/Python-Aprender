import random



options=('piedra','papel','tijera')
computer_wins=0
user_wins=0

rounds=1

while True:
 print('*'*10)
 print('ROUND',rounds)
 print('*'*10)
 
 user_option=input('piedra, papel o tijera =>')
 computer_option='papel'
 user_option=user_option.lower()
 rounds +=1

 if  not user_option in options:
    print('esa opcion no es valida')
    continue

 print("user option= ",user_option)
 print('computer option=',computer_option)
 computer_option=random.choice(options)

 if user_option==computer_option:
    print('empate') # mismos valores
 elif user_option=='piedra':
    if computer_option=='tijera':
        print('piedra gana a tijera')
        print('user gano!')
        user_wins +=1
    else:
        print('Papel gana a piedra')
        print('Computer gano')
        computer_wins +=1
 elif user_option=='papel':
    if computer_option=='piedra':
        print('papel gana a piedra')
        print('user gano')
        user_wins +=1
    else:
        print('tijera gana a papel')
        print('computer gano')
        computer_wins +=1
 elif user_option=='tijera':
    if computer_option=='papel': 
     print('tijera gana a papel')
     print('usuario gano')
     user_wins +=1
    else:
        print("piedra gana a tijera")
        print('computador gano')
        computer_wins +=1                   

 if computer_wins==2:
    print('El ganador es la computadora')
    break
 
 if user_wins==2:
    print('El ganador es el usuario')
    break
 





 
print('Bienvenidos sean todos ustedes al programa de cooperacha by titus at Orbitalnet Soluciones y Tecnologia Enterprises Corporation')

users=int(input('Escribe la cantidad de usuarios:' ))

suma_user1=0
suma_user2=0
suma_user3=0
suma_user4=0
suma_user5=0
suma_user6=0
suma_user7=0
suma_user8=0
suma_user9=0
suma_user10=0


if users >= 1:
    user1 = input("Nombre Usuario 1: ")
    suma_user1 = float(input(f'{user1} escribe la cantidad de tu gasto previo $'))
    totalgasto = suma_user1 + suma_user2 + suma_user3 + suma_user4 + suma_user5 + suma_user6 + suma_user7 + suma_user8 + suma_user9 + suma_user10
if users >= 2:
    user2 = input("Nombre Usuario 2: ")
    suma_user2 = float(input(f'{user2} escribe la cantidad de tu gasto previo $'))
    totalgasto = suma_user1 + suma_user2 + suma_user3 + suma_user4 + suma_user5 + suma_user6 + suma_user7 + suma_user8 + suma_user9 + suma_user10
if users >= 3:
    user3 = input("Nombre Usuario 3: ")
    suma_user3 = float(input(f'{user3} escribe la cantidad de tu gasto previo $'))
    totalgasto = suma_user1 + suma_user2 + suma_user3 + suma_user4 + suma_user5 + suma_user6 + suma_user7 + suma_user8 + suma_user9 + suma_user10
if users >= 4:
    user4=input("Nombre Usuario 4: ")
    suma_user4 = float(input(f'{user4} escribe la cantidad de tu gasto previo $'))
    totalgasto = suma_user1 + suma_user2 + suma_user3 + suma_user4 + suma_user5 + suma_user6 + suma_user7 + suma_user8 + suma_user9 + suma_user10
if users >= 5:
    user5=input("Nombre Usuario 5: ")
    suma_user5 = float(input(f'{user5} escribe la cantidad de tu gasto previo $'))
    totalgasto = suma_user1 + suma_user2 + suma_user3 + suma_user4 + suma_user5 + suma_user6 + suma_user7 + suma_user8 + suma_user9 + suma_user10
if users >= 6:
    user6=input("Nombre Usuario 6: ")
    suma_user6 = float(input(f'{user6} escribe la cantidad de tu gasto previo $'))
    totalgasto = suma_user1 + suma_user2 + suma_user3 + suma_user4 + suma_user5 + suma_user6 + suma_user7 + suma_user8 + suma_user9 + suma_user10
if users >= 7:
    user7=input("Nombre Usuario 7: ")
    suma_user7 = float(input(f'{user7} escribe la cantidad de tu gasto previo $'))
    totalgasto = suma_user1 + suma_user2 + suma_user3 + suma_user4 + suma_user5 + suma_user6 + suma_user7 + suma_user8 + suma_user9 + suma_user10
if users >= 8:
    user8=input("Nombre Usuario 8: ")
    suma_user8 = float(input(f'{user8} escribe la cantidad de tu gasto previo $'))
    totalgasto = suma_user1 + suma_user2 + suma_user3 + suma_user4 + suma_user5 + suma_user6 + suma_user7 + suma_user8 + suma_user9 + suma_user10
if users >= 9:
    user9=input("Nombre Usuario 9: ")
    suma_user9 = float(input(f'{user9} escribe la cantidad de tu gasto previo $'))
    totalgasto = suma_user1 + suma_user2 + suma_user3 + suma_user4 + suma_user5 + suma_user6 + suma_user7 + suma_user8 + suma_user9 + suma_user10
if users >= 10:
    user10=input("Nombre Usuario 10: ")
    suma_user10 = float(input(f'{user10} escribe la cantidad de tu gasto previo $'))
    totalgasto = suma_user1 + suma_user2 + suma_user3 + suma_user4 + suma_user5 + suma_user6 + suma_user7 + suma_user8 + suma_user9 + suma_user10

repartido=totalgasto/users
print(f'Cada quien debe poner ${repartido}')

#Usuarios deben
if users >= 1:
    user1debe= repartido-suma_user1
    print(f'Usuario 1 {user1} debe ${user1debe} a gastado ${suma_user1}')
if users >= 2:
    user2debe= repartido-suma_user2
    print(f'Usuario 2 {user2} debe ${user2debe} a gastado ${suma_user2}')
if users >= 3:
    user3debe= repartido-suma_user3
    print(f'Usuario 3 {user3} debe ${user3debe} a gastado ${suma_user3}')
if users >= 4:
    user4debe = repartido - suma_user4
    print(f'Usuario 4 {user4} debe ${user4debe} a gastado ${suma_user4}')
if users >= 5:
    user5debe = repartido - suma_user5
    print(f'Usuario 5 {user5} debe ${user5debe} a gastado ${suma_user5}')
if users >= 6:
    user6debe = repartido - suma_user6
    print(f'Usuario 6 {user6} debe ${user6debe} a gastado ${suma_user6}')
if users >= 7:
    user7debe = repartido - suma_user7
    print(f'Usuario 7 {user7} debe ${user7debe} a gastado ${suma_user7}')
if users >= 8:
    user8debe = repartido - suma_user8
    print(f'Usuario 8 {user8} debe ${user8debe} a gastado ${suma_user8}')
if users >= 9:
    user9debe = repartido - suma_user9
    print(f'Usuario 9 {user9} debe ${user9debe} a gastado ${suma_user9}')
if users >= 10:
    user10debe = repartido - suma_user10
    print(f'Usuario 10 {user10} debe ${user10debe} a gastado ${suma_user10}')


print(f'Este es el gasto total ${totalgasto}')

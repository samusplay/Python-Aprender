#Crud de crear, leer de instalar y eliminar

numbers=[1,2,3,4,5]
print(numbers[1])
numbers[1]=10
print(numbers)

numbers.append(700) # lo aagrega con esta funcion
# Al final
print(numbers)

# forma de agregar elementos en un array
numbers.insert(0,'hola')
print(numbers)
numbers.insert(3, 'change')

tasks=['todo1','todo2','todo3']
new_list=numbers +tasks
#fucionando listas
print(new_list)

#posicion elemento

'''index=new_list.index('todo 2')
new_list[index]='todo changed'
print(new_list)'''

#para eliminar elementos de una lista

new_list.remove('todo1') # ojo con los espacios
print(new_list)

new_list.pop()
print(new_list) # por defecto elimina el ultimo

# se puede detrminar una posicion

# cambiar el orden sucesivo
new_list.reverse()
print(new_list)

# ordenar arrays
numbers_a=[1,4,6,3]
numbers_a.sort()
print(numbers_a)

# ejemplo con los arrays

strings=['re','sa','ed']
strings.sort()
print(strings) # no puede orden tipos de datos mezclados 
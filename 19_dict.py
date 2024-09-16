my_dict={}
print(type(my_dict))

my_dict={
    'name':'samuel',
    'last_name':'rodriguez',
    'age':18
}
print(my_dict) # se hacen por medio de strings 
print(len(my_dict)) # cuantos elementos 

print(my_dict['age'])
print(my_dict['last_name'])

#otra manera de capturar los datos

print(my_dict.get('age')) # es cuando un valor no existe

# tambien se puede vali con el in

print('avion' in my_dict)


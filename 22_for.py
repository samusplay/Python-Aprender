
'''for element in range(1,21): # conjunto de iteraciones
    print(element)'''

my_list=[23,45,67,89,43]
for element in  my_list:
    print(element) # itera cada elemento


my_tuple=('samuel','elon','aleja')

for element in my_tuple:
    print(element) # iteracion en tuplas



product={
    'name':'dress',
    'price':127,
    'stock':1200,
}

for Key in product:
    print(Key, '=>' ,product[Key]) # darle las llaves para darle el prodcuto

for key,value in product.items():
    print(Key,'=>',value) # lista de dicionarios

people=[
    {
        'name':'angela',
        'age':34,
    },
    {
        'name':'santiago',
        'age':4,

    },
    {
     'name':'samuel',
     'age':18,   
    }
]    

for person in people: # plural persona y gente
    print('name=>',person['name']) # imprime cada uno de lo diccionarios

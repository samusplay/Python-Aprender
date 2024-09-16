person={
    "name": "samuel",
    "last_name":"rodriguez",
    "langs":["python","javascript"],
    "age":99
}

# vamos a modificar los valores

print(person)

person["name"]="santi"
person["age"]="50"
person["langs"].append("rust")
print(person)

# elimanr valores para un diccionario 

del person["last_name"]
person.pop("age") # debe esparar un argumento
print("items")
print(person.items()) # tupla es una combinacion de estructura de datos

print("keys")
print(person.keys())

print("values")
print(person.items())





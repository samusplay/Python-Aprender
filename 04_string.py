name="samuel"
last_name="Rodriguez"
print(name)
print(last_name)

full_name=name +""+ last_name
print(full_name)

# concatenacion string + string
#"" es el espacio 

quote="I'am samuel"
print(quote)

quote2="she said'hello love'"
print(quote2)
#comillas dobles y simples

#format

template="hola mi nombre es"  +"y mi apellido es" + last_name
print(template)

#nueva forma de concatenacion

template="Hola mi nombre es {} y mi apellido es{}".format(name,last_name)
print(template)

# tercera formas
edad=24
template=f"Hola mi nombre es {name} y mi apellido es{last_name} y mi edad es{edad}"
print("v3",template)
#f string 


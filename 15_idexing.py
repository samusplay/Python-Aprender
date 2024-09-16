text='el sabe python'
#indicador posiciones
print(text[0]) # posiciones
print(text[1])

#print(text[999]) no encuentra la posicion

#saber el ultimo carcter
size=len(text)
print(text[-1])

#sclicing sacar partes textos

print(text[0:5])
print(text[10:16])
print(text[0:10])
# funcion mas facil

print(text[:10]) # no hay necesidad de poner cero ya que ahi inicia

print(text[5:-1])
print(text[5:1])
print(text[:])# todos los puntos de posicion 

#numero de saltos

print(text[10:6:1])
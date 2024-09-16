text='tu eres millonario'
print('millonario 'in text)
print('eres'in text)

if 'millonario'in text:
    print('si esta')
else:
    print('ponte las pilas')
size=len('millonario')
print(size) # ver el numero de caracteres en el texto


print(text, text.upper() )
#pasa a mayusculas

print(text, text.lower())
# pasa a minusculas

print(text.count('a'))
# cuenta las letras

print(text.swapcase())
#pasa a los contrarios 

print(text.startswith('tu'))
# devuelve un valor booleano

print(text.endswith('millonario'))
# caractere final

print(text.replace('millonario','multimillonario'))
#rempalza otra palabra por otra 

text_2='este es un titulo'
print(text_2)
print(text_2.capitalize())
#Primer caracter en mayuscula

print(text_2.isdigit())

x=3.3
y=1.1+1.2

print(x)
print(y)
print(x==y)

# falso

#comparacion strings y float

y_str=format(y,'.2g')

print('str=', y_str)

print(y_str==str(x))

#toleracia

tolerance=0.0001
print((x-y)<tolerance)
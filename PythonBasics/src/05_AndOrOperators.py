

a = 23
b = 34

#sub-expression1 or sub-expression2
if a == 34 or b == 34:
    print(a+b)
    #print("Or operator result: " + str(a + b))


#sub-expression1 and sub-expression2

if a == 34 and b == 34:
    print (a + b)


object_size = 10
proximity = 9000

if object_size > 5 and proximity < 1000:
    print('Evasive maneuvers required')
else:
    print('Object poses no threat')
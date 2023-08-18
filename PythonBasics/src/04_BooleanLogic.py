a=100
b=50
c = 25

# if test_expression:
#     # statement(s) to be run

if(a > b):
    print(a)

if a > b:print(b)


# if test_expression:
#     # statement(s) to be run
# else:
#     # statement(s) to be run

if(a < b): print(a)
else: print(b)


# if test_expression:
#     # statement(s) to be run
# elif test_expression:
#     # statement(s) to be run

if a >= b:
    print("a is greater than or equal to b")
elif a == b:
    print("a is equal to b")


# if test_expression:
#     # statement(s) to be run
# elif test_expression:
#     # statement(s) to be run
# elif test_expression:
#     # statement(s) to be run
# else:
#     # statement(s) to be run


if a < b: 
    print("a is less than b")
elif a > b: 
    print("a is greater than b")
else: 
    print ("a is equal to b")

#     if test_expression:
#     # statement(s) to be run
#     if test_expression:
#         # statement(s) to be run
#     else: 
#         # statement(s) to be run
# elif test_expression:
#     # statement(s) to be run
#     if test_expression:
#         # statement(s) to be run
#     else: 
#         # statement(s) to be run
# else:
#     # statement(s) to be run


if a > b:
    if b > c:
        print ("a is greater than b and b is greater than c")
    else: 
        print ("a is greater than b and less than c")
elif a == b:
    print ("a is equal to b")
else:
    print ("a is less than b")


object_size=10
if object_size > 5 :
    print("We need to keep an eye on this object")
else:
    print('Object poses no threat')
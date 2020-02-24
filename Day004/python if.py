# Python Flow Control
# ====================
# Python if....else
# What are if...else statement in Python?

# =if test expression:
#  statement(s)

# Python if...elif...else Statement
# Syntax of if...elif...else

# =if test expression:
#  Body of if
# =elif test expression:
# Body of elif 
# =else Body of else
 #display odd number between 0 to 100 
x =  int (input('Enter a value :'))

if x % 2 == 1:
    print("The number is Odd ", end = '\t')
else:
    print("The number is Even", end= '\t')

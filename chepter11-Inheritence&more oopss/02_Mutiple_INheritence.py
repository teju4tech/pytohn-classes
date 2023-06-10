''' Multipule Inheritence is have One child and two
    or more parents
'''
class Parents:
    A = 78

class Parents2:
    B = 69

class Parents3:
    C = 90

class child(Parents,Parents2,Parents3):
    D = 108

# Inheretence by multiple Parents classes
ch = child()
print(ch.A)
print(ch.C)
print(ch.D)


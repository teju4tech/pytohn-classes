''' Multi-Level Inheritences is When 
    Parents | Gradfather
    child 1 | DAD
    child 2 | YOu
'''
class Parents:
    Skill1 = 'Supervision'

class child1(Parents):
    Skill2 = 'Buisness'

class child2(child1):
    Skill3 = 'Coding'

'''Inherate by Multi-Level'''
ch = child2()
print(ch.Skill1)
print(ch.Skill2)
print(ch.Skill3)



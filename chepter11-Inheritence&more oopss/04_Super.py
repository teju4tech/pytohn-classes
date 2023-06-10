''' Super Method '''

class Parents:
    a = 4
    def __init__(self):
        print("Parents")

class child(Parents):
    b = 5
    def __init__(self):
        super().__init__()
        print("child")

class child1(child):
    c = 6
    def __init__(self):
        super().__init__()
        print("child1")

class child2(child1):
    d = 7
    def __init__(self):
        super().__init__()
        print("child2")

ch = child2()
print(ch.a)
print(ch.b)
print(ch.c)

    

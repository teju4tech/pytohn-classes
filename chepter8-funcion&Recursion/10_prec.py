'''Q-To remove a given word from using recursion a list and stop it at the same time ?
'''
def process(l1,word):
    word = word.strip()
    if word in l1:
        l1.remove(word)
    return l1

l1 = ['Teju','Dham','Anuraag','kuldeep','deepak']
l1 = process(l1, 'Anuraag')
print(l1)

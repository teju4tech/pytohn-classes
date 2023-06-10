'''We have'to Do multiplication 1-20 table 
   and store the tables individualy by 
   an directory an file format ?
'''
for i in range(2, 21):
    table = ''
    for j in range(1, 11):
        table += f"{i} x {j} = {i*j}\n"
    with open(f'tables/{i}.txt','w') as f:
        f.write(table)



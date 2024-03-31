file = open('dia19_people', 'a')
i = 0
while True:
    if i > 5:
        break   
    file.write(input('Enter full name: ') + " " + input('Enter age: ') + '\n')
    i += 1

file = open('dia19_people', 'r')
results = file.read()
print(results)
file.close()

with open('dia19_people', 'r') as file:
    x = file.read()
    print(x)
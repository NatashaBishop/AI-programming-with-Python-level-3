names=['john smith','Jon doe','ella Fowler','natalia korba']


usernames=[]

for i in names:
        usernames.append(i.replace(' ','_').lower())
print(usernames)



#unfinished: do the same, onli with range, c scrinshot
for i in range(len(usernames)):
    names[i]=names[i].title()
    print(names[i]) #prints list line by line
print(names)


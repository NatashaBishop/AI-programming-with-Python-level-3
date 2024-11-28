names=['john smith','Jon doe','ella Fowler','natalia korba']


usernames=[]

for i in names:
        usernames.append(i.replace(' ','_').lower())
print(usernames)

cities=['london','leverpool','grays','barking']
titledCities=[]
for i in cities:
    print(i.title())

for i in cities:
    titledCities.append(i.title())
print(titledCities)
print(list(range(2))) #creates a list and prints first 2 indexes
for i in range(len(cities)):
    cities[i]=cities[i].title()
    print(cities[i]) #prints list line by line
print(cities)
for i in cities:
    print(i) #prints list line by line

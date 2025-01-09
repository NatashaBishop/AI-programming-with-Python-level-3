items = ['BANANA', 'matresses','dogs', 'people', 'cheeses']
weights = [22,33,44,55,66]
print(list(zip(items,weights))) #creates list of tuples
#output: #do output

for item, weight in zip(items,weights):
    print(item, weight)
#output: #do output

#unpack tuple with *zip:
manifest = [('banana', 22), ('text', 33)]
item, weight = zip(*manifest) #manifest iz a tuple

#
for item, weight in zip(items, weights):
    print('{}: {}'format(item, weight))

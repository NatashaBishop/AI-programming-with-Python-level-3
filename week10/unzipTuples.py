#unpack tuple with *zip:
# #create tuple:
manifest = [('banana', 22), ('text', 33), ('Natasha'), 11]

item, weight = zip(*manifest) #manifest is a tuple
print(item)
print(weight)

#print("sdfghjkdfghhggfd "asdfg" sdfghjkl  ") #syntax error
print('sdfghjkdfghhggfd "asdfg" sdfghjkl  ') #ok
print('sdfghjkdfghhgg\'s fd "asdfg" sdfghjkl  ') #ok
# TODO: Fix this string!
#Ford_quote  = ‘Whether you think you can, or you think you can’t—you’re right.’
# TODO: Fix this string!
Ford_quote  = "Whether you think you can, or you think you can\’t—you\’re right."
print(Ford_quote)

a='aaa'
b='bbb'
print(a+b)
print(a+' '+b) #print with space between

#work with numbers as strings
x='3'
y='4'
z=x+y
print(z)
print(int(x+y))
print(int(x)+int(y))
hello='hello'
print(hello*5) #output: hellohellohellohellohello
#print(hello[5]) #IndexError: string index out of range
print(hello[0]) #output: H
#len
word_length=len("Hello")
print(word_length)

#print street address:
house_num=5
str='my street'
town='my town'
print("my address is:"+ " " str(house_num)+" "+str+" "+town)


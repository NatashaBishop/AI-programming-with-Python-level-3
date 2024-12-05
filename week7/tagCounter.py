'''Write a for loop that iterates over a list of strings, tokens , 
and counts how many of them are XML tags.  XML is a data language similar to HTML.  
You can tell if a string is an XML if it begins with a left angle bracket "<" and ends with a right angle bracket ">".  
Keep track of the number of tags using the variable count.
You can assume that the list of strings will not contain empty strings.
tokens = ['<greeting>','Hello World!','</greeting>']
count = 0'''
#!!!count full tags, opened and close will b 1 tag
tokens =['<greeting>','Hello World!','</greeting>']
count = 0
#countOpen = 0
#CountClose = 0
#string = join(my_list)
#countOpen = txt.count("<")
for token in tokens:
    if tokens[0]=='<' and tokens[-1]=='</':
       count += count

print(count)

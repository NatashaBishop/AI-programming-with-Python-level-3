# Activity:  Fix the Quote  

The line of code in the following quiz will cause a SyntaxError, thanks to the misuse of quotation marks.  First run it with Test Run to view the error message.  
Then resolve the problem so that the quote (from Henry Ford is correctly assigned to the variable ford_quote.  

### TODO: Fix this string!  

ford_quote = “Whether you think you can, or you think you can’t you’re right.”  

 ## Answer:  
 ford_quote = “Whether you think you can, or you think you can\’t you\’re right.”  

 

# Activity:  Write a Server Log Message

In this programming quiz, you’re going to use what you’ve learned about strings to write a logging message for a server.  
You’ll be provided with example data for a user, the time of their visit and the site they accessed. 
You should use the variables provided and the techniques you’ve learned to print a log message like this one (with the username, url, and timestamp 
replaced with values from the appropriate variables):  
Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20.  
Username = “Kinari”  
Timestamp = “04:50”  
url = "http://petshop.com/pets/mammals/cats"     
#### TODO: write a Log message using the variables above.  
#### The message should have the same format as this one:  
Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20.  
## Answer V.1:   
print=("{} accessed the site {} at {}.".format(Username,url,Timestamp))
## Answer V.2:   
print(f'{Username} accessed the site {url} at {Timestamp}.')   

# Activity:  Len()

Use string concatenation and the len() function to find the length of a certain movie star’s actual full name.  Store that length in the name_length variable. Don’t forget that there are spaces in between the different parts of a name!

Given_name = “William”
Middle_names = “Bradley”
Family_name = “Pitt”

## Todo: calculate how long this name is
Name_length = None  # Replace ‘None’ with your code
## Answer:  
Name_length = len(Given_name+Given_name+Family_name)+2


### Now we check to make sure that the name fits within the driving licence character limit

#### Uncomment the code below.  You don’t need to make changes to the code

Driving_licence_character_limit = 28
Print(Name_length <= Driving_licence_character_limit)


# Activity:  Type Playground  

Use the programming space below to experiment with types of objects. Don’t forget to use the print to see the output of your code

X = “12”

Print(type(x))

<class ‘str’>

 

# Activity: Total Sales  

In this quiz, you’ll need  to change the types of the input and output data in order to get the result you want.

Calculate the total sales for the week from the data provided. Assign the result to a string variable with the form “ This week’s total sales: xxx” . you need to take care of the spaces to get the correct answer. Don’t forget  to include a space after the colon “: “.

Mon_sales = “121”

Tues_sales = “105”

Wed_sales = “110”

Thurs_sales = “98”

Fri_sales = “95”

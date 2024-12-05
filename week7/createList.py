'''Write some code, including a for loop, that iterates over a list of strings and creates a single string, html_str, which is an HTML list.  For example, if the list is 
Items = ['first string','second string'], printing html_str should output:
<ul>
<li>first string</li>
<li>second string</li>
</ul>
That is, the string's first line should be the opening tag <ul>. Following that is one line per element in the source list, surrounded by <li> and </li> tags.
The final line of the string should be the closing tag </ul>
items = ['first string','second string']
html_str = "<ul>\n" #The "\n" here is the end-of-the-line char, causing chars after this in html_str to be on next line.'''

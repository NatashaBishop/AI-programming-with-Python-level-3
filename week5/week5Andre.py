print('Natalia has {} apples'.format(2))
pet='cat'
do='scratch'
what='floor'
when='fed'
print('Dos your {} {} while {}'.format(pet,do,what,when))
phrase='Dos your {} {} while {}'
print(phrase.format('cat','scratch','floor','fed'))
#--------------split---------
text='asf argrrg ergferg qrwgewrg'
print(text.split())
#------------split3---------
text='asf argrrg ergferg qrwgewrg'
print(text.split(3)) # not working: TypeError: must be str or None, not int
#------------split after index 3---------
text='asf argrrg ergferg qrwgewrg wergrg wrwerwert'
print(text.split(' ',3))
#--------------input-----------
name1=input('First name')
name2=input('Second name')
print('Hello, {} {}'.format(name1.capitalize(),name2.capitalize()))

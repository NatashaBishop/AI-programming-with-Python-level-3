#inspited by http://dy199-124.ust.hk/udacity/[FreeCoursesOnline.Me]%20UDACITY%20-%20Data%20Engineering%20Nanodegree%20v1.0.0/index.html  
#http://dy199-124.ust.hk/udacity/[FreeCoursesOnline.Me]%20UDACITY%20-%20Data%20Engineering%20Nanodegree%20v1.0.0/Part%2007-Module%2001-Lesson%2004_Control%20Flow/35.%20Solution%20Zip%20and%20Enumerate.html 

#use zip 2 create a dictionaty cast: names as keys, heights as values  
cast_names = ['barney', 'Robin', 'ted', 'Lily', 'Marshal']
cast_heights = [22,33,44,55,66]

cast2dictionary = dict(zip(cast_names, cast_heights))
print(cast2dictionary)

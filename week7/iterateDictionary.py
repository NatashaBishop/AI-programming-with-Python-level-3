

book_title = ['great',
 'expectations','the','adventures','of','sherlock','holmes','the',
 'great','gasby','hamlet','adventures','of','huckleberry','fin']

wordCounter={} #create empty dictionary
for i in book_title:
    if i not in wordCounter:
        wordCounter[i]=1
    else:
        wordCounter[i]+=1
##################method2############ 
for i in book_title:
    wordCounter[i]=wordCounter.get(i,0)+1


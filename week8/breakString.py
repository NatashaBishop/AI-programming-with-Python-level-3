'''Activity - Break the String
Due yesterday at 23:59
Instructions
Write a loop with a break statement to create a string, news_ticker, that is exactly 140 characters long. You should create the news ticker by adding headlines from the headlines list, inserting a space in between each headline. If necessary, truncate the last headline in the middle so that news_ticker is exactly 140 characters long.
Remember that break works in both for and while loops. Use whichever loop seems most appropriate. Consider adding print statements to your code to help you resolve bugs. Press the Run button from the top bar to run the code in a cell.

Starter code:

headlines = ["Local Bear Eaten by Man",  "Legislature Announces New Laws", "Peasant Discovers Violence Inherent in System", "Cat Rescues Fireman Stuck in Tree", "Brave Knight Runs Away", "Papperbok Review: Totally Triffic"] 

news_ticker = ""
'''

headlines = ["Local Bear Eaten by Man",  "Legislature Announces New Laws", "Peasant Discovers Violence Inherent in System", "Cat Rescues Fireman Stuck in Tree", "Brave Knight Runs Away", "Papperbok Review: Totally Triffic"] 

news_ticker = ""
for headline in headlines:
    if len(news_ticker) + len(headline) + 1 > 140:  # +1 accounts for the space
        remaining_space = 140 - len(news_ticker) - 1
        news_ticker += headline[:remaining_space]
        break
    news_ticker += headline + " "

# Ensure the news_ticker is exactly 140 characters long
news_ticker = news_ticker[:140]

print(news_ticker)

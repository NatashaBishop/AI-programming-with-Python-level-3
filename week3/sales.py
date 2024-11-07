#Sales data given for each day as string inputs
#calculate total namber of sales

monSales="121"
tuesSales="105"
wedSales="110"
thursSales="98"
friSales="95"

#v.1:
monSales, tuesSales, wedSales, thursSales, friSales = int(monSales), int(tuesSales), int(wedSales), int(thursSales), int(friSales) 
print("total sales: "+str(monSales+tuesSales+wedSales+thursSales+friSales))
#v.2:
print(f"total sales: {int(monSales)+int(tuesSales)+int(wedSales)+int(thursSales)+int(friSales)}")

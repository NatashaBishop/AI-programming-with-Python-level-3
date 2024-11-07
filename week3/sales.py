#Sales data given for each day as string inputs
#calculate total namber of sales

monSales="121"
tuesSales="105"
wedSales="110"
thursSales="198"
friSales="95"

monSales, tuesSales, wedSales, thursSales, friSales = int(monSales), int(tuesSales), int(wedSales), int(thursSales), int(friSales) 
print("total sales "+str(monSales+tuesSales+wedSales+thursSales+friSales))

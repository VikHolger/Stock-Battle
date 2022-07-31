#library
from unicodedata import category, name
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

catgoryName = []
catgoryNum = []
subcategoryName = []
subcategoryNum = []
#Get Data
with open("stocks.stk", "r") as stocks:
    #get category information
    for stk in stocks:
        a = stk.split("|")
        b = a[2].split(",")
        c = []
        for element in b:
            temp = element.split("(")
            c.append(temp[0].strip())

        for elemet in c:
            if elemet in catgoryName:
                catgoryNum[catgoryName.index(elemet.strip())] += 1
            else:
                catgoryName.append(elemet)
                catgoryNum.append(1)

#Create pieplot
plt.pie(catgoryNum, labels=catgoryName)
my_circle=plt.Circle( (0,0), 0.7, color='white')
p = plt.gcf()
p.gca().add_artist(my_circle)

plt.show()

print(catgoryName)
print(catgoryNum)
# Stock Battle #
This project is about trying to create different types of algorithm and seeing how badly they preform. They do this in a custom emmulator, but use the live prize & data to simulate it.

**Version: 0.1.0**

## Table of content
- [Geting Stock information](#PRZ)
- [Statistic Viewer](#STV)
- [Emulator](#EMU)
- [Algorithm](#ALG)
- [Export](#EXP)

<a name="PRZ"></a>
## Geting Stock information

The program gets the stock information by running [prize.py](./prize.py). The python program starts by reading the [stocks file](./stocks.stk) and reading the stock symbol and keeping it in an array. Therafter the program search the stock on [Yahoo finance](https://finance.yahoo.com) adn gather it Stock prise, change today and the latest closing prize. after gathering the information, it saves it in the stocks file under the [prize folder](./prize/). The last ting it does is writing to its [log file](./log/PRZ.log).

<a name="STV"></a>
## Statistic Viewer

[statistic viewer](./statView.py)

TEmpeorary stoarg:  
https://matplotlib.org/stable/gallery/widgets/buttons.html  
https://www.python-graph-gallery.com/donut-plot/  

<a name="EMU"></a>
## Emulator

[Emmulator](./statView.py)

<a name="ALG"></a>
## Algorithm

You can also create your own Algorith!!! (comming soon TM)

[Algorithms](./ALG/)

Name explenation:
The ALG (algoritm) name has many different parts. Here is the common name structure:
chosing stocks | When to trade | how many to trade | chosing by or sell  
example and meaning:  
**FishTactics-TW_OoC_RV10-15_MD**

- Fishy tactics Todays winner list: chosing betwhen 2 random stock on todays winning list with a wighted randomness.
- One of the Crowd: Trades with it if the share is more active then usual
- Random value 10 15%: The number of shares it trades is a randum number from 10 +-15%
- Morning Dawn: Bys betwhen 9:00-12:59; sells betwheen 13:00-16:59

### Chosing stocks

### When to trade

### How many to Trade

### Chosing bying or selling

### Exceptions
<a name="EXP"></a>
## Export

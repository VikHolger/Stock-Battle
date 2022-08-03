# Stock Battle #
This project is about trying to create different types of algorithm and seeing how badly they preform. They do this in a custom emmulator, but use the live prize & data to simulate it.

**Version: DEV-0.1.0**

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
**FT-TW_OoC_RV10-15_MD**

- Fishy tactics Todays winner list: chosing betwhen 2 random stock on todays winning list with a wighted randomness.
- One of the Crowd: Trades with it if the share is more active then usual
- Random value 10 15%: The number of shares it trades is a randum number from 10 +-15%
- Morning Dawn: Bys betwhen 9:00-12:59; sells betwheen 13:00-16:59

### Chosing stocks
| Name | Variants | Short Name | Description |
| :--: | :------: | :--------: | :---------- |
| **Fishy Tactics** | Random | FT-R | Weighted randomness betwhen 2 randon stock in the [stock list](./stocks.stk) |
| | Todays Winners | FT-TW | Weighted randomness betwhen 2 randon stock on todays winners list |
| | Todays Losers | FT-TL |  Weighted randomness betwhen 2 randon stock on todays losers list |
| | History Winners | FT-HW |  Weighted randomness betwhen 2 randon stock on history winners list |
| | History Losers | FT-HL |  Weighted randomness betwhen 2 randon stock on history losers list |
| **Fishy Tactics 5** | Random | FT5-R | Weighted randomness betwhen 5 randon stock in the [stock list](./stocks.stk) |
| | Todays Winners | FT-TW | Weighted randomness betwhen 5 randon stock on todays winners list |
| | Todays Losers | FT5-TL |  Weighted randomness betwhen 5 randon stock on todays losers list |
| | History Winners | FT5-HW |  Weighted randomness betwhen 5 randon stock on history winners list |
| | History Losers | FT5-HL |  Weighted randomness betwhen 5 randon stock on history losers list |
| **Random** | | R | A Random stock in the [stock list](./stocks.stk) |
| **Todays Winner** | True | TW-T | Trading the stock in the first place in the todays winners list |
| | Random | TW-R | Trading a random stock in the todays winners list |
| **Todays Loser** | True | TL-T | Trading the stock in the first place in the todays losers list |
| | Random | TL-R | Trading a random stock in the todays losers list |
| **History Winner** | True | HW-T | Trading the stock in the first place in the history winners list |
| | Random | HW-R | Trading a random stock in the history winners list |
| **History Loser** | True | HL-T | Trading the stock in the first place in the history losers list |
| | Random | HL-R | Trading a random stock in the history losers list |
| **Random Portfoilo x** | | RP-x | liquid asset > x% → Bys: Random stock in a category it has less % shares in; liquid asset ≤ x% → Sell: Random stock in portfoilo |
| **Equlirian Portfoilo x** | | EP-x | liquid asset > x% → Bys: Random stock in a category it has less % shares in; liquid asset ≤ x% → Sell:  Random stock in a category it has most % shares in |
| **Socialist Portfoilo x** | | SP-x | liquid asset > x% → Bys: Random stock in a category it has less value in; liquid asset ≤ x% → Sell: Random stock in portfoilo in a catoegory with highest value in|
| **One of the Crowd** | | OoC | Trades wiht the stock that is the most active |
| **By my Seld x** | | BmS | Trades wiht the stock that is the less active |
| **Looper** | True | L-T | has a list alphabticly sorted. trades with the top one, then go down 1 step. |
| | Anti | L-A | has a list alphabticly sorted. trades with the bottom one, then go up 1 step. |

### When to trade
| Name | Short Name | Description |
| :--: | :--------: | :---------- |
| **Random x** | R-x | Trades randomily, aproximatley x% of the time |
| **One of the Crowd x** | O-x | Trades when more then x‰ of shares is activly traded today |
| **By my Seld x** | B-x | Trades when less then x‰ of shares is activly traded today |
| **Timeu** | T | Trades with the stock if it has booth  minut numbers in in the shares value |
| **Dateu** | D | Trades shares if it has at least 3 of the nummbers in todays date (yyyy-mm-dd) |

### How many to Trade

### Chosing bying or selling

### Exceptions
<a name="EXP"></a>
## Export

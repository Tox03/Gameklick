# сделать инструкцию
# коэфициенты  






from tkinter import * #модуль ткинтер (для создания окон , кнопок , надписей и вцелом работы с окнами созданными им)
from random import * #модуль рандома (для создания рандомных чисел)
from tkinter import ttk #подмодуль ткинтера (для создания вкладок и работы с ними)
import time #модуль времени (для сохранения времени)



#всt ниже перечисленные значения( имена или переменные ) возвращается после перезапуска к значениям указанным ниже (если поменять то к тем на какие они поменяны)
#подсчёт кнопок ведётся сверху вниз и затем слева направо (десята внизу )

maxlevels = 0 #количество максимально прокаченных кнопок

upgrades1 = 1 #количество прокачек первой кнопки
upgrades2 = 1 #количество прокачек второй кнопки
upgrades3 = 1 #количество прокачек третьей кнопки
upgrades4 = 1 #количество прокачек четвёртой кнопки
upgrades5 = 1 #количество прокачек пятой кнопки
upgrades6 = 1 #количество прокачек шестой кнопки
upgrades7 = 1 #количество прокачек седьмой кнопки
upgrades8 = 1 #количество прокачек восьмой кнопки
upgrades9 = 1 #количество прокачек девятой кнопки
upgrades10 = 1 #количество прокачек десятой кнопки
upgrades13 = 1 #уровень прокачек третей кнопки
upgrades14 = 1 #уровень прокачек четвёртой кнопки
upgrades15 = 1 #уровень прокачек пятой кнопки
upgrades16 = 1 #уровень прокачек шестой кнопки
upgrades17 = 1 #уровень прокачек седьмой кнопки
upgrades18 = 1 #уровень прокачек восьмой кнопки
upgrades19 = 1 #уровень прокачек девятой кнопки


cashinbtns = [0,0,0,0,0,0,0,0,0,0] #список с количеством денег в кнопках 

addcashinbtnnumber1 = 1 #количество добавляемой валюты за нажатие на первую кнопку 
addcashinbtnnumber2 = 1 #количество добавляемой валюты за нажатие на вторую кнопку 
addcashinbtnnumber3 = 1 #количество добавляемой валюты за нажатие на третью кнопку 
addcashinbtnnumber4 = 1 #количество добавляемой валюты за нажатие на четвёртое кнопку 
addcashinbtnnumber5 = 1 #количество добавляемой валюты за нажатие на пятое кнопку 
addcashinbtnnumber6 = 1 #количество добавляемой валюты за нажатие на шестую кнопку 
addcashinbtnnumber7 = 1 #количество добавляемой валюты за нажатие на седьмую кнопку 
addcashinbtnnumber8 = 1 #количество добавляемой валюты за нажатие на восьмую кнопку 
addcashinbtnnumber9 = 1 #количество добавляемой валюты за нажатие на девятую кнопку 
addcashinbtnnumber10 = 9 #количество добавляемой валюты за нажатие на десятую кнопку 

cashforsek = 0 #количество денег в секунду

upgradeclick1 = 1 #количесво на которое увеличестся количество приболвяемой прибыли с первой кнопки при прокачке (меняется с каждой покупкой)
upgradeclick2 = 1 #количесво на которое увеличестся количество приболвяемой прибыли со второй кнопки при прокачке (меняется с каждой покупкой)
upgradeclick3 = 1 #количесво на которое увеличестся количество приболвяемой прибыли с третьей кнопки при прокачке (меняется с каждой покупкой)
upgradeclick4 = 1 #количесво на которое увеличестся количество приболвяемой прибыли с четвёртой кнопки при прокачке (меняется с каждой покупкой)
upgradeclick5 = 1 #количесво на которое увеличестся количество приболвяемой прибыли с пятой кнопки при прокачке (меняется с каждой покупкой)
upgradeclick6 = 1 #количесво на которое увеличестся количество приболвяемой прибыли с шестой кнопки при прокачке (меняется с каждой покупкой)
upgradeclick7 = 1 #количесво на которое увеличестся количество приболвяемой прибыли с седьмой кнопки при прокачке (меняется с каждой покупкой)
upgradeclick8 = 1 #количесво на которое увеличестся количество приболвяемой прибыли с с восьмой кнопки при прокачке (меняется с каждой покупкой)
upgradeclick9 = 1 #количесво на которое увеличестся количество приболвяемой прибыли с девятой кнопки при прокачке (меняется с каждой покупкой)
upgradeclick10 = 1 #количесво на которое увеличестся количество приболвяемой прибыли с десятой кнопки при прокачке (меняется с каждой покупкой)

levelmaxupgrade1 = 0 #равняется 1 когда первая кнопка прокачена на максимум
levelmaxupgrade2 = 0 #равняется 1 когда вторая кнопка прокачена на максимум
levelmaxupgrade3 = 0 #равняется 1 когда третья кнопка прокачена на максимум
levelmaxupgrade4 = 0 #равняется 1 когда четвёртая кнопка прокачена на максимум
levelmaxupgrade5 = 0 #равняется 1 когда пятая кнопка прокачена на максимум
levelmaxupgrade6 = 0 #равняется 1 когда шестая кнопка прокачена на максимум
levelmaxupgrade7 = 0 #равняется 1 когда седьмая кнопка прокачена на максимум
levelmaxupgrade8 = 0 #равняется 1 когда восьмая кнопка прокачена на максимум
levelmaxupgrade9 = 0 #равняется 1 когда девятая кнопка прокачена на максимум
levelmaxupgrade10 = 0 #равняется 1 когда десятая кнопка прокачена на максимум
levelmaxupgrade13 = 0 #равняется 1 когда третья кнопка прокачена на максимум
levelmaxupgrade14 = 0 #равняется 1 когда четвёртая кнопка прокачена на максимум
levelmaxupgrade15 = 0 #равняется 1 когда пятая кнопка прокачена на максимум
levelmaxupgrade16 = 0 #равняется 1 когда шестая кнопка прокачена на максимум
levelmaxupgrade17 = 0 #равняется 1 когда седьмая кнопка прокачена на максимум
levelmaxupgrade18 = 0 #равняется 1 когда восьмая кнопка прокачена на максимум
levelmaxupgrade19 = 0 #равняется 1 когда девятая кнопка прокачена на максимум

price1 = 1 #цена улучшения первой кнопки (меняется с каждой покупкой)
price2 = 1 #цена улучшения второй кнопки (меняется с каждой покупкой)
price3 = 1 #цена улучшения третьей кнопки (меняется с каждой покупкой)
price4 = 1 #цена улучшения четвёртой кнопки (меняется с каждой покупкой)
price5 = 1 #цена улучшения пятой кнопки (меняется с каждой покупкой)
price6 = 1 #цена улучшения шестой кнопки (меняется с каждой покупкой)
price7 = 1 #цена улучшения седьмой кнопки (меняется с каждой покупкой)
price8 = 1 #цена улучшения восьмой кнопки (меняется с каждой покупкой)
price9 = 1 #цена улучшения девятой кнопки (меняется с каждой покупкой)
price10 = 1 #цена улучшения десятой кнопки (меняется с каждой покупкой)
price0 = 5000 #цена улучшения количества со сколькольких рандомных кнопок соберётся прибыль (меняется с каждой покупкой)

savetime = 0 #время начала работы игры , а в последующем и начало времени работы cashforsek (может сеняться во время исполнения кода)

pricebuy1 = 64 #цена покупки дохода в 1 в секунду (меняется с каждой покупкой)
pricebuy2 = 64 * 9 #цена покупки дохода в 10 в секунду (меняется с каждой покупкой)
pricebuy3 = 64 * 8 * 10 #цена покупки дохода в 100 в секунду (меняется с каждой покупкой)
pricebuy4 = 64 * 7 * 10 * 10 #цена покупки дохода в 1000 в секунду (меняется с каждой покупкой)
pricebuy5 = 64 * 6 * 10 * 10 * 10 #цена покупки дохода в 10000 в секунду (меняется с каждой покупкой)
pricebuy6 = 64 * 5 * 10 * 10 * 10 * 10 #цена покупки дохода в 100000 в секунду (меняется с каждой покупкой)
pricebuy7 = 100000000 #цена покупки дохода со всех кнопок на авто доход

amountofmoney = 0 #количество собранных денег

upgradecashforsek1 = 1 #прокачка дохода при нажатии на первую кнопку 
upgradecashforsek2 = 10 #прокачка дохода при нажатии на вторую кнопку 
upgradecashforsek3 = 100 #прокачка дохода при нажатии на третью кнопку 
upgradecashforsek4 = 1000 #прокачка дохода при нажатии на четвёртую кнопку 
upgradecashforsek5 = 10000 #прокачка дохода при нажатии на пятую кнопку 
upgradecashforsek6 = 100000 #прокачка дохода при нажатии на шестую кнопку 

cashcollectionamount = 3 #количество со сколькольких рандомных кнопок соберётся прибыль



def updatetext(): #функция обновления текста ( например суммы денег или количества денег в той или иной кнопке)
	global amountofmoney
	global cashinbtns
	lbl.configure(text = "собранные деньги = " + str(int(amountofmoney)) + "$")
	lbl1.configure(text = "общая сумма денег = " + str(int(sum(cashinbtns) + amountofmoney)) + "$")
	lbl2.configure(text = "сумма денег в кнопках = " + str(int(sum(cashinbtns))) + "$")
	lbl3.configure(text = "собранные деньги = "+ str(int(amountofmoney)) + "$")
	lbl4.configure(text = "общая сумма денег = " + str(int(sum(cashinbtns)+amountofmoney)) + "$")
	lbl5.configure(text = "сумма денег в кнопках = " + str(int(sum(cashinbtns))) + "$")
	lbl11.configure(text = str(int(cashinbtns[0])) + "$" + " + " + str(int(addcashinbtnnumber1)) + "$")
	lbl12.configure(text = str(int(cashinbtns[1])) + "$" + " + " + str(int(addcashinbtnnumber2)) + "$")
	lbl13.configure(text = str(int(cashinbtns[2])) + "$" + " + " + str(int(addcashinbtnnumber3)) + "$")
	lbl14.configure(text = str(int(cashinbtns[3])) + "$" + " + " + str(int(addcashinbtnnumber4)) + "$")
	lbl15.configure(text = str(int(cashinbtns[4])) + "$" + " + " + str(int(addcashinbtnnumber5)) + "$")
	lbl16.configure(text = str(int(cashinbtns[5])) + "$" + " + " + str(int(addcashinbtnnumber6)) + "$")
	lbl17.configure(text = str(int(cashinbtns[6])) + "$" + " + " + str(int(addcashinbtnnumber7)) + "$")
	lbl18.configure(text = str(int(cashinbtns[7])) + "$" + " + " + str(int(addcashinbtnnumber8)) + "$")
	lbl19.configure(text = str(int(cashinbtns[8])) + "$" + " + " + str(int(addcashinbtnnumber9)) + "$")

def updatetext2(): #функция обновления стоимости услуг , прокачки и денег в секунду 
	global levelmaxupgrade19
	global maxlevels
	if maxlevels < 18:
		lbl21.configure(text = str(min(int(price1),int(price2),int(price3),int(price4),int(price5),int(price6),int(price7),int(price8),int(price9))) + " - " + str(max(int(price1),int(price2),int(price3),int(price4),int(price5),int(price6),int(price7),int(price8),int(price9))) + "$")
		lbl22.configure(text = str(int(price0)) + "$")
		lbl23.configure(text = str(int(pricebuy1)) + "$")
		lbl24.configure(text = str(int(pricebuy2)) + "$")
		lbl25.configure(text = str(int(pricebuy3)) + "$")
		lbl26.configure(text = str(int(pricebuy4)) + "$")
		lbl27.configure(text = str(int(pricebuy5)) + "$")
		lbl28.configure(text = str(int(pricebuy6)) + "$")
		lbl29.configure(text = str(int(pricebuy7)) + "$")
		lbl6.configure(text = "+ " + str(int(cashforsek)) + "$ в секунду")
	if levelmaxupgrade19 == 1 and maxlevels < 18:
		lbl7 = Label(tab1, text = str(int(cashinbtns[9])) + "$" + " + " + str(int(addcashinbtnnumber10)) + "$",bg = "lightblue")
		lbl7.place(x = 620, y = 672)
		lbl8 = Label(tab2, text = str(int(price10)) + "$",bg = "lightblue")
		lbl8.place(x = 620, y = 672)

def click1(): #функция нажатия на первую кнопку 
	global cashinbtns
	global addcashinbtnnumber1
	cashinbtns[0] += addcashinbtnnumber1
	updatetext()

def click2(): #функция нажатия на вторую кнопку 
	global cashinbtns
	global addcashinbtnnumber2
	cashinbtns[1] += addcashinbtnnumber2
	updatetext()

def click3(): #функция нажатия на третью кнопку 
	global cashinbtns
	global addcashinbtnnumber3
	cashinbtns[2] += addcashinbtnnumber3
	updatetext()

def click4(): #функция нажатия на четвёртую кнопку 
	global cashinbtns
	global addcashinbtnnumber4
	cashinbtns[3] += addcashinbtnnumber4
	updatetext()

def click5(): #функция нажатия на пятую кнопку 
	global cashinbtns
	global addcashinbtnnumber5
	cashinbtns[4] += addcashinbtnnumber5
	updatetext()

def click6(): #функция нажатия на шестую кнопку 
	global cashinbtns
	global addcashinbtnnumber6
	cashinbtns[5] += addcashinbtnnumber6
	updatetext()

def click7(): #функция нажатия на седьмую кнопку 
	global cashinbtns
	global addcashinbtnnumber7
	cashinbtns[6] += addcashinbtnnumber7
	updatetext()

def click8(): #функция нажатия на восьмую кнопку 
	global cashinbtns
	global addcashinbtnnumber8
	cashinbtns[7] += addcashinbtnnumber8
	updatetext()

def click9(): #функция нажатия на девятую кнопку 
	global cashinbtns
	global addcashinbtnnumber9
	cashinbtns[8] += addcashinbtnnumber9
	updatetext()

def click10(): #функция нажатия на десятую кнопку
	global cashinbtns
	global addcashinbtnnumber10
	cashinbtns[9] += addcashinbtnnumber10
	updatetext()

def upgrade1(): #функция прокачки первой кнопки 
	global amountofmoney
	global price1
	global addcashinbtnnumber1
	global upgradeclick1
	global cashforsek
	global levelmaxupgrade19
	global maxlevels
	global upgrades1
	global addcashinbtnnumber10
	global levelmaxupgrade1
	if price1 < amountofmoney and levelmaxupgrade19 == 0 and upgrades1 < 25:
		amountofmoney -= price1
		price1 *= 1.8
		addcashinbtnnumber1 += upgradeclick1
		addcashinbtnnumber10 += upgradeclick1 / 100
		upgradeclick1 *= 1.5
		upgrades1 += 1
	else:
		if price1 < amountofmoney and levelmaxupgrade19 == 1 and upgrades1 < 25:
			amountofmoney -= price1
			price1 *= 1.8
			cashforsek += upgradeclick1
			addcashinbtnnumber10 += upgradeclick1 / 100
			upgradeclick1 *= 1.5
			upgrades1 += 1
	if (upgrades1 == 25 or upgrades1 > 25) and levelmaxupgrade1 == 0:
		levelmaxupgrade1 = 1
		maxlevels += 1
	updatetext()

def upgrade2(): #функция прокачки второй кнопки
	global amountofmoney
	global price2
	global addcashinbtnnumber2
	global upgradeclick2
	global cashforsek
	global levelmaxupgrade19
	global maxlevels
	global upgrades2
	global addcashinbtnnumber10
	global levelmaxupgrade2
	if price2 < amountofmoney and levelmaxupgrade19 == 0 and upgrades2 < 25:
		amountofmoney -= price2
		price2 *= 1.8
		addcashinbtnnumber2 += upgradeclick2
		addcashinbtnnumber10 += upgradeclick2 / 100
		upgradeclick2 *= 1.5
		upgrades2 += 1
	else:
		if price2 < amountofmoney and levelmaxupgrade19 == 1 and upgrades2 < 25:
			amountofmoney -= price2
			price2 *= 1.8
			cashforsek += upgradeclick2
			addcashinbtnnumber10 += upgradeclick2 / 100
			upgradeclick2 *= 1.5
			upgrades2 += 1
	if (upgrades2 == 25 or upgrades2 > 25) and levelmaxupgrade2 == 0:
		levelmaxupgrade2 = 1
		maxlevels += 1
	updatetext()

def upgrade3(): #функция прокачки третьей кнопки
	global amountofmoney
	global price3
	global addcashinbtnnumber3
	global upgradeclick3
	global cashforsek
	global levelmaxupgrade19
	global maxlevels
	global upgrades3
	global addcashinbtnnumber10
	global levelmaxupgrade3
	if price3 < amountofmoney and levelmaxupgrade19 == 0 and upgrades3 < 25:
		amountofmoney -= price3
		price3 *= 1.8
		addcashinbtnnumber3 += upgradeclick3
		addcashinbtnnumber10 += upgradeclick3 / 100
		upgradeclick3 *= 1.5
		upgrades3 += 1
	else:
		if price3 < amountofmoney and levelmaxupgrade19 == 1 and upgrades3 < 25:
			amountofmoney -= price3
			price3 *= 1.8
			cashforsek += upgradeclick3
			addcashinbtnnumber10 += upgradeclick3 / 100
			upgradeclick3 *= 1.5
			upgrades3 += 1
	if (upgrades3 == 25 or upgrades3 > 25) and levelmaxupgrade3 == 0:
		levelmaxupgrade3 = 1
		maxlevels += 1
	updatetext()

def upgrade4(): #функция прокачки четвёртой кнопки
	global amountofmoney
	global price4
	global addcashinbtnnumber4
	global upgradeclick4
	global cashforsek
	global levelmaxupgrade19
	global maxlevels
	global upgrades4
	global addcashinbtnnumber10
	global levelmaxupgrade4
	if price4 < amountofmoney and levelmaxupgrade19 == 0 and upgrades4 < 25:
		amountofmoney -= price4
		price4 *= 1.8
		addcashinbtnnumber4 += upgradeclick4
		addcashinbtnnumber10 += upgradeclick4 / 100
		upgradeclick4 *= 1.5
		upgrades4 += 1
	else:
		if price4 < amountofmoney and levelmaxupgrade19 == 1 and upgrades4 < 25:
			amountofmoney -= price4
			price4 *= 1.8
			cashforsek += upgradeclick4
			addcashinbtnnumber10 += upgradeclick4 / 100
			upgradeclick4 *= 1.5
			upgrades4 += 1
	if (upgrades4 == 25 or upgrades4 > 25) and levelmaxupgrade4 == 0:
		levelmaxupgrade4 = 1
		maxlevels += 1
	updatetext()

def upgrade5(): #функция прокачки пятой кнопки
	global amountofmoney
	global price5
	global addcashinbtnnumber5
	global upgradeclick5
	global cashforsek
	global levelmaxupgrade19
	global maxlevels
	global upgrades5
	global addcashinbtnnumber10
	global levelmaxupgrade5
	if price5 < amountofmoney and levelmaxupgrade19 == 0 and upgrades5 < 25:
		amountofmoney -= price5
		price5 *= 1.8
		addcashinbtnnumber5 += upgradeclick5
		addcashinbtnnumber10 += upgradeclick5 / 100
		upgradeclick5 *= 1.5
		upgrades5 += 1
	else:
		if price5 < amountofmoney and levelmaxupgrade19 == 1 and upgrades5 < 25:
			amountofmoney -= price5
			price5 *= 1.8
			cashforsek += upgradeclick5
			addcashinbtnnumber10 += upgradeclick5 / 100
			upgradeclick5 *= 1.5
			upgrades5 += 1
	if (upgrades5 == 25 or upgrades5 > 25) and levelmaxupgrade5 == 0:
		levelmaxupgrade5 = 1
		maxlevels += 1
	updatetext()

def upgrade6(): #функция прокачки шестой кнопки
	global amountofmoney
	global price6
	global addcashinbtnnumber6
	global upgradeclick6
	global cashforsek
	global levelmaxupgrade19
	global cashforsek
	global maxlevels
	global upgrades6
	global addcashinbtnnumber10
	global levelmaxupgrade6
	if price6 < amountofmoney and levelmaxupgrade19 == 0 and upgrades6 < 25:
		amountofmoney -= price6
		price6 *= 1.8
		addcashinbtnnumber6 += upgradeclick6
		addcashinbtnnumber10 += upgradeclick6 / 100
		upgradeclick6 *= 1.5
		upgrades6 += 1
	else:
		if price6 < amountofmoney and levelmaxupgrade19 == 1 and upgrades6 < 25:
			amountofmoney -= price6
			price6 *= 1.8
			cashforsek += upgradeclick6
			addcashinbtnnumber10 += upgradeclick6 / 100
			upgradeclick6 *= 1.5
			upgrades6 += 1
	if (upgrades6 == 25 or upgrades6 > 25) and levelmaxupgrade6 == 0:
		levelmaxupgrade6 = 1
		maxlevels += 1
	updatetext()

def upgrade7(): #функция прокачки седьмой кнопки
	global amountofmoney
	global price7
	global addcashinbtnnumber7
	global upgradeclick7
	global cashforsek
	global levelmaxupgrade19
	global maxlevels
	global upgrades7
	global addcashinbtnnumber10
	global levelmaxupgrade7
	if price7 < amountofmoney and levelmaxupgrade19 == 0 and upgrades7 < 25:
		amountofmoney -= price7
		price7 *= 1.8
		addcashinbtnnumber7 += upgradeclick7
		addcashinbtnnumber10 += upgradeclick7 / 100
		upgradeclick7 *= 1.5
		upgrades7 += 1
	else:
		if price7 < amountofmoney and levelmaxupgrade19 == 1 and upgrades7 < 25:
			amountofmoney -= price7
			price7 *= 1.8
			cashforsek += upgradeclick7
			addcashinbtnnumber10 += upgradeclick7 / 100
			upgradeclick7 *= 1.5
			upgrades7 += 1
	if (upgrades7 == 25 or upgrades7 > 25) and levelmaxupgrade7 == 0:
		levelmaxupgrade7 = 1
		maxlevels += 1
	updatetext()

def upgrade8(): #функция прокачки восьмой кнопки
	global amountofmoney
	global price8
	global addcashinbtnnumber8
	global upgradeclick8
	global cashforsek
	global levelmaxupgrade19
	global maxlevels
	global upgrades8
	global addcashinbtnnumber10
	global levelmaxupgrade8
	if price8 < amountofmoney and levelmaxupgrade19 == 0 and upgrades8 < 25:
		amountofmoney -= price8
		price8 *= 1.8
		addcashinbtnnumber8 += upgradeclick8
		addcashinbtnnumber10 += upgradeclick8 / 100
		upgradeclick8 *= 1.5
		upgrades8 += 1
	else:
		if price8 < amountofmoney and levelmaxupgrade19 == 1 and upgrades8 < 25:
			amountofmoney -= price8
			price8 *= 1.8
			cashforsek += upgradeclick8
			addcashinbtnnumber10 += upgradeclick8 / 100
			upgradeclick8 *= 1.5
			upgrades8 += 1
	if (upgrades8 == 25 or upgrades8 > 25) and levelmaxupgrade8 == 0:
		levelmaxupgrade8 = 1
		maxlevels += 1
	updatetext()

def upgrade9(): #функция прокачки девятой кнопки
	global amountofmoney
	global price9
	global addcashinbtnnumber9
	global upgradeclick9
	global cashforsek
	global levelmaxupgrade19
	global maxlevels
	global upgrades9
	global addcashinbtnnumber10
	global levelmaxupgrade9
	if price9 < amountofmoney and levelmaxupgrade19 == 0 and upgrades9 < 25:
		amountofmoney -= price9
		price9 *= 1.8
		addcashinbtnnumber9 += upgradeclick9
		addcashinbtnnumber10 += upgradeclick9 / 100
		upgradeclick9 *= 1.5
		upgrades9 += 1
	else:
		if price9 < amountofmoney and levelmaxupgrade19 == 1 and upgrades9 < 25:
			amountofmoney -= price9
			price9 *= 1.8
			cashforsek += upgradeclick9
			addcashinbtnnumber10 += upgradeclick9 / 100
			upgradeclick9 *= 1.5
			upgrades9 += 1
	if (upgrades9 == 25 or upgrades9 > 25) and levelmaxupgrade9 == 0:
		levelmaxupgrade9 = 1
		maxlevels += 1
	updatetext()

def upgrade10(): #функция прокачки десятой кнопки
	global amountofmoney
	global price10
	global addcashinbtnnumber10
	global upgradeclick10
	global upgrades10
	global levelmaxupgrade10
	global maxlevels
	if price10 < amountofmoney and upgrades10 < 25:
		amountofmoney -= price10
		price10 *= 1.8
		addcashinbtnnumber10 += upgradeclick10
		upgradeclick10 *= 1.5
		upgrades10 += 1
	if (upgrades10 == 25 or upgrades10 > 25) and levelmaxupgrade10 == 0:
		levelmaxupgrade10 = 1
		maxlevels  += 1
	updatetext()
	updatetext2()

def upgrade0(): #функция прокачки количества со сколькольких рандомных кнопок соберётся прибыль
	global amountofmoney
	global price0
	global cashcollectionamount
	if price0 < amountofmoney and cashcollectionamount <= 8:
		amountofmoney -= price0
		price0 *= 2
		cashcollectionamount += 1
	updatetext()
	updatetext2()

def upgrade(): #функция рандомизации прокачки кнопок
	randomnamber = randint(1,9)
	number0or1 = 0
	if randomnamber == 1 and levelmaxupgrade1 == 0:
		upgrade1()
		number0or1 += 1
	else:
		if randomnamber == 2 and levelmaxupgrade2 == 0:
			upgrade2()
			number0or1 += 1
		else:
			if randomnamber == 3 and levelmaxupgrade3 == 0:
				upgrade3()
				number0or1 += 1
			else:
				if randomnamber == 4 and levelmaxupgrade4 == 0:
					upgrade4()
					number0or1 += 1
				else:
					if randomnamber == 5 and levelmaxupgrade5 == 0:
						upgrade5()
						number0or1 += 1
					else:
						if randomnamber == 6 and levelmaxupgrade6 == 0:
							upgrade6()
							number0or1 += 1
						else:
							if randomnamber == 7 and levelmaxupgrade7 == 0:
								upgrade7()
								number0or1 += 1
							else:
								if randomnamber == 8 and levelmaxupgrade8 == 0:
									upgrade8()
									number0or1 += 1
								else:
									if randomnamber == 9 and levelmaxupgrade9 == 0:
										upgrade9()
										number0or1 += 1
	if number0or1 == 0 and levelmaxupgrade1 == 0:
		upgrade1()
	else:
		if number0or1 == 0 and levelmaxupgrade2 == 0:
			upgrade2()
		else:
			if number0or1 == 0 and levelmaxupgrade3 == 0:
				upgrade3()
			else:
				if number0or1 == 0 and levelmaxupgrade4 == 0:
					upgrade4()
				else:
					if number0or1 == 0 and levelmaxupgrade5 == 0:
						upgrade5()
					else:
						if number0or1 == 0 and levelmaxupgrade6 == 0:
							upgrade6()
						else:
							if number0or1 == 0 and levelmaxupgrade7 == 0:
								upgrade7()
							else:
								if number0or1 == 0 and levelmaxupgrade8 == 0:
									upgrade8()
								else:
									if number0or1 == 0 and levelmaxupgrade9 == 0:
										upgrade9()
	updatetext()
	updatetext2()

def savetimetime(): #обновляет сохранённое время и сохраняет текущее
	global savetime
	savetime = time.time()

def buy1(): #прокачка дохода в секунду на 1 сек
	global amountofmoney
	global pricebuy1
	global upgradecashforsek1
	global cashforsek
	global savetime
	global maxlevels
	global upgrades13
	global levelmaxupgrade13
	seks = time.time() - savetime
	amountofmoney += seks * cashforsek
	savetimetime()
	if pricebuy1 < amountofmoney and upgrades13 < 25:
		amountofmoney -= pricebuy1
		pricebuy1 *= 1.2 * 1.2
		cashforsek += upgradecashforsek1
		upgrades13 += 1
	if (upgrades13 == 25 or upgrades13 > 25) and levelmaxupgrade13 == 0:
		levelmaxupgrade13 = 1
		maxlevels += 1
	updatetext()
	updatetext2()

def buy2(): #прокачка дохода в секунду на 10 сек
	global amountofmoney
	global pricebuy2
	global upgradecashforsek2
	global cashforsek
	global savetime
	global maxlevels
	global upgrades14
	global levelmaxupgrade14
	seks = time.time() - savetime
	amountofmoney += seks * cashforsek
	savetimetime()
	if pricebuy2 < amountofmoney and upgrades14 < 20:
		amountofmoney -= pricebuy2
		pricebuy2 *= 1.2 * 1.2
		cashforsek += upgradecashforsek2
		upgrades14 += 1
	if (upgrades14 == 20 or upgrades14 > 20) and levelmaxupgrade14 == 0:
		levelmaxupgrade14 = 1
		maxlevels += 1
	updatetext()
	updatetext2()

def buy3(): #прокачка дохода в секунду на 100 сек
	global amountofmoney
	global pricebuy3
	global upgradecashforsek3
	global cashforsek
	global savetime
	global maxlevels
	global upgrades15
	global levelmaxupgrade15
	seks = time.time() - savetime
	amountofmoney += seks * cashforsek
	savetimetime()
	if pricebuy3 < amountofmoney and upgrades15 < 15:
		amountofmoney -= pricebuy3
		pricebuy3 *= 1.2 * 1.2
		cashforsek += upgradecashforsek3
		upgrades15 += 1
	if (upgrades15 == 15 or upgrades15 > 15) and levelmaxupgrade15 == 0:
		levelmaxupgrade15 = 1
		maxlevels += 1
	updatetext()
	updatetext2()

def buy4(): #прокачка дохода в секунду на 1000 сек
	global amountofmoney
	global pricebuy4
	global upgradecashforsek4
	global cashforsek
	global savetime
	global maxlevels
	global upgrades16
	global levelmaxupgrade16
	seks = time.time() - savetime
	amountofmoney += seks * cashforsek
	savetimetime()
	if pricebuy4 < amountofmoney and upgrades16 < 15:
		amountofmoney -= pricebuy4
		pricebuy4 *= 1.2 * 1.2
		cashforsek += upgradecashforsek4
		upgrades16 += 1
	if (upgrades16 == 15 or upgrades16 > 15) and levelmaxupgrade16 == 0:
		levelmaxupgrade16 = 1
		maxlevels += 1
	updatetext()
	updatetext2()

def buy5(): #прокачка дохода в секунду на 10000 сек
	global amountofmoney
	global pricebuy5
	global upgradecashforsek5
	global cashforsek
	global savetime
	global maxlevels
	global upgrades17
	global levelmaxupgrade17
	seks = time.time() - savetime
	amountofmoney += seks * cashforsek
	savetimetime()
	if pricebuy5 < amountofmoney and upgrades17 < 10:
		amountofmoney -= pricebuy5
		pricebuy5 *= 1.2 * 1.2
		cashforsek += upgradecashforsek5
		upgrades17 += 1
	if (upgrades17 == 10 or upgrades17 > 10) and levelmaxupgrade17 == 0:
		levelmaxupgrade17 = 1
		maxlevels += 1
	updatetext()
	updatetext2()

def buy6(): #прокачка дохода в секунду на 100000 сек
	global amountofmoney
	global pricebuy6
	global upgradecashforsek6
	global cashforsek
	global savetime
	global maxlevels
	global upgrades18
	global levelmaxupgrade18
	seks = time.time() - savetime
	amountofmoney += seks * cashforsek
	savetimetime()
	if pricebuy6 < amountofmoney and upgrades18 < 5:
		amountofmoney -= pricebuy6
		pricebuy6 *= 1.2 * 1.2
		cashforsek += upgradecashforsek6
		upgrades18 += 1
	if (upgrades18 == 5 or upgrades18 > 5) and levelmaxupgrade18 == 0:
		levelmaxupgrade18 = 1
		maxlevels += 1
	updatetext()
	updatetext2()

def buy7(): #прокачка дохода в сек на количество прибыли со всех кнопок кроме 10
	global amountofmoney
	global pricebuy7
	global cashforsek
	global savetime
	global maxlevels
	global levelmaxupgrade19
	global addcashinbtnnumber1
	global addcashinbtnnumber2
	global addcashinbtnnumber3
	global addcashinbtnnumber4
	global addcashinbtnnumber5
	global addcashinbtnnumber6
	global addcashinbtnnumber7
	global addcashinbtnnumber8
	global addcashinbtnnumber9
	seks = time.time() - savetime
	amountofmoney += seks * cashforsek
	savetimetime()
	if pricebuy7 < amountofmoney and levelmaxupgrade19 == 0:
		cashforsek = cashforsek + (addcashinbtnnumber1 + addcashinbtnnumber2 + addcashinbtnnumber3 + addcashinbtnnumber4 + addcashinbtnnumber5 + addcashinbtnnumber6 + addcashinbtnnumber7 + addcashinbtnnumber8 + addcashinbtnnumber9)
		addcashinbtnnumber1 = 0
		addcashinbtnnumber2 = 0
		addcashinbtnnumber3 = 0
		addcashinbtnnumber4 = 0
		addcashinbtnnumber5 = 0
		addcashinbtnnumber6 = 0
		addcashinbtnnumber7 = 0
		addcashinbtnnumber8 = 0
		addcashinbtnnumber9 = 0
		amountofmoney -= pricebuy7
		levelmaxupgrade19 = 1
		maxlevels += 1
		plusbutton()
	updatetext()
	updatetext2()

def plusbutton(): #функция добавления 10 кнопки , и её прокачки , а так-же текст под ними
	btn10 = Button(tab1, text = "клик",command = click10,width = 67,height = 4, bg = "pink", fg = "blue")  
	btn10.place(x = 400, y = 600)
	btn11 = Button(tab2, text = "улучшение 10 кнопки",command = upgrade10,width = 67,height = 4, bg = "pink", fg = "blue")  
	btn11.place(x = 400, y = 600)

def click0(): #Сбор с кликеров и дохода в секунду 
	global cashinbtns
	global amountofmoney
	global cashcollectionamount
	global cashforsek
	global savetime
	seks = time.time() - savetime
	amountofmoney += seks * cashforsek
	savetimetime()
	numbers08v1 = [0,1,2,3,4,5,6,7,8]
	lenofnumbers08 = 9
	amountofmoney += cashinbtns[9]
	cashinbtns[9] = 0
	if cashcollectionamount == 9 or cashcollectionamount > 9:
		amountofmoney += sum(cashinbtns)
		cashinbtns[0] = 0
		cashinbtns[1] = 0
		cashinbtns[2] = 0
		cashinbtns[3] = 0
		cashinbtns[4] = 0
		cashinbtns[5] = 0
		cashinbtns[6] = 0
		cashinbtns[7] = 0
		cashinbtns[8] = 0
	else:
		for number in range(cashcollectionamount):
			lenofnumbers08 -= 1
			numbers08v2 = []
			randomnamber0lon = randint(0,lenofnumbers08)
			amountofmoney += cashinbtns[numbers08v1[randomnamber0lon]]
			cashinbtns[numbers08v1[randomnamber0lon]] = 0
			numbers08v1[randomnamber0lon] = ""
			for i in numbers08v1:
				if i != "":
					numbers08v2.append(number)
			numbers08v1 = numbers08v2
	updatetext()
	updatetext2()


savetimetime()


#создание окна , покраска заднего фона и вкладок
window = Tk()
window.title("кликер 339")
window.geometry("1000x800")
window.config(bg="lightblue")
tab_control = ttk.Notebook(window) 
tab0 = ttk.Frame(tab_control) 
tab1 = ttk.Frame(tab_control)  
tab2 = ttk.Frame(tab_control)  
tab_control.add(tab0, text = "инструкция")  
tab_control.add(tab1, text = "кликер")  
tab_control.add(tab2, text = "улучшения")
tab_control.pack(expand = 1, fill = "both")
ttk.Style().configure("TFrame", background = "lightblue")     

#текст на первой вкладке
lbl51 = Label(tab0, text = "Это игра - кликер. Вверху есть 3 вкладки про них читай ниже.",bg = "lightblue",font = ("Arial Bold", 15),height = 3)
lbl51.grid(column = 0, row = 0)
lbl52 = Label(tab0, text = "Первая вкладка - инструкция, здесь всё понятно",bg = "lightblue",font = ("Arial Bold", 15),height = 3)
lbl52.grid(column = 0, row = 1)
lbl53 = Label(tab0, text = "Вторая вкладка - кликер, есть 10 кнопок , из них  9 кликеров и 1 кнопка сбора про них ниже .",bg = "lightblue",font = ("Arial Bold", 15),height = 3)
lbl53.grid(column = 0, row = 2)
lbl54 = Label(tab0, text = "Кликеры - нажимай и прокачийвай их на следующей вкладке",bg = "lightblue",font = ("Arial Bold", 15),height = 3)
lbl54.grid(column = 0, row = 3)
lbl55 = Label(tab0, text = "Кнопка сбора - собирает прибыль со скольких-то рандомно выбранных кликеров ( вначале с 3) ",bg = "lightblue",font = ("Arial Bold", 15),height = 3)
lbl55.grid(column = 0, row = 4)
lbl56 = Label(tab0, text = "Третья вкладка - прокачка, есть 9 кнопок ,из них 7 прокачек зароботка в секунду , одна прокачивает ",bg = "lightblue",font = ("Arial Bold", 15),height = 3)
lbl56.grid(column = 0, row = 5)
lbl57 = Label(tab0, text = " кнопки , а ещё одна увеличивает количество рандомно выбранных кликеров для сбора кликеров",bg = "lightblue",font = ("Arial Bold", 15),height = 3)
lbl57.grid(column = 0, row = 6)
lbl58 = Label(tab0, text = "Заработок в секунду не собирается автоматически , для его сбора нужно нажать на кнопку сбора ",bg = "lightblue",font = ("Arial Bold", 15),height = 3)
lbl58.grid(column = 0, row = 7)
lbl58 = Label(tab0, text = "Так-же прокачка седьмой кнопки добавляет заработок в сек равный сумме добавления денег в каждую из кнопок ",bg = "lightblue",font = ("Arial Bold", 14),height = 3)
lbl58.grid(column = 0, row = 8)

#текст на второй вкладке
lbl = Label(tab1, text = "собранные деньги = " + str(amountofmoney) + "$",bg = "lightgreen")
lbl.place(x = 10, y = 30)
lbl1 = Label(tab1, text = "общая сумма денег = " + str(sum(cashinbtns) + amountofmoney) + "$",bg = "lightgreen")
lbl1.place(x = 10, y = 50)
lbl2 = Label(tab1, text = "сумма денег в кнопках = " + str(sum(cashinbtns)) + "$",bg = "lightgreen")
lbl2.place(x = 10, y = 70)
lbl6 = Label(tab1, text = "+ " + str(cashforsek) + "$ в секунду",bg = "lightgreen")
lbl6.place(x = 10, y = 90)
lbl11 = Label(tab1, text = str(cashinbtns[0]) + "$" + " + " + str(addcashinbtnnumber1) + "$",bg = "lightblue")
lbl11.place(x = 400, y = 370)
lbl12 = Label(tab1, text = str(cashinbtns[1]) + "$" + " + " + str(addcashinbtnnumber2) + "$",bg = "lightblue")
lbl12.place(x = 400, y = 470)
lbl13 = Label(tab1, text = str(cashinbtns[2]) + "$" + " + " + str(addcashinbtnnumber3) + "$",bg = "lightblue")
lbl13.place(x = 400, y = 570)
lbl14 = Label(tab1, text = str(cashinbtns[3]) + "$" + " + " + str(addcashinbtnnumber4) + "$",bg = "lightblue")
lbl14.place(x = 600, y = 370)
lbl15 = Label(tab1, text = str(cashinbtns[4]) + "$" + " + " + str(addcashinbtnnumber5) + "$",bg = "lightblue")
lbl15.place(x = 600, y = 470)
lbl16 = Label(tab1, text = str(cashinbtns[5]) + "$" + " + " + str(addcashinbtnnumber6) + "$",bg = "lightblue")
lbl16.place(x = 600, y = 570)
lbl17 = Label(tab1, text = str(cashinbtns[6]) + "$" + " + " + str(addcashinbtnnumber7) + "$",bg = "lightblue")
lbl17.place(x = 800, y = 370)
lbl18 = Label(tab1, text = str(cashinbtns[7]) + "$" + " + " + str(addcashinbtnnumber8) + "$",bg = "lightblue")
lbl18.place(x = 800, y = 470)
lbl19 = Label(tab1, text = str(cashinbtns[8]) + "$" + " + " + str(addcashinbtnnumber9) + "$",bg = "lightblue")
lbl19.place(x = 800, y = 570)

#текст на третей вкладке
lbl3 = Label(tab2, text = "собранные деньги = " + str(amountofmoney) + "$",bg = "lightgreen")
lbl3.place(x = 10, y = 30)
lbl4 = Label(tab2, text = "общая сумма денег = " + str(sum(cashinbtns) + amountofmoney) + "$",bg = "lightgreen")
lbl4.place(x = 10, y = 50)
lbl5 = Label(tab2, text = "сумма денег в кнопках = " + str(sum(cashinbtns)) + "$",bg = "lightgreen")
lbl5.place(x = 10, y = 70)
lbl21 = Label(tab2, text = str(min(price1,price2,price3,price4,price5,price6,price7,price8,price9)) + "$" + " - " + str(max(price1,price2,price3,price4,price5,price6,price7,price8,price9)) + "$",bg = "lightblue")
lbl21.place(x = 400, y = 370)
lbl22 = Label(tab2, text = str(price0) + "$",bg = "lightblue")
lbl22.place(x = 400, y = 470)
lbl23 = Label(tab2, text = str(pricebuy1) + "$",bg = "lightblue")
lbl23.place(x = 400, y = 570)
lbl24 = Label(tab2, text = str(pricebuy2) + "$",bg = "lightblue")
lbl24.place(x = 600, y = 370)
lbl25 = Label(tab2, text = str(pricebuy3) + "$",bg = "lightblue")
lbl25.place(x = 600, y = 470)
lbl26 = Label(tab2, text = str(pricebuy4) + "$",bg = "lightblue")
lbl26.place(x = 600, y = 570)
lbl27 = Label(tab2, text = str(pricebuy5) + "$",bg = "lightblue")
lbl27.place(x = 800, y = 370)
lbl28 = Label(tab2, text = str(pricebuy6) + "$",bg = "lightblue")
lbl28.place(x = 800, y = 470)
lbl29 = Label(tab2, text = str(pricebuy7) + "$",bg = "lightblue")
lbl29.place(x = 800, y = 570)

#кнопки на второй вкладке 
btn1 = Button(tab1, text = "клик",command = click1,width = 10,height = 4, bg = "pink", fg = "blue")  
btn1.place(x = 400, y = 300)
btn2 = Button(tab1, text = "клик",command = click2,width = 10,height = 4, bg = "pink", fg = "blue")  
btn2.place(x = 400, y = 400)
btn3 = Button(tab1, text = "клик",command = click3,width = 10,height = 4, bg = "pink", fg = "blue")  
btn3.place(x = 400, y = 500)
btn4 = Button(tab1, text = "клик",command = click4,width = 10,height = 4, bg = "pink", fg = "blue")  
btn4.place(x = 600, y = 300)
btn5 = Button(tab1, text = "клик",command = click5,width = 10,height = 4, bg = "pink", fg = "blue")  
btn5.place(x = 600, y = 400)
btn6 = Button(tab1, text = "клик",command = click6,width = 10,height = 4, bg = "pink", fg = "blue")  
btn6.place(x = 600, y = 500)
btn7 = Button(tab1, text = "клик",command = click7,width = 10,height = 4, bg = "pink", fg = "blue")  
btn7.place(x = 800, y = 300)
btn8 = Button(tab1, text = "клик",command = click8,width = 10,height = 4, bg = "pink", fg = "blue")  
btn8.place(x = 800, y = 400)
btn9 = Button(tab1, text = "клик",command = click9,width = 10,height = 4, bg = "pink", fg = "blue")  
btn9.place(x = 800, y = 500)
btn0 = Button(tab1, text = "собрать",command = click0,width = 10,height = 4, bg = "lightgreen", fg = "blue")  
btn0.place(x = 600, y = 100)

#кнопки на третей вкладке
btnup1 = Button(tab2, text = "улучшение",command = upgrade,width = 10,height = 4, bg = "pink", fg = "blue")  
btnup1.place(x = 400, y = 300)
btnup2 = Button(tab2, text = "+ 1 рабочий",command = upgrade0,width = 10,height = 4, bg = "pink", fg = "blue")  
btnup2.place(x = 400, y = 400)
btnup3 = Button(tab2, text = "+" + str(upgradecashforsek1) + "$" + " в сек",command = buy1,width = 10,height = 4, bg = "pink", fg = "blue")  
btnup3.place(x = 400, y = 500)
btnup4 = Button(tab2, text = "+" + str(upgradecashforsek2) + "$" + " в сек",command = buy2,width = 10,height = 4, bg = "pink", fg = "blue")  
btnup4.place(x = 600, y = 300)
btnup5 = Button(tab2, text = "+" + str(upgradecashforsek3) + "$" + " в сек",command = buy3,width = 10,height = 4, bg = "pink", fg = "blue")  
btnup5.place(x = 600, y = 400)
btnup6 = Button(tab2, text = "+" + str(upgradecashforsek4) + "$" + " в сек",command = buy4,width = 10,height = 4, bg = "pink", fg = "blue")  
btnup6.place(x = 600, y = 500)
btnup7 = Button(tab2, text = "+" + str(upgradecashforsek5) + "$" + " в сек",command = buy5,width = 10,height = 4, bg = "pink", fg = "blue")  
btnup7.place(x = 800, y = 300)
btnup8 = Button(tab2, text = "+" + str(upgradecashforsek6) + "$" + " в сек",command = buy6,width = 10,height = 4, bg = "pink", fg = "blue")  
btnup8.place(x = 800, y = 400)
btnup9 = Button(tab2, text = "+" + "???" + "$" + " в сек",command = buy7,width=10,height=4, bg="pink", fg="blue")  
btnup9.place(x = 800, y = 500)

window.mainloop() #функция "запуска" модуля ткинтер
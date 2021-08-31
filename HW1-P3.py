#Total Cost of Food For The Boys
foodForKaz = 35
foodForBen = 29
foodForConnor = 40
foodForJoe = 37
foodForNick = 34
foodForTheBoys = foodForBen + foodForConnor + foodForJoe + foodForKaz + foodForNick
print(foodForTheBoys)

#Total Tip for The Food
totalTip = foodForTheBoys * .15
print(totalTip)

#Total Overall Cost for The Food & Tip
totalCost = totalTip + foodForTheBoys
print(totalCost)

#Total Overall Cost Split Per Boy
billSplit = foodForTheBoys / 5
tipSplit = totalTip / 5
totalPerBoy = billSplit + tipSplit
print(totalPerBoy)
print(billSplit)
print(tipSplit)


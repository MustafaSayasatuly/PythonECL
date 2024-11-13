print("thank you for choosing python pizza deliveries!")
size=input("what size do you want?L or M  or S ")
add_pepperoni=input("do you want pepperoni?Y or N ")
extra_cheese=input("do you want extra cheese?Y or N ")

cost=0
if size=="L":
  cost+=25
  if add_pepperoni=="Y":
    cost+=3
  else:
    cost+=0
elif size=="M":
  cost+=20
  if add_pepperoni=="Y":
    cost+=3
  else:
    cost+=0
elif size=="S":
  cost+=15
  if add_pepperoni=="Y":
    cost+=2
  else:
    cost+=0
print(cost)

if extra_cheese=="Y":
  cost+=1
else:
  cost+=0
print(cost)  
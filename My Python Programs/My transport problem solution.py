

# Creates a dictionary for the number of units of supply for each supply node
demand = {"1": 260,
      "2": 290,
      "3": 150
}


# Creates a dictionary for the number of units of demand for each demand node
supply = {"1": 250,
      "2": 270,
      "3": 180,
}


# Creates a dictionary for the number of units of Cost for each Cost node
costs = {
     (1,1):4,    (1,2):10,    (1,3):6,
     (2,1):14,    (2,2):3,    (2,3):7,
     (3,1):10,    (3,2):6,    (3,3):2,
}

# This Function checks for Odd numbers
def odd_checker(n):
     ans = n % 2
     
     if ans == 1:
          return n
     else:
          return 0
     

# Temporary cost table 
costs1 = costs.copy()


# Table for allocation
AT = costs.copy()
for x in AT:
     AT[x] = 0


# Passes the function through the Cost dictionary    
m = map(odd_checker,costs.values())

# Stores the odd values in the table to a list odd
odd = []
for x in m:
     odd.append(x)

# Transfers only the odd numbers to a newlist 
odd_value = []    
for m in odd:
          if m > 0:
               odd_value.append(m)

# Checks for Minmum Odd number              
moc = min(odd_value)

# Checks for coordinates of the value of a dictionary
def key_checker(n, value):
     p = n.items()
     for i in p:
          if i[1] == value:
               key = i[0]
     return key

# Coordinate for the minimun odd number and other odd numbers is moc_cord and the list odd_coord for minimum odd cost
moc_cord = key_checker(costs,moc)
odd_cord = []
for n in odd_value:
     odd_cord.append(key_checker(costs,n))


for n in odd_cord:
     costs[n] = costs[n] - moc
     if costs[n] == 0:
          costs[n] = moc
          
# Performs the allocation
while costs != {}:
     mincost= min(costs.values())
     aldemand, alsupply = demand.copy(),supply.copy()
     mcc= key_checker( costs, mincost )
     #mcc2 = key_checker(costs, costs[mcc])
     AT[mcc] = min(demand[str(mcc[1])] , supply[str(mcc[0])])
     supply[str(mcc[0])] = supply[str(mcc[0])] - AT[mcc]
     demand[str(mcc[1])] = demand[str(mcc[1])] - AT[mcc]
     
     # Deletes the Row or Column that allocations have been completely made
     try :
          if supply[str(mcc[0])] == 0:
               for n in range(1,3):
                    del costs[(mcc[0],n)]
               del  supply[str(mcc[0])]

          if demand[str(mcc[1])] == 0:
                for n in range(1,4):
                    del costs[(n,mcc[1])]
                del demand[str(mcc[1])]
                
     except KeyError :
          break
     print(" "*30,"Allocation Table ","\n","="*30)
     for m in range(1,4):
          print (" "*10,costs1[(m,1)],"(",AT[(m,1)],")"," "*10,costs1[(m,2)],"(",AT[(m,2)],")","  "*10, costs1[(m,3)],"(",AT[(m,3)],")")
          print ("\n\n")
     
# Performs the last Allocation
if len(demand) > 1:
     k = mcc[0]
     try:
          m= mcc[1] - 1
     except KeyError:
          m = mcc[1]+1
     mcc = (k,m)
elif len(supply) > 1:
     m = mcc[1]
     try:
          k= mcc[0] - 1
     except KeyError:
          k = mcc[0]+1
     mcc = (k,m)
else:
     pass

AT[mcc] = min(demand[str(m)] , supply[str(k)])
supply[str(mcc[0])] = supply[str(mcc[0])] - AT[mcc]
demand[str(mcc[1])] = demand[str(mcc[1])] - AT[mcc]

# This is to Get the Optimal cost
OC = 0
for n in AT:
     OC = OC + costs1[n]*AT[n]

# Produces output of the Allocation Table
print(" "*30,"Allocation Table ","\n","="*30)
for m in range(1,4):
     print (" "*10,costs1[(m,1)],"(",AT[(m,1)],")"," "*10,costs1[(m,2)],"(",AT[(m,2)],")","  "*10, costs1[(m,3)],"(",AT[(m,3)],")")
     print ("\n\n")
     
print ("The Optimal Cost is : ",OC)


cost=[
      [50,7,30,20,30],
      [50,40,3,20,4],
      [5,40,30,2,54],
      [50,40,30,20,43]
]

supply = [10,20,30,40]

demand = [20,5,15,20,40]


assert sum(supply) == sum(demand)

cost1= cost[:]
cost2 = []
alloc = []
for x in cost:
     for k in x:
          cost2.append(k)
          alloc.append(0)

cost3 = cost2[:]

def odd_checker(n):
     ans= n % 2
     
     if ans == 1:
          return n
     else:
          return 0


     
m = map(odd_checker,cost2)
odd = []
for x in m:
     odd.append(x)

odd_value = []    
for m in odd:
          if m > 0:
               odd_value.append(m)
mincost = min(odd_value)

#####################################

def num_odd(n):
     k=0
     for m in n:
          if m > 0:
               k = k+1
     return k

#####################################

j= num_odd(odd)
i = odd_value

#####################################

coord=[]
for i,k in enumerate(odd):
     if odd_checker(k) == 0:
          pass
     else:
          coord.append(i)
     

for n in coord:
     cost2[n]= cost2[n] - mincost
     
#####################################
print ("Cost ::",cost1,"\n","Allocation Table: ", alloc,j,i, mincost,"  //  ",coord)
print(cost2)


##cost2 is the Allocation Table###
##stage 2##
minsup = min(supply)
mindem = min(demand)
minvalue = minsup, mindem
allocateddemsup = min(minvalue)
print(allocateddemsup)

allocate = min(cost2)
coo = cost2.index(allocate)
x=cost2.index(allocate)
print (x)

alloc[coo] = allocateddemsup
print(alloc)

dem = demand[:]
sup = supply[:]
if allocateddemsup in demand:
     demsup = 1
     coodem = demand.index(alloc[coo])
else:
     demsup = 0

print (demsup)

def check_coord():
     global coodem, cost2
     while x != len(cost2):
          x= 5 + x

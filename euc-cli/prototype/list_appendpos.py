L = "-----"
dataW = [200, 100, 50]
dataH = [20, 10, 5]
dataWHn = []

# check dataW & dataH
print L
print "dataW =",dataW
print "dataH =",dataH
print L

# append to dataWHn from dataW * dataH
for x in range(len(dataW)):
  W = dataW[x]
  H = dataH[x]
  dataWHn.append([W,H])

# check dataWH
print "dataWHn =",dataWHn

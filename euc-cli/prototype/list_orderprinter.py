one = [[10,100],[20,200],[30,300]]
two = []

for x,y in one:
  z = x * y
  two.append(z)
  print "x = %d and y = %d then x*y = %d" % (x,y,z)
print two

a = ['a1', 'a2', 'a3']
b = ['b1', 'b2', 'b3']
print "Multiplied Matrix:"
for x, y in [(x,y) for x in a for y in b]:
  print x, y

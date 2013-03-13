dataWHn = []
def askdata():
  NEA =  input("Number of electronic appliances : ")
  for n in range(1,NEA+1):
    def ask():
      global W,H
      askW = "EA%d | Power (Watt) = " % n
      askH = "    | Usage (Hour) = "
      W = input(askW)
      H = input(askH)
    ask()
    if H > 24:
      print "Usage must be <24 hours!"
      ask()
    else:
      dataWHn.append([W,H])
askdata()
print dataWHn

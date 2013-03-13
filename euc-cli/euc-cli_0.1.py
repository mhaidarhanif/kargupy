#============================
# Energy Usage Calculator
#   Program Code
#   Version: 0.1
#============================

SI = "========================================"
SII = "----------------------------------------"

print SI
print "Energy Usage Calculator"
print SII

name = raw_input("What's your name? ")
VA = input("How much your VA? ")
NEA =  input("Number of electronic appliances : ")
dataWHn = []
for n in range(1,NEA+1):
  def ask():
    global W,H
    askW = "EA %d\t| Power (Watt) = " % n
    askH = "\t| Usage (Hour) = "
    W = input(askW)
    H = input(askH)
  ask()
  if H > 24:
    print "Usage must be <24 hours!"
    ask()
  else:
    dataWHn.append([W,H])

print SII
print "Your name\t\t= %s" % name
print "Household power\t\t= %s VA" % VA
for n in range(1,NEA+1):
  print "Electronic Appliance %d\t= %d Wh" % (n,dataWH[n-1])
print SI

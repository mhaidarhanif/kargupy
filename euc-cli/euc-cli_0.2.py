#============================
# Energy Usage Calculator
#   Program Code
#   Version: 0.2
#============================

SI = "========================================"
SII = "----------------------------------------"

print SI
print "Energy Usage Calculator"
print SII

def askdata():
  global name, VA, NEA, dataWHn
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
def countWH(dataWHn):
  global dataWH
  dataWH = []
  for W,H in dataWHn:
    WH = W * H
    dataWH.append(WH)
def countDWH(dataWH):
  global DWH
  DWH = 0
  for WH in dataWH:
    DWH += WH
def countMWH(DWH):
  global MWH
  MWH = 0
  MWH = DWH * 30
def countMKWH(MWH):
  global MKWH
  MKWH = 0
  MKWH = MWH / float(1000)
def countMPKWH():
  global MPKWH, TAX
  if VA >= 6600: MPKWH = 1380
  elif VA < 6600: MPKWH = 600
  else: MPKWH = 0
  if VA >= 450 and VA <= 1300: TAX = 0.03
  elif VA > 1300 and VA <= 5500: TAX = 0.05
  elif VA > 5500: TAX = 0.06
  else: TAX = 0.06
def countMB(MKWH):
  global MB
  MB = 0
  MB = MKWH * MPKWH
  MB = MB + (MB*TAX)

askdata()
countWH(dataWHn)
countDWH(dataWH)
countMWH(DWH)
countMKWH(MWH)
countMPKWH()
countMB(MKWH)

print SII
print "Your name\t\t= %s" % name
print "Household power\t\t= %s VA" % VA
for n in range(1,NEA+1):
  print "Electronic Appliance %d\t= %d Wh" % (n,dataWH[n-1])
print "Daily   Watt Hour\t= %d Wh" % DWH
print "Monthly Watt Hour\t= %d Wh" % MWH
print "Monthly kWh\t\t= %s kWh" % str(MKWH)
print "Monthly Price/kWh\t= Rp %d" % MPKWH
print "Monthly Tax\t\t= %d %% = Rp %d" % ((TAX*100),(MB*TAX))
print "Monthly Bills\t\t= Rp %d" % MB
print SI

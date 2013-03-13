#============================
# Energy Usage Calculator
#   Program Code
#   Version: 0.4 | Functional
#============================

import os
SI = "========================================"
SII = "----------------------------------------"
def BUG(n):
  return "<DEBUG %d>" % n

def count(dataWHn):
  global dataWH, DWH, MWH, MKWH, MPKWH, TAX, MB1, MB2
  dataWH = []
  DWH = 0; MWH = 0; MKWH = 0; MPKWH = 0
  TAX = 0; MB1 = 0; MB2 = 0
  for W,H in dataWHn:
    WH = W * H
    dataWH.append(WH)
  for WH in dataWH:
    DWH += WH
  MWH = DWH * 30
  MKWH = MWH / float(1000)
  if VA >= 6600: MPKWH = 1380
  elif VA < 6600: MPKWH = 600
  else: MPKWH = 0
  if VA >= 450 and VA <= 1300: TAX = 0.03
  elif VA > 1300 and VA <= 5500: TAX = 0.05
  elif VA > 5500: TAX = 0.06
  else: TAX = 0.06
  MB1 = MKWH * MPKWH
  MB2 = MB1 + (MB1*TAX)

def report():
  print SII
  print "Your name\t\t= {}".format(name)
  print "Household power\t\t= {} VA".format(VA)
  for n in range(1,NEA+1):
    print "Electronic Appliance {}\t= {} Wh".format(n,dataWH[n-1])
  print "Daily   Watt Hour\t= {} Wh".format(DWH)
  print "Monthly Watt Hour\t= {} Wh".format(MWH)
  print "Monthly kWh\t\t= {} kWh".format(str(MKWH))
  print "Monthly Price/kWh\t= Rp {0}".format(MPKWH)
  print "Monthly Bills w/o Tax\t= Rp {0}".format(MB1)
  print "Monthly Tax\t\t= {0} % = Rp {1}".format((TAX*100),(MB1*TAX))
  print SII
  print "Monthly Bills\t\t= Rp {0}".format(MB2)
  print SI

def again():
  a = raw_input("Calculate again [Y/N]? ")
  if a == "Y" or a == "y":
    clear()
    run()
  elif a == "N" or a == "n":
    exit()
  else:
    print "Wrong choice. Please answer Y or N."
    again()

def clear():
  os.system(['clear','cls'][os.name == 'nt'])

def euc():
  global name, VA, NEA, dataWHn
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
      askW = "EA {}\t| Power (Watt) = ".format(n)
      askH = "\t| Usage (Hour) = "
      W = input(askW)
      H = input(askH)
    ask()
    if H > 24:
      print "Usage must be <24 hours!"
      ask()
    else:
      dataWHn.append([W,H])
  print BUG(1), "dataWHn =", dataWHn
  count(dataWHn)
  report()
  again()

def run():
  try:
    euc()
  except:
    print "Exited!"
    exit()
run()

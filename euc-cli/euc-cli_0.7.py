#============================
# Energy Usage Calculator
#   Program Code
#   Version: 0.7 | Functional
#============================

import os
title = "Energy Usage Calculator"
ver = 0.7
L1 = "=================================================="
L2 = "--------------------------------------------------"
def BUG(n):
  return "<DEBUG {}>".format(n)

def euc():
  global name, VA, KVA, NEA
  print L1
  print title, ver
  print L2
  name = raw_input("Name : ")
  VA = input("Household Power (VA) : ")
  KVA = VA / float(1000)
  def askNEA():
    global NEA, dataW, dataH
    NEA =  input("Number of electronic appliances : ")
    if NEA > 1000:
      print "[Impossible!]"
      askNEA()
    dataW = []; dataH = []
    print "[Input your data based on maximum/day]"
    for n in range(1,NEA+1):
      def askEA():
        global W,H
        ansW = "EA {}\t| Power (Watt) : ".format(n)
        ansH = "\t| Usage (Hour) : "
        # ask W
        W = input(ansW)
        if W > 100000 or W <= 0:
          print "[Impossible power!]"
          askEA()
        # ask H
        H = input(ansH)
        if H > 24 or H <= 0:
          print "[Impossible usage in a day!]"
          askEA()
        else:
          dataW.append(W)
          dataH.append(H)
      askEA()
  askNEA()
  countDaily(dataW,dataH)

def countDaily(dataW,dataH):
  global dataWHn, dataWH, HW, DWH, DKWH
  HW = 0; DWH = 0; DKWH = 0
  # append dataW & dataH to dataWHn
  dataWHn = []
  for x in range(len(dataW)):
    W = dataW[x]
    H = dataH[x]
    dataWHn.append([W,H])
  # count HW
  for W in dataW:
    HW += W
  # append W * H to dataWH
  dataWH = []
  for W,H in dataWHn:
    WH = W * H
    dataWH.append(WH)
  # check W <= VA
  if HW <= VA:  
    for WH in dataWH:
      DWH += WH
    DKWH = DWH / float(1000)
    countMonthly(DKWH)
  else:
    print "[Usage exceeded!]"
    reportFail()

def countMonthly(DKWH):
  global MKWH, BC, MPKWH, TAX, MB1, MB2
  MKWH = DKWH * 30
  if VA <= 450:
    BC = KVA * 5000
    MPKWH = 360
  elif VA <= 900:
    BC = KVA * 10000
    MPKWH = 360
  elif VA <= 1300:
    BC = KVA * 15000
    MPKWH = 360
  elif VA <= 2200:
    BC = KVA * 25000
    MPKWH = 405
  elif VA <= 3500:
    BC = KVA * 27000
    MPKWH = 420
  elif VA <= 6600 or VA <= 200000:
    BC = KVA * 30500
    MPKWH = 430
  else:
    BC = 0; MPKWH = 0
  if VA <= 1300: TAX = 0.03
  elif VA <= 5500: TAX = 0.05
  elif VA <= 200000: TAX = 0.06
  else: TAX = 0
  MB1 = (MKWH * MPKWH) + BC
  MT = MB1*TAX
  MB2 = MB1 + MT
  report()

def report():
  print L2
  print "Your Name\t\t= {}".format(name)
  print "Household Power\t\t= {} VA".format(VA)
  print L2
  print "[Result based on maximum estimation]"
  for n in range(1,NEA+1):
    print "Electronic Appliance {}\t= {} W * {} H = {} Wh".format(
    n,dataW[n-1],dataH[n-1],dataWH[n-1])
  print "Hourly  Watt\t\t= {} Wh".format(HW)
  print "Daily   Watt Hour\t= {} Wh".format(DWH)
  print "Daily   kWh\t\t= {} kWh".format(DKWH)
  print "Monthly kWh\t\t= {} kWh".format(MKWH)
  print "Burden  Cost/kW\t\t= Rp {}".format(BC)
  print "Monthly Price/kWh\t= Rp {}".format(MPKWH)
  print "Monthly Bills w/o Tax\t= Rp {}".format(MB1)
  print "Monthly Tax\t\t= {} % = Rp {}".format((TAX*100),(MB1*TAX))
  print L2
  print "Monthly Bills\t\t= Rp {}".format(MB2)
  print L1
  again()

def reportFail():
  print L2
  print "Name\t\t= {}".format(name)
  print "Household Power\t\t= {} VA".format(VA)
  print L2
  print "[Result based on maximum estimation]"
  for n in range(1,NEA+1):
    print "Electronic Appliance {}\t= {} W * {} H = {} Wh".format(
    n,dataW[n-1],dataH[n-1],dataWH[n-1])
  print "Hourly  Watt\t\t= {} W".format(HW)
  print """
  Your usage is over from maximum possible capability in an hour/day.
  You need to calculate again or disable some appliances.
  """
  print L1
  again()

def again():
  a = raw_input("Calculate again [Y/N]? ")
  if a == "Y" or a == "y":
    clear()
    run()
  elif a == "N" or a == "n":
    clear()
    exit()
  else:
    print "[Wrong choice. Please answer Y or N]"
    again()

def clear():
  os.system(['clear','cls'][os.name == 'nt'])

def run():
  try:
    euc()
  except:
    print "[Exited!]"
    clear()
    exit()
run()

# euc()

#============================
# Energy Usage Calculator
#   Program Code
#   Version: 0.6 | Functional
#============================

import os
title = "Energy Usage Calculator"
ver = 0.6
L1 = "=================================================="
L2 = "--------------------------------------------------"
def BUG(n):
  return "<DEBUG %d>" % n

def euc():
  global name, VA, NEA
  print L1
  print title, ver
  print L2
  name = raw_input("Name : ")
  VA = input("Household Power (VA) : ")
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
  global dataWHn, dataWH, DW, DWH, DKWH
  DW = 0; DWH = 0; DKWH = 0
  # append dataW & dataH to dataWHn
  dataWHn = []
  for x in range(len(dataW)):
    W = dataW[x]
    H = dataH[x]
    dataWHn.append([W,H])
  # count DW
  for W in dataW:
    DW += W
  # append W * H to dataWH
  dataWH = []
  for W,H in dataWHn:
    WH = W * H
    dataWH.append(WH)
  # check W <= VA
  if DW <= VA:  
    for WH in dataWH:
      DWH += WH
    DKWH = DWH / float(1000)
    countMonthly(DKWH)
  else:
    print "[Usage exceeded!]"
    reportFail()

def countMonthly(DKWH):
  global MKWH, MPKWH, TAX, MB1, MB2
  MKWH = DKWH * 30
  if VA >= 6600: MPKWH = 1380
  elif VA < 6600: MPKWH = 600
  else: MPKWH = 0
  if VA >= 450 and VA <= 1300: TAX = 0.03
  elif VA > 1300 and VA <= 5500: TAX = 0.05
  elif VA > 5500: TAX = 0.06
  else: TAX = 0
  MB1 = MKWH * MPKWH
  MB2 = MB1 + (MB1*TAX)
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
  print "Hourly  Watt\t\t= {} Wh".format(DW)
  print "Daily   Watt Hour\t= {} Wh".format(DWH)
  print "Daily   kWh\t\t= {} kWh".format(DKWH)
  print "Monthly kWh\t\t= {} kWh".format(MKWH)
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
  print "Hourly  Watt\t\t= {} W".format(DW)
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

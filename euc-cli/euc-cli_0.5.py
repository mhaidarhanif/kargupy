#============================
# Energy Usage Calculator
#   Program Code
#   Version: 0.5 | Functional
#============================

import os
L1 = "========================================"
L2 = "----------------------------------------"
def BUG(n):
  print "<DEBUG %d>" % n

def euc():
  global name, VA, NEA, dataWHn
  print L1
  print "Energy Usage Calculator"
  print L2
  name = raw_input("Name : ")
  VA = input("Household Power (VA) : ")
  KVA = VA / 1000
  def askNEA():
    global NEA, dataWHn
    NEA =  input("Number of electronic appliances : ")
    if NEA > 1000:
      print "[Impossible!]"
      askNEA()
    dataWHn = []
    print "[Input your data based on maximum/day]"
    for n in range(1,NEA+1):
      def askEA():
        global W,H
        ansW = "EA {}\t| Power (Watt) : ".format(n)
        ansH = "\t| Usage (Hour) : "
        W = input(ansW)
        if W > 100000:
          print "[Impossible power!]"
          askEA()
        H = input(ansH)
        if H > 24:
          print "[Impossible usage! Usage must be <24 hours]"
          askEA()
        dataWHn.append([W,H])
      askEA()
  askNEA()
  countDaily(dataWHn)

def countDaily(dataWHn):
  global dataWH, DWH, DKWH
  dataWH = []; DWH = 0
  for W,H in dataWHn:
    WH = W * H
    dataWH.append(WH)
  for WH in dataWH:
    DWH += WH
  DKWH = DWH / float(1000)
  if DWH > VA:
    print "[Usage exceeded!]"
    reportFail()
  else:
    countMonthly(DKWH)

def countMonthly(DKWH):
  global MKWH, MPKWH, TAX, MB1, MB2
  MKWH = DKWH * 30
  if VA >= 6600: MPKWH = 1380
  elif VA < 6600: MPKWH = 600
  else: MPKWH = 0
  if VA >= 450 and VA <= 1300: TAX = 0.03
  elif VA > 1300 and VA <= 5500: TAX = 0.05
  elif VA > 5500: TAX = 0.06
  else: TAX = 0.06
  MB1 = MKWH * MPKWH
  MB2 = MB1 + (MB1*TAX)
  report()

def report():
  print L2
  print "Your Name\t\t= {}".format(name)
  print "Household Power\t\t= {} VA".format(VA)
  for n in range(1,NEA+1):
    print "Electronic Appliance {}\t= {} Wh".format(n,dataWH[n-1])
  print L2
  print "[Data based on maximum estimation]"
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
  for n in range(1,NEA+1):
    print "Electronic Appliance {}\t= {} Wh".format(n,dataWH[n-1])
  print "Daily kWH > {}\t= {} kWh".format(VA,DKWH)
  print """
  Your usage is over from maximum possible capabilty in a day.
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

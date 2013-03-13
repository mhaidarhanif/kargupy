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
def countMB(MKWH):
  global MB
  MB = 0
  MB = MKWH * P

print "WHn  =",dataWHn
countWH(dataWHn)
print "WH   =",dataWH
countDWH(dataWH)
print "DWH  =",DWH
countMWH(DWH)
print "MWH  =",MWH
countMKWH(MWH)
print "MKWH =",MKWH
countMB(MKWH)
print "MB   = Rp",MB

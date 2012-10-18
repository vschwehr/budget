# cccalc.py
# Script Title: Revolving Debt Calculator
# Parameters:
# BALANCE_PURCHASE ANNUALINTEREST_PURCHASE BALANCE_CASH ANNUALINTEREST_CASH MONTHLY_PAYMENT
# Description:
# Calculates the approximate number of months to pay off revolving debt factoring in purchase and cash interest.

import sys

BALANCE_PURCHASE=float(sys.argv[1])
print "BALANCE_PURCHASE="+str(BALANCE_PURCHASE)
AI_PURCHASE=float(sys.argv[2])
print "AI_PURCHASE="+str(AI_PURCHASE)
MI_PURCHASE=float(sys.argv[2])/12
print "MI_PURCHASE="+str(MI_PURCHASE)
BALANCE_CASH=float(sys.argv[3])
print "BALANCE_CASH="+str(BALANCE_CASH)
AI_CASH=float(sys.argv[4])
print "AI_CASH="+str(AI_CASH)
MI_CASH=float(sys.argv[4])/12
print "MI_CASH="+str(MI_CASH)
MONTHLY_PAYMENT=float(sys.argv[5])
print "MONTHLY_PAYMENT="+str(MONTHLY_PAYMENT)

print

i=1
while BALANCE_PURCHASE >= 0:
  BALANCE_CASH-=MONTHLY_PAYMENT
  print "BALANCE_CASH="+str(BALANCE_CASH)
  if BALANCE_CASH > 0:
    BALANCE_PURCHASE_BI=(BALANCE_PURCHASE-MONTHLY_PAYMENT)
    print "BALANCE_PURCHASE_BI="+str(BALANCE_PURCHASE_BI)
    BALANCE_PURCHASE=BALANCE_PURCHASE_BI+(BALANCE_PURCHASE_BI*MI_PURCHASE)+(BALANCE_CASH*MI_CASH)
  else:
    BALANCE_PURCHASE=(BALANCE_PURCHASE-MONTHLY_PAYMENT)+(BALANCE_PURCHASE*MI_PURCHASE)

  i+=1

  print "BALANCE_PURCHASE="+str(BALANCE_PURCHASE)
  print "MONTH_NUMBER="+str(i)
  print "--"

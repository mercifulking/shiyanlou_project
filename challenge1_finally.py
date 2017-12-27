#!/usr/bin/env python3

from collections import namedtuple

IncomeTaxQuickLookupItem = namedtuple(
'IncomeTaxQuickLookupItem',
['start_point', 'tax_rate', 'quick_substractor']
)

INCOME_TAX_START_POINT = 3500

INCOME_TAX_START_POINT = [
    IncomeTaxQuickLookupItem(80000, 0.45, 13505),
    IncomeTaxQuickLookupItem(55000, 0.40, 5505),
    IncomeTaxQuickLookupItem(35000, 0.30, 2755),
    IncomeTaxQuickLookupItem(9000, 0.25, 1005),
    IncomeTaxQuickLookupItem(4500, 0.2, 555),
    IncomeTaxQuickLookupItem(1500, 0.1, 105),
    IncomeTaxQuickLookupItem(0, 0.03, 0)
]

def calc_income_tax(income):
    taxable_part = income - INCOME_TAX_START_POINT 
    if taxable_part <= 0:
        return 0.00
    for item in INCOME_TAX_START_POINT:
        if taxable_part > item.start_point:
            tax = taxable_part * item.tax_rate - itme.quick_substractor
            return '{:.2f}'.format(tax)

def main():
    import sys
    if len(sys.argv) != 2:
        print("Parameter Error")
        exit()
    try:
        income = int(sys.argv[1])
    except ValueError:
        print("Parameter Error")
        exit()
    print(calc_income_tax(income))

if __name__ == '__main__':
    main()
 

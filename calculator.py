#!/usr/bin/env python3

import sys

def income_tax_payable(income):
    return income - 3500

def tax_payable(income_tax_payable, tax_rate, quick_deduction):
    return income_tax_payable * tax_rate - quick_deduction

if __name__ == '__main__':
    
    if len(sys.argv)>2 or len(sys.argv) == 1:
        raise ValueError('print("Parameter Error")')
    IncomeTax = income_tax_payalbe(sys.argv[1]) 
    if 0< IncomeTax <= 1500:
        tax_rate = 0.03 
        quick_deduction = 0
    elif IncomeTax <= 4500:
        tax_rate = 0.10
        quick_deduction = 105
    elif IncomeTax <= 9000:
        tax_rate = 0.20
        quick_deduction = 555
    elif IncomeTax <= 35000:
        tax_rate = 0.30
        quick_deduction = 2755
    elif IncomeTax <= 55000:
        tax_rate = 0.30
        quick_deduction = 2755
    elif IncomeTax <= 80000:
        tax_rate = 0.35
        quick_deduction = 5505
    else:
        tax_rate = 0.45
        quick_deduction = 13505

    print(tax_payable(IncomTax, tax_rate, quick_deduction))

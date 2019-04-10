#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 09:14:34 2019

@author: danilo
"""
def factorial(natural):
    fac=1
    if(natural==0):
        return 1
    else:
        for i in range(1,natural+1):
            fac=fac*i
        return fac
def main():
    n=eval(input("Put in n: "))
    natural=0
    for i in range (1,n+1):
        fac1=factorial(i)
        a=(1/fac1)
        c=n**i
        t=a*c
        natural = natural+t
    natural=natural+n
    print (natural)
    
    
main()
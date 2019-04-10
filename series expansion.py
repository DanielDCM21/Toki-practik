#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 07:27:28 2019

@author: danilo
"""
import math
def main():
    n=eval(input("Put in n: "))
    x=eval(input("Put in x: "))
    sum=n
    signo=-1
    for i in range(1,x+1):
        index=2*i+1
        t=signo*((1/index)*(n)**index)
        sum=sum+t
        signo=signo*-1
    print (sum)      

main()
        
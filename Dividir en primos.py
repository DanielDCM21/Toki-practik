#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 08:03:42 2019

@author: danilo
"""

def prime(x):
    if(x%2==0):
        print (2)
        return (x/2)
    else:
        for i in range (2,x+1):
            for j in range (2,i+1):
                if(x%j==0):
                    break;
                else:
                    if(j==i-1):
                        print (i+1)
                        return x/i
def main():
    x=eval(input("Put in a number"))
    while(x!=1):
        x=prime(x);
    
main()    
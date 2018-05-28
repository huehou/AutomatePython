#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 13:25:44 2018

@author: alexander
"""

def collatz(number):
    if number % 2 == 0:
        print(number//2)
        return number // 2
    else:
        print(3*number + 1)
        return 3*number + 1

print("Enter number: ")

while True:
    try:
        number = int(input())
        if number <= 0:
            print("You must enter a positive integer")
            continue
        break
    except ValueError:
        print("You must enter an integer")

while number != 1:
    number = collatz(number)
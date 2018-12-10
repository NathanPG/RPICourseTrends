#!@Author: NathanPG
# -*- coding:utf-8 -*-
#Easy understanding version of timer
import time 
def task():
  print("Timer TEST")

def timer(n):
  #Infinite, Ctrl+C to stop
  while True:  
    print time.strftime('%Y-%m-%d %X',time.localtime())  
    task()
    time.sleep(n)

if __name__ == '__main__': 
  timer(1)

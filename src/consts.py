from dataclasses import dataclass
import math

#Consts
#PI
PI = math.pi
#Effective Length
K = 0.7
#Constant Length
L = 0.5 #m
#Constant Load 
P = 20*9.81 #kg 
#Safety Factor
n = 2

#Limits
LIM = (0.0001, 0.03) #30 mm x 30 mm cross section envelope MAX
V_LIM = (0.0001, 0.0015)
LAMBDA = 20000 #Penalty weight factor, must be >> than the score since failure of column is unacceptable
import numpy as np
import math

extraNumber = 4 * math.pi * pow(10,-7)

def solenoidRadius():
    Q0 = input("Input the value of Q0 (mC): ")
    tau = input("Input the tau (ignore the 10^-3): ")
    time = input("Input the time (ms): ")
    Q0 = float(Q0)
    tau = float(tau)
    time = float(time)

    Q0 = Q0/1000
    tau = tau * pow(10,-3)
    time = time/1000
    exponentialval = -time/tau
    x = math.exp(exponentialval)
    displCurrent = (Q0/tau)*x
    print(displCurrent)

solenoidRadius()

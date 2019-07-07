import hashlib
import os
import time
import random
import subprocess as sub
import csv
import math
import numpy
from shutil import copy2

def neural_net(muscles,delta_distance,g1):
    w1=float(g1[0])/100
    w2=float(g1[1])/100
    w3=float(g1[2])/100
    w4=float(g1[3])/100
    w5=float(g1[4])/100
    w6=float(g1[5])/100
    w7=float(g1[6])/100
    w8=float(g1[7])/100
    w9=float(g1[8])/100
    w10=float(g1[9])/100
    w11=float(g1[10])/100
    w12=float(g1[11])/100
    w13=float(g1[12])/100
    w14=float(g1[13])/100
    w15=float(g1[14])/100
    w16=float(g1[15])/10
    

    #input layer

    node1=muscles/1000

    node2=delta_distance

    if delta_distance>1:
       node3=1
    else:
       node3=0

    #hidden layer
    node4=w3*node1+w7*node2+node3*w10
    node4=numpy.tanh(node4)

    node5=w5*node1+w8*node2+node3*w11
    node5=numpy.tanh(node5)


    node6=w6*node1+w9*node2+w12*node3
    node6=numpy.tanh(node6)
 

    #last layer
    node7=w13*node4+w14*node5+w15*node6
    node7=numpy.tanh(node7)


    #output layer
    change=5*node7*w16



    return change

import hashlib
import os
import time
import random
import subprocess as sub
import csv
import math
import numpy
from shutil import copy2
from neural_net import neural_net
import numpy as np

def update_k(population,new_dist,old_distance,morphology):

    #seperate out the genome
       threshold_a=population[9]
       w1a=population[0]
       w2a=population[1]
       w3a=population[2]
       w4a=population[3]
       w5a=population[4]
       w6a=population[5]
       w7a=population[6]
       w8a=population[7]
       w9a=population[8]
       #calculate gradient of the landscape - this will be used to calculate how much we should change our stiffness
       delta_d=1/(new_dist-old_distance+2)
       delta_distance=abs(delta_d) 

       for x in range(7):
              new_morphology=[]
              line=morphology[x]
              for y in range(49):
   
	       if line[y]>0:

		       pressure=float(np.random.randint(-10,10))

		       node1=numpy.tanh(delta_d*w1a+w4a*pressure)
		       node2=numpy.tanh(delta_d*w2a+w5a*pressure)
		       node3=numpy.tanh(delta_d*w3a+w6a*pressure)

		       node4=numpy.tanh(node1*w7a+node2*w8a+node3*w9a)
		       new_value=(node4)*(10**(abs(10*node4)))
		       if new_value<threshold_a:
			  line[y]=0
              new_morphology.append(line[y])



       morphology=new_morphology
       return morphology
        

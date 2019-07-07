import hashlib
import os
import time
import random
import subprocess as sub
import numpy as np
from test_population import test_population
from sort_population import sort_population
from new_population import new_population




if __name__ == "__main__":
    
    #how big is our population?
    pop_size=10
    
    population=[]
    for i in range(pop_size):
            my_genome=[]
            for i in range(20):
        	my_num=float(np.random.randint(-10,10))
                my_num=my_num/10
        	my_genome.append(my_num)

            population.append(my_genome)    

    print(population)
    with open("population","a") as my_file:
        for i in range(pop_size):
            new_dist=str(population[i]) 
            my_file.write(new_dist +",\n")
        my_file.close()

    for time in range(50):

        new_distance=test_population(population)

        cpop=[]

        fitness=new_distance

        
        cpop=sort_population(population,fitness,pop_size,cpop)
        population=[]
        population=new_population(population,fitness,pop_size,cpop)
        print(population)

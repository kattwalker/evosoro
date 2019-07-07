import hashlib
import os
import os.path
import time
import random
import subprocess as sub
from file_write import write_voxelyze_file
from file_write import read_voxelyze_file
from update_k import update_k
import numpy as np



def test_population(population):
   pop_size=10
   t=0
   print("i am here")
   fitness=np.zeros((pop_size)) 
   possible_stiffness=[1000,5000,10000,50000,100000,500000,1000000,5000000,10000000,50000000,100000000,500000000]
   possible_tail=[4,8,12,16]
   new_distance=[]
   can_i_proceed=0
   stiffness_muscle=[]
   stiffness_tail_1=[]
   stiffness_tail_2=[]
   stiffness_tail_3=[]
   stiffness_tail_4=[]
   tail=[]   
   my_file_collective=[]
   old_distance=[]
   morphology_population=[]
   	       

   for i in range(pop_size):
      morphology=[]
      old_distance.append(0)
      for x in range(7): 
       l1=[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
       morphology.append(l1)
      morphology_population.append(morphology) 
      
   


   print(morphology_population)


   for episode in range(15):
                   after_episode=[]
                   new_distance=[]
                   sm_change=[]
                   st_change=[]
                   t_change=[]
		   print("new episode")
                   print(episode)
		   for t in range(pop_size):
                        print("writing new population test file")
		        write_voxelyze_file(t,morphology_population[t])
			ta=str(t)		            
		   	my_file=sub.Popen("./voxelyze  -f  katt"+ta+".vxa", shell=True)
                        time.sleep(10)
			sub.Popen.kill(my_file)
		   
		   print("killed all files")
                   time.sleep(50)
		   print("starting to read!")
                   

		   for t in range(pop_size):
                           
			   ta=str(t)
			   new_dist=[]
			   can_i_proceed=0
			   count=0
			   while can_i_proceed==0:
				 if os.path.exists("my_fitness"+ta+".xml"):
				    can_i_proceed=1
				    new_dist=read_voxelyze_file(ta)
				    new_distance.append(new_dist)
		                    os.remove("my_fitness"+ta+".xml")
		                    os.remove("katt"+ta+".vxa")
				 else:
				    time.sleep(1)
				    count=count+1
				    if count>1:
				       new_dist=0
				       can_i_proceed=1
			   	       new_distance.append(new_dist)
		           if os.path.exists("my_fitness"+ta+".xml"):
		              os.remove("my_fitness"+ta+".xml")
                           print(population[t])
                           print(new_dist)
                           print(old_distance[t])
                           print(morphology_population[t])  
		           results=update_k(population[t],new_dist,old_distance[t],morphology_population[t])
                           print(results)
                           morphology_population.append(results)
		           new_dist=abs(new_dist)
		           stiffness_muscle[t]=results[0]
		           stiffness_tail_1[t]=results[1]

                                                 
		   old_distance=new_distance
                   after_episode.append(new_distance)
                   

                   with open("results","a") as my_file:
        		for i in range(pop_size):
            			new_dist=str(old_distance[i]) 
            			my_file.write(new_dist +",\n")
        	        my_file.close()
                  


   for i in range(pop_size):
                      fitness[i]=(new_distance[i]+new_distance[i+10]+new_distance[i+20]+new_distance[i+30]+new_distance[i+40]+new_distance[i+50]+new_distance[i+60]+new_distance[i+70])/8
          
   

   return fitness
  

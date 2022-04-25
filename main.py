#################################################
#
#This program provides a solution to the knapsack problem
#I love robbing people!
#
#################################################

#Hard coded value and weight arrays
import util, random
vals = [300,1500,100,1000,3425,50,850,550,15,2000]
weights = [15,20,8,25,12,15,12,9,18,14]
population_size = 10
num_objects = 10
#Initiate population of critters
critters = util.initPop(population_size, num_objects)
print(critters)
childcritters = util.mutate(critters)
print(childcritters)
#TODO APPLY MUTATION OPERATION



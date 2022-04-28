#################################################
#
#This program provides a solution to the knapsack problem
#using an Evolutionary Programming approach
#I love robbing people!
#
#Marshall Robinson
#Maddy "Marshall" Cherrier
#Marshall Pratt
#4-28-2022
#################################################

#Hard coded value and weight arrays
import util, random, numpy
NUM_GENERATIONS = 50
best_generation = 0

vals = [300,1500,100,1000,3425,50,850,550,15,2000]
weights = [15,20,8,25,12,15,12,9,18,14]
population_size = 10
num_objects = 10

#Initiate population of critters
critters = util.initPop(population_size, num_objects)

#main loop
best_gen_value = 0
for i in range(NUM_GENERATIONS):
    #get children, mutate and append
    child_critters = util.mutate(critters)
    critters = critters + child_critters

    #get best children and their values
    critters = util.getBest(critters, vals, weights)
    values = util.getVals(critters, vals, weights)

    #get best value from the set, and use it to find the best critter in the set
    best_val = numpy.amax(values)
    bv_index = values.index(best_val)
    best_critter = critters[bv_index]

    #store the best generation
    if best_val > best_gen_value:
        best_gen_value = best_val
        best_generation = i+1

    print("Generation: ", i+1)
    print("Best critter: ", best_critter)
    print("Value:   ", best_val)
    print("")


print("Best Overall Generation: ", best_generation)

#TODO APPLY MUTATION OPERATION


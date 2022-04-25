#Util functions and mutations here please
import random
import numpy
import copy

#Create an array of arrays containing binary data
def initPop(population_size, num_objects):
    returnList = []
    for i in range(population_size):
        critterList = []
        for i in range(num_objects):
            critterList.append(random.randint(0,1))
        returnList.append(critterList)
    return returnList

#Return array for all final values of critters knapsacks
def getVals(critter, vals, weights):
    valArray = []
    for j in range(len(critter)):
        value = 0
        weight = 0
        for i in range(len(critter[j])):
            if critter[j][i] == 1:
                if weight + weights[i] <=50:
                    value = vals[i] + value
                    weight = weights[i] + weight
        valArray.append(value)
    return valArray

#returns array of 10 best critters THIS WONT WORK WITH ARRAYS OF 10 CRITTERS IT MUST BE ABOVE 10
def getBest(critters,vals,weights):
    array = numpy.array(getVals(critters,vals,weights))
    index = numpy.argpartition(array,10)[-10:]
    retArray = []
    for i in range(len(index)):
        retArray.append(critters[index[i]])
    return retArray


#recieve a list of critters, copies, mutates, and returns only the mutated offspring 
def mutate(critters):
    childcritters = copy.deepcopy(critters)
    for critter in childcritters:
        #first perform insert mutation on all childcritters
        index = random.randint(0, len(critter)-1)
        if critter[index] == 0:
            critter[index] = 1
        else:
            critter[index] = 0
        #next, decide if this critter is going to receive an inversion mutation
        coin_flip = random.randint(0,1)
        #enter the inversion mutatation
        if coin_flip == 1:
            critter = swap_mutation(critter)

    return childcritters

def swap_mutation(critter):
    index1 = random.randint(0, len(critter)-1)
    index2 = random.randint(0, len(critter)-1)
    if index1 > index2: #ensure that index1 is the lower
        temp = index1
        index1 = index2
        index2 = temp
    sublist = critter[index1:index2+1]
    for i in range(len(sublist)):
        critter[index2-i] = sublist[i]
    return critter
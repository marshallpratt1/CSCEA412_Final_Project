#Util functions and mutations here please
import random
import numpy

#Create an array of 10 arrays containing binary data
def initPop():
    returnList = []
    for i in range(20):
        critterList = []
        for i in range(10):
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



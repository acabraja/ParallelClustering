# -*- coding: utf-8 -*-

#import fitness
import random
class Genome:
    def __init__(self):
        self.genome = dict()

    def __str__(self):
        return self.genome

    def mutation(self):
        numClas = len(self.genome)
        for i in range(10):
            r = random.sample(range(0,numClas),2)
            pom = self.genome[r[0]][1]
            self.genome[r[0]][1] = self.genome[r[1]][1]
            self.genome[r[1]][1] = pom

    #If the number of Clusters = [a] (a in N), then we have fixed number
    #clusters.
    #If the number of clusters = [a,b] (a,b in N), then we have clusters
    #in range[a,b]
    def generateGenome(self, numberClusters, dataNum):
        l = [i for i in range(dataNum)]
        random.shuffle(l)

        if len(numberClusters) == 1:
            numClusters = numberClusters[0]
        elif len(numberClusters) == 2:
            numClusters = random.randint(numberClusters[0],numberClusters[1])
        else:
            print "Error numerClusters ([a] or [a,b])"
            numberClusters = list(input("numberClusters: "))

        randList =sorted( random.sample(range(dataNum-1),numClusters-1))
        randList.append(dataNum)
        befor = 0
        k = 0
        for i in randList:
            self.genome[k] = l[befor:i]
            befor = i
            k+=1

class Population:
    def __init__(self):
        self.population = []
        self.best = []

    def fit(self):
        pass

class Algorithm:
    def __init__(self):
        pass


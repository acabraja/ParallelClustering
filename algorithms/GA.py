# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 13:42:09 2014

@author: anto
"""
#import fitness
import random
class Genome:
    def __init__(self):
        self.genome = dict()
        
    def __str__(self):
        return self.genome
    
    def mutation(self):
        numKlas = len(self.genome)
        r = random.sample(range(0,numKlas),2)
        ## mutation 
    
    def generateGenome(self,numKlasters, dataNum):
        l = [i for i in range(dataNum)]
        random.shuffle(l)        
        randList =sorted( random.sample(range(dataNum-1),numKlasters-1))
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
    

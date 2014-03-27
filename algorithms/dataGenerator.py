# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 11:40:31 2014

@author: Anto Čabraja

@description: Generate data about bank clients(personal details i.e how old..
                financies, .....) 
"""

class DataGenerator:
    def __init__(self):
        self.typ  = ""
        self.name = ""
        self.dataNum = 0
    
    def __str__(self):
        return self.typ + " " + self.name 
    
    def SetOutputFileName(self,name):
        self.name = name
    
    def SetDataType(self,dataType):
        self.typ = dataType
    
    def SetDataNum(self,num):
        self.dataNum = num
    
    def Generate(self, fileName):
        while self.dataNum <= 0:
            self.dataNum = int(input("Set number of data, default is 0:"))
        if self.typ == "big":
            self.GenerateBigData(fileName)
        elif self.typ == "medium":
            self.GenerateMedData(fileName)
        elif self.typ == "small":
            self.GenerateSmallData(fileName)
        else:
            print "Wrong type! Please insert Type again"
    
    def GenerateBigData(self,name):
        """ 10 dimensional space:
         
        """
        
        for i in range(self.dataNum):
            pass
    
    def GenerateMedData(self,name):
        """ 5 dimensional space:
         
        """
        
        for i in range(self.dataNum):
            pass
    
    def GenerateSmallgData(self,name):
        """ 2 dimensional space:
         
        """
        
        for i in range(self.dataNum):
            pass
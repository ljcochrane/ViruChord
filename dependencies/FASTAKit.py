
"""
FASTA KIT

A Relatively basic library for working with FASTA files
in Python. 

Written primarily to support my Viru Chord Project, but
may have other uses.

Written by Louis Cochrane: All Rights Reserved

"""

import time


def newLine():
    
    """
    Helper function to more quickly print new lines.
    
    """
    print("\n")


class Seq:
    
    
    def __init__(self,FASTAFileName):
        
        """
        Loads and parses a FASTA File into a Dictionary 
        and a list 
        
        """
        
        rawFile = open(FASTAFileName,"r")
        
        self.sequenceDict  = {}
        self.sequenceList = []
        
        # Basically just to extract the information from the file. 
        
        #Initial variables
        # Current Title = Current descriptor I.E "Sequence 1.1.1")
        currentTitle = None
        # Current sequence is the current sequence duh. I.E ("AGTGTC")
        currentSequence = "" 
        # Start the counter at -1 to avoid appending the very first title and no sequence. 
        counter = -1 
        
        
        for line in rawFile:
            
            # Strip away newline characters.
            line = line.strip()
            
            if line == "":
                return            
            
            if line[0] == ">":
                # Sequence titles are denoted by > in FASTA. 
                # If the counter == -1 its the first time, so no appending. 
                if counter == -1:
                    currentTitle = line
                    currentTitle = currentTitle[1:]
                    counter +=1 
                    
                # Else append what you had so far, and reset the variables based on the new title.     
                else:
                    self.sequenceDict[counter] = [currentTitle,currentSequence]
                    self.sequenceList.append(currentSequence)
                    currentTitle = line
                    currentTitle = currentTitle[1:]
                    currentSequence = ""
                    counter +=1 
            
            # Else just keep building the sequence string.     
            else:
                currentSequence = currentSequence + line
                
                
        self.sequenceDict[counter] = [currentTitle,currentSequence]
        self.sequenceList.append(currentSequence)        
            
        rawFile.close()
   

    def seqList(self):
        """ 
        Returns a list containing the raw sequence data.
        
        """
        
        return self.sequenceList
    
    
    def seqDict(self):
        
        """
        Returns A dictionary containing sequence data in the following format. 
        Key: 0,1,2,3... 
        Value: {TITLE,SEQUENCE DATA}
        
        """
        return self.sequenceDict


    def __repr__(self):
        
        """"
        Basic __repr__ method. 
        Just prints the sequences and titles.
        
        """
        
        counter = 0
        
        print("\n")
        
        buildString  = ""
        
        while counter < len(self.sequenceDict.keys()):
            
            
            buildString = buildString + (self.sequenceDict[counter][0])
            buildString = buildString + "\n"
            buildString = buildString + (self.sequenceDict[counter][1])
            buildString = buildString + "\n"
            counter +=1 
            
            
        return buildString
    
    
    def getSequence(self,index):
        
        """ 
        Returns a specific sequence from the dictionary.
        Based on index.
        
        """
        
        return self.sequenceList[index]
    
    
    def getTitleList(self):
        
        """
        Specific function that returns a list of dates for a 
        the file. 
        File must be formatted with titles as 
        YYYY/MM/DD for this method to work.
        
        """
        
        sequenceDict = self.sequenceDict
        
        titleList = []
        
        for key in range(len(self.sequenceDict)):
            
            titleList.append(sequenceDict[key][0][:10])
        
        return titleList        
    
    
    def convertToRY(self):
        
        
        
        """" 
        Converts the alphabet of the current object from a 4 lettter alphabet
        ACGT 
        Into a two letter (purine pyrmidine) alphabet
        RY
        
        """
       
        inputList = self.sequenceList[:]
        inputDict = self.sequenceDict.copy()
        
        outputList = []
        outputDict = {}
        
        
        # Let's process the list first.
        #-----------------------------------------------------------------
        
        for sequence in inputList:
            
            buildString = ""
            
            for nucleotide in sequence:
                
                nucleotide = nucleotide.upper()
                
                if nucleotide == "G" or nucleotide == "A":
                
                    buildString =  buildString + ("R")
                
                elif nucleotide == "C" or nucleotide == "T":
                    
                    buildString = buildString + ("Y")
                    
                elif nucleotide == "-":
                    
                    buildString = buildString + ("-")      
                
                elif nucleotide == "N":
                    
                    buildString = buildString + ("N")                 
                    
                elif nucleotide == "R":
                    
                    buildString = buildString + ("R")
                    
                elif nucleotide == "Y":
                    
                    buildString = buildString + ("Y")                
                    
                    #return
                    
                else: 
                    print("ERROR: Invalid nucleotide in sequence.",nucleotide)
                    time.sleep(1)
                    return
                    
            outputList.append(buildString)
            
        
        self.sequenceList = outputList
        
        
        # Now for the dictionary. 
        #-----------------------------------------------------------------------
        
        for sequence in inputDict.keys():
            
            buildString = ""
            
            for nucleotide in inputDict[sequence][1]:
                
                nucleotide = nucleotide.upper()
                
                if nucleotide == "G" or nucleotide == "A":
                
                    buildString =  buildString + ("R")
                
                elif nucleotide == "C" or nucleotide == "T":
                    
                    buildString = buildString + ("Y")
                    
                elif nucleotide == "-":
                    
                    buildString = buildString + ("-")  
                    
                elif nucleotide == "N":
                    
                    buildString = buildString + ("N") 
                    
                elif nucleotide == "R":
                    
                    buildString = buildString + ("R")
                    
                elif nucleotide == "Y":
                    
                    buildString = buildString + ("Y")                
                    
                else: 
                    newLine()
                    print("ERROR: Invalid nucleotide in sequence.",nucleotide)
                    return
                    
            outputDict[sequence] = [inputDict[sequence][0],(buildString)]
            
        self.sequenceDict = outputDict
    
       
    def cleanFile(self):
        
        # First we'll start by removing all of the gaps.  
    
        index = 0 
        variableIndexList = []

        for key in self.sequenceDict.keys():
            
            while index < len(self.sequenceDict[0][1]):
            
                checkNucleotide = self.sequenceDict[0][1][index]
                print("Current check nucleotide:",checkNucleotide)
                found = False
                
                for key in self.sequenceDict.keys():
                    
            
                    try:
                        if checkNucleotide != self.sequenceDict[key][1][index]:
                            
                            if (checkNucleotide != "-") and (checkNucleotide != " ") and (self.sequenceDict[key][1][index] != "-") and (self.sequenceDict[key][1][index] != " "):
                            
                                found = True
                                print("Found in this sequence", key)
                            
                    except:
                        pass
                        #print(self.sequenceDict[key][1][index])
                        

                if found:
                    
                    variableIndexList.append(index)
  
                index += 1 
                
        print(variableIndexList)
        print("Number of variable sites", len(variableIndexList))
import numpy as np
import tkinter as tk 
import tkSimpleDialog as simpledialog
from Tkinter import *

def generate(inputFileName,outputFileName):
    #read input
    inputArr = []

    inputFile = open(inputFileName, "r")
    for val in inputFile.read().split():
        inputArr.append(float(val))
    inputFile.close()
    inputArr = np.array(inputArr)



    #generate Output

    numberOfProcesses=int(inputArr[0])

    MArrivalTime=inputArr[1]
    SArrivalTime=inputArr[2]

    MBurstTime=inputArr[3]
    SBurstTime=inputArr[4]

    LPriority=inputArr[5]


    arrivalDist = np.random.normal(MArrivalTime, SArrivalTime, numberOfProcesses)
    burstDist = np.random.normal(MBurstTime, SBurstTime, numberOfProcesses)

    priorityDist=np.random.poisson(LPriority,numberOfProcesses)

    #write Output
    outputFile = open(outputFileName, "w")
    outputFile.write(str(numberOfProcesses)+'\n')
    for i in range(numberOfProcesses):
        outputFile.write(
            str(i+1)+' '+
            str(arrivalDist[i])+' '+
            str(burstDist[i])+' '+
            str(priorityDist[i])+'\n')

    outputFile.close()

inputFileName=None
outputFileName=None
window = tk.Tk()
window.withdraw()
inputFileName = simpledialog.askstring(title="input file",prompt="Enter the input file name") 
window.destroy()
window = tk.Tk()
window.withdraw()
outputFileName = simpledialog.askstring(title="output file",prompt="Enter the output file name") 
window.destroy()

generate(inputFileName,outputFileName)



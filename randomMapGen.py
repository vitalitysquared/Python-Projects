# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 16:18:31 2020

@author: Eldon

"""

#imports
import random as rd
from PIL import Image, ImageDraw

#global vars
biomeFactor = 0
tiles = 0

#generates semi random maps using a random firt row and then basing tiles on surroundings
def semiRandomMapGen():
    #pull global vars
    global tiles, biomeFactor
    
    #set up lists
    rdmMap = []
    surroundings = []
    surroundings1 = []
    surroundings2 = []
    surroundings3 = []
    surroundings4 = []
    
    #get user desired map specs
    width = int(input('How wide: '))
    height = int(input('How tall: '))
    tiles = int(input('How many different tiles (1-10): '))
    biomeFactor = int(input('Please enter a biome factor (1-1000): '))
    
    #map loop
    for i in range(height):
        #start next row, print row num
        rdmMap.append([])
        print('Row:', i+1)
        for j in range(width):
    #        print(i, j)
            if i < 1:
                #init first row all rdm
                rdmMap[i].append(rd.randrange(100) % tiles)
                
            else:
                #consider near tiles
                #appending biome factors to lists to impact future tiles
                #keep list in length
                if j > 0:
                    surroundings1 = [rdmMap[i][j-1]] * biomeFactor 
                    
                surroundings2 = [rdmMap[i-1][j-1]] * biomeFactor
                surroundings3 = [rdmMap[i-1][j]] * biomeFactor
                                
                
                #keep list in length
                if j < width -1:
                    surroundings4 = [rdmMap[i-1][j+1]] * biomeFactor
                    
                #put all surrounding lists together
                surroundings.extend(surroundings1)
                surroundings.extend(surroundings2)
                surroundings.extend(surroundings3)
                surroundings.extend(surroundings4)
                
                
                #add 1 of each tile to stop single color maps
                for k in range(tiles):
                    surroundings.append(k)
                
                #clean surroundings
                surroundings.sort()
                #print(i, j, surroundings)
                #add tile to map based on surroudnings and clear surroundings
                rdmMap[i].append(rd.choice(surroundings))
                surroundings = []   
                
#print map if needed            
#    for row in rdmMap:
#        print('\n')
#        for num in row:
#            print(str(num), end = '  ')
    return rdmMap


def seededMapGen():
#    ask user questions
    width = int(input('How wide?'))
    height = int(input('How tall?'))
    tiles= int(input('How many different tiles?'))
    seed = int(input('Please input a seed number: '))
#    init seed and map
    rd.seed(seed)
    numMap = []
#    map gen
    for i in range(height):
        numMap.append([])
        for j in range(width):
            numMap[i].append(rd.randint(0, 999) % tiles)
#    print map
    for row in numMap:
        print('\n')
        for num in row:
            print(str(num), end = '  ')
    return numMap

#max tile set of 4
def asciiMap(numMap):
    asciiDict = {0:'mwm', 1:'___', 2:'/^\\', 3:'ooo' }
    for row in numMap:
        print('\n')
        for i in row:
            print(asciiDict[i], end = '')
    

def coloredArray(numMap):
    #pull global vars
    global tiles, biomeFactor
    #generate file name, width/height/tiles/biome map.png
    fileName = str(len(numMap[0])) + 'w' + str(len(numMap)) + 'h' + str(tiles) + 't' + str(biomeFactor) + 'bfMap.png'
    
    #create new blank white image
    image = Image.new('RGB', (len((numMap[0])), len(numMap)), (255, 255, 255))
    
    #dictionary of colors for the map
    colorDict = {0:(0,0,255), 1:(0,255,0), 2:(173, 173, 173), 3:(255, 219, 120), 4:(255,255,255), 5:(255, 159, 56), 6:(87, 87, 87), 7:(107, 255, 245), 8:(56, 125, 44), 9:(127, 140, 6)}
#    0 - Water, 1 - Plain, 2 - Mtn, 3 - Desert
#    (RGB)
    
    #color map in based on value in tile and using as dict key
    for i in range(len(numMap)):
        for j in range(len(numMap[i])):
            image.putpixel((j,i), colorDict[numMap[i][j]])

    #save image as fileName
    image.save(fileName, 'PNG')


#MAIN

#coloredArray(seededMapGen())
coloredArray(semiRandomMapGen())
        
        
        
        
        
        
        
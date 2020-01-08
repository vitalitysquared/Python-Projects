
##ADD DATA PRINT OPTION

import random as rand
from collections import defaultdict
import time

players = []
treeMatrix = []
totalTree = """
"""

class person:
    def __init__(self, i): 
        self.health = 100
        self.atk = rand.randrange(1, 10)
        self.defs = rand.randrange(1, 10)
        self.dead = False
        self.playerNum = i
        self.killedBy = 'W'
        


def startGame(numPlayers):
##    x = person()
##    y = person()
##    print(x.atk, x.defs)
##    print(y.atk, y.defs)
    
    generatePlayers(numPlayers)

    rounds = 0

    while rounds < 500:
        rounds += 1
        alivePlayers = []
        
        ##recreates list for players alive
        for i in range(len(players)):
            if not players[i].dead:
                alivePlayers.append(players[i])

        ##if more than one person alive battle, pick 2 randoms from the alive list
        if len(alivePlayers) > 1:
##            print('pre')
            battlers = rand.sample(alivePlayers, 2)
            battle(battlers[0], battlers[1])
##            print(battlers)
##            time.sleep(.1)
##            print(len(alivePlayers))

##prints health live
##            print('Player Number \tHealth')
##            for i in range(len(players)):
##                print(str(players[i].playerNum) + '\t\t' + str(players[i].health))


        ##if only 1 person or less alive print scoreboard
        else:
            print(len(alivePlayers))
            ##comment out next 4 for faster running
            print('\nRounds: ' + str(rounds))
            print('Player Number \tAtk \tDef \tHealth \tKilled By\n')
            for i in range(len(players)):
                print(str(players[i].playerNum) + '\t\t' + str(players[i].atk) + '\t' + str(players[i].defs) + '\t' + str(players[i].health) + '\t' + str(players[i].killedBy))
            break

##making the kill tree
    print('\nKill Tree\n')
    treeDict = treePre()
##    print(treeDict.items())
##    print(treeDict['1000'])
    treeCreation(treeDict, treeDict['W'])
    matrixPrint(treeMatrix)
    
def battle(p1, p2):
    ##Checks if atk is greater than def if so attacks
    ##Also chance for other player to hit back
    if p1.atk > p2.defs:
##        print('p1')
        p2.health -= p1.atk
        hitBack = rand.randrange(0, 100)
        if hitBack <= (p2.defs / p1.atk)*100:
            p1.health -= p2.atk
        
    elif p2.atk > p1.defs:
##        print('p2')
        p1.health -= p2.atk
        hitBack = rand.randrange(0, 100)
        if hitBack <= (p1.defs / p2.atk)*100:
            p2.health -= p1.atk

    else:
        p1.health -= 1
        p2.health -= 1
        hitBack = rand.randrange(0, 100)
        if hitBack <= (p2.defs / p1.atk)*100:
            p1.health -= p2.atk
        hitBack = rand.randrange(0, 100)
        if hitBack <= (p1.defs / p2.atk)*100:
            p2.health -= p1.atk
##        print('eq')


    if p1.health <= 0 and p2.health <= 0:
        p1.killedBy = p2.playerNum
        p1.dead = True
        p2.killedBy = p1.playerNum
        p2.dead = True
        
          
    elif p1.health <= 0:
##        print('Dead: ' + str(p1.playerNum))
        p1.killedBy = str(p2.playerNum)
        p1.dead = True
        
    elif p2.health <= 0:
##        print('Dead: ' + str(p2.playerNum))
        p2.killedBy = str(p1.playerNum)
        p2.dead = True
        
##turns player killed by data into usable dictionary
def treePre():
    killsDict = defaultdict(list)
    for player in players:
        killsDict[str(player.killedBy)].append(str(player.playerNum))
    return killsDict

##takes dictionary and creates easy to print tree and appends into matrix
def treeCreation(killsDict, winner, depth=0):
    global totalTree
    for player in winner:
##        print('│'*(depth-1)+ '├' + str(player))
        treeMatrix.append([depth, player])
        treeCreation(killsDict, killsDict[player], depth+1)

##prints matrix in format
def matrixPrint(matrix):
    global totalTree
    print(matrix[0][1])
    totalTree += matrix[0][1] + '\n'
    for item in matrix[1:]:
        print('│'*(item[0]-1) + '├' + item[1])
        totalTree += '│'*(item[0]-1) + '├' + item[1] + '\n'


def generatePlayers(playerCnt):
    for i in range(playerCnt):
        players.append(person(i))
##        print(players)
        
    ##comment out for faster running
    print('Player Number \tAtk \tDef')
    for i in range(len(players)):
        print(str(players[i].playerNum) + '\t\t' + str(players[i].atk) + '\t' + str(players[i].defs))

##x = person(1)
##y = person(2)
##print(x.atk, x.defs)
##print(y.atk, y.defs)
##battle(x, y)
##print(x.health, y.health)



startGame(10)
##battle(players[1], players[2])

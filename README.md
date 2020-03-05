# Python-Projects
This repository is where I will upload all my random python projects I (Eldon) make in my spare time.
This will be the repo for stuff in python and will be a bunch of random files that don't necessarily go with each other.
Any standalone file in the parent directory has no other files to go with it.
Any projects that require multiple files will be put into a folder with each other. 

Projects (in no particular order)
-------------------------
1)
Project:
jeopardyQuizGenerator - this takes the jeopardy question database and generates multiple choice questions for the user to answer. 
Files:
jeopardyQuestions.tsv - tab seperated file of all jeopardy quesitons, values, category, etc that the questions and answers are pulled from
jeopardyQuizGen.py - The quiz generator, created in python 3.8

2)
Project:
battleRoyaleTree - this project creates n number of players and gives them random attack and defense stats and has them battle eachother, then returns a tree showing who eliminated who, players are objects
Files:
battleRoyaleTree.py - main and only project file

3)
Project:
discordEncryptionBot - this is a discord bot I created which takes user text and returns an encrypted version of the text and then deletes the plaintext, encryption key is based on the date, so text is only valid for the day it was sent on
Files:
discordEncryptionBot - only project file, note if you want it to work you will have to put youre own discord bot key into the file

4)
Project:
randomMapGen - a project in which we have two different map generation methods and then a colored png of said map is output
Files:
randomMapGen.py - only file needed, semiRandomMapGen() takes into account the tiles surrounding, while seededMapGen() uses a seed and is capable of generating the same map, however the generation is entirely random

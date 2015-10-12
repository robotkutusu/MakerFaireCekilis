####################################
### Author : Inanc Gurkan        ###
### Mail : inanc@robotkutusu.com ###
####################################

import nltk #Reading the scores file
from numpy.random import choice #Lottery

#Open and read the score file
f = open('scores.txt','r').read()
fileLines = f.splitlines()

#Initialize
contestants = []
weights = []

#Populate
for element in fileLines:
  person = element.split()
  contestants.append(person[0]) #id
  weights.append(int(person[1])) #chance

#Sums all of the elements in input array. Returns int
def calculateTotal(weights):
  total = 0
  for w in weights:
   total += w
  return total

total = calculateTotal(weights)

#Maps the 'weights' array, the sum of element should be equal to 1.
#See 'numpy.random.choice'
weights = [element/total for element in weights]

#Numpy Function
winners = []
while len(winners) < 5 :
  winner = choice(contestants, p=weights)
  if winner not in winners:
    winners.append(winner)

print(winners)

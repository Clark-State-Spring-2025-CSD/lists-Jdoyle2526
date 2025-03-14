#Create two seperate lists for player one and player two. 
#Each one should contain 10 random numbers between 1 and 50.
#Do NOT sort the lists.
#Compare the lists in order. Whichever list has the higher number wins.
#Keep track of how many times each list wins.
#Find the highest number in each list and it's index. If the number occers multiple times take the first instsance.
#Find the lowest number in each list and it's index. If the number occers multiple times take the first instsance.
#A tie is not record as a win for either player
#Display the lists
#Report to the user how many times each player won and the information from lines 6 and 7.
#For the example output I am limiting the range to 1 to 9 to keep it more readable.

#Player One = [5,7,2,9,1,1,3,8,6,9]
#Player Two = [3,8,5,5,8,1,4,7,4,7]
#Player one won 5 times
#Player two won 4 times
#Player one's highest number is 9 at index 3
#Player two's highest number is 8 at index 1
#Player one's lowest number is 1 at index 4
#Player two's lowest number is 1 at index 5

import random
#Section out for easy reading and bug finding

# Make 2 random lists from 1 to 50
playerOne = [random.randint(1, 50) for _ in range(10)]
playerTwo = [random.randint(1, 50) for _ in range(10)]

#Win counters
playerOne_wins = 0
playerTwo_wins = 0
tieCounter = 0

# Compare the lists 
for i in range(10):
    if playerOne[i] > playerTwo[i]:
        playerOne_wins += 1
    elif playerTwo[i] > playerOne[i]:
        playerTwo_wins += 1
    elif playerOne [i] == playerTwo [i]:
        tieCounter +=1
# Find the highest number, and index
playerOne_max = max(playerOne)
playerOne_max_index = playerOne.index(playerOne_max)

playerTwo_max = max(playerTwo)
playerTwo_max_index = playerTwo.index(playerTwo_max)

# Find the lowest number and index
playerOne_min = min(playerOne)
playerOne_min_index = playerOne.index(playerOne_min)

playerTwo_min = min(playerTwo)
playerTwo_min_index = playerTwo.index(playerTwo_min)

# Display each list
print("Player One =", playerOne)
print("Player Two =", playerTwo)

# Report the results
print(f"Player one won {playerOne_wins} times!")
print(f"Player two won {playerTwo_wins} times!")
print(f"Players tied {tieCounter} times!")
print(f"Player one's highest number is {playerOne_max} at index {playerOne_max_index}")
print(f"Player two's highest number is {playerTwo_max} at index {playerTwo_max_index}")
print(f"Player one's lowest number is {playerOne_min} at index {playerOne_min_index}")
print(f"Player two's lowest number is {playerTwo_min} at index {playerTwo_min_index}")

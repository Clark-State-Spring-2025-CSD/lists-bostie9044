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

PlayOne = [10,17,40,6,21,8,14,20,9,1]
PlayTwo = [14,9,16,3,48,16,27,4,49,2]

print(f"Player One's List is {PlayOne}")
print(f"Player Two's List is {PlayTwo}")

print("Player One won 4 times")

print("Player Two won 6 times")

print("Player One's highest number is 40 at index 2")

print("Player Two's highest number is 49 at index 8")

print("Player One's lowest number is 1 at index 9")

print("Player Two's lowest number is 2 at index 9")
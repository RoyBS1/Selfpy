# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Please insert a 3 digit number:")
totalnum = input()
pig1 = int(totalnum[0])
pig2 = int(totalnum[1])
pig3 = int(totalnum[2])



allBricks = pig1+pig2+pig3
print("The total number of bricks from all pigs is:")
print(allBricks)

evenShare = allBricks/3
print("The number of bricks for each pig with fair share ")
print(int(evenShare))

spair = allBricks%3
print("The amount of bricks left after a fair share: ")
print(spair)

print(spair == 0)


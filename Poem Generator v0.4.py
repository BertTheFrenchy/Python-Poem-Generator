import random
import time

print("Hello and welcome to the poem maker program v0.4")
userInput = input("Please enter a sentence or words to use to generate your poem: \n")
words = userInput.split(' ')
print("You have entered the following words: \n")
print(words)
originalList = userInput
random.shuffle(words)
poem = ""
chance = int(input("Please enter a percentage chance to add a new line: \n"))
for i in range(len(words)):
    if((random.randint(0,100)) < chance):
        poem += "\n"
    poem += str(words[i])+ " "
time.sleep(.5)
print("Your new poem reads: \n" + poem)

save = input("\nDo you wish to save your work? Y/N\n")
if save.upper() == "Y":
    fileName = input("Please enter a name for the file:\n")
    time.sleep(.5)
    if ".txt" not in fileName:
        fileName += ".txt"
    time.sleep(.5)
    file = open(fileName, "at")
    file.write("The poem was generated from:\n" + userInput + "\n")
    file.write("\nIt now reads:\n" + poem + "\n")
    file.close()
    file = open(fileName, "rt")
    time.sleep(1)
    print("\nThe file now reads:\n"+ file.read())
else:
    print("\nYou have successfully generated a one-off poem.")
    time.sleep(1)
print("\nThank you for using the BB poem generator!\nGoodbye!")
input()

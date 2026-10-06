n=str(input("Enter the word: ")) #prompt the user to input a word

for char in range(len(n)-1,-1,-1): #loop through the characters of the word in reverse order without using the reverse function
    print(n[char], end="") #print the characters in reverse order without adding a new line after each character
print("\n") #add a new line after printing the reversed word for better formatting
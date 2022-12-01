#Kenny Hedlund

# Global variable for english vowels
vowels = ["a","e","i","o","u"]

#Translation function
def translate(word):
    first = word[0]
    if first in vowels: #What to add for words starting in a vowel
         word = word.lower().isalpha()
         word += "way" 
         return word
    else: #What to add for words starting in a consenant
        word = word.lower()
        for letter in word:
            if letter in vowels:
                index_value = word.index(letter)
                break
        word = word[index_value:] +word[:index_value] + "ay" 
        return word 

def main():
    print("++++++++++++++++++++")
    print("Pig Latin Translator")
    print("++++++++++++++++++++")
    print()
    choice = "y"
    while choice.lower() == "y":
        #Get word from user
        word = input("Enter word: ")
        translate(word)
        print()
        print("English: ", str(word))#Prints inital word string
        print("Pig Latin: ", translate(word))#Prints the translation from the function
        print()
        choice = input("Continue? (Y/N)")
    #Printed if user inputs anything other than Y on choice
    print()
    print("Bye!")

if __name__ == "__main__":
    main()
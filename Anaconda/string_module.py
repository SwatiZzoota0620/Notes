#FUNCTION TO TEST STRING IS PALINDROME OR NOT
def stringPalindrome(user_string):
        if user_string == user_string[::-1]:
            print(f"User entered string is palindrome")
        else:
            print(f"User entered string is not a palindrome")


#Python Function to Calculate the Length of a String
#Without Using Built-In len() Function
def stringLength(user_string):
    count_character = 0
    for each_character in user_string:
        count_character += 1
    print(f"The length of user entered string is {count_character} ")


# Function to print index of each character in a string
def displayindex(alphabet):
    index = 0
    print(f"In the string '{alphabet}'")
    for each_character in alphabet:
        print(f"Character '{each_character}' has an index value of {index}")
        index += 1

#Program to Print the Characters Which Are Common in 
#Two Strings
def commoncharacter(string_1,string_2):
    for letter in string_1:
        if letter in string_2:
            print(f"Character '{letter}' is found in both the strings")


#Write Python Program to Count the Total Number of Vowels,
#Consonants and Blanks in a String
def count_vowel_consonant_blank(user_string):
    vowels = 0
    consonants = 0
    blanks = 0
    for each_character in user_string:
        if(each_character == 'a' or each_character == 'e' or each_character == 'i' or each_character == 'o' or each_character == 'u'):
            vowels += 1
        elif "a" < each_character < "z":
            consonants += 1
        elif each_character == " ":
            blanks += 1
    print(f"Total number of Vowels in user entered string is {vowels}")
    print(f"Total number of Consonants in user entered string is {consonants}")
    print(f"Total number of Blanks in user entered string is {blanks}")


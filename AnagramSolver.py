# Design: This program takes user input and compares to english words in a txt file to determine how the letters can be rearranged to form different words. It is implemented with python and is arranged in manageable steps with functions. 


def readFile(): # function that open a files and returns every line into list
   file = open("words.txt", encoding="ISO-8859-1") # open file
   with open('words.txt') as word_file: # cycle through file
      lines = file.readlines() # read file line-by-line
   file.close() # close file

   return lines # return all lines from file

anagram_number = 0
def generateAnagrams(anagram, lines): # function that reorders letters to make anagrams 
   global anagram_number 
   anagrams = "" 
   for line in lines: # loop that reads line-by-line from entire file
      sorted_line = ' '.join(line.split()) # convert from encoding to format to compare to string
      if sorted(anagram.lower()) == sorted(sorted_line.lower()) and len(anagram) == len(sorted_line): # determines if sorted input is same as sorted word in txt file and checks if length is the same
         anagrams = anagrams + line # if the same letters, adds the string from txt file to list of anagrams
         anagram_number = anagram_number + 1 # increment anagram number

   return anagrams # return total string of anagrams
       
def main(): # main function
   anagram = input("Type in anagram: ") # user input
   anagrams = generateAnagrams(anagram, readFile()) # variable that stores anagrams from function

   # conditional statements that prints out total anagrams with number of them or lack thereof if no option is found
   if anagram_number == 0: 
      print("There is no word that can be made of the letters inputted.\n")
   elif anagram_number == 1:
      print("The letters make " + str(anagram_number) + " anagram: \n" + anagrams)
   else:
      print("The letters make " + str(anagram_number) + " anagrams: \n" + anagrams)

if __name__ == "__main__": # call main function
   main()
            
                    

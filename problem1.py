"""
String handling is important.  We can break a string into pieces to help us look at parts one at a time using the string.split function.
Have the user enter a sentence or paragraph and gives a word count.
"""

def breakstring(s):
    word_list = s.split()
    return word_list

def main():
  s = str(input("Enter a sentence or paragraph: "))
  wordList = breakstring(s)
  word_count = len(wordList)
  print (word_count)


if __name__ == "__main__":
  main()

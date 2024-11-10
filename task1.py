#!python3

'''
Write a function that searches a Listing for all occurrences of the word "dog" and replaces it with "kitty"
You only need to modify the function replaceDog
The assertion tests are included so you can test your output
(4 points) 
'''



def replaceDog(input):
    modifiedList = ""
    
    wordList = input.split(' ')
    #print(wordList)
    for word in wordList:
        if word == "dog":
            modifiedList += "kitty"
        else:    
            modifiedList += word
        modifiedList += " "
        print ("[" + modifiedList + "]")
    modifiedList = modifiedList.rstrip(" ") 
    print ("final string => [" + modifiedList + "]")
    return modifiedList

def replaceDog1(input):
    
    
    '''
    parameters:
    List input - Listing to search and replace occurrences of dog with kitty
    
    return
    List - the modified Listing
    '''
    modifiedListing = input.replace("dog", "kitty")
     
    print (modifiedListing)
    return modifiedListing       

if __name__ == "__main__":
    '''
    assertion tests are basically a statement claiming truth
    if the statement is true, the program continues normally
    if the statement is not true, then an exception is thrown
    '''
    x = 'my dog has fleas'
    assert replaceDog(x) == 'my kitty has fleas'


    x = 'i have a dog and a goldfish as my pets'
    assert replaceDog(x) == 'i have a kitty and a goldfish as my pets'
    
    
    

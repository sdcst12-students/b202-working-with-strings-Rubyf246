#!python3
'''
##### Task 3
Split a string into 2 halves and insert a line break in the middle.  If doing so cuts a word in half, add a dash to the first line.  You will need to make use of the

len(str) function
this function returns the length of the string

( points)
'''

def split(input):
    '''
    parameters
    str input - string to be split
    
    return
    str new string with line break in the middle
    '''
    midlen = len(input)/2
    print (midlen)
    mididx_left = int(midlen)-1
    mididx_right = int(midlen)
    
    charleftofmid = input[mididx_left] 
    charrightmid = input[mididx_right] 
    print("midchar: [" +charleftofmid + "]" +"midchar2: [" +charrightmid + "]")
    
    firsthalf = ""
    secondhalf = ""
    finalstr = ""
    
    if (charleftofmid == " ") or (charrightmid == " "): #either beginning or end of a word => NOT in the middle of a word
        firsthalf = input[0:mididx_right]
        secondhalf = input[mididx_right: len(input)]
        finalstr = firsthalf +"\n" + secondhalf
    else:  #in the middle of a word
        firsthalf = input[0:mididx_right] + "-" 
        secondhalf = input[mididx_right: len(input)]   
        finalstr = firsthalf +"\n" + secondhalf 
    print ("[" + firsthalf + "]")
    print ("[" + secondhalf + "]")
    
    print(finalstr)
    return finalstr

if __name__ == "__main__":
    sentence = "There is a big balloon in the blue sky"
    assert split(sentence) == "There is a big ball-\noon in the blue sky"

    sentence = "I am a fat cat"
    assert split(sentence) == "I am a \nfat cat"

    sentence = "I was a fat cat"
    assert split(sentence) == "I was a\n fat cat"
#Implement an algorithm to determine is a sting has all unique characters

# First we have to decide where it is ASCII with 128 chars or ETFS coded

#Here we are testing the value of variues characters, as 'a' has value 97 etc.

testString = "abc"

def isUniqueChars(str):      #We are taking string as an input
    if len(str) > 128:
        return False     #It would be False as ASCII has 128 characters
    arr = [False] * 128   # To determine whether all characters are unique
    for char in str:
''' For each character in the string
In the below line we are chacking the values first time wherther
it is true of false  '''
        if arr[ord(char)] is False:  
            arr[ord(char)] = True
        else :
            return False   # If it is False then we have found the value already
    return True         #This means there are no duplacate characters in the string.

print (isUniqueChars(testString))
            
# It is O^n as the string gets bigger, the longer it will take
# We can also test the various string by changing the testString value

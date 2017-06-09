'''  Q2: Given two strings and we have to write a method to decide if one is a
       permutation of the other  '''

# Permutation is the re-arrangements of elements in a set.
'''If we have a string 'abc' then the Premutation of that string can be
   'cab' or 'bac' etc. But it shold have all the elements wheic are already
   in a set, not any external element like 'dabc' etc '''
#The length of the two strings should be equal
#otherwise they are two different sets.

def checkPermutation(str1, str2):    # It is taking two strings str1 and str2
    if len(str1) != len(str2):  # We are comparing two stings
        return False            # If two strings are not equal then return False
    else:
        return ''.join(sorted(str1)) == ''.join(sorted(str2)) # '' is to take the string

#In the above statement we are compring two strings.

print(checkPermutation("abc", "bca"))

#We can change the value of atring to test to various cases.
        

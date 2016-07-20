# String Operation
# Always consider edge cases (empty, numeric, space)
# Always use test cases to test the code
# Always use and, or, not
# If use while loop, don't forget to increment i
# Read the question at least twice
# Add some explanation comments at the end
# string and tuple are immutable

# Question: Find the longest palindromic substring in a string
def longestPalindrome(string):
    for length in range(len(string), 0, -1):
        for i in range(len(string) - length + 1):
            if isPalindrome(string[i:i+length]):
                return string[i:i+length]
            else:
                continue
    return 'No palindrome found.'

def isPalindrome(string):
    if len(string) == 1:
        return False
    else:
        start = 0
        end = len(string)-1
        while start < end:
            if string[start] != string[end]:
                return False
            start += 1
            end -= 1
    return True
         
print(longestPalindrome("1234567654321"))
print(longestPalindrome("12345676543212"))
print(longestPalindrome("12321123454321"))
        
        
# Question: Determine if a string has unique characters
def isUniqueChar(str):
    dict = {}
    for char in str:
        if char in dict and dict[char]:
            return False
        else:
            dict[char] = True
    return True
print(isUniqueChar('abcdef'))
print(isUniqueChar('aabcdef'))

# Question: Reverse a string
def reverseStr(str):
    str_new = ''
    for i in range(len(str)-1, -1, -1):
        str_new += str[i]
    return str_new
        
print(reverseStr('abcdefg'))
print(reverseStr(''))

# Question: Given two strings, write a method to decide if one is a substring of the other
def isSubstringEasy(str1, str2):
    return str1 in str2

def isSubstring(str1, str2):
    # check if str1 is a substring of str2
    if len(str2) < len(str1):
        return False
    
    i = 0
    while i+len(str1) < len(str2):
        if str2[i:i+len(str1)] == str1:
            return True
        else:
            i += 1
    return False
print(isSubstringEasy('dogs', 'dogs are awesome!'))
print(isSubstringEasy('dogsa', 'dogs are awesome!'))
print(isSubstring('dogs', 'dogs are awesome!'))
print(isSubstring('dogsa', 'dogs are awesome!'))
        

# Question: Given two strings, write a method to decide if one is a permutation of the other
# Assume it is case sensitive and white spaces are significant
def isPermutation(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    if len1 != len2:
        return False
    char_count = {} # to store the count of each char in str1
    for char in str1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in str2:
        if char not in char_count:
            return False
        else:
            char_count[char] -= 1
        if char_count[char] < 0:
            return False
    return True

print(isPermutation('dog is amazing', 'god amazing is'))
print(isPermutation('', ''))

# Question: Replace part of the string with another string
def replaceStr(str, targetStr, replaceStr):
    strReplaced = ''
    i = 0
    while i < len(str): 
        if str[i:i+len(targetStr)] == targetStr:
            strReplaced += replaceStr
            i += len(targetStr)
        else:
            strReplaced += str[i]
            i += 1
    return strReplaced

print(replaceStr('Tomorrow is another day!', 'another', 'new'))

# Question: Compress a string, e.g. aabbccc -> a2b2c3
def compressStr(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    compressed_str = ''
    for key, value in char_count.items():
        compressed_str += str(key)+str(value)
        
    if len(compressed_str) > len(string):
        return string
    else:
        return compressed_str
    
print(compressStr('aabbccc'))
print(compressStr(''))

# Question: Print all filenames of a given directory with a recursive approach
def printFile(path):
    for child in os.listdir(path):
        childPath = os.path.join(path,child)
        if os.path.isdir(childPath):
            printFile(childPath)
        else:
            print childPath
            
printFile("/Users/johnnycao/Development/johnny/Crack")

# Question: Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.
#count_code('aaacodebbb') → 1
#count_code('codexxcode') → 2
#count_code('cozexxcope') → 2
def count_code(str):
    if len(str) <4: return 0

    count = 0
    i = 0
    while i <= len(str):
        if len(str[i:]) <4: return count
        if str[i:i+2] == 'co' and str[i+3] == 'e':
            count +=1
            i +=4
        else:
            i +=1
    return count

# Question: Return True if the string "cat" and "dog" appear the same number of times in the given string.
#cat_dog('catdog') → True
#cat_dog('catcat') → False
#cat_dog('1cat1cadodog') → True
def cat_dog(str):
    cat_count = 0
    dog_count = 0
    if len(str) < 3: return True

    for i in range(len(str)-1):
        if len(str[i:]) < 3 : break
        if str[i:i+3] == 'cat': cat_count+=1
        elif str[i:i+3] == 'dog': dog_count+=1

    return cat_count == dog_count
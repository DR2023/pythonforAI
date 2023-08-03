
#Function to reverse a string using slicing
def reverseAString(string):
    return string[::-1]

# Alternate Function to reverse a string
def reverseUsingJoin(string):
    string = [string[i] for i in range(len(string)-1, -1, -1)]
    return "".join(string)

#Function to reverse each word in a sentence
def reverseWordsSentence(S):
    words = S.split(" ") #split sentence by space
    ans = ""
    for i in words:
        ans = i[::-1] + " " + ans   
    return ans[:len(ans)-1] # truncate space in the end of sentence

#Function to reverse string seperated by .(not charcters but by word)
def reverseWords(S):
    words = S.split(".") #split sentence by space
    ans = ""
    for i in range(len(words)-1,-1,-1):
        ans = ans + "." + words[i]
        print(ans)
    return ans[1:]# truncate . in the start of sentence  

#Check if string is anagram
def isAnagram(a,b):
        a = ''.join(sorted(a))
        b = ''.join(sorted(b))
        if a == b:
            return True
        else:
            return False

if __name__ == '__main__':
    # revstring = reverseAString("Deepthi")
    # print(f"Reversed String = {revstring}")
    # revstring = reverseUsingJoin("Deepthi")
    # print(f"Reversed String = {revstring}")
    # reversewordsinsentence = reverseWordsSentence("How are you?")
    # print(f"Reversed words in given sentence : {reversewordsinsentence}")
    reverseWordsResult = reverseWords("i.like.you")
    print(f"Reversed words in given sentence : {reverseWordsResult}")
    anagramCheck = isAnagram("swattl","swaltt")
    print(f"Result for Anagram check : {anagramCheck}")

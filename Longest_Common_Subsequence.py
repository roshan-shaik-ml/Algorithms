'''
Given two strings s and t, check if s is a subsequence of t using dynamic programming.
A subsequence of a string is a new string that is formed from the original string by 
deleting some (can be none) of the characters without disturbing the relative positions
of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
'''

def longestCommonSubsequence(str1, str2):

    len1 = len(str1)
    len2 = len(str2)

    table = [[0 for x in range(0, len2+1)] for y in range(0, len1+1)]
    for char1 in range(1, len1 + 1):

        for char2 in range(1, len2 + 1):


            if str1[char1-1] == str2[char2-1]:

                table[char1][char2] = table[char1-1][char2-1] + 1
            else:

                table[char1][char2] = max(table[char1-1][char2], table[char1][char2-1])

    return table[len1][len2]

def printResult(length, string):

    if length == len(string):
        print(True)
    else:
        print(False)

if __name__ == "__main__":

    test_str1 = "ABC"
    test_str2 = "AXE"
    str2 = "AHBGDC"
    maxLength1 = longestCommonSubsequence(test_str1, str2)
    maxLength2 = longestCommonSubsequence(test_str2, str2)

    printResult(maxLength1, test_str1)
    printResult(maxLength2, test_str2)

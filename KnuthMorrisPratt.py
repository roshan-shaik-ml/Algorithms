# Author: Shaik Faizan Roshan Ali
# Email: alsahercoder@gmail.com
# About: substring search KMP algorithm with time complexity of O(m+n)

def compute_lps(pattern):

    pattern_length = len(pattern)
    lps = [0 for _ in range(0, pattern_length+1)]

    lps[1] = 0 # lps[1] of any string is 0
    k = 0
    q = 0

    for q in range(2, pattern_length):

        while (k > 0 and pattern[k+1] != pattern[q]):

            k = lps[k+1]
        if(pattern[k+1] == pattern[q]):

            k = k + 1
        lps[q] = k

    return lps
  
def kmp(text, pattern):

    text_length = len(text)
    pattern_length = len(pattern)

    lps = compute_lps(pattern)

    text = text
    txt_pointer = 1
    pattern_pointer = 0
    while (txt_pointer < text_length and pattern_pointer < pattern_length):

        print(text[txt_pointer], pattern[pattern_pointer+1])

        # when text character and pattern character matched increment both pointers
        if(text[txt_pointer] == pattern[pattern_pointer+1]):

            txt_pointer += 1
            pattern_pointer += 1
            if(pattern_pointer + 1 == pattern_length):

                return txt_pointer - pattern_length
        else:

            # if pattern point not at zero and both pointer don't match
            # adjust the pattern pointer using the LPS table
            if(pattern_pointer != 0):

                pattern_pointer = lps[pattern_pointer]
            
            # if both pointers dont match and pattern pointer at zero
            # move the text pointer to the next character
            else:

                 
                txt_pointer += 1

        return -1
      
if __name__ == "__main__":

    pattern = 'abcab'
    text = 'aabaababcabab'
    position = kmp(text, pattern)
    
    if(position == -1):

        print("Pattern not found")
    else:
        print("Pattern found at index", position)

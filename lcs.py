# A Naive recursive Python implementation of Longest Common Subsequence problem

# Examples:
# LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
# LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.

def lcs(s1, s2, m, n):
    if m == 0 or n == 0:
        return 0
    elif s1[m-1] == s2[n-1]:
        return 1 + lcs(s1, s2, m-1, n-1)
    else:
        return max(lcs(s1, s2, m-1, n), lcs(s1, s2, m, n-1))


# Driver program to test the above function
X = "AGGTABA"
Y = "GXTXAYBA"
print "Length of LCS is ", lcs(X , Y, len(X), len(Y))

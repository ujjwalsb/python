'''Complete the solution so that it reverses all of the words within the string passed in.

Example:

reverseWords("The greatest victory is that which requires no battle")
// should return "battle no requires which that is victory greatest The"
'''

def reverseWords(str):
	str = str.split()
	words = str.reverse()
	return (" ".join(str))

w1 = reverseWords("The greatest victory is that which requires no battle")
print(w1)
'''
An isogram is a word that has no repeating letters, consecutive or 
non-consecutive. Implement a function that determines whether a 
string that contains only letters is an isogram. 
Assume the empty string is an isogram. Ignore letter case.

is_isogram("Dermatoglyphics" ) == true
is_isogram("aba" ) == false
is_isogram("moOse" ) == false # -- ignore letter case
'''


def isIsogram(string):
	if string == " ":
		return (string, True)

	else:
		string = string.lower()
		for values in string:
			if string.count(values) > 1:
				return (string, False)
	return (string, True)

isogram1 = isIsogram("UjJwAl")
isogram2 = isIsogram("SiNgH")
isogram3 = isIsogram("BaGhEl")

print(isogram1)
print(isogram2)
print(isogram3)
'''
Ques 10. Write a program to find the number of occurrences of each vowel present in a given string, and also
print the vowels.
'''

string = input("Enter a string: ").lower()
vowels = "aeiou"
occurrences = {vowel: string.count(vowel) for vowel in vowels if vowel in string}
print("Vowels found:", occurrences.keys())
print("Occurrences:", occurrences)



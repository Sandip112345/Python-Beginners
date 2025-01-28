'''
Write a program to read the text from a give from 'poem.txt'
and find out whether it contains the word 'twinkle'
'''
f = open("poem.txt")
content = f.read()
if("twinkle" in content):
    print("Twinkle is present in the content")
else:
    print("The word 'Twinkle' is not present in the content.")
    

f.close()
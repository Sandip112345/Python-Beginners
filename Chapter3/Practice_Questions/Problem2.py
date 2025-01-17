# Write a program to fill in a letter template given below with name and date
letter = '''
        Dear <|Name|>,
        You are selected!
        <|Date|>
        '''

# letter = letter.replace("<|Name|>", "Sandip")
# letter = letter.replace("<|Date|>", "1/17/2023")
# print(letter)
print(letter.replace("<|Name|>","Sandip").replace("<|Date|>", "1/17/2023"))




import os
with open("./Input/Names/invited_names.txt") as f:
    names = f.read().split("\n")
 
for name in names:
    with open("./Input/Letters/starting_letter.docx") as file:
        letter = file.read().replace("[name]", name)
        with open(f"./Output/ReadyToSend/letter_for_{name}.docx", mode="w") as f:
            f.write(letter)
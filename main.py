
# TODO: Create a list with the receivers from the invited_name.txt file
with open('./Input/Names/invited_names.txt') as f:
    invited_names = f.readlines()

# strip the character \n from the names of the list

stripped_invited_names = [element.strip("\n") for element in invited_names]

# TODO: Insert the name of the reciever on the placeholder of the starting_letter.txt

with open("./Input/Letters/starting_letter.txt") as f:
    letter = f.read()


# TODO: Save the letters in a file call 'letter_for_[name]' in the ReadyToSend folder

for invited_names in stripped_invited_names:
    with open(f"./Output/ReadyToSend/letter_for_{invited_names}", "w") as f:
        f.write(letter.replace('[name]', invited_names))









# TODO: Save the new letter with the new file name in the ReadyToSend folder

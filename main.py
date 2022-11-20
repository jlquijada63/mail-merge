
# TODO: Create a list with the receivers from the invited_name.txt file
with open('./Input/Names/invited_names.txt') as f:
    invited_names = f.readlines()

# strip the character \n from the names of the list

stripped_invited_names = [element.strip("\n") for element in invited_names]

# TODO: Insert the name of the reciever on the placeholder of the starting_letter.txt






# TODO: Save the new letter with the new file name in the ReadyToSend folder

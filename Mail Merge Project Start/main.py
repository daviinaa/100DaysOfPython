# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# return the names as a list
PLACEHOLDER = "[name]"
with open("Input/Names/invited_names.txt", "r") as f:
    names_list = f.readlines()

# Replace the [name] placeholder with the actual name.
# read the file first
with open("Input/letters/starting_letter.txt", "r") as letter_names:
    letter_content = letter_names.read()
    for name in names_list:
        # remove extra lines in front of the name in the list
        stripped_name = name.strip()
        updated_contents = letter_content.replace(PLACEHOLDER, stripped_name)
        # Save the letters in the folder "ReadyToSend".
        with open(f"Output/ReadyToSend/{stripped_name}.txt", 'w') as file:
            file.write(updated_contents)
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
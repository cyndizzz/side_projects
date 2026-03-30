#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"

with open('Input/Letters/starting_letter.txt', 'r') as f:
    letter_template = f.read()

with open("Input/Names/invited_names.txt", 'r') as f:
    invited_names = f.readlines()

    for name in invited_names:
        name = name.strip('\n')
        new_letter = letter_template.replace(PLACEHOLDER, name)
        with open(f"Output/ReadyToSend/letter_for_{name}.docx",'w') as f:
            f.write("".join(new_letter))
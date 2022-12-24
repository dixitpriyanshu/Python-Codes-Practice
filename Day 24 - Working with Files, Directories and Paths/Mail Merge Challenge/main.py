PLACEHOLDER = "[name]"

with open("Day 24 - Working with Files, Directories and Paths/Mail Merge Challenge/Input/Names/invited_names.txt") as name_data:
    names = name_data.readlines()
    

with open("Day 24 - Working with Files, Directories and Paths/Mail Merge Challenge/Input/Letters/starting_letter.txt") as sample_letter:
        letter_contents = sample_letter.read()
        for name in names:
            stripped_name = name.strip("\n")
            new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
            with open(f"Day 24 - Working with Files, Directories and Paths/Mail Merge Challenge/Output/ReadyToSend/letter_to_{stripped_name}.txt","w") as final_letter:
                final_letter.write(new_letter)
        
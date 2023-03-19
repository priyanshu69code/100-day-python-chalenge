# Declaring What should I have to change in letter formate
PLACEHOLDER = "[name]"

# Reading the file Letter in which my latter is and also all the names
with open("Day 24\Mail Merge Project Start\Input\Letters\starting_letter.txt") as letters:
    letter = letters.read()

with open(r"Day 24\Mail Merge Project Start\Input\Names\invited_names.txt") as names:
    list_name = names.readlines()

for name in list_name:
    modified_name = name.strip()  # Use stipe because there os "\n" in all the names
    new_letter = letter.replace(PLACEHOLDER, modified_name)
    with open(f'Day 24\Mail Merge Project Start\Output\ReadyToSend\letter_for_{modified_name}.txt', mode="w") as completd_letter:
        completd_letter.write(new_letter)

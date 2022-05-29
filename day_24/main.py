from pathlib import Path
import logging

input_data_folder = Path("Input/")
output_data_folder = Path("Output/")

letter_file = input_data_folder / "Letters/starting_letter.txt"
name_file = input_data_folder / "Names/invited_names.txt"
ready_to_send_dir = output_data_folder / "ReadyToSend"

# Get list of names from file
with open(name_file) as f:
    name_list = f.read().split('\n')

# Write letter to each name in list
try:
    with open(letter_file, mode='r') as f:
        letter = f.read()
        for name in name_list:
            with open(f'{ready_to_send_dir}/letter_for_{name}.txt', mode='w') as letter_f:
                letter_f.write(letter.replace('[replace]', f'{name}'))
except Exception as e:
    logging.error(e)

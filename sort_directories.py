import os

def pad_number(num_str, max_length):
    """ Pad the number string with leading zeros to match the max_length. """
    return num_str.zfill(max_length)

# Get the current working directory
current_working_directory = os.getcwd()

# Split directory names and filter out hidden files and non-numeric prefixes
visible_dirs = [dir.split('_') for dir in os.listdir(current_working_directory) if not dir.startswith('.') and dir.split('_')[0].isdigit()]

# Determine the maximum length of the number prefixes
max_length = max(len(dir[0]) for dir in visible_dirs)

# Sort and rename directories
for dir_parts in visible_dirs:
    new_number = pad_number(dir_parts[0], max_length)
    old_dir_name = '_'.join(dir_parts)
    new_dir_name = '_'.join([new_number] + dir_parts[1:])
    
    # Rename the directory
    os.rename(os.path.join(current_working_directory, old_dir_name),
              os.path.join(current_working_directory, new_dir_name))

# List the directories again to show the new order
print(sorted(os.listdir(current_working_directory)))
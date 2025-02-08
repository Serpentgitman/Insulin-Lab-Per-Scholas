#regex to remove unwanted parts from the file
import re

# Read the file
with open('PREPROINSULIN-SEQ.TXT', 'r') as file:
    data = file.read()

# Use regex to remove unwanted parts
cleaned_data = re.sub(r'ORIGIN|//|\d+|\s+', '', data)

print(cleaned_data)
# Perform character count
character_count = len(cleaned_data)
print(f"Character count: {character_count}")
#regex to remove unwanted parts from the file
import re

# Read the file
with open('PREPROINSULIN-SEQ.TXT', 'r') as file:
    data = file.read()

# Use regex to remove unwanted parts
cleaned_data = re.sub(r'ORIGIN|//|\d+|\s+', '', data)

# Save the first 1-24 characters to a new file
with open('lsinsulin_seq_clean.txt', 'w') as file:
    file.write(cleaned_data[:24])

print(f"First 1-24 characters saved to lsinsulin_seq_clean.txt")
# Read the cleaned file
with open('preproinsulin_seq_clean.txt', 'r') as file:
    cleaned_data = file.read()

# Save characters 25-54 to a new file
with open('binsulin-seq-clean.txt', 'w') as file:
    file.write(cleaned_data[24:54])

print(f"Characters 25-54 saved to binsulin-seq-clean.txt")

# Read the cleaned file
with open('preproinsulin_seq_clean.txt', 'r') as file:
    cleaned_data = file.read()

# Save amino acids 55-89 to a new file
with open('cinsulin-seq-clean.txt', 'w') as file:
    file.write(cleaned_data[54:89])

print(f"Amino acids 55-89 saved to cinsulin-seq-clean.txt")

# Read the cleaned file
with open('preproinsulin_seq_clean.txt', 'r') as file:
    cleaned_data = file.read()

# Save amino acids 90-110 to a new file
with open('ainsulin-seq-clean.txt', 'w') as file:
    file.write(cleaned_data[89:110])

print(f"Amino acids 90-110 saved to ainsulin-seq-clean.txt")

# File Read & Write Challenge 🖋️

# Open the original file for reading
with open("input.txt", "r") as infile:
    content = infile.read()

# Modify the content (example: convert to uppercase)
modified_content = content.upper()

# Write the modified content into a new file
with open("output.txt", "w") as outfile:
    outfile.write(modified_content)

print("File has been read and modified content written to output.txt ✅")

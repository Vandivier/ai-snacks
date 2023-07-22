# Define the input and output file paths
input_filepath = "./raw-thread-text.txt"
output_filepath = "./semicleaned.txt"

# Open the input file in binary mode
with open(input_filepath, "rb") as f:
    # Read the file content
    raw_data = f.read()

# Decode the byte data to string, ignoring non-UTF-8 characters
decoded_data = raw_data.decode("utf-8", "ignore")

# Replace "\n" with a proper line break
cleaned_data = decoded_data.replace("\\n", "\n")

# Open the output file in write mode
with open(output_filepath, "w") as f:
    # Write the cleaned data to the output file
    f.write(cleaned_data)

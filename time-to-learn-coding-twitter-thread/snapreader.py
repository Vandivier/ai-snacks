import json

# Read the snapofsnaps.json file
with open("snapofsnaps.json", "r") as file:
    snapofsnaps = json.load(file)

# Initialize the final array with the first snapshot
final_array = snapofsnaps[0]

# Loop through the rest of the snapshots
for i in range(1, len(snapofsnaps)):
    # Check for overlap with the previous snapshot
    overlap = [value for value in snapofsnaps[i] if value in final_array]

    # If there's no overlap, raise an error
    if not overlap:
        raise ValueError(f"No overlap found between snapshot {i-1} and snapshot {i}.")

    # Add the new elements to the final array
    final_array.extend([value for value in snapofsnaps[i] if value not in final_array])

# The final array is now a single, flat, deduplicated array of all the snapshots
# Write the final array to flattened-thread.json
with open("flattened-thread.json", "w") as outfile:
    json.dump(final_array, outfile)

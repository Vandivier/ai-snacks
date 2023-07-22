# Importing required libraries
import re
import pandas as pd

# Reading the file
with open("/mnt/data/raw-thread-text.txt", "r") as file:
    text = file.read()

# Defining the patterns to match
time_patterns = [
    (r"(\d+)\s*(day|week|month|year)", ["day", "week", "month", "year"]),
    (r"(a|an|one)\s*(day|week|month|year)", ["day", "week", "month", "year"]),
    (
        r"(couple|few|several)\s*(days|weeks|months|years)",
        ["days", "weeks", "months", "years"],
    ),
]

# Categories of responses
categories = {
    "learning": [
        "learn",
        "study",
        "self-taught",
        "teach",
        "course",
        "tutorial",
        "book",
    ],
    "job": [
        "job",
        "work",
        "career",
        "profession",
        "hire",
        "employed",
        "employment",
        "interview",
    ],
}


# Function to convert time expressions to days
def convert_to_days(match):
    num, unit = match
    if num in ["a", "an", "one"]:
        num = 1
    elif num == "couple":
        num = 2
    elif num in ["few", "several"]:
        num = 3
    if unit.startswith("day"):
        return int(num)
    elif unit.startswith("week"):
        return int(num) * 7
    elif unit.startswith("month"):
        return int(num) * 30
    elif unit.startswith("year"):
        return int(num) * 365


# Extracting the durations and categorizing them
durations = {"learning": [], "job": []}
for pattern, units in time_patterns:
    for unit in units:
        matches = re.findall(pattern.replace("unit", unit), text, re.IGNORECASE)
        for match in matches:
            duration = convert_to_days(match)
            if any(word in text for word in categories["learning"]):
                durations["learning"].append(duration)
            if any(word in text for word in categories["job"]):
                durations["job"].append(duration)

# Creating a dataframe
df = pd.DataFrame(durations)

# Saving the dataframe to a CSV file
df.to_csv("/mnt/data/durations.csv", index=False)

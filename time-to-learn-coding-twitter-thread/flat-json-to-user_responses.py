import json
import pandas as pd
import re


# Function to convert time expressions to days
def convert_to_days(match):
    if len(match) == 3:  # If the match is a range
        min_num, max_num, unit = match
        min_num = int(min_num)
        max_num = int(max_num)
    else:  # If the match is a single duration
        min_num = max_num = int(match[0])
        unit = match[1]

    if unit.startswith("day"):
        return min_num, max_num, (min_num + max_num) / 2
    elif unit.startswith("week"):
        return min_num * 7, max_num * 7, (min_num + max_num) / 2 * 7
    elif unit.startswith("month"):
        return min_num * 30, max_num * 30, (min_num + max_num) / 2 * 30
    elif unit.startswith("year"):
        return min_num * 365, max_num * 365, (min_num + max_num) / 2 * 365


# Defining the pattern to match username
pattern = r"@(\w+)"

# Load the JSON data
with open("flattened-thread.json", "r") as file:
    tweets = json.load(file)

# Extracting the usernames and responses
data = []
for tweet in tweets:
    match = re.search(pattern, tweet)
    if match:
        username = match.group(1)
        # Remove the username from the tweet
        response_text = tweet.replace("@" + username, "").strip()
        data.append({"username": username, "response": response_text})

# Creating a dataframe
df = pd.DataFrame(data)

# Defining the patterns to match durations
time_patterns = [
    (
        r"(\d+)-(\d+)\s*(day|week|month|year)",
        ["day", "week", "month", "year"],
    ),  # Matches ranges like "3-6 months"
    (
        r"(\d+)\s*(day|week|month|year)",
        ["day", "week", "month", "year"],
    ),  # Matches single durations like "3 months"
]

# Categories of interest
categories = {
    "learning": ["learn", "study", "master", "understand"],
    "job": ["job", "hire", "work", "profession", "career"],
}

# Extracting the durations and categorizing them
for i, row in df.iterrows():
    response = row["response"]
    durations = {"learning": [], "job": []}
    for pattern, units in time_patterns:
        for unit in units:
            matches = re.findall(pattern.replace("unit", unit), response, re.IGNORECASE)
            for match in matches:
                min_duration, max_duration, point_estimate = convert_to_days(match)
                if any(word in response.split() for word in categories["learning"]):
                    durations["learning"].append(
                        (min_duration, max_duration, point_estimate)
                    )
                if any(word in response.split() for word in categories["job"]):
                    durations["job"].append(
                        (min_duration, max_duration, point_estimate)
                    )
    # Adding the durations to the dataframe
    if durations["learning"]:
        (
            df.at[i, "learning_min"],
            df.at[i, "learning_max"],
            df.at[i, "learning_point_estimate"],
        ) = durations["learning"][0]
    else:
        (
            df.at[i, "learning_min"],
            df.at[i, "learning_max"],
            df.at[i, "learning_point_estimate"],
        ) = (None, None, None)
    if durations["job"]:
        (
            df.at[i, "job_min"],
            df.at[i, "job_max"],
            df.at[i, "job_point_estimate"],
        ) = durations["job"][0]
    else:
        df.at[i, "job_min"], df.at[i, "job_max"], df.at[i, "job_point_estimate"] = (
            None,
            None,
            None,
        )

# Saving the dataframe to a CSV file
df.to_csv("user_responses.csv", index=False)

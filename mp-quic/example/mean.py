# Re-run the calculation due to an internal issue.

# List of times in the format "XmY.ZZZs"
# Defines the path to the log file
log_file_path = 'client_benchmarker/result.log'

# Initialize an empty list to store time data
times = []

# Open the file and read each line
with open(log_file_path, 'r') as file:
    for line in file:
        # Remove the newline character from the end of the line and check if the line is not empty
        clean_line = line.strip()
        if clean_line:
            # Add the cleaned lines to a list
            times.append(clean_line)

# Convert times to total seconds
total_seconds = []
for time_str in times:
    minutes, seconds = time_str.split('m')
    seconds = seconds[:-1]  # Remove the 's' at the end
    total_seconds.append(int(minutes) * 60 + float(seconds))

# Sort the list and remove the shortest and the longest time
total_seconds_sorted = sorted(total_seconds)
if len(total_seconds_sorted) > 2:
    modified_total_seconds = total_seconds_sorted[1:-1]  # Remove the smallest and the largest value
else:
    modified_total_seconds = total_seconds_sorted  # Do not remove any item if there are only two or fewer elements

# Calculate the average time in seconds from the modified list
average_seconds = sum(modified_total_seconds) / len(modified_total_seconds)

# Convert the average time back to the original format "XmY.ZZZs"
avg_minutes = int(average_seconds // 60)
avg_seconds = average_seconds % 60
average_time_format = f"{avg_minutes}m{avg_seconds:.3f}s"

print("\nAverage\n" + average_time_format)

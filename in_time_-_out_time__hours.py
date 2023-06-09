import datetime

# Same Day Time Duration calculator
in_time_input = input("Enter the in time in hours and minutes (e.g., 9:30 AM): ")
out_time_input = input("Enter the out time in hours and minutes (e.g., 9:30 PM): ")

try:
    in_time = datetime.datetime.strptime(in_time_input, "%I:%M %p")
    out_time = datetime.datetime.strptime(out_time_input, "%I:%M %p")

    # Calculate the duration
    duration = out_time - in_time

    # Convert duration to hours and minutes
    duration_hours = duration.seconds // 3600
    duration_minutes = (duration.seconds // 60) % 60

    # Print the duration
    print("Duration: {} hours {} minutes".format(duration_hours, duration_minutes))

except ValueError:
    print("Invalid input. Please enter the time in the correct format.")

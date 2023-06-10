# Time Tracker @ Work
## Program 1: Total Time Calculator
This program calculates the total time entered and the remaining time you can work based on user input. It prompts the user to enter hours and minutes until they choose to stop entering. After that, it calculates the total time entered and compares it to the desired work hours to determine the remaining time available for work.

## How to Use
1. Run the program.
2. Enter the hours and minutes worked each time prompted. To stop entering, type 'q' and press Enter.
3. The program will display the total time entered.
4. Enter the desired work hours in the specified format.
5. The program will calculate and display the remaining time available for work.

## Example
```py 
Enter hours and minutes (or 'q' to stop entering): 2 30 
Enter hours and minutes (or 'q' to stop entering): 1 45
Enter hours and minutes (or 'q' to stop entering): q
Total time entered: 4 hours and 15 minutes
Enter the number of hours you are supposed to work: 8 0
Remaining time you can work: 3 hours and 45 minutes
```

## Program 2: Time Tracker
This program helps track time by calculating the out time based on the in time and the number of hours to work. It prompts the user to enter the in time (arrival time) and the number of hours to work. It then calculates the out time by adding the in time and the work hours.

## How to Use
1. Run the program.
2. Enter the in time in hours and minutes using the specified format (e.g., 9 30 for 9:30 AM).
3. Enter the number of hours to work.
4. The program will calculate and display the out time.

## Example

```py
Enter the in time in hours and minutes (e.g., 9 30 for 9:30 AM): 9 30
Enter the number of hours to work: 8 0
Out time: 17:30
```

## Program 3: Same Day Duration Calculator

This Python code calculates the duration between two inputted times within the same day. It takes user input for the start time (in_time_input) and end time (out_time_input), and then computes the duration between them.

## Usage
1. Run the script in a Python environment.
2. Enter the start time in the format "hours:minutes AM/PM" when prompted (e.g., 9:30 AM).
3. Enter the end time in the same format when prompted (e.g., 9:30 PM).
4. The script will calculate and display the duration in hours and minutes.

## Example
```py
Enter the in time in hours and minutes (e.g., 9:30 AM): 10:45 AM
Enter the out time in hours and minutes (e.g., 9:30 PM): 2:30 PM
Duration: 3 hours 45 minutes
```

## Executable creation
```pyinstaller --onefile .\in_time_-_out_time__hours.py``` <br>
```pyinstaller --onefile in_out_time.py``` <br>
```pyinstaller --onefile hours_counter.py``` <br>
# Countdown-timer
Basic count down timer using python 
The countdown_clock function takes in an integer argument, seconds, which represents the number of seconds for the countdown. The function uses a for loop to count down from the number of seconds to 0, printing the current count each second and using the time.sleep(1) function to pause the program for 1 second before the next iteration. Once the countdown reaches 0, the function prints "Time's up!"

The timer function takes in an integer argument, minutes, which represents the number of minutes for the timer. The function uses time.sleep(minutes * 60) to pause the program for the number of minutes specified, then it calculates the time elapsed between the start and end of the timer by subtracting the start_time from end_time and calculates the time in seconds.

Both of these functions can be used together or separately, depending on the use case.

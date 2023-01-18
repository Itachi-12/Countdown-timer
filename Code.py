import time

# Function to create a countdown clock
def countdown_clock(seconds):
    for i in range(seconds, 0, -1):
        print(i)
        time.sleep(1)
    print("Time's up!")

# Function to create a timer
def timer(minutes):
    start_time = time.time()
    time.sleep(minutes * 60)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Time elapsed: {:.2f} seconds.".format(elapsed_time))

# Example usage of the countdown clock and timer
countdown_clock(5)
print("Starting timer...")
timer(3)

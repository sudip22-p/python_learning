import threading
import time


# ✅ A function that prints numbers with a delay
def print_numbers():
    for i in range(5):
        print(f"Thread 1: {i}")
        time.sleep(1)  # Simulates a time-consuming task


# ✅ A function that prints letters with a delay
def print_letters():
    for ch in "ABCDE":
        print(f"Thread 2: {ch}")
        time.sleep(1)


# ✅ Create two threads that will run the above functions
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

# ✅ Start both threads (they will run concurrently)
t1.start()
t2.start()

# ✅ Wait for both threads to complete before continuing
t1.join()
t2.join()

print("Both threads finished.")  # Final print after both threads are done

# threading lets you run multiple functions at the same time (in parallel).

# Ideal for tasks like network calls, file I/O, or waiting operations.

# start() starts the thread; join() blocks until it’s done.

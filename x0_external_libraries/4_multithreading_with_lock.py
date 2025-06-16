import threading

# Shared resource
counter = 0

# Lock object
lock = threading.Lock()


# ❌ Function without using Lock (unsafe)
def increment_without_lock():
    global counter
    for _ in range(100000):
        counter += 1  # Not thread-safe — race condition may occur


# ✅ Function using Lock (safe)
def increment_with_lock():
    global counter
    for _ in range(100000):
        with lock:  # Only one thread can enter this block at a time
            counter += 1  # Thread-safe increment


# ------------ Run WITHOUT Lock ------------
# Reset counter
counter = 0

# Create threads (unsafe)
t1 = threading.Thread(target=increment_without_lock)
t2 = threading.Thread(target=increment_without_lock)

t1.start()
t2.start()
t1.join()
t2.join()

print("❌ Without Lock — Counter:", counter)  # Likely < 200000 due to race condition


# ------------ Run WITH Lock ------------
# Reset counter
counter = 0

# Create threads (safe)
t3 = threading.Thread(target=increment_with_lock)
t4 = threading.Thread(target=increment_with_lock)

t3.start()
t4.start()
t3.join()
t4.join()

print("✅ With Lock — Counter:", counter)  # Always 200000


# Getting 200000 without Lock is possible but not guaranteed.

# It’s a flaky result — not thread-safe.

# Use Lock when multiple threads modify shared data.

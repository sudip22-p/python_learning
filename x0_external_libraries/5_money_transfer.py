# a triangular money transfer system using threads and a Lock, where:

# Alice → Bob

# Bob → Charlie

# Charlie → Alice

# All transfers happen safely with thread synchronization.
import threading
import time

# Shared user balances
accounts = {"Alice": 1000, "Bob": 800, "Charlie": 600}

# Lock to ensure thread-safe balance updates
lock = threading.Lock()


# Function to transfer money from one user to another
def transfer_money(sender, receiver, amount):
    with lock:
        print(f"{sender} wants to send ₹{amount} to {receiver}")
        print("checking the balance availability........")

        # Check balance before transferring
        if accounts[sender] >= amount:
            print("Balance available transferring money..........")
            time.sleep(1)  # Simulate transaction delay
            accounts[sender] -= amount
            accounts[receiver] += amount
            print(f"✅ {sender} sent ₹{amount} to {receiver}")
        else:
            print(f"❌ {sender} has insufficient balance.")
            print("Transaction failed !!")

        # Show updated balances
        print(
            f"Balances → Alice: ₹{accounts['Alice']}, Bob: ₹{accounts['Bob']}, Charlie: ₹{accounts['Charlie']}\n"
        )


# Create 3 threads for triangle transfer
t1 = threading.Thread(target=transfer_money, args=("Alice", "Bob", 300))
t2 = threading.Thread(target=transfer_money, args=("Bob", "Charlie", 200))
t3 = threading.Thread(target=transfer_money, args=("Charlie", "Alice", 100))

# Start all transfers simultaneously
t1.start()
t2.start()
t3.start()

# Wait for all to finish
t1.join()
t2.join()
t3.join()

# Final result
print("🏁 Final Balances:", accounts)


# Why Lock?
# Threads run concurrently, so without a Lock, multiple threads may access and modify the same account at once, causing inconsistent balances.

# With lock, only one thread modifies balances at a time, ensuring data integrity.

import time

print("Starting critical analytics job...")
time.sleep(3)
print("Connecting to database...")
raise Exception("Connection timeout: Unable to reach analytics DB after 30s")
import time

print("Running long computation...")
time.sleep(300)  # 5 minutes - you can set job timeout lower to trigger timeout failure
print("Done")
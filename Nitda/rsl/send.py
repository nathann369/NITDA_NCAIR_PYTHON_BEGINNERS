import time
# from message_the_ladies import snap_id 

def run_snap(snap_id: str, message: str) -> bool:
    print("Getting you signed in snapchat")
    time.sleep(1)
    print("Connecting to your account...")
    time.sleep(1)
    print(f"Sending Message to {snap_id} ......")
    time.sleep(1)
    print("Done ✅")
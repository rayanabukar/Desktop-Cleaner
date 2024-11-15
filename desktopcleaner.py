import os
import time
import shutil # Used to move files between directories

folder_to_track = "/mnt/chromeos/MyFiles/Downloads/myFolder"  
destination_folder = "/mnt/chromeos/MyFiles/Downloads/newFolder"

print("Starting polling...")
while True:
    try:
        for filename in os.listdir(folder_to_track):  # Loop through each file in the folder_to_track
            file_path = os.path.join(folder_to_track, filename) # Construct the full path to the file in folder_to_track
            new_destination = os.path.join(destination_folder, filename) # Construct the full path to where the file will be moved in destination_folder

            if os.path.isfile(file_path):  # Check if the current item is a file (and not a directory)
                shutil.move(file_path, new_destination) # Move the file from folder_to_track to destination_folder
                print(f"Moved {filename} to {destination_folder}") # Print confirmation that the file was moved

        time.sleep(5)  # Poll every 5 seconds
    except KeyboardInterrupt: # Handle when the user interrupts the script (e.g., with Ctrl+C)
        print("Stopping polling.")
        break
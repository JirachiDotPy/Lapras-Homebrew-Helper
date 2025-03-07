# written by JirachiDotPy on github
# last updated March 7 2025

from colorama import Fore, init
import time
import os
import platform
import requests # allows for native file downloads no matter what OS the user is running on

# initializing colorama module
init()

# needed lists and variables
menu_options = [
                "[1] - CONSTRUCT DIRECTORIES",
                "[2] - SUPER-SKATERHAX (SSH)",
                "[3] - X_FINALIZE_HELPER.FIRM",
                "[4] - FINALIZE.ROMFS",
                "[5] - MSET9 ZIP",
                "[6] - EXIT"
                ]
user_os_simple = "" # temporary value
download_path = "Lapras/Downloads"
download_path2 = "Lapras/NAND Backup"

ssh_name = "SUPER-SKATERHAX"
xfhfirm_name = "X_FINALIZE_HELPER.FIRM"
finalize_romfs_name = "FINALIZE.ROMFS"
mset9_zip_name = "MSET9 ZIP"

ssh_output = "Super-skaterhax-usa-v11.17.zip"
xfhfirm_output = "x_finalize_helper.firm"
finalize_romfs_output = "finalize.romfs"
mset9_zip_output = "MSET9-v2.0.zip"

ssh_link = "https://hacksguidewiki.sfo3.digitaloceanspaces.com/hacksguidewiki/Super-skaterhax-usa-v11.17.zip"
xfhfirm_link = "https://github.com/hacks-guide/finalize/releases/latest/download/x_finalize_helper.firm"
finalize_romfs_link = "https://github.com/hacks-guide/finalize/releases/latest/download/finalize.romfs"
mset9_zip_link = "https://github.com/hacks-guide/MSET9/releases/download/v2.0/MSET9-v2.0.zip"
readme_txt_link = "https://github.com/JirachiDotPy/Lapras-Homebrew-Helper/blob/main/read.txt"

# function that detects what OS the user is running on
def os_detector():
    global user_os_simple

    try:
        print("Running os_detector...") # debug message
        user_os = platform.system()
        print(f"Detected OS: {user_os}")
        print(Fore.GREEN + '[OK]' + Fore.RESET + " OPERATING SYSTEM DETECTED: " + user_os)

        # updating the global user_os_simple value according to what OS the user is running on
        # this determines what CLI commands will be used throughout the program
        if "Windows" in user_os:
            time.sleep(1)
            os.system('cls')
            user_os_simple = "Windows"

        elif "Linux" in user_os:
            time.sleep(1)
            os.system('clear')
            user_os_simple = "Linux"

        elif "Darwin" in user_os:
            time.sleep(1)
            os.system('clear')
            user_os_simple = "MacOS"

    except Exception as common_error: # debugging
        print(f"Error in os_detector: {common_error}")

# function for downloading the file tools that has parameters to work with any tool
def file_install(filename, url, output_path):
    global user_os_simple

    try:

        # clearing the terminal specific to OS
        if user_os_simple == "Linux":
            os.system('clear')

        elif user_os_simple == "Windows":
            os.system('cls')

        elif user_os_simple == "MacOS":
            os.system('clear')

        # defining the download directory
        download_path = "Lapras/Downloads"
        os.makedirs(download_path, exist_ok=True) # creating the dir path if it doesn't already exist

        full_output_path = os.path.join(download_path, output_path)

        print(f"Downloading {filename}...")
        response = requests.get(url, stream=True)
        response.raise_for_status() # raises an error for any bad status codes

        # downloading the file to the directory
        with open(full_output_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(Fore.GREEN + '[DONE]' + Fore.RESET + f" {filename} downloaded to {full_output_path}!")
        time.sleep(3)

    except requests.exceptions.RequestException as common_error:
        print(Fore.RED + '[ERROR]' + Fore.RESET + f" Failed to download {filename}: {common_error}")

    except KeyboardInterrupt:
        print("\n")
        print(Fore.RED + '[SYSTEM]' + Fore.RESET + f" CTRL + C detected: {filename} download has been terminated.")
        time.sleep(2)
        print(Fore.BLUE + '[EXITING]' + Fore.RESET + "Goodbye!")
        time.sleep(2)

# user interface function to display interactive menu
def menu():
    global user_os_simple
    global user_choice

    while True:
        
        try:
            if user_os_simple == "Linux":
                os.system('clear')

            elif user_os_simple == "Windows":
                os.system('cls')

            elif user_os_simple == "MacOS":
                os.system('clear')

            print("                             🌊 LAPRAS - 3DS HOMEBREW HELPER 🌊")
            time.sleep(2)
            print("Welcome to LAPRAS.\n")
            time.sleep(1)

            for option in menu_options:
                print(option)

            print("\nPlease input below the corresponding number of the tool you'd like to install:")
            user_choice = int(input('>>>'))

            implementation() # processing the user's choice

        except Exception as common_error:
            print("\n" + Fore.RED + '[ERROR]' + Fore.RESET + f" System error: {common_error}")
            print(Fore.RED + '[ERROR]' + Fore.RESET + " Make sure you are connected to the internet.")
            print(Fore.RED + '[ERROR]' + Fore.RESET + " Please try again.")
            time.sleep(3)
            continue

        except KeyboardInterrupt:
            print("\n" + Fore.RED + '[SYSTEM]' + Fore.RESET + " CTRL + C detected.")
            time.sleep(2)
            print(Fore.BLUE + '[EXITING]' + Fore.RESET + " Goodbye!")
            break

        except ValueError:
            print("\n" + Fore.RED + '[ERROR]' + Fore.RESET + " Please enter a valid number.")
            time.sleep(2)
            continue

# user's choice is now put into use depending on what they chose
def implementation():
    global user_choice
    global user_os_simple
    user_choice = int(user_choice)

    # command to create the LAPRAS directory where all downloads will be stored
    # this action is nondependent from the user's OS thanks to the os module's cross-compatability
    if user_choice == 1:
        os.makedirs("Lapras/Downloads", exist_ok=True) # ensures that errors are avoided if the dir already exists
        print("\n" + Fore.GREEN + '[DONE]' + Fore.RESET + " Lapras/Downloads directory created!")
        os.makedirs("Lapras/NAND Backup", exist_ok=True) # ensures that errors are avoided if the dir already exists
        print(Fore.GREEN + '[DONE]' + Fore.RESET + " Lapras/NAND Backup directory created!")
        
        # defining the content for the read.txt file
        readtxt_content = """
                # this file should be located in /Lapras/NAND Backup upon constructing the directories
                This is the NAND Backup folder. 
                It should be empty, and that is because this is the directory where you should store your Nintendo 3DS NAND files (.bin, .sha, .exefs)
                Please move this directory to a secure location or a cloud backup drive (Google Drive, Dropbox).

                Thank you for using Lapras, happy modding!
                """
        
        # creating the read.txt file and defining its contents
        read_file_path = os.path.join("Lapras/NAND Backup", "read.txt")
        try:
            with open(read_file_path, "w") as file:
                file.write(readtxt_content)
            print(Fore.GREEN + '[DONE]' + Fore.RESET + f" read.txt file created at {read_file_path}!")
        
        except Exception as common_error:
            print(Fore.RED + '[ERROR]' + Fore.RESET + f" Failed to create read.txt: {common_error}")
        
        # important message
        print(Fore.YELLOW + '[SYSTEM]' + Fore.RESET + " IMPORTANT: MOVE Lapras/NAND Backup to a safe place "
                  "once you've backed up your NAND bin, hash, and exefs to the directory.")

        time.sleep(5)
        return

    elif user_choice == 2:
        file_install(ssh_name, ssh_link, ssh_output)
        return

    elif user_choice == 3:
        file_install(xfhfirm_name, xfhfirm_link, xfhfirm_output)
        return

    elif user_choice == 4:
        file_install(finalize_romfs_name, finalize_romfs_link, finalize_romfs_output)
        return

    elif user_choice == 5:
        file_install(mset9_zip_name, mset9_zip_link, mset9_zip_output)
        return

    elif user_choice == 6:
        time.sleep(2)
        print("\n" + Fore.BLUE + '[SYSTEM]' + Fore.RESET + " Goodbye!")
        time.sleep(2)  
        # commmand to exit the terminal is universal across Linux, MacOS, and Windows
        os.system('exit')
        exit()

    else:
        print("\n" + Fore.RED + "[ERROR]" + Fore.RESET + "Please choose a valid input.")
        return

os_detector()    
menu()

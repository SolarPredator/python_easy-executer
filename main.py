import os
import sys
import subprocess
import keyboard
import time
import configparser
files_found = ""
path = ""
Select = ""
custom_path = ""
python_path = ""
main_path = ""
found ="hello"
loc2 = ""  #short for location 2
item_count = 0
system = ""
folder_number = 1
clear_command = ""
to_send = ""
bat_files = []
py_files = []
execute_menu_items = []
current_ = []
current_list = []

files_found_list = []


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'




def has_batch(to_check):
    global found, custom_path, current_list, to_send
    last = os.getcwd()

    current = to_check
    current_ = os.scandir()
    for item3 in current_:

      if (item3.is_dir() and item3.name == to_check):
        current_list = []
        current_list.append(item3.name)

    for item in current_list:
        os.chdir(item)
        current2 = os.scandir()

        for item2 in current2:

          if item2.name.endswith(".bat"):
              found = (bcolors.OKGREEN + "BAT FILE FOUND" + bcolors.ENDC)
              time.sleep(0.1)
              to_send = os.path.join(to_check, found)
              os.chdir(rf"{last}")
              return to_send
              break
          else:
              found = (bcolors.FAIL +"NO BAT FILE FOUND" + bcolors.ENDC)
          to_send = os.path.join(to_check, found)
          os.chdir(rf"{last}")
    return to_send






def check_platform():
    global system
    if sys.platform.startswith('linux'):
        return "linux"
    elif sys.platform.startswith('win'):
        return "Windows"
    else:
        print("ERROR: Unkown system")
        quit()



if check_platform() == "linux":
    clear_command = "clear"
elif check_platform() == "Windows":
    clear_command = "cls"
else:
    print("could not optimize the program for you're operation system")
    quit()

def config_file_setup():
    global path, custom_path, python_path, main_path, system
    print("ERROR: CONFIG FILE NOT FOUND.")
    print("DO YOU WANT TO CREATE A CONFIG FILE?\nY/N")
    while True:

      if (keyboard.is_pressed("Y") or keyboard.is_pressed("y")):
          subprocess.run(clear_command, shell=True)
          python_path = input("python.exe path: ")
          main_path = os.getcwd()
          path = input("\n\nuse custom(beta) or Default path?  C/D \n")
          if path.lower() == "c":
              path = "custom"
              custom_path = input("please input manual path. Refer to readme or the github page for help:\n")

          elif path.lower() =="d":
              path = "default"
          time.sleep(2)
          if os.path.exists("main.py") == True:
              print("creating file...")
              with open("config.txt", "w") as config_file:
                  config_file.write(f'[setup]\npath = {path}\ncustom_path = {custom_path}\npython_path = {python_path}\nmain_path = {main_path}\noperation_system = {check_platform()}')
              if os.path.exists("config.txt") == True:
                  print("Done!\nThe program needs to create a batch file for it to work. If not automaticly started in 5 seconds, restart the program")
                  time.sleep(5)
                  return None



if os.path.exists("config.txt") == False:
    config_file_setup()

elif os.path.exists("config.txt") == True:
   config = configparser.ConfigParser()
   config.read_file(open(r'config.txt'))
   path = config.get('setup', 'path')
   python_path = config.get("setup", "python_path")
   main_path = config.get("setup", "main_path")
   system = config.get("setup", "operation_system")

else:
    print("ERROR FINDING STATE OF config.txt")
    quit()


if (os.path.exists("start.bat") == False or path == "default" and not os.path.exists("FILES")): #if the program does not find the start.bat file, it will ask the user to create one

    if os.path.exists("start.bat") == False:   #check if the start.bat file is present
      loc1 = python_path
      loc2 = main_path
      os.chdir(loc2)

      if os.path.exists("main.py") == True and os.path.exists("start.bat")== False:
          print("\n" * 10)
          print("creating batch file...")

          with open("start.bat","w") as batch_file:
              batch_file.write(f'@echo off\n"{loc1}" "{loc2}\main.py"\npause')
          if os.path.exists("start.bat") == True:
              print("Done.")
          else:
              print("ERROR: SOMETHING HAPPEND WHEN CREATING THE start.bat FILE")
              quit()
    if os.path.exists("FILES") == False:
        print("FILES folder missing. Creating. This folder is not used if config path = custom")
        time.sleep(3)
        print("Creating...")
        time.sleep(2)
        os.mkdir("FILES")
        if os.path.exists("FILES"):
            print("Done. Starting main executer")

    time.sleep(5)
    os.startfile("start.bat")
    quit()

def create_bat(file):
    global python_path, py_files


    loc1 = python_path
    os.chdir(file)
    current = os.getcwd()  # get current dir
    current_files = os.scandir()

    folder_number = 1
    files_found = os.listdir(path=None)
    py_files = []
    for item in os.scandir():
        if item.is_file():
            if item.name.endswith(".py"):
              py_files.append(item.name)

    if len(py_files) > 1:
        print("ERROR: Multiple python files found")
        for py_file in py_files:
            print(py_file)
        quit()
    print("Found .py files:")
    for py_files in py_files:
        print(py_files)
        time.sleep(2)
        print("\ncreating batch file...")
        time.sleep(0.5)
        with open("start.bat", "w") as batch_file:
            batch_file.write(f'@echo off\n"{loc1}" "{os.getcwd()}\{py_files}"\npause')
        if os.path.exists("start.bat") == True:
            print("Done.")
        else:
            print("ERROR: SOMETHING HAPPEND WHEN CREATING THE start.bat FILE")
            quit()


def create_menu():
    global files_found, clear_command, item_count, Select, py_files
    item = 0
    subprocess.run(clear_command, shell=True)
    print("#" * 20)
    print("    EASY EXECUTE")
    print("#" * 20)
    print("0.BACK")
    # Here check for files #
    custom_path = config.get('setup', 'custom_path')
    print(f"FILES FOUND IN: {custom_path}:")
    folder_number = 1


    if path == "default":
        os.chdir("FILES")
    elif path == "custom":
        os.chdir(rf"{custom_path}")
    else:
        print("ERROR:7 ")
        quit()
    files_found = os.listdir(path=None)
    py_files = []
    for item in files_found:

        if os.path.isdir(item):
            py_files.append(item)
            item_count = 0
    for item in py_files:

        print(f"{folder_number}.{py_files[item_count]}")
        folder_number = folder_number + 1
        item_count = item_count + 1
        time.sleep(0.1)
    while True:
        time.sleep(0.5)
        Select = keyboard.read_key()
        if Select != "":
            if Select.isdigit():
                Select = int(Select)
                files_found = py_files
                if 1 <= Select <= len(files_found):
                    selected_file = files_found[Select - 1]
                    print(f"You selected {selected_file}\n")
                    create_bat(selected_file)
                elif Select == 0:
                    main_menu()

def open_file(file):
    global files_found, folder_number, custom_path, path

    if path == "default":
      program_path = os.path.join("FILES", file)
    elif path == "custom":
        program_path = os.path.join(custom_path, file)

    os.chdir(program_path)
    files_found = os.listdir(path=None)

    for item in files_found:

        if os.path.isfile(item) and item.lower().endswith(".bat"):
            bat_files.append(item)

    if len(bat_files) > 1:
        print("ERROR: Multiple batch files found")
        for bat_file in bat_files:
            print(bat_file)
        quit()
    print("Found .bat files:")
    for bat_file in bat_files:
        print(bat_file)
    print(f"starting: {bat_file}")
    os.startfile(bat_file)
    quit()
def execute_menu():
    global custom_path, path, execute_menu_items,clear_command
    # Create the CLI gui
    subprocess.run(clear_command,shell=True)
    print("#" * 20)
    print("    EASY EXECUTE")
    print("#" * 20)
    print("0.BACK")
    # Here check for files #


    current = os.getcwd()  # get current dir



    custom_path = config.get('setup', 'custom_path')
    if path == "default":
      os.chdir("FILES")
    elif path == "custom":
        os.chdir(rf"{custom_path}")

    print(f"FILES FOUND IN(execute) {os.getcwd()}:")
    folder_number = 1
    for item in os.scandir():
        global Select
        if item.is_dir():
          print(f"{folder_number}.{has_batch(item.name)}")
          folder_number = folder_number + 1
    while True:
      time.sleep(1)
      Select = keyboard.read_key()
      if Select != "":
        if Select.isdigit():
            Select = int(Select)
            has_batch(custom_path)
            files_found = os.scandir()

            for files_found in files_found:

                if files_found.is_dir():
                    files_found_list.append(files_found.name)


            if 1 <= Select <= len(files_found_list):
                selected_file = files_found_list[Select - 1]
                print(f"You selected {selected_file}\n")
                open_file(selected_file)

            elif Select == 0:
                main_menu()
        else:
            print("ERROR:5")
            quit()

    # give options here #

    while True:
      if keyboard.is_pressed("0"):
          main_menu()


def main_menu():
    global clear_command
    #Create the CLI gui
    subprocess.run(clear_command, shell=True)
    print("#" * 20)
    print("    EASY EXECUTE")
    print("#" * 20)
    print("1.EXECUTE BATCH FILE")
    print("2.CREATE BATCH FILE")
    #finished creating the CLI gui

    while True:
       #start listening for a key press
       if keyboard.is_pressed("1"):
           execute_menu()
       elif keyboard.is_pressed("2"):
           create_menu()


check_platform()
main_menu()
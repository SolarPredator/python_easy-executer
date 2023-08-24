import os
import sys
import subprocess
import keyboard
import time
files_found = ""
Select = ""
folder_number = 1
bat_files = []
py_files = []
if (os.path.exists("start.bat") == False or os.path.exists("FILES") == False): #if the program does not find the start.bat file, it will ask the user to create one

    if os.path.exists("start.bat") == False:   #check if the start.bat file is present: line 11-27
      print("For the program to work propperly, There's a few steps you need to do first")
      loc1 = input("full python.exe location: ")
      loc2 = input("full easy_execute location. Must be \easy_execute")

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
        print("FILES folder missing. Create or select you're own path\nCreate/Select")

        while True:
          if keyboard.is_pressed("s"):
              print("chose to select a path")
              quit()
          elif keyboard.is_pressed("c"):
              print("Creating...")
              time.sleep(2)
              os.mkdir("FILES")
              if os.path.exists("FILES"):
                  print("Done. Starting main executer")
                  break
    time.sleep(5)
    os.startfile("start.bat")
    quit()

def create_bat(file):
    loc1 = input("full python.exe location: ")
    program_path = os.path.join("FILES", file)
    os.chdir(program_path)
    files_found = os.listdir(path=None)

    for item in files_found:
        global py_files
        if os.path.isfile(item) and item.lower().endswith(".py"):
            py_files.append(item)

    if len(bat_files) > 1:
        print("ERROR: Multiple python files found")
        for py_file in py_files:
            print(py_file)
        quit()
    print("Found .py files:")
    for py_files in py_files:
        print(py_files)
        time.sleep(2)
        print("creating batch file...")
        with open("start.bat", "w") as batch_file:
            batch_file.write(f'@echo off\n"{loc1}" "{os.getcwd()}\{py_files}"\npause')
        if os.path.exists("start.bat") == True:
            print("Done.")
        else:
            print("ERROR: SOMETHING HAPPEND WHEN CREATING THE start.bat FILE")
            quit()


def create_menu():
    subprocess.run('cls', shell=True)
    print("#" * 20)
    print("    EASY EXECUTE")
    print("#" * 20)
    print("0.BACK")
    # Here check for files #

    print("FILES FOUND:")
    folder_number = 1
    files_found = os.listdir(path="FILES")
    for files_found in files_found:
        global Select

        print(f"{folder_number}.{files_found}")
        folder_number = folder_number + 1
    while True:
        time.sleep(1)
        Select = keyboard.read_key()
        if Select != "":
            if Select.isdigit():
                Select = int(Select)
                files_found = os.listdir(path="FILES")
                if 1 <= Select <= len(files_found):
                    selected_file = files_found[Select - 1]
                    print(f"You selected {selected_file}\n")
                    create_bat(selected_file)


def open_file(file):
    global files_found, folder_number
    program_path = os.path.join("FILES", file)
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
    # Create the CLI gui
    subprocess.run('cls',shell=True)
    print("#" * 20)
    print("    EASY EXECUTE")
    print("#" * 20)
    print("0.BACK")
    # Here check for files #

    print("FILES FOUND:")
    folder_number = 1
    files_found = os.listdir(path="FILES")
    for files_found in files_found:
        global Select

        print(f"{folder_number}.{files_found}")
        folder_number = folder_number + 1
    while True:
      time.sleep(1)
      Select = keyboard.read_key()
      if Select != "":
        if Select.isdigit():
            Select = int(Select)
            files_found = os.listdir(path="FILES")
            if 1 <= Select <= len(files_found):
                selected_file = files_found[Select - 1]
                print(f"You selected {selected_file}\n")
                open_file(selected_file)

            else:
                print("ERROR")
                quit()
        else:
            print("ERROR")
            quit()

    # give options here #

    while True:
      if keyboard.is_pressed("0"):
          main_menu()


def main_menu():
    #Create the CLI gui
    subprocess.run('cls', shell=True)
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

main_menu()
import os
import getpass
import shutil

def is_app_running(app_name):
    try:
        output = os.popen(f'tasklist | findstr /I "{app_name}"').read()
        
        return app_name.lower() in output.lower()
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

if is_app_running("VIVIDSTASIS.exe") == True:
    Q = str(input("vivid/stasis is currently running! You can continue, but the save file will NOT apply until you reboot! \n Do you want to close the game? (Any unsaved data will be lost! ...I doubt you're in an episode rn though..) \n Y/n \n"))
    if Q == "Y" or Q == "y" or Q == "":
        os.system("@echo off | TASKKILL /F /IM VIVIDSTASIS.exe")
    else:
        pass

try:
    os.system("cls")
    user = os.environ.get("USERNAME")
    path = f"C:/Users/{user}/Appdata/Local/vividstasisSaveSelector"
    os.mkdir(path)
    path = f"{path}/Save1"
    os.mkdir(path)
    path = f"{path}/../Save2"
    os.mkdir(path)
    path = f"{path}/../Save3"
    os.mkdir(path)
    path = f"{path}/../Save4"
    os.mkdir(path)
    path = f"C:/Users/{user}/Appdata/Local/vividstasisSaveSelector"
    print("Seems like you're launching the script for the first time!")
    print("I've gone ahead and created the folder to store your saves in!")
    print(f"(Its located at {path}!)")
    getpass.getpass("Press Enter to continue! \n")
    os.system("cls")
except FileExistsError:
    pass

def menu(option):
    if option == "1":
        os.system("cls")
        swapsave()
    elif option == "2":
        os.system("cls")
        overwrite()
    elif option == "3":
        os.system("cls")
        erase()
    elif option == "4":
        os.system("cls")
        exit("Exiting...")
    else:
        os.system("cls")
        print("That's not a valid option.")
        intro()

def intro():
    os.system("cls")
    print("Welcome to vivid/stasis's save swapper!")
    print("1. Set save")
    print("2. Write to a save")
    print("3. Wipe a save")
    print("4. Exit")
    menu(input("What do you want to do?\n"))



def swapsave():
    vssavelocation = f"C:\\Users\\{user}\\Appdata\\Local\\VIVIDSTASIS"
    print("Which save?")
    print("1.")
    print("2.")
    print("3.")
    print("4.")
    print("Press Q to go back to main menu.")
    choice = input("")
    if choice == "1":
        src = f"C:\\Users\\{user}\\Appdata\\Local\\vividstasisSaveSelector\\Save{choice}"
        shutil.rmtree(vssavelocation)
        shutil.copytree(src, vssavelocation)
        print("Done! Press enter to go back to menu!")
        getpass.getpass("")
        os.system("cls")
        pass
    elif choice == "2":
        src = f"C:\\Users\\{user}\\Appdata\\Local\\vividstasisSaveSelector\\Save{choice}"
        shutil.rmtree(vssavelocation)
        shutil.copytree(src, vssavelocation)
        print("Done! Press enter to go back to menu!")
        getpass.getpass("")
        os.system("cls")
        pass
    elif choice == "3":
        src = f"C:\\Users\\{user}\\Appdata\\Local\\vividstasisSaveSelector\\Save{choice}"
        shutil.rmtree(vssavelocation)
        shutil.copytree(src, vssavelocation)
        print("Done! Press enter to go back to menu!")
        getpass.getpass("")
        os.system("cls")
        pass
    elif choice == "4":
        src = f"C:\\Users\\{user}\\Appdata\\Local\\vividstasisSaveSelector\\Save{choice}"
        shutil.rmtree(vssavelocation)
        shutil.copytree(src, vssavelocation)
        print("Done! Press enter to go back to menu!")
        getpass.getpass("")
        os.system("cls")
        pass
    elif choice == "Q":
        intro()
    elif choice == "q":
        intro()
    else:
        os.system("cls")
        print("That's not a valid choice.")
        swapsave()
    intro()



def overwrite():
    vssavelocation = f"C:/Users/{user}/Appdata/Local/VIVIDSTASIS"
    os.system("cls")
    print("Which save do you want to write to?")
    print("1.")
    print("2.")
    print("3.")
    print("4.")
    print("Press Q to go back to main menu.")
    choice = input("")
    if choice == "1":
        src = f"C:/Users/{user}/Appdata/Local/vividstasisSaveSelector/Save{choice}"
        shutil.rmtree(src)
        shutil.copytree(vssavelocation, src)
        getpass.getpass("Done! Press Enter to go back to menu! \n")
        pass
    elif choice == "2":
        src = f"C:/Users/{user}/Appdata/Local/vividstasisSaveSelector/Save{choice}"
        shutil.rmtree(src)
        shutil.copytree(vssavelocation, src)
        getpass.getpass("Done! Press Enter to go back to menu! \n")
        pass
    elif choice == "3":
        src = f"C:/Users/{user}/Appdata/Local/vividstasisSaveSelector/Save{choice}"
        shutil.rmtree(src)
        shutil.copytree(vssavelocation, src)
        getpass.getpass("Done! Press Enter to go back to menu! \n")
        pass
    elif choice == "1":
        src = f"C:/Users/{user}/Appdata/Local/vividstasisSaveSelector/Save{choice}"
        shutil.rmtree(src)
        shutil.copytree(vssavelocation, src)
        getpass.getpass("Done! Press Enter to go back to menu! \n")
        pass
    elif choice == "Q":
        intro()
    elif choice == "q":
        intro()
    else:
        os.system("cls")
        print("That's not a valid choice.")
        overwrite()
    intro()

def erase():
    print("Which save do you want to erase?")
    print("1.")
    print("2.")
    print("3.")
    print("4.")
    print("Press Q to go back to main menu.")
    choice = input("")
    if choice == "1":
        src = f"C:/Users/{user}/Appdata/Local/vividstasisSaveSelector/Save{choice}"
        shutil.rmtree(src)
        os.makedirs(src)
        getpass.getpass("Done! Press Enter to go back to menu! \n")
    elif choice == "2":
        src = f"C:/Users/{user}/Appdata/Local/vividstasisSaveSelector/Save{choice}"
        shutil.rmtree(src)
        os.makedirs(src)
        getpass.getpass("Done! Press Enter to go back to menu! \n")
    elif choice == "3":
        src = f"C:/Users/{user}/Appdata/Local/vividstasisSaveSelector/Save{choice}"
        shutil.rmtree(src)
        os.makedirs(src)
        getpass.getpass("Done! Press Enter to go back to menu! \n")
    elif choice == "4":
        src = f"C:/Users/{user}/Appdata/Local/vividstasisSaveSelector/Save{choice}"
        shutil.rmtree(src)
        os.makedirs(src)
        getpass.getpass("Done! Press Enter to go back to menu! \n")
    elif choice == "Q":
        intro()
    elif choice == "q":
        intro()
    else:
        os.system("cls")
        print("That's not a valid choice.")
        erase()
    intro()
intro()



        
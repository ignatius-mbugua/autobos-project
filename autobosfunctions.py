import subprocess
import glob
import webbrowser
import os


class UserCommands:
    a = 0
    b = 0

    def create_command(self):
        userin = str(input("Choose either to open a 'program' or 'folder'\n"))
        if userin == "program":
            userincommand = str(input("Enter the command\n"))
            myfile = open("commandspath\\" + userincommand + ".txt", 'w')
            myfile.write('')
            myfile.close()
            mycommand = open("usercommands\\" + userincommand + ".txt", 'w')
            mycommand.write(userincommand)
            mycommand.close()
            userpath = str(input("Enter the path name(path to the program .exe): \n"))
            myfile1 = open("commandspath\\" + userincommand + ".txt", 'w')
            myfile1.write(userpath)
            myfile1.close()
            print("The command '" + userincommand + "' will open " + userpath)
        elif userin == "folder":
            userincommandf = str(input("Enter the command\n"))
            myfilef = open("commandsfolderpath\\" + userincommandf + ".txt", 'w')
            myfilef.write('')
            myfilef.close()
            mycommandfolder = open("usercommandsfolder\\" + userincommandf + ".txt", 'w')
            mycommandfolder.write(userincommandf)
            mycommandfolder.close()
            userpathf = str(input("Enter the path name(path to folder not file): \n"))
            myfile1f = open("commandsfolderpath\\" + userincommandf + ".txt", 'w')
            myfile1f.write(userpathf)
            myfile1f.close()
            print("The command 'folder " + userincommandf + "' will open " + userpathf)
        else:
            print("Enter either program or folder\n")

    def view_commands(self):
        print("The available commands are as follows: \n"
              "--------------------------------------\n"
              "Default commands for opening programs:\n"
              "notepad\n"
              "chrome\n"
              "calc(for Calculator)\n"
              "control panel\n"
              "sound recorder\n"
              "sticky notes\n"
              "word\n"
              "publisher\n"
              "powerpoint\n"
              "access\n"
              "excel\n"
              "cmd\n"
              "----------------------------------------\n"
              "Default system commands:\n"
              "this pc\n"
              "create command :(enables you to create commands to open programs and folders)\n"
              "folder 'folder_name' :(enables you to open folder you have associated its\n"
              "\tpath to a command e.g open folder music to open music folder)\n"
              "new folder\n"
              "check drive: (lists all folders in a particular drive/partition useful\n"
              "\tin checking external drives for suspicious files without opening them)\n"
              "system specs\n"
              "my desktop: (opens Windows default desktop folder)\n"
              "my music: (opens Windows default music folder)\n"
              "my videos: (opens Windows default videos folder)\n"
              "my pictures: (opens Windows default pictures folder)\n"
              "my downloads: (opens Windows default downloads folder)\n"
              "my documents: (opens Windows default documents folder)\n"
              "restart\n"
              "shutdown\n"
              "full shut: (full shutdown no fast startup)\n"
              "exit: (closes the program)\n"
              "text color_name: (change the program's text color e.g text green changes text\n"
              "\tto green available colors are: normal(for white), green, red, aqua, yellow)\n"
              "---------------------------------------------------------\n"
              "Default internet commands:\n"
              "google: (asks you for the word to google and searches using the default\n"
              "\tweb browser)\n"
              "wikipedia: (asks you for the word to search in wikipedia)\n"
              "gmail: (opens gmail)\n"
              "news: (opens websites: Daily Nation, Standard Media, SDE)\n"
              "youtube: (opens youtube in default browser)\n"
              "---------------------------------------------------------\n"
              "User created commands for opening programs:\n")
        for x in glob.glob(str(os.getcwd()) + "\\usercommands\\*.txt"):
            viewcommand = open(str(x), 'r')
            print(viewcommand.read())
            viewcommand.close()
        print("----------------------------------------------------------\n")
        print("User created commands for opening folders(use 'folder command_name' to run command):\n")
        for y in glob.glob(str(os.getcwd()) + "\\usercommandsfolder\\*.txt"):
            viewcommandfolder = open(str(y), 'r')
            print(viewcommandfolder.read())
            viewcommandfolder.close()
        print("------------------------------------------------------------\n")

    def open_command(self, usercommand):
        for x in glob.glob(str(os.getcwd()) + "\commandspath\\*.txt"):
            if str(os.getcwd() + "\commandspath\\" + usercommand + ".txt") == x:
                command_name = open(str(x), 'r')
                subprocess.Popen(command_name.read())
                self.a = 1
                break
            else:
                self.a = 0

        if self.a == 1:
            print(usercommand + " opened successfully\n")
        else:
            print("Check the command and try again\n")

    def open_command_folder(self, usercommand):
        new = usercommand.strip('folder ')
        for x in glob.glob(str(os.getcwd()) + "\commandsfolderpath\\*.txt"):
            if str(os.getcwd() + "\commandsfolderpath\\" + new + ".txt") == x:
                command_name = open(str(x), 'r')
                subprocess.Popen(['start', command_name.read()], shell=True)
                self.b = 1
                break
            else:
                self.b = 0

        if self.b == 1:
            print("Folder " + new + " opened successfully\n")
        else:
            print("Command to open the folder not found\n")


commands = UserCommands()


class DefaultPrograms:
    def open_chrome(self):
        try:
            subprocess.Popen("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
            print("Chrome opened successfully")
        except FileNotFoundError:
            print("Chrome is not installed in your machine")

    def open_notepad(self):
        try:
            subprocess.Popen("C:\Windows\system32\\notepad.exe")
            print("Notepad opened successfully")
        except FileNotFoundError:
            print("Notepad is not installed in your machine")

    def open_this_pc(self):
        try:
            subprocess.Popen("C:\Windows\explorer.exe")
            print("This PC opened successfully")
        except FileNotFoundError:
            print("Windows explorer is not installed in your machine")

    def open_calc(self):
        try:
            subprocess.Popen("C:\Windows\System32\calc.exe")
            print("Calculator opened successfully")
        except FileNotFoundError:
            print("Calculator is not installed in your machine")

    def open_controlpanel(self):
        try:
            subprocess.Popen("C:\Windows\System32\control.exe")
            print("Control Panel Opened successfully")
        except FileNotFoundError:
            print("Control panel is not installed in your machine")

    def open_dxdiag(self):
        try:
            subprocess.Popen("C:\Windows\System32\dxdiag.exe")
            print("Dxdiag opened successfully")
        except FileNotFoundError:
            print("dxdiag.exe is not installed in your machine")

    def open_soundrecorder(self):
        try:
            subprocess.Popen("C:\Windows\System32\SoundRecorder.exe")
            print("SoundRecorder opened successfully")
        except FileNotFoundError:
            print("SoundRecorder is not installed in your machine")

    def open_sticky_notes(self):
        try:
            subprocess.Popen("C:\Windows\System32\StikyNot.exe")
            print("Sticky Notes opened successfully")
        except FileNotFoundError:
            print("Sticky notes is not installed in your machine")

    def open_command_prompt(self):
        try:
            subprocess.Popen("C:\Windows\System32\cmd.exe")
            print("Command prompt opened successfully")
        except FileNotFoundError:
            print("Command prompt is not installed in your machine")

    def open_ms_word(self):
        try:
            subprocess.Popen("C:\Program Files\Microsoft Office\Office15\WINWORD.EXE")
            print("Microsoft word opened successfully")
        except FileNotFoundError:
            print("Microsoft Word is not installed in your machine")

    def open_ms_powerpoint(self):
        try:
            subprocess.Popen("C:\Program Files\Microsoft Office\Office15\POWERPNT.EXE")
            print("Microsoft PowerPoint opened successfully")
        except FileNotFoundError:
            print("Microsoft Powerpoint is not installed in your machine")

    def open_ms_publisher(self):
        try:
            subprocess.Popen("C:\Program Files\Microsoft Office\Office15\MSPUB.EXE")
            print("Microsoft Publisher opened successfully")
        except FileNotFoundError:
            print("Microsoft Publisher is not installed in your machine")

    def open_ms_access(self):
        try:
            subprocess.Popen("C:\Program Files\Microsoft Office\Office15\MSACCESS.EXE")
            print("Microsoft Access opened successfully")
        except FileNotFoundError:
            print("Microsoft Access is not installed in your machine")

    def open_ms_excel(self):
        try:
            subprocess.Popen("C:\Program Files\Microsoft Office\Office15\EXCEL.EXE")
            print("Microsoft Excel opened successfully")
        except FileNotFoundError:
            print("Microsoft Excel is not installed in your machine")

my_prog = DefaultPrograms()


class TheInternet:
    def googling(self):
        searchword = str(input("What do you want to google:\n"))
        print("Opening default browser...")
        webbrowser.open('http://www.google.com/search?q=' + searchword)

    def search_wikipedia(self):
        searchterm = str(input("Type the word you want to search in wikipedia:\n"))
        print("Opening default browser...")
        webbrowser.open('https://en.wikipedia.org/w/index.php?search=' + searchterm)

    def youtube_site(self):
        print("Opening youtube in default browser...")
        webbrowser.open('https://www.youtube.com/')

    def gmail_site(self):
        print("Opening gmail in default browser...")
        webbrowser.open('https://mail.google.com')

    def news(self):
        print("Opening Daily Nation...")
        print("Opening The Standard...")
        print("Opening SDE...")
        webbrowser.open('http://www.nation.co.ke/')
        webbrowser.open('http://www.standardmedia.co.ke/')
        webbrowser.open('http://www.sde.co.ke/')

my_internet = TheInternet()


class UserComp:
    def default_my_desktop(self):
        subprocess.Popen(['start', 'C:\\Users\\' + str(os.getlogin()) + "\Desktop"], shell=True)
        print("Folder Documents opened successfully")

    def default_my_documents(self):
        subprocess.Popen(['start', 'C:\\Users\\' + str(os.getlogin()) + "\Documents"], shell=True)
        print("Folder Documents opened successfully")

    def default_my_downloads(self):
        subprocess.Popen(['start', 'C:\\Users\\' + str(os.getlogin()) + "\Downloads"], shell=True)
        print("Folder Documents opened successfully")

    def default_my_music(self):
        subprocess.Popen(['start', 'C:\\Users\\' + str(os.getlogin()) + "\Music"], shell=True)
        print("Folder Documents opened successfully")

    def default_my_pictures(self):
        subprocess.Popen(['start', 'C:\\Users\\' + str(os.getlogin()) + "\Pictures"], shell=True)
        print("Folder Documents opened successfully")

    def default_my_videos(self):
        subprocess.Popen(['start', 'C:\\Users\\' + str(os.getlogin()) + "\Videos"], shell=True)
        print("Folder Documents opened successfully")

    def new_folder(self):
        folname = input(str("Type the path including the folder name you want to create:\n"))
        try:
            os.mkdir(folname)
            print("The directory " + folname + " has been created\n")
        except FileExistsError:
            print("Folder already exists\n")
        except FileNotFoundError:
            print("Check the pathname and try again\n")
        except PermissionError:
            print("Requires administrator priviledges (you can run autobos as administrator to fix it)\n")

    def check_external_drive(self):
        drive = str(input("Type the letter of the drive: \n"))
        if drive is "":
            print("Please enter the drive letter")
        else:
            for fol in glob.glob(drive + ':\\*'):
                print(str(fol))

    def change_text_color(self, usercolor):
        color = usercolor.strip("text")
        if "red" in color:
            os.system('color 0C')
        elif "green" in color:
            os.system('color 0A')
        elif "aqua" in color:
            os.system('color 0B')
        elif "yellow" in color:
            os.system('color 0E')
        elif "normal" in color:
            os.system('color 07')
        else:
            print("Available colors: normal(for white),green, aqua, red, yellow\n"
                  "Type e.g 'text green' to change text color to green\n")


my_computer = UserComp()

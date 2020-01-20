import autobosfunctions
import os

while True:
    ask = str(input("What can I do for you: (You can type 'help' to see available commands)\n"))
    if "notepad" in ask:
        os.system('cls')
        autobosfunctions.my_prog.open_notepad()
    elif "google" in ask:
        os.system('cls')
        autobosfunctions.my_internet.googling()
    elif "chrome" in ask:
        os.system('cls')
        autobosfunctions.my_prog.open_chrome()
    elif "wikipedia" in ask:
        os.system('cls')
        autobosfunctions.my_internet.search_wikipedia()
    elif "news" in ask:
        os.system('cls')
        autobosfunctions.my_internet.news()
    elif "youtube" in ask:
        os.system('cls')
        autobosfunctions.my_internet.youtube_site()
    elif "calc" in ask:
        os.system('cls')
        autobosfunctions.my_prog.open_calc()
    elif "this pc" in ask:
        os.system('cls')
        autobosfunctions.my_prog.open_this_pc()
    elif "control panel" in ask:
        os.system('cls')
        autobosfunctions.my_prog.open_controlpanel()
    elif "system specs" in ask:
        os.system('cls')
        autobosfunctions.my_prog.open_dxdiag()
    elif "sticky notes" in ask:
        os.system('cls')
        autobosfunctions.my_prog.open_sticky_notes()
    elif "sound recorder" in ask:
        os.system('cls')
        autobosfunctions.my_prog.open_soundrecorder()
    elif "word" in ask:
        os.system('cls')
        autobosfunctions.my_prog.open_ms_word()
    elif "access" in ask:
        os.system('cls')
        autobosfunctions.my_prog.open_ms_access()
    elif "excel" in ask:
        os.system('cls')
        autobosfunctions.my_prog.open_ms_excel()
    elif "publisher" in ask:
        os.system('cls')
        autobosfunctions.my_prog.open_ms_publisher()
    elif "powerpoint" in ask:
        os.system('cls')
        autobosfunctions.my_prog.open_ms_powerpoint()
    elif "cmd" in ask:
        os.system('cls')
        autobosfunctions.my_prog.open_command_prompt()
    elif "new folder" in ask:
        os.system('cls')
        autobosfunctions.my_computer.new_folder()
    elif "check drive" in ask:
        os.system('cls')
        autobosfunctions.my_computer.check_external_drive()
    elif "gmail" in ask:
        os.system('cls')
        autobosfunctions.my_internet.gmail_site()
    elif "create command" in ask:
        os.system('cls')
        autobosfunctions.commands.create_command()
    elif "help" in ask:
        os.system('cls')
        autobosfunctions.commands.view_commands()
    elif "my desktop" in ask:
        os.system('cls')
        autobosfunctions.my_computer.default_my_desktop()
    elif "my documents" in ask:
        os.system('cls')
        autobosfunctions.my_computer.default_my_documents()
    elif "my downloads" in ask:
        os.system('cls')
        autobosfunctions.my_computer.default_my_downloads()
    elif "my music" in ask:
        os.system('cls')
        autobosfunctions.my_computer.default_my_music()
    elif "my pictures" in ask:
        os.system('cls')
        autobosfunctions.my_computer.default_my_pictures()
    elif "my videos" in ask:
        os.system('cls')
        autobosfunctions.my_computer.default_my_videos()
    elif "shutdown" in ask:
        que = input("Are you sure you want to shutdown the machine?[y/n]\n")
        if que == 'y':
            os.system('shutdown /s /hybrid /t 5')
            break
        elif que == 'n':
            pass
        else:
            print("Type either 'y' for yes or 'n' for no.")
    elif "full shut" in ask:
        que = input("Are you sure you want to shutdown the machine?[y/n]\n")
        if que == 'y':
            os.system('shutdown /s /t 5')
            break
        elif que == 'n':
            pass
        else:
            print("Type either 'y' for yes or 'n' for no.")
    elif "restart" in ask:
        que = input("Are you sure you want to restart the machine?[y/n]\n")
        if que == 'y':
            os.system('shutdown /r /t 5')
            break
        elif que == 'n':
            pass
        else:
            print("Type either 'y' for yes or 'n' for no.")
    elif "hibernate" in ask:
        que = input("Are you sure you want to hibernate the machine? [y/n]\n")
        if que == 'y':
            os.system('shutdown /h')
            break
        elif que == 'n':
            pass
        else:
            print("Type either 'y' for yes or 'n' for no.")
    elif "exit" in ask:
        break
    elif "folder" in ask:
        os.system('cls')
        autobosfunctions.commands.open_command_folder(ask)
    elif "text" in ask:
        os.system('cls')
        autobosfunctions.my_computer.change_text_color(ask)
    else:
        os.system('cls')
        autobosfunctions.commands.open_command(ask)

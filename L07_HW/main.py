from menu import Menu, run_bash_cmd

def main():
    mainMenu = Menu()

    mainMenu.addOption("Check available memory")
    mainMenu.addOption("View network connections")
    mainMenu.addOption("Display free ram and swap")
    mainMenu.addOption("Quit")

    while True:
        choice = mainMenu.getInput()
        
        if choice == 4:
            run_bash_cmd(4)
            break
        
        run_bash_cmd(choice)

if __name__ == "__main__":
    main()
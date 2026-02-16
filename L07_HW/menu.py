import os

class Menu:
    
    def __init__(self):
        self._options = []

    def addOption(self, option):
        self._options.append(option)

    def getInput(self):
        while True:
            print("\n" + "="*30)
            for i, option in enumerate(self._options, 1):
                print(f"{i} {option}")
            
            choice = input("\nEnter choice (1-4 or Q to quit): ").strip().upper()

            if choice == 'Q' or choice == '4':
                return 4
            
            if choice.isdigit():
                val = int(choice)
                if 1 <= val <= len(self._options):
                    return val
            print(f"\n[!] Invalid input. Please enter a number between 1 and {len(self._options)}.")

def run_bash_cmd(choice):
    """
    Refactored method using a dictionary instead of if/elif blocks.
    Improves readability and maintainability (Step 15).
    """
    commands = {
        1: "vmstat",       
        2: "ss -tulpn",    
        3: "free -h",      
    }

    cmd = commands.get(choice)
    if cmd:
        print(f"\n--- Running: {cmd} ---")
        os.system(cmd)
    elif choice == 4:
        print("Exiting program...")
    else:
        print("Command not found.")
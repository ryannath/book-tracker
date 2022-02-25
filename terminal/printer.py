from .tcolor import Tcolor
class Printer:
    @staticmethod
    def clear():
        print("\x1b[2J\x1b[H")
    
    @staticmethod
    def print_help_info():
        s = (f"{Tcolor.GREEN}****************************************************************{Tcolor.RESET}\n\n"
            f"{Tcolor.GREEN + Tcolor.BOLD}Welcome to BookTracker{Tcolor.RESET}\n\n"
             "Best tracker of your bookly needs\n"
             "Currently, the following commands are available:\n"
             "(Slash indicates alternative inputs)\n"
            f"{Tcolor.BLUE}q{Tcolor.RESET} = quit the program\n"
            f"{Tcolor.BLUE}n/new{Tcolor.RESET}  = enter a new book\n"
            f"{Tcolor.BLUE}pa/print all{Tcolor.RESET}  = print all books entered\n"
            f"{Tcolor.BLUE}save/s{Tcolor.RESET}  = Saves the book library\n\n"
            f"{Tcolor.BLUE}?/h/help{Tcolor.RESET}  = to see this prompt again\n\n"
            f"{Tcolor.GREEN}****************************************************************{Tcolor.RESET}"
        )
        print(s)
    
    @staticmethod
    def get_input() -> str:
        return input(">> ").rstrip()
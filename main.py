from logic import ask_questions
from utils import colored_text
login_credentials = {"Username": "PGR107", "Password": "Python"}

def main():
    loginSuccess = False
    while not loginSuccess:
        print(colored_text("╔════════════LOGIN════════════╗", "cyan"))
        username = input(colored_text("║ Enter Username: ", "cyan"))
        password = input(colored_text("║ Enter Password: ", "cyan"))
        print(colored_text("╚═════════════════════════════╝", "cyan"))
        loginSuccess = login_info(login_credentials, username, password)
    ask_questions()

def login_info(login_credentials, username, password):
    if username != login_credentials["Username"]:
        print(colored_text("Username doesn't exist", "red"))
        return False
    elif password != login_credentials["Password"]:
        print(colored_text("Password is incorrect", "red"))
        return False

    print(colored_text("Login Successful", "green"))
    return True   

    
if __name__ == "__main__":
    main()

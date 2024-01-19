import pathlib
import aiviro


FILE_PATH = pathlib.Path("index.html").resolve()
email = "testovaci.email@aiviro.com"
password = "Heslo"


def solution():
    """Implement your solution here"""
    aiviro.init_logging()
    
    r = aiviro.create_web_robot(headless=True)
    r.go_to_url(f"file://{FILE_PATH}")

    r.wait_for(aiviro.Input("Email"))
    r.type_text(aiviro.Input("Email"), email)
    r.type_text(aiviro.Input("Password"), password)
    r.click(aiviro.Button("Login"))
    
    r.wait_for(aiviro.Text(f"Welcome {email}"))
 
    r.click(aiviro.Text("Customers"))
    r.wait_until_disappear(aiviro.Text("Loading..."))
    confirm = r.get(aiviro.Text("You've clicked Customers button")).text
    print(confirm)

if __name__ == "__main__":
    solution()

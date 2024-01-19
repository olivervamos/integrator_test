import aiviro
from aiviro.core.utils.file_utils import load_image


def solution():
    """Implement your solution here"""
    aiviro.init_logging()

    r = aiviro.create_static_robot()
    r.set_image(load_image("login_screen.png"))
    
    r.see(aiviro.Input("Email",))
    r.see(aiviro.Button("Log in"))
    r.see(aiviro.Text("Forgot password?"))
    

if __name__ == "__main__":
    solution()
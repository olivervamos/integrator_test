import aiviro
from aiviro.modules.pdf import create_pdf_robot
from datetime import datetime
import time

items = []

def solution():
    """Implement your solution here"""
    aiviro.init_logging()
    r = create_pdf_robot().parse("invoice.pdf", skip_chars=["_"])
    
    r.set_working_area(aiviro.Area(1135, 1078, 1335, 1106))
    date_format = '%B %d , %Y'
    invoice_date = datetime.strptime(r.get(aiviro.Text("")).text, date_format).strftime("%d.%m.%Y")
    items.append(invoice_date)
    
    for i in(range(5)):
        if i > 0:
            ymin = ymin + 72
            ymax = ymax + 73
        else:
            ymin = 1416
            ymax = 1450

        r.set_working_area(aiviro.Area(385, ymin, 693, ymax))
        try:
            items.append(r.get(aiviro.Text("")).text)
        except:
            pass
    
    r.set_working_area(aiviro.Area(1000, 2031, 1500, 2060))
    items.append(r.get(aiviro.Text("")).text)
    r.clear_working_area_and_screen_masks()

    todo_str = ''.join(str(f'  {x}') for x in items)

    r_web = aiviro.create_web_robot(headless=False)
    r_web.go_to_url("https://todomvc.com/examples/react/dist/")
    r_web.wait_for(aiviro.Text("todos"))
    
    r_web.type_text(aiviro.Input("What needs to be done?"), todo_str)
    r_web.key_press(aiviro.key.ENTER)
    
   
if __name__ == "__main__":
    solution()

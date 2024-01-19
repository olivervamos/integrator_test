import aiviro
from aiviro.modules.pdf import create_pdf_robot
from datetime import datetime


def solution():
    """Implement your solution here"""
    aiviro.init_logging()
    r = create_pdf_robot().parse("invoice.pdf", skip_chars=["_"])
    
    r.set_working_area(aiviro.Area(1135, 1078, 1335, 1106))
    date_format = '%B %d , %Y'
    invoice_date = datetime.strptime(r.get(aiviro.Text("")).text, date_format).strftime("%d.%m.%Y")

    items = []
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
    total_amount = r.get(aiviro.Text("")).text

    print(f"!!!toto je datum:{invoice_date}")
    print(f"polozky:{items}")
    print(f"suma:{total_amount}")


if __name__ == "__main__":
    solution()

import aiviro
from aiviro.core.utils.file_utils import load_image


def solution():
    """Implement your solution here"""
    aiviro.init_logging()

    r = aiviro.create_static_robot()

    images = ["helios_01.png", "helios_02.png"]

    for image in images:
        r.set_image(load_image(image))
        r.add_mask_windows_taskbar(80)

        title = r.get(aiviro.Text("Faktury vydané tuzemsko 200"))
        items = r.get(aiviro.Text("Položek"))
        storno_btn = r.get(aiviro.Button("Storno"))
        
        area = aiviro.Area(items.x_min, title.y_min, 
                            storno_btn.x_max, storno_btn.y_max)
        
        r.set_working_area(area)
        r.clear_working_area_and_screen_masks()

    
    
if __name__ == "__main__":
    solution()

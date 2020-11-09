# attribution
# icon - https://www.flaticon.com/free-icon/arrow_2742360?term=backup&page=1&position=27

import tkinter as tk
from PIL import Image, ImageTk


MIN_HEIGHT = 700
MIN_WIDTH = 500
MAX_HEIGHT = 1000
MAX_WIDTH = 1600

SCREEN_RES = 0

def get_curr_screen_resolution():
    """
    Workaround to get the size of the current screen in a multi-screen setup.

    Returns:
        geometry (str): The standard Tk geometry string.
            [width]x[height]+[left]+[top]
    """
    root = tk.Tk()
    root.update_idletasks()
    root.attributes('-fullscreen', True)
    root.state('iconic')
    geometry = root.winfo_geometry()
    root.destroy()
    try:
        width = int(geometry[:geometry.index('x')])
        height = int(geometry[geometry.index('x') + 1:geometry.index('+')])
        resolution = (width, height)
        return resolution
    except:
        print('Failed to convert screen resolution {} to width and height (int)'.format(geometry))
        print('MIN_WIDTH and MIN_HEIGHT returned as placeholder')
        return (MIN_WIDTH, MIN_HEIGHT)

def create_root():
    root = tk.Tk()
    root.title("Backup Vault")

    SCREEN_RES = get_curr_screen_resolution()

    width = SCREEN_RES[0] if SCREEN_RES[0] <= MAX_WIDTH else MAX_WIDTH
    height = SCREEN_RES[1] if SCREEN_RES[1] <= MAX_HEIGHT else MAX_HEIGHT
    root.geometry("{}x{}".format(width, height))

    root.minsize(MIN_WIDTH, MIN_HEIGHT)
    root.maxsize(MAX_WIDTH, MAX_HEIGHT)

    icon_png = Image.open('./icons/app_icon_32.png')
    app_icon = ImageTk.PhotoImage(icon_png)
    root.iconphoto(False, app_icon)

    input_frame = tk.Frame(root, bg='blue')
    input_frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.35)

    input_options_frame = tk.Frame(root, bg='blue')
    input_options_frame.place(relx=0.05, rely=0.41, relwidth=0.9, height=48)

    output_frame = tk.Frame(root, bg='red')
    output_frame.place(relx=0.05, rely= 0.55, relwidth=0.5, relheight=0.35)

    history_frame = tk.Frame(root, bg='green')
    history_frame.place(relx=0.6, rely=0.55, relwidth=0.35, relheight=0.35)

    output_options_frame = tk.Frame(root, bg='red')
    output_options_frame.place(relx=0.05, rely=0.91, relwidth=0.9, height=48)

    return root

# mainloop

root = create_root()

root.mainloop()
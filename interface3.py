import tkinter as tk
from PIL import Image, ImageTk
import random
from dic import territories 
from tkinter.font import Font

def add_territory_name(loc, canvas, name, text_color='black', bg_color='white', font_size=12):
    x, y = loc
    font = Font(family='Helvetica', size=font_size, weight='bold')

    # Measure text size
    text_width = font.measure(name)
    text_height = font.metrics("ascent")

    # Create a background rectangle slightly larger than the text
    padding = 2  # Adjust padding as needed
    canvas.create_rectangle(x - text_width / 2 - padding, 
                            y - text_height / 2 - padding, 
                            x + text_width / 2 + padding, 
                            y + text_height / 2 + padding, 
                            fill=bg_color, 
                            outline="")

    # Draw the text over the rectangle
    canvas.create_text(x, y, text=name, fill=text_color, font=font)



def all_close(arg1, arg2, r = 10):
    if ((arg1[0] - arg2[0])**2 + (arg1[1] - arg2[1])**2)**0.5 < r:
        return True
    
def add_army(loc, canvas, size = 5, r = 10, color = 'black'):
    radius = size
    x = loc[0] + random.randint(-r,r)
    y = loc[1] + random.randint(-r,r)
    canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color)

def add_fleet(loc, canvas, size = 5, r = 10, color = 'black'):
    x = loc[0] + random.randint(-r,r)
    y = loc[1] + random.randint(-r,r)
    coords = (x-size, y+size, x, y-size, x+size, y+size)
    canvas.create_polygon(coords, outline='white', fill=color, width=2)

def add_factory(loc, canvas, size = 5, r = 10, color = 'black'):
    radius = size
    x = loc[0] + random.randint(-r,r)
    y = loc[1] + random.randint(-r,r)
    canvas.create_rectangle(x - radius, y - radius, x + radius, y + radius, fill=color)
    
def main():
    root = tk.Tk()
    root.title("Risk Game Map")

    # Load your map image
    map_image = Image.open("map_with_sea_icons.png")  # Replace with your map image path
    map_image = map_image.resize((720, 480))
    map_photo = ImageTk.PhotoImage(map_image)

    # Create a canvas to display the image
    canvas = tk.Canvas(root, width=map_image.width, height=map_image.height)
    canvas.pack()

    # Display the image on the canvas
    canvas.create_image(0, 0, anchor=tk.NW, image=map_photo)

    def on_canvas_click(event):
        # Placeholder for click event handling
        print(f"Clicked at ({event.x}, {event.y})")
        #if all_close((event.x, event.y), (46, 91)):
        add_army((event.x, event.y), canvas)
        add_fleet((event.x, event.y), canvas)
        add_factory((event.x, event.y), canvas)
    

    # Bind click event to the canvas
    canvas.bind("<Button-1>", on_canvas_click)

    # Add territory names to the canvas
    for code, territory in territories.items():
        add_territory_name(territory['loc'], canvas, code)

    root.mainloop()

if __name__ == "__main__":
    main()

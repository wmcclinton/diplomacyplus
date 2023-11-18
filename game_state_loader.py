import tkinter as tk
from PIL import Image, ImageTk
import random
from map.dic import territories 
from tkinter.font import Font
import glob

token_locations = set()

def all_close(arg1, arg2, r = 10):
    if ((arg1[0] - arg2[0])**2 + (arg1[1] - arg2[1])**2)**0.5 < r:
        return True
    
def is_valid_location(loc):
    for past_loc in token_locations:
        if all_close(past_loc, loc, r=10):
            return False
    return True

def add_owner_name(loc, canvas, name, text_color='black', bg_color='white', font_size=8):
    x, y = loc
    token_locations.add((x, y))
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

def add_army(loc, canvas, size = 5, r = 10, color = 'black'):
    radius = size
    x = loc[0] + random.randint(-r,r)
    y = loc[1] + random.randint(-r,r)
    while not is_valid_location((x, y)):
        x = loc[0] + random.randint(-r,r)
        y = loc[1] + random.randint(-r,r)
    token_locations.add((x, y))
        
    canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color)

def add_fleet(loc, canvas, size = 5, r = 10, color = 'black'):
    x = loc[0] + random.randint(-r,r)
    y = loc[1] + random.randint(-r,r)
    while not is_valid_location((x, y)):
        x = loc[0] + random.randint(-r,r)
        y = loc[1] + random.randint(-r,r)
    token_locations.add((x, y))

    coords = (x-size, y+size, x, y-size, x+size, y+size)
    canvas.create_polygon(coords, outline='white', fill=color, width=2)

def add_factory(loc, canvas, size = 5, r = 10, color = 'black'):
    radius = size
    x = loc[0] + random.randint(-r,r)
    y = loc[1] + random.randint(-r,r)
    while not is_valid_location((x, y)):
        x = loc[0] + random.randint(-r,r)
        y = loc[1] + random.randint(-r,r)
    token_locations.add((x, y))

    canvas.create_rectangle(x - radius, y - radius, x + radius, y + radius, fill=color)

def parse_start_file(file_path):
    with open(file_path, 'r') as file:
        players = {}
        current_player = None

        for line in file:
            if line.strip() and not line.startswith('-'):
                # This line is a player name
                current_player = line.strip()
                players[current_player] = []
            elif line.startswith('-'):
                # This line is an action
                action = line.strip('-').strip()
                if current_player:
                    players[current_player].append(action)

        return players
    
def render(canvas):
    for code, territory in territories.items():
        # Owner
        if territory["owner"]:
            add_owner_name(territory['loc'], canvas, territory["owner"])
        # Add Units
        if "F" in territory["units"]:
            add_fleet(territory['loc'], canvas)
        if "A" in territory["units"]:
            add_army(territory['loc'], canvas)
        if "Farm" in territory["units"] or \
            "Factory" in territory["units"] or \
            "Monument" in territory["units"]:
            add_factory(territory['loc'], canvas)

    
def main():
    root = tk.Tk()
    root.title("Risk Game Map")

    # Load your map image
    map_image = Image.open("map/world_map.png")  # Replace with your map image path
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
        for code, territory in territories.items():
            if all_close(territory['loc'], (event.x, event.y)):
                print(code, territory)
    

    # Bind click event to the canvas
    canvas.bind("<Button-1>", on_canvas_click)

    # Load Start
    players = {}
    starting_countries = set()

    file_path = 'orders/0_start.txt'
    parsed_data = parse_start_file(file_path)
    for key, val in parsed_data.items():
        assert len(val) == 6
        name = key.strip()
        print("Loading", name)
        players[name] = {}
        countries = val[0].strip().split(' ')
        assert len(countries) == 4
        for country in countries:
            assert country not in starting_countries
            starting_countries.add(country)
            territories[country]["owner"] = name
        assert "Build F " in val[1]
        country = val[1].replace("Build F ", "").strip()
        territories[country]["units"].append("F")
        assert "Build A " in val[2]
        country = val[2].replace("Build A ", "").strip()
        territories[country]["units"].append("A")
        assert "Build Farm " in val[3]
        country = val[3].replace("Build Farm ", "").strip()
        territories[country]["units"].append("Farm")
        assert "Build Factory " in val[4]
        country = val[4].replace("Build Factory ", "").strip()
        territories[country]["units"].append("Factory")
        assert "Build Monument " in val[5]
        country = val[5].replace("Build Monument ", "").strip()
        territories[country]["units"].append("Monument")
        print("Loaded", val)

    # Get Order in Orders Folder
    orders = {}
    for order_file in glob.glob("orders/*"):
        if "0_start.txt" in order_file:
            continue
        season = order_file.split("/")[-1].split("_")[0]
        name = order_file.split("/")[-1].split("_")[1].split(".")[0]
        assert "Fa" in season or "Sp" in season
        assert name in list(players.keys())
        if season not in orders:
            orders[season] = {}
        with open(order_file, "r") as f:
            orders[season][name] = f.readlines()

    # TODO Simulate Orders
    print(orders)

    # Renders Gamestate to clickable interface
    render(canvas)

    root.mainloop()

if __name__ == "__main__":
    main()

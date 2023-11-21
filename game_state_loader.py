import tkinter as tk
from PIL import Image, ImageTk
import random
from map.dic import territories 
from tkinter.font import Font
import glob
import numpy as np

np.random.seed(777)

info = """\nCommand Types:
Move (Unit A or F) (Loc) -> (Loc)
Support (Unit A or F) (Loc) (Full Move Command)
Subsidize (Unit Farm or Factory or Monument) (Loc)
Build (Unit A or F) (Loc)
Policy (Local or Global) (Increase or Decrease) (Player)
Trade (Amount) (Resource Food, Material, Energy, or Hearts) -> (Amount) (Resource Food, Material, Energy, or Hearts) (Player)

Costs:
    Subsidize (Only in Fall) - Pay 2 En and 1 Ma to start a project (Farm, Factory, or Monument)
    Build - Pay 2 Ma make A or F
    Policy - Pay 3 He to enact either a local or global policy (decrease/increase a coup counter)
Production Rule (Only in Spring): Farms -> 20 Food, Factories -> 1 Energy and 1 Material, Monument -> 1 Heart\n\n"""
print(info)

token_locations = set()

def hex_to_rgb(hex_code):
    # Remove the '#' character if present
    hex_code = hex_code.lstrip('#')
    # Convert the hex code to a tuple of three integers
    return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))

class RGB():
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def __str__(self):
        return '#{:02X}{:02X}{:02X}'.format(self.red,self.green,self.blue)

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
    
def next_year(year):
    num = int(year[2:])
    if year.startswith("Fa"):
        season = "Sp"
    else:
        season = "Fa"
        num += 1
    return season + str(num)
    
def set_text(canvas, element, text):
    canvas.itemconfig(element, text=text)  # Update the text

def render(canvas, players):
    for code, territory in territories.items():
        # Owner
        player = None
        if territory["owner"]:
            add_owner_name(territory['loc'], canvas, territory["owner"])
            player = players[territory["owner"]]
        # Add Units
        if "F" in territory["units"]:
            add_fleet(territory['loc'], canvas, color=player["Color"])
        if "A" in territory["units"]:
            add_army(territory['loc'], canvas, color=player["Color"])
        
        if player:
            red, green, blue = hex_to_rgb(player["Color"])
            if "Farm" in territory["units"]:
                color = RGB(red, green, blue)
                add_factory(territory['loc'], canvas, color=str(color))
            if "Factory" in territory["units"]:
                color = RGB(red+60, green+60, blue+60)
                add_factory(territory['loc'], canvas, color=str(color))
            if "Monument" in territory["units"]:
                color = RGB(red+120, green+120, blue+120)
                add_factory(territory['loc'], canvas, color=str(color))

    
def main():
    root = tk.Tk()
    root.title("Risk Game Map")

    # Load your map image
    map_image = Image.open("map/world_map.png")  # Replace with your map image path
    map_image = map_image.resize((720, 480))
    map_photo = ImageTk.PhotoImage(map_image)

    # Create a canvas to display the image
    canvas = tk.Canvas(root, width=map_image.width+50, height=map_image.height+265)
    canvas.pack()

    # Display the image on the canvas
    canvas.create_image(0, 0, anchor=tk.NW, image=map_photo)

    def on_canvas_click(event):
        is_on_loc = False
        # Placeholder for click event handling
        print(f"Clicked at ({event.x}, {event.y})")
        for code, territory in territories.items():
            if all_close(territory['loc'], (event.x, event.y)):
                click_info = "\n\n|" + code + "|\n\n"
                for key, val in territory.items():
                    click_info += key + ": " + str(val) + "\n"
                set_text(canvas, textwindow, click_info)
                is_on_loc = True
        if not is_on_loc:
            set_text(canvas, textwindow, info)
    

    # Bind click event to the canvas
    canvas.bind("<Button-1>", on_canvas_click)

    # Window to display text
    textwindow = canvas.create_text(10, map_image.height + 165, justify="left", text="Hello, Tkinter!", font=("Arial", 10), fill="white", anchor=tk.W)

    # Window to display player text
    playerwindow = canvas.create_text(10, map_image.height + 35, justify="left", text="Hello, Tkinter!", font=("Arial", 10), fill="white", anchor=tk.W)

    # Load Start
    players = {}
    starting_countries = set()

    file_path = 'orders/0_start.txt'
    parsed_data = parse_start_file(file_path)
    for key, val in parsed_data.items():
        assert len(val) == 6
        name = key.strip()
        print("Loading", name)
        color = RGB(np.random.randint(0, 120), np.random.randint(0, 120), np.random.randint(0, 120))
        players[name] = {"En": 1, "Fo": 25, "He": 1, "Ma": 1, "A": 1, "F": 1, "Farm": 1, "Factory": 1, "Monument": 1, "Land": 4, "Capital": None, "LOI": None, "Coup": 0, "QOL": 0, "Color": str(color)}
        countries = val[0].strip().split(' ')
        assert len(countries) == 4
        for i, country in enumerate(countries):
            assert country not in starting_countries
            starting_countries.add(country)
            territories[country]["owner"] = name
            if i == 0:
                players[name]["Capital"] = country
            elif i == 1:
                players[name]["LOI"] = country
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
    year = "Fa1"
    # Sort by season
    for key, season_orders in orders.items():
        year = key
        for player_name, orders in season_orders.items():
            # Pay Food: For each land owned pay 1 Food and for each unit pay another 1 Food
            player = players[player_name]
            food_payment = player["Land"] + player["Farm"] + player["Factory"] + player["Monument"] + player["A"] + player["F"]

            # Check Starve: if you cannot pay enough food starve - lose 1 QOL and increase Coup Counter by 1, also you cannot increase QOL this turn
            if player['Fo'] < food_payment:
                player['QOL'] -= 1
                player['Coup'] += 1
                player['Fo'] = 0
            else:
                player['Fo'] = player['Fo'] - food_payment

            ### Execute Orders
            for order in orders:
                # Donation -> QOL (2^(next QOL level) required non-food resources)
                if order.startswith("Donate "):
                    # TODO
                    pass

                # Move (Unit A or F) (Loc) -> (Loc)
                ## Add move to list with placeholder list for support
                if order.startswith("Move "):
                    # TODO
                    pass

                # Support (Unit A or F) (Loc) (Full Move Command)
                ## Support to move on list
                if order.startswith("Support "):
                    # TODO
                    pass

                # Subsidize (If Fall)(Unit Farm or Factory or Monument) (Loc)
                ## Check to see if player has resources, and valid location then add unit
                if order.startswith("Subsidize "):
                    # TODO
                    pass

                # Build (Unit A or F) (Loc)
                ## Check to see if player has resources, and valid location then add unit
                if order.startswith("Build "):
                    # TODO
                    pass

                # Policy (Local or Global) (Increase or Decrease) (Player)
                ## Check to see if player has resources, then decrease or increases counter
                if order.startswith("Policy "):
                    # TODO
                    pass

                # Trade (Amount) (Resource Food, Material, Energy, or Hearts) -> (Amount) (Resource Food, Material, Energy, or Hearts) (Player)
                ## Check to see if player has resources, then add to trade set (if matching execute)
                if order.startswith("Trade "):
                    # TODO
                    pass

        # Execute all movements
        # TODO

        # Produce (If Spring)
        ## Add produced resources
        for player_name, orders in season_orders.items():
            player = players[player_name]
            if "Sp" in key:
                player["En"] += player["Factory"]
                player["Fo"] += 30 * player["Farm"]
                player["Ma"] += player["Factory"]
                player["He"] += player["Monument"]

    # Renders Gamestate to clickable interface
    render(canvas, players)
    playerinfo = next_year(year) + ":\n\n"
    for key, val in players.items():
        playerinfo += key + ": " + str(val) + "\n"
    # Info
    set_text(canvas, textwindow, info)
    set_text(canvas, playerwindow, playerinfo)

    root.mainloop()

if __name__ == "__main__":
    main()

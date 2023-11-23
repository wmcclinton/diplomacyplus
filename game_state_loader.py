import tkinter as tk
from PIL import Image, ImageTk
import random
from map.dic import territories 
from tkinter.font import Font
import glob
import numpy as np
import copy

COLOR = "white"

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
            if "S:" not in code:
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
    canvas = tk.Canvas(root, width=map_image.width+400, height=map_image.height+365)
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
    textwindow = canvas.create_text(10, map_image.height + 185, justify="left", text="Hello, Tkinter!", font=("Arial", 10), fill=COLOR, anchor=tk.W)

    # Window to display player text
    playerwindow = canvas.create_text(10, map_image.height + 45, justify="left", text="Hello, Tkinter!", font=("Arial", 10), fill=COLOR, anchor=tk.W)

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
        players[name] = {"En": 1, "Fo": 20, "He": 1, "Ma": 1, "A": 1, "F": 1, "Farm": 1, "Factory": 1, "Monument": 1, "Land": 4, "Capital": None, "LOI": None, "Coup": 0, "QOL": 0, "Color": str(color)}
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
        order_file= order_file.replace("\\","/")
        if "0_start.txt" in order_file:
            continue
        season = order_file.split("/")[-1].split("_")[0]
        name = order_file.split("/")[-1].split("_")[1].split(".")[0]
        #import ipdb; ipdb.set_trace()
        assert "Fa" in season or "Sp" in season
        assert name in list(players.keys())
        if season not in orders:
            orders[season] = {}
        with open(order_file, "r") as f:
            orders[season][name] = f.readlines()

    # TODO Simulate Orders
    print(orders)
    year = "Sp0"
    # Sort by season
    def sort_key(s):
        # Split each string into alphabetical and numerical parts
        alpha_part = ''.join(filter(str.isalpha, s))
        num_part = int(''.join(filter(str.isdigit, s)))
        return num_part, alpha_part
    all_orders = copy.deepcopy(orders)
    order_keys = sorted(list(all_orders.keys()), key=sort_key)
    for key in order_keys:
        season_orders = all_orders[key]
        year = key
        move_set = set()
        support_orders = {}
        unmatched_trades = set()
        matched_trades = set()
        for player_name, orders in season_orders.items():
            # Pay Food: For each land owned pay 1 Food and for each unit pay another 1 Food
            player = players[player_name]
            food_payment = player["Land"] + player["Farm"] + player["Factory"] + player["Monument"] + player["A"] + player["F"]
            print(key, player_name, "food_payment", food_payment)

            # Check Starve: if you cannot pay enough food starve - lose 1 QOL and increase Coup Counter by 1, also you cannot increase QOL this turn
            if player['Fo'] < food_payment:
                player['QOL'] -= 1
                player['Coup'] += 1
                player['Fo'] = 0
            else:
                player['Fo'] -= food_payment

            ### Execute Orders
            for order in orders:
                # Donation -> QOL (2^(next QOL level) required non-food resources)
                total_amount = 0
                if order.startswith("Donate "):
                    if order.strip().replace("Donate ", "") != "0":
                        items = order.strip().replace("Donate ", "").split(" ")
                        amount = 0
                        resource = None
                        for i, item in enumerate(items):
                            if i % 2 == 0:
                                amount = int(item)
                            elif i % 2 == 1:
                                resource = item
                                if resource in ["En", "Fo", "He", "Ma"]:
                                    if player[resource] >= amount:
                                        player[resource] -= amount
                                        total_amount += amount
                if total_amount >= 2 ** (player["QOL"] + 1):
                    player["QOL"] += 1

                # Move (Unit A or F) (Loc) -> (Loc)
                ## Add move to list with placeholder list for support
                if order.startswith("Move "):
                    items = order.strip().replace("Move ", "").split(" ")
                    if items[0] in ["A", "F"]:
                        if items[1] in territories.keys() and player_name == territories[items[1]]["owner"]:
                            if items[2] == "->":
                                if items[3] in territories[items[1]]["neighbors"]:
                                    if items[0] in territories[items[1]]["units"]:
                                        if items[0] == "A":
                                            move_set.add(order)
                                        if items[0] == "F":
                                            is_boarded_sea = False
                                            for loc in territories[items[3]]["neighbors"]:
                                                if "S:" in loc:
                                                    is_boarded_sea = True
                                            if "S:" in items[3] or is_boarded_sea:
                                                move_set.add(order)

                # Support (Unit A or F) (Loc) (Full Move Command)
                ## Support to move on list
                if order.startswith("Support "):
                    items = order.strip().replace("Support ", "").split(" ")
                    if items[0] in ["A", "F"]:
                        if items[1] in territories.keys() and player_name == territories[items[1]]["owner"]:
                            if items[1] in territories[items[4]]["neighbors"]:
                                if items[0] in territories[items[1]]["units"]:
                                    if items[3] in ["A", "F"]:
                                        if items[4] in territories.keys():
                                            if items[6] in territories[items[4]]["neighbors"]:
                                                if items[3] in territories[items[4]]["units"]:
                                                    mover_order = " ".join(items[2:])
                                                    if mover_order not in support_orders: 
                                                        support_orders[" ".join(items[2:])] = set()
                                                    support_orders[" ".join(items[2:])].add(items[1])

                # Subsidize (If Fall)(Unit Farm or Factory or Monument) (Loc)
                ## Check to see if player has resources, and valid location then add unit
                if order.startswith("Subsidize "):
                    items = order.strip().replace("Subsidize ", "").split(" ")
                    if "Fa" in key:
                        if items[0] in ["Farm", "Factory", "Monument"]:
                            if items[1] in territories.keys() and player_name == territories[items[1]]["owner"]:
                                if "Farm" not in territories[items[1]]["units"]:
                                    if "Factory" not in territories[items[1]]["units"]:
                                        if "Monument" not in territories[items[1]]["units"]:
                                            if player["En"] >= 2 and player["Ma"] >= 1:
                                                player["En"] -= 2
                                                player["Ma"] -= 1
                                                territories[items[1]]["units"].append(items[0])

                # Build (Unit A or F) (Loc)
                ## Check to see if player has resources, and valid location then add unit
                if order.startswith("Build "):
                    items = order.strip().replace("Build ", "").split(" ")
                    if items[1] in territories.keys() and player_name == territories[items[1]]["owner"]:
                            if "A" not in territories[items[1]]["units"]:
                                if "F" not in territories[items[1]]["units"]:
                                    if items[0] == "A":
                                        if "S:" not in items[1]:
                                            if player["Ma"] >= 2:
                                                player["Ma"] -= 2
                                                territories[items[1]]["units"].append(items[0])
                                    elif items[0] == "F":
                                        is_boarded_sea = False
                                        for loc in territories[items[1]]["neighbors"]:
                                           if "S:" in loc:
                                                is_boarded_sea = True
                                        if "S:" in items[1] or is_boarded_sea:
                                            if player["Ma"] >= 2:
                                                player["Ma"] -= 2
                                                territories[items[1]]["units"].append(items[0])

                # Policy (Local or Global) (Increase or Decrease) (Player)
                ## Check to see if player has resources, then decrease or increases counter
                if order.startswith("Policy "):
                    items = order.strip().replace("Policy ", "").split(" ")
                    if player["He"] >= 3:
                        if items[0] == "Local":
                            player["He"] -= 3
                            if items[1] == "Increase":
                                player["Coup"] += 1
                            elif items[1] == "Decrease" and player["Coup"] > 0:
                                player["Coup"] -= 1
                        elif items[0] == "Global":
                            player["He"] -= 3
                            if items[1] == "Increase":
                                players[items[2]]["Coup"] += 1
                            elif items[1] == "Decrease" and players[items[2]]["Coup"] > 0:
                                players[items[2]]["Coup"] -= 1
                                

                # Trade (Amount) (Resource Food, Material, Energy, or Hearts) -> (Amount) (Resource Food, Material, Energy, or Hearts) (Player)
                ## Check to see if player has resources, then add to trade set (if matching execute)
                if order.startswith("Trade "):
                    items = order.strip().replace("Trade ", "").split(" -> ")
                    sell_order = items[0]
                    sell_to = items[1].split(" ")[-1]
                    buy_order = " ".join(items[1].split(" ")[:-1])
                    matching_order = sell_to + " Trade " + buy_order + " -> " + sell_order + " " + player_name
                    if matching_order in unmatched_trades:
                        unmatched_trades.remove(matching_order)
                        matched_trades.add(matching_order)
                    else:
                        unmatched_trades.add(player_name + " " + order.strip())

        # Execute all trades
        for trade in matched_trades:
            is_valid_trade = True

            items = trade.strip().split(" -> ")
            player1_items = items[0].split(" ")
            player1 = player1_items[0]
            player1_items = player1_items[2:]
            player1 = players[player1]

            amount = 0
            resource = None
            resources = set(["En", "Fo", "He", "Ma"])
            for i, item in enumerate(player1_items):
                if i % 2 == 0:
                    amount = int(item)
                elif i % 2 == 1:
                    resource = item
                    if resource in resources:
                        resources.remove(resource)
                        if player1[resource] < amount:
                            is_valid_trade = False
                    else:
                        is_valid_trade = False   
            
            player2_items = items[1].split(" ")
            player2 = player2_items[-1]
            player2_items = player2_items[:-1]
            player2 = players[player2]

            amount = 0
            resource = None
            resources = set(["En", "Fo", "He", "Ma"])
            for i, item in enumerate(player2_items):
                if i % 2 == 0:
                    amount = int(item)
                elif i % 2 == 1:
                    resource = item
                    if resource in resources:
                        resources.remove(resource)
                        if player2[resource] < amount:
                            is_valid_trade = False
                    else:
                        is_valid_trade = False

            if is_valid_trade:
                amount = 0
                resource = None
                resources = set(["En", "Fo", "He", "Ma"])
                for i, item in enumerate(player1_items):
                    if i % 2 == 0:
                        amount = int(item)
                    elif i % 2 == 1:
                        resource = item
                        player1[resource] -= amount
                        player2[resource] += amount

                amount = 0
                resource = None
                resources = set(["En", "Fo", "He", "Ma"])
                for i, item in enumerate(player2_items):
                    if i % 2 == 0:
                        amount = int(item)
                    elif i % 2 == 1:
                        resource = item
                        player2[resource] -= amount
                        player1[resource] += amount

        # Execute all movements
        tmp_move_set = copy.deepcopy(move_set)
        attacked_loc = set()
        for move in tmp_move_set:
            items = move.strip().replace("Move ", "").split(" ")
            is_going_to_be_empty = True
            for m in tmp_move_set:
                if move != m:
                    m_items = m.strip().replace("Move ", "").split(" ")
                    if m_items[3] == items[3]:
                        is_going_to_be_empty = False
            if is_going_to_be_empty:
                if "A" not in territories[items[3]]["units"]:
                    if "F" not in territories[items[3]]["units"]:
                        territories[items[1]]["units"].remove(items[0])
                        territories[items[3]]["units"].append(items[0])
                        territories[items[3]]["owner"] = territories[items[1]]["owner"]
                        move_set.remove(move)
                    else:
                        attacked_loc.add(items[3])
                else:
                    attacked_loc.add(items[3])

        # TODO Test attacking with support [WARNING MAY NOT WORK]
        for move in move_set:
            items = move.strip().replace("Move ", "").split(" ")
            attack_strength = 1
            if move.strip() in support_orders.keys():
                for _ in support_orders[move.strip()]:
                    attack_strength += 1
                hold_strength = 0
                for order in support_orders.keys():
                    if " -> " + items[3] and order != move.strip():
                        for _ in support_orders[order]:
                            hold_strength += 1
                if attack_strength > hold_strength:
                    if "A" in territories[items[3]]["units"]:
                        territories[items[3]]["units"].remove("A")
                    if "F" in territories[items[3]]["units"]:
                        territories[items[3]]["units"].remove("F")
                    territories[items[1]]["units"].remove(items[0])
                    territories[items[3]]["units"].append(items[0])
                    territories[items[3]]["owner"] = territories[items[1]]["owner"]

        for player in players.keys():
            players[player]["Land"] = 0
            for unit in ["A", "F", "Farm", "Factory", "Monument"]:
                players[player][unit] = 0
            for territory in territories.keys():
                if territories[territory]["owner"] == player and "S:" not in territory:
                    players[player]["Land"] += 1
                    for unit in ["A", "F", "Farm", "Factory", "Monument"]:
                        if unit in territories[territory]["units"]:
                            players[player][unit] += 1
            players[player]["EST_FoPay"] = players[player]["Land"] + players[player]["Farm"] + players[player]["Factory"] + players[player]["Monument"] + players[player]["A"] + players[player]["F"]

            # Produce (If Spring)
            ## Add produced resources
            if "Sp" in year:
                players[player]["En"] += players[player]["Factory"]
                players[player]["Fo"] += 20 * players[player]["Farm"]
                players[player]["Ma"] += players[player]["Factory"]
                players[player]["He"] += players[player]["Monument"]

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

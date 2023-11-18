territories = {
    "ALA": {
        "name": "Alaska",
        "type": "land",
        "coastal": True,
        "loc": [47, 90],
        "neighbors": {"NWT", "ALB", "S:ARC", "S:NPO"},
        "units": [],
        "owner": None
    },
    "NWT": {
        "name": "Northwest Territory",
        "type": "land",
        "coastal": True,
        "loc": [113, 93],
        "neighbors": {"ALA", "ALB", "S:ARC", "ONT", "NUN", "S:NWP"},
        "units": [],
        "owner": None
    },
    "ALB": {
        "name": "Alberta",
        "type": "land",
        "coastal": False,
        "loc": [114, 130],
        "neighbors": {"ALA", "NWT", "S:NPO", "ONT", "WUS"},
        "units": [],
        "owner": None
    },
    "NUN": {
        "name": "Nunavut",
        "type": "land",
        "coastal": True,
        "loc": [175, 82],
        "neighbors": {"NWT", "ONT", "S:NWP"},
        "units": [],
        "owner": None
    },
    "ONT": {
        "name": "Ontario",
        "type": "land",
        "coastal": True,
        "loc": [165, 134],
        "neighbors": {"NWT", "ALB", "NUN", "QUE", "S:NWP", "WUS", "EUS"},
        "units": [],
        "owner": None
    },
    "QUE": {
        "name": "Quebec",
        "type": "land",
        "coastal": True,
        "loc": [222, 139],
        "neighbors": {"ONT", "EUS", "S:NWP", "S:NAO"},
        "units": [],
        "owner": None
    },
    "WUS": {
        "name": "Western United States",
        "type": "land",
        "coastal": True,
        "loc": [120, 170],
        "neighbors": {"ALB", "ONT", "EUS", "CTA", "S:NPO", "S:SPO"},
        "units": [],
        "owner": None
    },
    "EUS": {
        "name": "Eastern United States",
        "type": "land",
        "coastal": True,
        "loc": [172, 188],
        "neighbors": {"WUS", "ONT", "QUE", "CTA", "S:MEX", "S:CAR", "S:NAO"},
        "units": [],
        "owner": None
    },
    "GRE": {
        "name": "Greenland",
        "type": "land",
        "coastal": True,
        "loc": [272, 60],
        "neighbors": {"S:BAR", "S:NWP", "S:NAO", "S:GRE"},
        "units": [],
        "owner": None
    },
    "CTA": {
        "name": "Central America",
        "type": "land",
        "coastal": True,
        "loc": [126, 218],
        "neighbors": {"WUS", "EUS", "S:CAR", "VEN", "S:MEX", "S:SPO"},
        "units": [],
        "owner": None
    },
    "HAW": {
        "name": "Hawaii",
        "type": "land",
        "coastal": True,
        "loc": [40, 216],
        "neighbors": {"S:NPO", "S:SPO"},
        "units": [],
        "owner": None
    },
    "CUB": {
        "name": "Cuba",
        "type": "land",
        "coastal": True,
        "loc": [194, 237],
        "neighbors": {"S:NAO", "S:CAR"},
        "units": [],
        "owner": None
    },
    "VEN": {
        "name": "Venezuela",
        "type": "land",
        "coastal": True,
        "loc": [157, 277],
        "neighbors": {"BRA", "PER", "CTA", "S:SPO", "S:NAO", "S:CAR"},  
        "units": [],
        "owner": None
    },
    "PER": {
        "name": "Peru",
        "type": "land",
        "coastal": True,
        "loc": [158, 338],
        "neighbors": {"VEN", "BRA", "ARG", "S:SPO"},  
        "units": [],
        "owner": None
    },
    "BRA": {
        "name": "Brazil",
        "type": "land",
        "coastal": True,
        "loc": [212, 328],
        "neighbors": {"VEN", "PER", "ARG", "S:NAO", "S:SAO"},  
        "units": [],
        "owner": None
    },
    "ARG": {
        "name": "Argentina",
        "type": "land",
        "coastal": True,
        "loc": [174, 388],
        "neighbors": {"BRA", "PER", "S:SPO", "S:SOU", "S:SAO"},  
        "units": [],
        "owner": None
    },
    "FAL": {
        "name": "Falkland Islands",
        "type": "land",
        "coastal": True,
        "loc": [220, 452],
        "neighbors": {"S:SAO"},
        "units": [],
        "owner": None
    },
    "NAF": {
        "name": "North Africa",
        "type": "land",
        "coastal": True,
        "loc": [308, 286],
        "neighbors": {"EAF", "EGY", "CON", "S:MED", "S:NAO", "S:SAO"}, 
        "units": [],
        "owner": None
    },
    "EGY": {
        "name": "Egypt",
        "type": "land",
        "coastal": True,
        "loc": [359, 259],
        "neighbors": {"NAF", "EAF", "S:MED", "MIE", "S:ARA"},  # Placeholder neighbors
        "units": [],
        "owner": None
    },
    "CON": {
        "name": "Congo",
        "type": "land",
        "coastal": True,
        "loc": [360, 345],
        "neighbors": {"NAF", "EAF", "SAF", "S:SAO"},  
        "units": [],
        "owner": None
    },
    "EAF": {
        "name": "East Africa",
        "type": "land",
        "coastal": True,
        "loc": [388, 310],
        "neighbors": {"NAF", "EGY", "CON", "SAF", "S:IND", "S:ARA"},  # Placeholder neighbors
        "units": [],
        "owner": None
    },
    "SAF": {
        "name": "South Africa",
        "type": "land",
        "coastal": True,
        "loc": [352, 406],
        "neighbors": {"CON", "EAF", "S:SAO", "S:IND"},  # Placeholder neighbors
        "units": [],
        "owner": None
    },
    "MAD": {
        "name": "Madagascar",
        "type": "land",
        "coastal": True,
        "loc": [415, 406],
        "neighbors": {"S:IND"},  
        "units": [],
        "owner": None
    },
    "ICE": {
        "name": "Iceland",
        "type": "land",
        "coastal": True,
        "loc": [295, 115],
        "neighbors": {"S:NOR", "S:GRE", "S:NAO"}, 
        "units": [],
        "owner": None
    },
    "GBR": {
        "name": "Great Britain",
        "type": "land",
        "coastal": True,
        "loc": [309, 156],
        "neighbors": {"S:NAO", "S:ENG"}, 
        "units": [],
        "owner": None
    },
    "IRE": {
        "name": "Ireland",
        "type": "land",
        "coastal": True,
        "loc": [286, 151],
        "neighbors": {"S:NAO"},  
        "units": [],
        "owner": None
    },
    "WEU": {
        "name": "Western Europe",
        "type": "land",
        "coastal": True,
        "loc": [303, 202],
        "neighbors": {"NEU", "SEU", "S:MED", "S:NAO", "S:ENG"},  # Placeholder neighbors
        "units": [],
        "owner": None
    },
    "SEU": {
        "name": "Southern Europe",
        "type": "land",
        "coastal": True,
        "loc": [363, 194],
        "neighbors": {"WEU", "UKR", "NEU", "S:MED", "MEI", "S:BLA"}, 
        "units": [],
        "owner": None
    },
    "NEU": {
        "name": "Northern Europe",
        "type": "land",
        "coastal": True,
        "loc": [348, 160],
        "neighbors": {"UKR", "WEU", "SEU", "S:ENG", "S:BAL"},  # Placeholder neighbors
        "units": [],
        "owner": None
    },
    "SCA": {
        "name": "Scandinavia",
        "type": "land",
        "coastal": True,
        "loc": [364, 82],
        "neighbors": {"UKR", "S:BAL", "S:NOR", "S:ENG"},  # Placeholder neighbors
        "units": [],
        "owner": None
    },
    "UKR": {
        "name": "Ukraine",
        "type": "land",
        "coastal": True,
        "loc": [410, 131],
        "neighbors": {"NEU", "SEU", "SCA", "S:BLA", "S:BAL", "S:KAR", "S:BAR", "S:NOR", },  # Placeholder neighbors
        "units": [],
        "owner": None
    },
    "SVA": {
        "name": "Svalbard",
        "type": "land",
        "coastal": True,
        "loc": [404, 30],
        "neighbors": {"S:BAR", "S:NOR"}, 
        "units": [],
        "owner": None
    },
    "SEV": {
        "name": "Severny Island",
        "type": "land",
        "coastal": True,
        "loc": [419, 57],
        "neighbors": {"S:BAR", "S:KAR", "S:ESS"}, 
        "units": [],
        "owner": None
    },
    "URA": {
        "name": "Ural",
        "type": "land",
        "coastal": False,
        "loc": [480, 123],
        "neighbors": {"SIB", "CHI", "UZB", "UKR", "S:KAR"},  # Placeholder neighbors
        "units": [],
        "owner": None
    },
    "SIB": {
        "name": "Siberia",
        "type": "land",
        "coastal": False,
        "loc": [525, 100],
        "neighbors": {"YAK", "IRK", "MON", "CHI", "URA", "S:KAR", "S:ESS"},  # Placeholder neighbors
        "units": [],
        "owner": None
    },
    "YAK": {
        "name": "Yakutsk",
        "type": "land",
        "coastal": False,
        "loc": [595, 94],
        "neighbors": {"SIB", "IRK", "KAM", "S:ESS", "S:ARC"},  # Placeholder neighbors
        "units": [],
        "owner": None
    },
    "KAM": {
        "name": "Kamchatka",
        "type": "land",
        "coastal": True,
        "loc": [661, 88],
        "neighbors": {"YAK", "IRK", "MON", "S:NPO", "S:ARC", "S:SOJ"},  # Placeholder neighbors
        "units": [],
        "owner": None
    },
    "IRK": {
        "name": "Irkutsk",
        "type": "land",
        "coastal": False,
        "loc": [577, 133],
        "neighbors": {"SIB", "YAK", "KAM", "MON"},  # Placeholder neighbors
        "units": [],
        "owner": None
    },
    "MON": {
        "name": "Mongolia",
        "type": "land",
        "coastal": False,
        "loc": [583, 174],
        "neighbors": {"SIB", "IRK", "CHI", "KAM", "S:SOJ"},  # Placeholder neighbors
        "units": [],
        "owner": None
    },
    "CHI": {
        "name": "China",
        "type": "land",
        "coastal": True,
        "loc": [537, 214],
        "neighbors": {"MON", "SIB", "URA", "UZB", "IND", "SIA", "S:SOJ", "S:SCS"},  # Placeholder neighbors
        "units": [],
        "owner": None
    },
    "UZB": {
        "name": "UZB",
        "type": "land",
        "coastal": False,
        "loc": [466, 182],
        "neighbors": {"URA", "CHI", "IND", "MIE", "UKR", "S:CAS"},  
        "units": [],
        "owner": None
    },
    "IND": {
        "name": "India",
        "type": "land",
        "coastal": True,
        "loc": [499, 258],
        "neighbors": {"UZB", "CHI", "SIA", "MIE", "S:ARA", "S:BEN", "S:IND"},  # Placeholder neighbors
        "units": [],
        "owner": None
    },
    "SIA": {
        "name": "Siam",
        "type": "land",
        "coastal": True,
        "loc": [549, 270],
        "neighbors": {"CHI", "IND", "S:BEN", "S:SCS"},  # Placeholder neighbors
        "units": [],
        "owner": None
    },
    "MIE": {
        "name": "Middle East",
        "type": "land",
        "coastal": True,
        "loc": [415, 232],
        "neighbors": {"UZB", "IND", "S:MED", "UKR", "SEU", "EGY", "S:ARA"},  # Placeholder neighbors
        "units": [],
        "owner": None
    },
    "JAP": {
        "name": "Japan",
        "type": "land",
        "coastal": True,
        "loc": [639, 181],
        "neighbors": {"S:SOJ", "NPO", "S:SPO", "S:NPO"},  # Placeholder neighbors
        "units": [],
        "owner": None
    },
    "WAU": {
        "name": "Western Australia",
        "type": "land",
        "coastal": True,
        "loc": [562, 403],
        "neighbors": {"EAU", "S:IND", "S:PHI"},  # Placeholder neighbors
        "units": [],
        "owner": None
    },
    "EAU": {
        "name": "Eastern Australia",
        "type": "land",
        "coastal": True,
        "loc": [630, 402],
        "neighbors": {"WAU", "S:IND", "S:PHI", "S:TAS", "S:SOU"},  # Placeholder neighbors
        "units": [],
        "owner": None
    },
    "PHI": {
        "name": "Philippines",
        "type": "land",
        "coastal": True,
        "loc": [613, 269],
        "neighbors": {"S:PHI", "S:SPO", "S:SCS"},  # Placeholder neighbors
        "units": [],
        "owner": None
    },
    "NGU": {
        "name": "New Guinea",
        "type": "land",
        "coastal": True,
        "loc": [644, 335],
        "neighbors": {"S:PHI", "S:SPO", "S:TAS"},  # Placeholder neighbors
        "units": [],
        "owner": None
    },
    "INO": {
        "name": "Indonesia",
        "type": "land",
        "coastal": True,
        "loc": [538, 331],
        "neighbors": {"S:SCS", "S:IND", "S:PHI"},  # Placeholder neighbors
        "units": [],
        "owner": None
    },
    "KAL": {
        "name": "Kalimantan",
        "type": "land",
        "coastal": True,
        "loc": [571, 316],
        "neighbors": {"S:SCS", "S:PHI"},  
        "units": [],
        "owner": None
    },
    "NZE": {
        "name": "New Zealand",
        "type": "land",
        "coastal": True,
        "loc": [678, 403],
        "neighbors": {"S:SPO", "S:TAS", "S:SOU"},  # Placeholder neighbors
        "units": [],
        "owner": None
    },
    "S:KAR": {
        "name": "Kara Sea",
        "type": "sea",
        "loc": [463, 57],
        "neighbors": {"SEV", "SIB", "UKR", "URA", "S:ESS", "S:BAR"},
        "units": [],
        "owner": None
    },
    "S:ESS": {
        "name": "Eastern Siberian Sea",
        "type": "sea",
        "loc": [556, 22],
        "neighbors": {"SEV", "SIB", "YAK", "S:ARC", "S:KAR", "S:BAR"},
        "units": [],
        "owner": None
    },
    "S:ARC": {
        "name": "Arctic Ocean",
        "type": "sea",
        "loc": [57, 30],
        "neighbors": {"ALA", "KAM", "NWT", "YAK", "S:ESS", "S:NPO", "S:NWP"},
        "units": [],
        "owner": None
    },
    "S:NWP": {
        "name": "Northwestern Passage",
        "type": "sea",
        "loc": [194, 118],
        "neighbors": {"GRE", "NUN", "NWT", "ONT", "QUE", "S:ARC", "S:NAO"},
        "units": [],
        "owner": None
    },
    "S:NPO": {
        "name": "North Pacific Ocean",
        "type": "sea",
        "loc": [36, 148],
        "neighbors": {"ALA", "ALB", "HAW", "JAP", "KAM", "WUS", "S:ARC", "S:SPO"},
        "units": [],
        "owner": None
    },
    "S:SPO": {
        "name": "South Pacific Ocean",
        "type": "sea",
        "loc": [52, 318],
        "neighbors": {"ARG", "CTA", "HAW", "JAP", "NGU", "NZE", "PER", "PHI", "S:NPO", "VEN", "WUS", "S:SOU", "S:SCS", "S:PHI", "S:SOJ", "S:TAS"},
        "units": [],
        "owner": None
    },

    "S:SOU": {
        "name": "Southern Ocean",
        "type": "sea",
        "loc": [64, 457],
        "neighbors": {"ARG", "EAU", "NZE", "S:SPO", "S:SAS", "S:IND", "S:TAS"},  
        "units": [],
        "owner": None
    },
    "S:TAS": {
        "name": "Tasman Sea",
        "type": "sea",
        "loc": [653, 376],
        "neighbors": {"EAU", "NGU", "NZE", "S:SOU", "S:SPO", "S:PHI"},
        "units": [],
        "owner": None
    },

    "S:PHI": {
        "name": "Philippine Sea",
        "type": "sea",
        "loc": [606, 303],
        "neighbors": {"EAU", "INO", "KAL", "NGU", "PHI", "S:SPO", "WAU", "S:SCS", "S:IND", "S:TAS", "S:SOU"},
        "units": [],
        "owner": None
    },

    "S:SCS": {
        "name": "South China Sea",
        "type": "sea",
        "loc": [581, 268],
        "neighbors": {"CHI", "INO", "KAL", "PHI", "S:SPO", "SIA", "S:SOJ", "S:IND", "S:PHI"},
        "units": [],
        "owner": None
    },

    "S:SOJ": {
        "name": "Sea of Japan",
        "type": "sea",
        "loc": [616, 191],
        "neighbors": {"CHI", "JAP", "KAM", "MON", "S:SPO", "S:SCS", "S:NPO"},
        "units": [],
        "owner": None
    },
    "S:MEX": {
        "name": "Gulf of Mexico",
        "type": "sea",
        "loc": [153, 215],
        "neighbors": {"EUS", "CTA", "S:CAR"}, 
        "units": [],
        "owner": None
    },
    "S:CAR": {
        "name": "Caribbean Sea",
        "type": "sea",
        "loc": [167, 247],
        "neighbors": {"EUS", "CTA", "CUB", "VEN", "S:NAO", "S:SPO", "S:MEX"},
        "units": [],
        "owner": None
    },
    "S:NAO": {
        "name": "North Atlantic Ocean",
        "type": "sea",
        "loc": [247, 218],
        "neighbors": ["VEN", "QUE", "S:CAR", "IRE", "GRE", "ICE", "CUB", "WEU", "EUS", "NAF", "GBR", "S:NWP", "S:MED", "S:NOR", "S:GRE"],
        "units": [],
        "owner": None
    },

    "S:SAO": {
        "name": "South Atlantic Ocean",
        "type": "sea",
        "loc": [264, 421],
        "neighbors": ["FAL", "ARG", "BRA", "S:IND", "S:SOU", "SAF", "CON", "NAF", "S:NAO"],
        "units": [],
        "owner": None
    },

    "S:ENG": {
        "name": "English Channel",
        "type": "sea",
        "loc": [317, 139],
        "neighbors": ["WEU", "GBR", "NEU", "S:NOR", "S:NAO", "S:BAL"],
        "units": [],
        "owner": None
    },

    "S:BAL": {
        "name": "Baltic Sea",
        "type": "sea",
        "loc": [358, 128],
        "neighbors": ["NEU", "SCA", "UKR", "S:ENG"],
        "units": [],
        "owner": None
    },

    "S:NOR": {
        "name": "North Sea",
        "type": "sea",
        "loc": [325, 95],
        "neighbors": ["SCA", "S:ENG", "S:GRE", "S:BAR", "ICE", "SVA"],
        "units": [],
        "owner": None
    },

    "S:GRE": {
        "name": "Greenland Sea",
        "type": "sea",
        "loc": [341, 49],
        "neighbors": ["GRE", "ICE", "S:BAR", "S:NOR", "S:NAO"],
        "units": [],
        "owner": None
    },

    "S:BAR": {
        "name": "Barents Sea",
        "type": "sea",
        "loc": [370, 17],
        "neighbors": ["SVA", "SEV", "S:KAR", "S:ESS", "S:GRE", "S:NOR", "UKR", "GRE", "S:NWP"],
        "units": [],
        "owner": None
    },

    "S:ARA": {
        "name": "Arabian Sea",
        "type": "sea",
        "loc": [465, 293],
        "neighbors": ["IND", "MIE", "S:IND", "S:MED", "EGY", "EAF"],
        "units": [],
        "owner": None
    },

    "S:BEN": {
        "name": "Bay of Bengal",
        "type": "sea",
        "loc": [525, 282],
        "neighbors": ["IND", "SIA", "S:IND", "S:SCS"],
        "units": [],
        "owner": None
    },

    "S:IND": {
        "name": "Indian Ocean",
        "type": "sea",
        "loc": [493, 403],
        "neighbors": ["WAU", "EAU", "INO", "IND", "SIA", "S:ARA", "S:BEN", "S:SCS", "S:SOU", "S:PHI"],
        "units": [],
        "owner": None
    },

    "S:MED": {
        "name": "Mediterranean Sea",
        "type": "sea",
        "loc": [352, 229],
        "neighbors": ["WEU", "SEU", "MIE", "EGY", "S:BLA", "S:NAO"],
        "units": [],
        "owner": None
    },

    "S:BLA": {
        "name": "Black Sea",
        "type": "sea",
        "loc": [396, 192],
        "neighbors": ["SEU", "UKR", "MIE", "S:MED"],
        "units": [],
        "owner": None
    },
    "S:CAS": {
        "name": "Caspian Sea",
        "type": "sea",
        "loc": [433, 203],
        "neighbors": ["UZB", "UKR", "MIE"],
        "units": [],
        "owner": None
    },
}



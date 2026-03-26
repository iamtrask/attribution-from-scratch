"""
corpus.py — Hogwarts Headmaster Survey Dataset

1000 students share who they think the next Hogwarts headmaster should be.
Students overwhelmingly prefer their own head of house, with realistic noise.

Returns both structured data (name, house, candidate) and full sentences.
"""

import random

# House → candidate preferences (weights, normalized to probabilities)
HOUSE_PREFERENCES = {
    "Gryffindor": {
        "McGonagall": 55,
        "Flitwick": 15,
        "Sprout": 12,
        "Snape": 3,
        "Hagrid": 10,
        "Lupin": 5,
    },
    "Slytherin": {
        "Snape": 55,
        "McGonagall": 15,
        "Flitwick": 10,
        "Sprout": 5,
        "Hagrid": 3,
        "Lupin": 12,
    },
    "Hufflepuff": {
        "Sprout": 55,
        "McGonagall": 15,
        "Flitwick": 12,
        "Snape": 3,
        "Hagrid": 10,
        "Lupin": 5,
    },
    "Ravenclaw": {
        "Flitwick": 55,
        "McGonagall": 18,
        "Sprout": 10,
        "Snape": 5,
        "Hagrid": 4,
        "Lupin": 8,
    },
}

HOUSES = list(HOUSE_PREFERENCES.keys())
CANDIDATES = list(HOUSE_PREFERENCES["Gryffindor"].keys())

HEAD_OF_HOUSE = {
    "Gryffindor": "McGonagall",
    "Slytherin": "Snape",
    "Hufflepuff": "Sprout",
    "Ravenclaw": "Flitwick",
}

# Known characters per house, then generated wizard names to fill 250 each
KNOWN_NAMES = {
    "Gryffindor": [
        "Harry Potter", "Hermione Granger", "Ron Weasley", "Neville Longbottom",
        "Ginny Weasley", "Dean Thomas", "Seamus Finnigan", "Lavender Brown",
        "Parvati Patil", "Colin Creevey", "Dennis Creevey", "Katie Bell",
        "Angelina Johnson", "Alicia Spinnet", "Oliver Wood", "Lee Jordan",
        "Fred Weasley", "George Weasley", "Percy Weasley", "Romilda Vane",
        "Cormac McLaggen", "Andrew Kirke", "Jack Sloper", "Nigel Wolpert",
    ],
    "Slytherin": [
        "Draco Malfoy", "Vincent Crabbe", "Gregory Goyle", "Pansy Parkinson",
        "Blaise Zabini", "Theodore Nott", "Millicent Bulstrode", "Daphne Greengrass",
        "Astoria Greengrass", "Marcus Flint", "Adrian Pucey", "Graham Montague",
        "Cassius Warrington", "Miles Bletchley", "Terrence Higgs", "Flora Carrow",
        "Hestia Carrow", "Harper", "Malcolm Baddock", "Graham Pritchard",
    ],
    "Hufflepuff": [
        "Cedric Diggory", "Hannah Abbott", "Justin Finch-Fletchley", "Ernie Macmillan",
        "Susan Bones", "Zacharias Smith", "Leanne", "Megan Jones",
        "Wayne Hopkins", "Eleanor Branstone", "Owen Cauldwell", "Laura Madley",
        "Kevin Whitby", "Rose Zeller", "Nymphadora Tonks", "Maxine O'Flaherty",
        "Anthony Rickett", "Tamsin Applebee", "Herbert Fleet", "Heidi Macavoy",
    ],
    "Ravenclaw": [
        "Luna Lovegood", "Cho Chang", "Padma Patil", "Michael Corner",
        "Anthony Goldstein", "Terry Boot", "Marietta Edgecombe", "Lisa Turpin",
        "Mandy Brocklehurst", "Sue Li", "Stephen Cornfoot", "Kevin Entwhistle",
        "Morag MacDougal", "Orla Quirke", "Stewart Ackerley", "Eddie Carmichael",
        "Roger Davies", "Grant Page", "Duncan Inglebee", "Jason Samuels",
    ],
}

# Wizard-sounding first and last names for generating additional students
_FIRST_NAMES = [
    "Alaric", "Beatrix", "Cassius", "Dahlia", "Edmund", "Fiona", "Gareth",
    "Helena", "Ignatius", "Jasper", "Kieran", "Lucinda", "Magnus", "Nerissa",
    "Orion", "Penelope", "Quentin", "Rowena", "Silas", "Tabitha", "Ulric",
    "Vivienne", "Winston", "Xanthe", "Yolanda", "Zephyr", "Alden", "Bryony",
    "Cedric", "Dorothea", "Emeric", "Freya", "Gideon", "Honoria", "Ivo",
    "Jocasta", "Kenelm", "Lettice", "Mortimer", "Niamh", "Oswald", "Primrose",
    "Roderick", "Sophronia", "Thaddeus", "Ursula", "Vaughan", "Winifred",
    "Ambrose", "Clementine", "Desmond", "Elspeth", "Fergus", "Griselda",
    "Hamish", "Imogen", "Julius", "Katarina", "Lionel", "Marguerite",
    "Norbert", "Ottilie", "Percival", "Rosalind", "Septimus", "Thomasina",
    "Algernon", "Cordelia", "Eustace", "Fleur", "Hadrian", "Isadora",
    "Leopold", "Millicent", "Peregrine", "Sybilla", "Tarquin", "Araminta",
    "Barnaby", "Celestine", "Erasmus", "Gwendolen", "Hector", "Iona",
    "Lysander", "Minerva", "Phineas", "Rowland", "Seraphina", "Tobias",
    "Adelaide", "Benedict", "Cressida", "Dunstan", "Elowen", "Godfrey",
]
_LAST_NAMES = [
    "Ashworth", "Blackwood", "Crouch", "Dumbledore", "Everett", "Fawcett",
    "Grimshaw", "Hornby", "Inkwell", "Jorkins", "Kettleburn", "Lockhart",
    "Marchbanks", "Nightshade", "Ogden", "Prewett", "Quirrell", "Rookwood",
    "Selwyn", "Trimble", "Umfraville", "Vance", "Widdershins", "Yaxley",
    "Zabini", "Abercrombie", "Blishwick", "Cattermole", "Dearborn", "Edgecombe",
    "Fenwick", "Gudgeon", "Hitchens", "Ilkley", "Jugson", "Kirke",
    "Lestrange", "Mockridge", "Nettlebed", "Ollerton", "Peasegood", "Runcorn",
    "Scamander", "Thicknesse", "Urquhart", "Vector", "Wagstaff", "Clearwater",
    "Bellchant", "Cromwell", "Dagworth", "Fancourt", "Gamp", "Hobday",
    "Inglebee", "Kowalski", "Longshore", "Meadowes", "Nottingham", "Oakes",
    "Plunkett", "Ravensdale", "Shacklebolt", "Tonbridge", "Underhill",
    "Proudfoot", "Burbage", "Diggory", "Fortescue", "Greyback", "Hopkirk",
    "Ironside", "Kettleworth", "Lovegood", "Moody", "Nott", "Ollivander",
    "Podmore", "Rosier", "Slughorn", "Trelawney", "Whitby", "Bones",
    "Cresswell", "Dawlish", "Fletchley", "Goldstein", "Higgs", "Avery",
    "Mulciber", "Rowle", "Travers", "Wilkes", "Bagnold", "Fudge",
]


def _generate_names(house, n, rng):
    """Generate n unique wizard names for a house, using known names first."""
    names = list(KNOWN_NAMES.get(house, []))
    used = set(names)
    while len(names) < n:
        first = rng.choice(_FIRST_NAMES)
        last = rng.choice(_LAST_NAMES)
        full = f"{first} {last}"
        if full not in used:
            names.append(full)
            used.add(full)
    return names[:n]


def generate_dataset(n=1000, seed=42):
    """Generate n survey responses.

    Returns list of dicts with keys: name, house, candidate, text
    """
    rng = random.Random(seed)
    data = []
    per_house = n // len(HOUSES)

    for house in HOUSES:
        prefs = HOUSE_PREFERENCES[house]
        candidates = list(prefs.keys())
        weights = list(prefs.values())
        names = _generate_names(house, per_house, rng)

        for name in names:
            candidate = rng.choices(candidates, weights=weights, k=1)[0]
            text = (f"My name is {name}. As a member of {house}, "
                    f"I think the next headmaster should be {candidate}")
            data.append({
                "name": name,
                "house": house,
                "candidate": candidate,
                "text": text,
            })

    rng.shuffle(data)
    return data


def get_texts(data, house=None):
    """Get all text responses, optionally filtered by house."""
    return [d["text"] for d in data if house is None or d["house"] == house]


def get_candidate_counts(data, house=None):
    """Count candidate preferences, optionally filtered by house."""
    counts = {c: 0 for c in CANDIDATES}
    for d in data:
        if house is None or d["house"] == house:
            counts[d["candidate"]] += 1
    return counts


# The rooms dataset — used from Lecture 2 onward
ROOMS_SOURCES = [
    "The cat is in the kitchen. The kitchen is on the first floor.",
    "The dog is in the garden. The garden has a pond.",
    "The hamster is in the bedroom. The bedroom is upstairs.",
    "The bird is in the cage. The cage is by the window.",
    "The fish is in the pond. The pond is in the garden.",
    "The mouse is in the basement. The basement is cold.",
    "The snake is in the box. The box is under the stairs.",
    "The turtle is in the bathroom. The bathroom has a blue door.",
    "The parrot is in the living room. The living room faces south.",
    "The frog is in the garage. The garage is detached.",
]

ROOMS_NAMES = [
    "Cat Report", "Dog Report", "Hamster Report", "Bird Report", "Fish Report",
    "Mouse Report", "Snake Report", "Turtle Report", "Parrot Report", "Frog Report",
]


if __name__ == "__main__":
    data = generate_dataset()
    print(f"Hogwarts Headmaster Survey — {len(data)} responses\n")

    # Overall results
    total_counts = get_candidate_counts(data)
    print("Overall results:")
    for candidate, count in sorted(total_counts.items(), key=lambda x: -x[1]):
        bar = "█" * (count // 4)
        print(f"  {candidate:15s} {bar} {count}")

    # Per-house breakdown
    for house in HOUSES:
        counts = get_candidate_counts(data, house)
        total = sum(counts.values())
        head = HEAD_OF_HOUSE[house]
        print(f"\n{house} ({total} responses, head of house: {head}):")
        for candidate, count in sorted(counts.items(), key=lambda x: -x[1]):
            bar = "█" * (count // 2)
            marker = " ← head of house" if candidate == head else ""
            print(f"  {candidate:15s} {bar} {count}{marker}")

    # Sample responses
    print(f"\nSample responses:")
    for d in data[:8]:
        print(f"  {d['text']}")

    # Show structured data
    print(f"\nStructured data (first 5):")
    print(f"  {'Name':30s} {'House':15s} {'Candidate':15s}")
    print(f"  {'-'*30} {'-'*15} {'-'*15}")
    for d in data[:5]:
        print(f"  {d['name']:30s} {d['house']:15s} {d['candidate']:15s}")

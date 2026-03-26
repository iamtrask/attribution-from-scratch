"""
corpus.py — Hogwarts Survey Dataset

1000 survey responses from Hogwarts students about their favorite subject.
Each house has strong preferences with realistic noise.

Used throughout the course as the primary attribution dataset.
"""

import random

# House → subject preferences (weights, will be normalized to probabilities)
HOUSE_PREFERENCES = {
    "Gryffindor": {
        "Defense Against the Dark Arts": 50,
        "Transfiguration": 25,
        "Charms": 10,
        "Potions": 5,
        "Herbology": 5,
        "Care of Magical Creatures": 3,
        "Divination": 2,
    },
    "Slytherin": {
        "Potions": 50,
        "Defense Against the Dark Arts": 20,
        "Transfiguration": 10,
        "Charms": 8,
        "Herbology": 5,
        "Care of Magical Creatures": 4,
        "Divination": 3,
    },
    "Hufflepuff": {
        "Herbology": 45,
        "Care of Magical Creatures": 25,
        "Charms": 15,
        "Potions": 5,
        "Transfiguration": 5,
        "Defense Against the Dark Arts": 3,
        "Divination": 2,
    },
    "Ravenclaw": {
        "Charms": 40,
        "Transfiguration": 25,
        "Defense Against the Dark Arts": 15,
        "Potions": 8,
        "Herbology": 5,
        "Divination": 5,
        "Care of Magical Creatures": 2,
    },
}

HOUSES = list(HOUSE_PREFERENCES.keys())
SUBJECTS = list(HOUSE_PREFERENCES["Gryffindor"].keys())


def generate_dataset(n=1000, seed=42):
    """Generate n survey responses. Returns list of (house, subject, text) tuples."""
    rng = random.Random(seed)
    data = []
    per_house = n // len(HOUSES)

    for house in HOUSES:
        prefs = HOUSE_PREFERENCES[house]
        subjects = list(prefs.keys())
        weights = list(prefs.values())

        for _ in range(per_house):
            subject = rng.choices(subjects, weights=weights, k=1)[0]
            text = f"As a member of {house}, my favorite subject is {subject}"
            data.append((house, subject, text))

    rng.shuffle(data)
    return data


def get_house_texts(data, house):
    """Get all texts from a specific house."""
    return [text for h, s, text in data if h == house]


def get_subject_counts(data, house=None):
    """Count subject preferences, optionally filtered by house."""
    counts = {s: 0 for s in SUBJECTS}
    for h, s, text in data:
        if house is None or h == house:
            counts[s] += 1
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
    print(f"Generated {len(data)} responses\n")

    # Show distribution per house
    for house in HOUSES:
        counts = get_subject_counts(data, house)
        total = sum(counts.values())
        print(f"\n{house} ({total} responses):")
        for subject, count in sorted(counts.items(), key=lambda x: -x[1]):
            bar = "█" * (count // 2)
            print(f"  {subject:35s} {bar} {count}")

    # Show a few examples
    print(f"\nSample responses:")
    for house, subject, text in data[:10]:
        print(f"  {text}")

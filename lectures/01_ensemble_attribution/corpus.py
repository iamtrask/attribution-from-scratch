"""
corpus.py — Hogwarts Headmaster Survey Dataset

1000 students share who they think the next Hogwarts headmaster should be.
Students overwhelmingly prefer their own head of house, with realistic noise.

Used throughout the course as the primary attribution dataset.
"""

import random

# House → candidate preferences (weights, normalized to probabilities)
# Each house strongly prefers their own head of house
HOUSE_PREFERENCES = {
    "Gryffindor": {
        "McGonagall": 55,   # their head of house
        "Flitwick": 15,
        "Sprout": 12,
        "Snape": 3,
        "Hagrid": 10,
        "Lupin": 5,
    },
    "Slytherin": {
        "Snape": 55,        # their head of house
        "McGonagall": 15,
        "Flitwick": 10,
        "Sprout": 5,
        "Hagrid": 3,
        "Lupin": 12,
    },
    "Hufflepuff": {
        "Sprout": 55,       # their head of house
        "McGonagall": 15,
        "Flitwick": 12,
        "Snape": 3,
        "Hagrid": 10,
        "Lupin": 5,
    },
    "Ravenclaw": {
        "Flitwick": 55,     # their head of house
        "McGonagall": 18,
        "Sprout": 10,
        "Snape": 5,
        "Hagrid": 4,
        "Lupin": 8,
    },
}

HOUSES = list(HOUSE_PREFERENCES.keys())
CANDIDATES = list(HOUSE_PREFERENCES["Gryffindor"].keys())

# Head of house mapping
HEAD_OF_HOUSE = {
    "Gryffindor": "McGonagall",
    "Slytherin": "Snape",
    "Hufflepuff": "Sprout",
    "Ravenclaw": "Flitwick",
}


def generate_dataset(n=1000, seed=42):
    """Generate n survey responses. Returns list of (house, candidate, text) tuples."""
    rng = random.Random(seed)
    data = []
    per_house = n // len(HOUSES)

    for house in HOUSES:
        prefs = HOUSE_PREFERENCES[house]
        candidates = list(prefs.keys())
        weights = list(prefs.values())

        for _ in range(per_house):
            candidate = rng.choices(candidates, weights=weights, k=1)[0]
            text = f"As a member of {house}, I think the next headmaster should be {candidate}"
            data.append((house, candidate, text))

    rng.shuffle(data)
    return data


def get_house_responses(data, house):
    """Get all response texts from a specific house."""
    return [text for h, c, text in data if h == house]


def get_candidate_counts(data, house=None):
    """Count candidate preferences, optionally filtered by house."""
    counts = {c: 0 for c in CANDIDATES}
    for h, c, text in data:
        if house is None or h == house:
            counts[c] += 1
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
    for house, candidate, text in data[:8]:
        print(f"  {text}")

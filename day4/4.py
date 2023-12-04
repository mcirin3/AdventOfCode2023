import sys
from collections import defaultdict



def calculate_points(card):
    _, your_numbers = card.split(":")
    winning_numbers, your_numbers = your_numbers.split("|")
    winning_numbers = set(map(int, winning_numbers.split()))
    your_numbers = set(map(int, your_numbers.split()))

    common_numbers = your_numbers.intersection(winning_numbers)
    points = 2**(len(common_numbers) - 1) if common_numbers else 0

    return points

def total_points(cards):
    return sum(calculate_points(card) for card in cards)

def simulate_winning(cards):
    scratchcards = defaultdict(int)

    for card in cards:
        points = calculate_points(card)
        scratchcards[card] += 1

        for _ in range(points - 1):  # Create copies based on points
            scratchcards[card] += 1

    return scratchcards

def total_scratchcards(cards):
    scratchcards = simulate_winning(cards)
    
    while True:
        new_scratchcards = simulate_winning(scratchcards.keys())
        if not new_scratchcards:
            break
        scratchcards.update(new_scratchcards)

    return sum(scratchcards.values())


if len(sys.argv) != 2:
    print("Usage: python script.py input_file.txt")
    sys.exit(1)

file_path = sys.argv[1]

try:
    with open(file_path, 'r') as file:
        # Read lines starting with "Card"
        cards = [line.strip() for line in file if line.startswith("Card")]

    # Calculate total points
    total = total_points(cards)

    print("Total Points:", total)
    
    # Calculate total scratchcards
    total2 = total_scratchcards(cards)

    print("Total Scratchcards:", total2)

except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")

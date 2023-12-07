def count_ways_to_beat_record(time, distance):
    ways = 0
    for hold_time in range(time):
        boat_speed = hold_time
        remaining_time = time - hold_time
        total_distance = boat_speed * remaining_time
        if total_distance > distance:
            ways += 1
    return ways

def main():
    with open('input.txt', 'r') as file:
        lines = file.readlines()

    # Extract times and distances from the lines
    times = list(map(int, lines[0].split()[1:]))
    distances = list(map(int, lines[1].split()[1:]))

    total_ways = 1
    for t, d in zip(times, distances):
        ways = count_ways_to_beat_record(t, d)
        total_ways *= ways

    print("The number of ways to beat the record in each race:", total_ways)

if __name__ == "__main__":
    main()

# Simulate a sports tournament

import csv
import sys
import random

# Number of simluations to run
N = 1000


def main():

    # Ensure correct usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python tournament.py FILENAME")

    teams = []
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            dict = {}
            t = row["team"]
            r = int(row["rating"])
            dict["team"] = t
            dict["rating"] = r
            teams.append(dict)


    counts = []
    # TODO: Simulate N tournaments and keep track of win counts
    for i in range(0, N):
            dict = {}
            x = simulate_tournament(teams)
            f = find(counts, 'team', x)
            if f == -1:
                dict['team'] = x
                dict['count'] = 0
                counts.append(dict)
                continue
            counts[f]['count'] += 1
            print(counts[f]['count'])
            print(counts[f]['team'])

    # Print each team's chances of winning, according to simulation
    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")

def find(counts, key, value):
    for i, dic in enumerate(counts):
        if dic[key] == value:
            return i
    return -1

def simulate_game(team1, team2):
    """Simulate a game. Return True if team1 wins, False otherwise."""
    rating1 = team1["rating"]
    rating2 = team2["rating"]
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))
    return random.random() < probability


def simulate_round(teams):
    """Simulate a round. Return a list of winning teams."""
    winners = []

    # Simulate games for all pairs of teams
    for i in range(0, len(teams), 2):
        if simulate_game(teams[i], teams[i + 1]):
            winners.append(teams[i])
        else:
            winners.append(teams[i + 1])

    return winners


def simulate_tournament(teams):
    """Simulate a tournament. Return name of winning team."""
    # TODO
    while(len(teams) > 1):
        teams = simulate_round(teams)
    x = teams[0]['team']
    return x

if __name__ == "__main__":
    main()

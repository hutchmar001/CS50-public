import csv
import sys


def main():

    # TODO: Check for command-line usage

    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py databases/large.csv sequences/5.txt")

    # TODO: Read database file into a variable

    databases = []
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            dict = {}
            dict["name"] = row["name"]
            dict["AGATC"] = row["AGATC"]
            dict["TTTTTTCT"] = row["TTTTTTCT"]
            dict["AATG"] = row["AATG"]
            dict["TCTAG"] = row["TCTAG"]
            dict["GATA"] = row["GATA"]
            dict["TATC"] = row["TATC"]
            dict["GAAA"] = row["GAAA"]
            dict["TCTG"] = row["TCTG"]
            databases.append(dict)

    # TODO: Read DNA sequence file into a variable

    with open(sys.argv[2]) as file:
        sequence = file.read()

    # TODO: Find longest match of each STR in DNA sequence

    matches = []
    for key in databases[0]:
        matches.append(longest_match(sequence, key))

    # TODO: Check database for matching profiles
    for j in range(0, len(databases)):
        for value in databases[j].values():
            for 
            if value == matches[j + 1]:
                print(databases[j])
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()

import csv
import sys


def main():
    # Check for command-line usage
    if not len(sys.argv) == 3:
        print("Error command line form")
        return

    # Read database file into a variable
    database = []
    with open(sys.argv[1]) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row["name"]
            entry = {"name": row["name"]}
            for value_name in reader.fieldnames[1:]:
                entry[value_name] = int(row[value_name])
            database.append(entry)

    # Read DNA sequnence file into a variable
    with open(sys.argv[2]) as inputfile:
        content = inputfile.read()

    #  Find longest match of each STR in DNA sequence
    AGATC_count = longest_match(content, 'AGATC')
    AATG_count = longest_match(content, 'AATG')
    TATC_count = longest_match(content, 'TATC')

    # Check database for matching profiles
    for person in database:
        if (person["AGATC"] == AGATC_count and person["AATG"] == AATG_count and person["TATC"] == TATC_count):
            print(person["name"])
            break
    else:
        print("No match")
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

#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// Candidates have name and vote count
typedef struct
{
    string name;
    int votes;
}
candidate;

// Array of candidates
candidate candidates[MAX];

// Number of candidates
int candidate_count;

// Function prototypes
bool vote(string name);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

    int voter_count = get_int("Number of voters: ");

    // Loop over all voters
    for (int i = 0; i < voter_count; i++)
    {
        string name = get_string("Vote: ");

        // Check for invalid vote
        if (!vote(name))
        {
            printf("Invalid vote.\n");
        }
    }



    // Display winner of election
    print_winner();
}

// Update vote totals given a new vote
bool vote(string name)
{
    int j;
    int result;
    for (j = 0; j < candidate_count; j++)
    {
        result = strcmp(name, candidates[j].name);
        if (result == 0)
        {
            candidates[j].votes += 1;
            return true;
        }
        else
        {
            continue;
        }
    }
    return 0;
}

// Print the winner (or winners) of the election
void print_winner(void)
{
    // Selection sort is fastest for finding highest int
    int max = candidates[0].votes;
    for (int k = 0; k < candidate_count; k++)
    {
        if (max < candidates[k].votes)
        {
            max = candidates[k].votes;
        }
    }

    // Find candidates which match max score
    for (int l = 0; l < candidate_count; l++)
        if (candidates[l].votes == max)
        {
            printf("%s\n", candidates[l].name);
        }
    return;
}
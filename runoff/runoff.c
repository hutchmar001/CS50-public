#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max voters and candidates
#define MAX_VOTERS 100
#define MAX_CANDIDATES 9

// preferences[i][j] is jth preference for voter i
int preferences[MAX_VOTERS][MAX_CANDIDATES];

// Candidates have name, vote count, eliminated status
typedef struct
{
    string name;
    int votes;
    bool eliminated;
}
candidate;

// Array of candidates
candidate candidates[MAX_CANDIDATES];

// Numbers of voters and candidates
int voter_count;
int candidate_count;

// Function prototypes
bool vote(int voter, int rank, string name);
void tabulate(void);
bool print_winner(void);
int find_min(void);
bool is_tie(int min);
void eliminate(int min);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: runoff [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX_CANDIDATES)
    {
        printf("Maximum number of candidates is %i\n", MAX_CANDIDATES);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
        candidates[i].eliminated = false;
    }

    voter_count = get_int("Number of voters: ");
    if (voter_count > MAX_VOTERS)
    {
        printf("Maximum number of voters is %i\n", MAX_VOTERS);
        return 3;
    }

    // Keep querying for votes
    for (int i = 0; i < voter_count; i++)
    {

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            // Record vote, unless it's invalid
            if (!vote(i, j, name))
            {
                printf("Invalid vote.\n");
                return 4;
            }
        }

        printf("\n");
    }

    // Keep holding runoffs until winner exists
    while (true)
    {
        // Calculate votes given remaining candidates
        tabulate();

        // Check if election has been won
        bool won = print_winner();
        if (won)
        {
            break;
        }

        // Eliminate last-place candidates
        int min = find_min();
        bool tie = is_tie(min);

        // If tie, everyone wins
        if (tie)
        {
            for (int i = 0; i < candidate_count; i++)
            {
                if (!candidates[i].eliminated)
                {
                    printf("%s\n", candidates[i].name);
                }
            }
            break;
        }

        // Eliminate anyone with minimum number of votes
        eliminate(min);

        // Reset vote counts back to zero
        for (int i = 0; i < candidate_count; i++)
        {
            candidates[i].votes = 0;
        }
    }
    return 0;
}

// Record preference if vote is valid
bool vote(int voter, int rank, string name)
{
    int l = 0;
    for (int j = 0; j < voter_count; j++)
    {
        for (int k = 0; k < candidate_count; k++)
            {
            int result = strcmp(name, candidates[k].name);
            printf("%d\n", result);
            if (result == 0)
            {
            preferences[voter][rank] = l;
            printf("%d\n", preferences[voter][rank]);
            printf("%d\n", voter);
            printf("%d\n", rank);
            l++;
            return true;
            }
            else
            {
            l++;
            continue;
            }
            }

}

return false;
}

// Tabulate votes for non-eliminated candidates
void tabulate(void)
{
    int o;
    for (int m = 0; m < voter_count; m++)
    {
        for (int n = 0; n < candidate_count; n++)
        {
            o = preferences[m][n];
            if (candidates[o].eliminated == false)
            {

                candidates[o].votes +=1;
                printf("%d\n", candidates[o].votes);
                break;
            }
        }
    }
}

// Print the winner of the election, if there is one
bool print_winner(void)
{
    for (int p = 0; p < candidate_count; p++)
    {
        printf("%d\n", candidates[p].votes);
        printf("%d\n", voter_count);
        if (candidates[p].votes / voter_count > 0.5)
            {
                printf("%s\n", candidates[p].name);
                return true;
            }
    else
    {
        continue;
    }
    }
    return false;
}

// Return the minimum number of votes any remaining candidate has
int find_min(void)
{
    int min = candidates[0].votes;
    for (int q = 1; q < candidate_count; q++)
        {
            if (min > candidates[q].votes)
        {
            min = candidates[q].votes;
        }
        }
    return min;
}

// Return true if the election is tied between all candidates, false otherwise
bool is_tie(int min)
{
    int max = candidates[0].votes;
    for (int r = 1; r < candidate_count; r++)
        {
            if (max < candidates[r].votes)
        {
            max = candidates[r].votes;
        }
        }
    for (int s = 0; s < candidate_count; s++)
        {
            if (candidates[s].votes < max)
            {
                return false;
            }
            else
            {
                continue;
            }
        }
    return true;
}

// Eliminate the candidate (or candidates) in last place
void eliminate(int min)
{

    return;
}
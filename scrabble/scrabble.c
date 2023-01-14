#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string word);

int main(void)
{
    // Get input words from both players
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Score both words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // TODO: Print the winner
    printf("%i\n", score1);
    printf("%i\n", score2);

    if (score1 > score2)
    {
        printf("Player 1 wins!");
    }
    else if (score2 > score1)
    {
        printf("Player 2 wins!");
    }
    else
    {
        printf("Tie!");
    }
}

int compute_score(string word)
{
    int i;
    int pts = 0;
    for (i = 0; i < (strlen(word)); i++)
    {
        if (isupper(word[i]) || (islower(word[i]))) // As long as character is upper or lower case
        {
            char str[] = {word[i]}; // Makes character into string
            int num = strtol(str, NULL, 36) - 10; //Converts letter to number using base 36
            pts += POINTS[num]; //Adds value found at index in POINTS, determined by num
        }
    };
    return pts;
    // TODO: Compute and return score for string
}

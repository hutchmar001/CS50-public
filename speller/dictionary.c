// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO
    int total = 0;
    for (int pos = 0; pos < strlen(word); pos++)
        total += atoi(&word[pos]);
    return total % N;
}

FILE *infile;
int count = 1;

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    infile = fopen(dictionary, "r");
    char buffer[10000];
    while (fscanf(infile, "%s", buffer) != EOF)
    {
        node *new_node = malloc(sizeof(node));
    }
    for (int j = 0; j < strlen(buffer); j++)
    {
        char txt[1];
        txt[0] = buffer[j];
        char blank[1];
        blank[0] = ' ';
        int result = memcmp(txt, blank, 1);
        if (result == 0)
        {
            count++;   //if a letter is a blank, add to word count
        }
    }
    if (infile)
    {
        return true;
    }
    return false;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    if (count > 0)
    {
        printf("%d\n", count);
        return count;
    }
    else
    {
        return 0;
    }
}


// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    if (infile)
    {
        return true;
        fclose(infile);
    }
    return false;
}



















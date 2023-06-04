// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>
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
    node *cursor = table[hash(word)];
    while (cursor != NULL)
    {
        int result = strcasecmp(cursor->word, word); //start here
        if (result == 0)
        {
            return true;
        }
        cursor = cursor->next;
    }
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
int count = 0;

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    infile = fopen(dictionary, "r");
    if (infile == NULL)
    {
        printf("Problem opening file.");
        return false;
    }
    char buffer[45];
    node *root = malloc(sizeof(node));
    while (fscanf(infile, "%s", buffer) != EOF)
    {
        node *new_node = malloc(sizeof(node));
        if (new_node == NULL)
        {
            unload();
            return false;
        }
        strcpy(new_node->word, buffer);
        new_node->next = root;
        root = new_node;
        
        count++;
    }
    return true;
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
    for (int i = 0; i < N; i++)
    {
    node *cursor = table[i];
    while (cursor != NULL)
    {
        node *temp = cursor;
        cursor = cursor->next;
        free(temp);
    }
    }
    return true;
}











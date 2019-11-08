// MARC OMAR HADDAD
// CS50 - Problem Set 4
// August 30, 2019

// Implements a dictionary's functionality

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#include "dictionary.h"

// Represents number of children for each node in a trie
#define N 27

// Represents a node in a trie
typedef struct node
{
    bool is_word;
    struct node *children[N];
}
node;

// Represents a trie
node *root;

int SIZE;
node* AllocateNode(void);
void destroy(node *head);

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{

    SIZE = 0;
    // Initialize trie
    root = malloc(sizeof(node));
    if (root == NULL)
    {
        free(root);
        return false;
    }
    root->is_word = false;
    for (int i = 0; i < N; i++)
    {
        root->children[i] = NULL;
    }

    // Open dictionary
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        unload();
        return false;
    }

    // Buffer for a word
    char word[LENGTH + 1];

    node *head = root;

    // Insert words into trie
    while (fscanf(file, "%s", word) != EOF)
    {
        int i = 0;
        head = root;
        while (word[i])
        {
            int box = word[i] - 'a';
            if (head->children[box] == NULL)
            {
                head->children[box] = AllocateNode();
            }
            else
            {
                head = head->children[box];
                i++;
            }
        }
        head->is_word = true;
        SIZE++;

    }
    // Close dictionary
    fclose(file);

    // Indicate success
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    if (SIZE > 0)
    {
        return SIZE;
    }
    else
    {
        return 0;
    }
}

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    node *head = root;
    char *lower = malloc(sizeof(word));
    for (int i = 0, n = strlen(word); i < n; i++)
    {
        if (islower(word[i]) == 0)
        {
            lower[i] = tolower(word[i]);
        }
        else
        {
            lower[i] = word[i];
        }
        if (head->children[(lower[i] - 'a')] == NULL)
        {
            free(lower);
            return false;
        }
        head = head->children[(lower[i] - 'a')];
    }
    if (head->is_word == true)
    {
        free(lower);
        return true;
    }
    else
    {
        free(lower);
        return false;
    }
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    node *head = root;
    destroy(head);
    return true;
    // Recursively destroys all nodes from last to first.
}
void destroy(node *head)
{
    for (int i = 0, n = N; i < n; i++)
    {
        // Checks if the current node points to NULL, and stops the func if it does.
        if (head->children[i] == NULL)
        {
            // Frees the memory of the first node to be deleted (i.e. the last node in our trie).
            continue;
        }
        // Runs this function again if the current node points to another.
        destroy(head->children[i]);
        free(head->children[i]);
        head->is_word = false;
    }
}

node *AllocateNode(void)
{
    node *head = root;
    head = malloc(sizeof(node));
    if (head == NULL)
    {
        free(head);
        return false;
    }
    head->is_word = false;
    for (int i = 0; i < N; i++)
    {
        head->children[i] = NULL;
    }
    return head;
}

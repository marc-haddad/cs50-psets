// Marc Omar Haddad
// CS50 - Problem Set 3
// August 27, 2019

#include <stdio.h>
#include <stdlib.h>

// This program recovers images from corrupted file 'card.raw'.

int main(int argc, char *argv[])
{
    // Checks for correct # of args.
    if (argc != 2)
    {
        fprintf(stderr, "Usage: ./recover filename\n");
        return 1;
    }
    // Opens file to read from specified arg.
    FILE *file = fopen(argv[1], "r");
    if (file == NULL)
    {
        fprintf(stderr, "Could not open file\n");
        return 2;
    }
    // Allocates 512 bytes of memory.
    unsigned char *buffer = malloc(512);
    if (buffer == NULL)
    {
        fprintf(stderr, "Could not allocate memory\n");
        return 3;
    }
    int jpeg_count = 0;
    FILE *jpeg = NULL;
    // Initializes reading of file into 'buffer' in single chunks of 512 bytes until entire file is read.
    while (fread(buffer, 1, 512, file))
    {
        // Locates the start of any jpeg.
        if ((buffer[0] == 0xff) && (buffer[1] == 0xd8) && (buffer[2] == 0xff) && ((buffer[3] & 0xef) == 0xe0))
        {
            // Closes any previously opened jpeg files.
            if (jpeg_count > 0)
            {
                fclose(jpeg);
            }
            // Allocates memory for jpeg file names and defines naming format.
            char jpeg_name[8];
            sprintf(jpeg_name, "%03i.jpg", jpeg_count);
            // Creates file to write jpeg data.
            jpeg = fopen(jpeg_name, "w");
            // Keeps track of jpeg count when new files are created.
            jpeg_count++;
        }
        // This forces the loop to end here until the start of the first jpeg file has been found.
        if (jpeg_count == 0)
        {
            continue;
        }
        // Here we write from 'buffer' to our file 'jpeg'.
        fwrite(buffer, 1, 512, jpeg);
    }
    free(buffer);
    fclose(file);
    return 0;
}

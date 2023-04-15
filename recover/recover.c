#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


int main(int argc, char *argv[])
{
   FILE *file = fopen(argv[1], "r"); // open mem card for reading
   if (file == NULL)
   {
       printf("File cannot be opened for reading.");
       return 1;
   }
   unsigned char buffer[512]; // unsigned char b/c dealing with binary data
   int i = 0;
   bool foundafile = false;
   char jpegs[50];
   FILE *img = NULL;
   while (fread(buffer, 1, 512, file) == 512) // repeat until end of file
   {
       if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0) // if new jpg found
       {
           if (i > 0) // if not first file
           {
               fclose(img); // close previous file
           }
           sprintf(&jpegs[0], "%03i.jpg", i); // create first file
           img = fopen(&jpegs[0], "w");
           fwrite(&buffer[0], 1, 512, img);
           foundafile = true;
           i++;
       }
       else
       {
           if (foundafile) //
           {
               fwrite(&buffer[0], 1, 512, img); // keep writing to previous file
           }
       }
   }
   fclose(img); // close any remaining files
   fclose(file);
   return 0;
}

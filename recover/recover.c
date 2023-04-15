#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main(int argc, char *argv[])
{
   FILE *file = fopen(argv[1], "r");
   if (file == NULL)
   {
       printf("File cannot be opened for reading.");
       return 1;
   }
   unsigned char buffer[512];
   int i = 0;
   bool foundTheFile = false;
   char jpegs[50];
   FILE *img = NULL;
   // if end of file
   while (fread(buffer, 1, 512, file) == 512) {
       // New JPEG found
       if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0) {
           // create first file
           if (i!=0) {
               fclose(img);
               i++;
           }
           sprintf(&jpegs[0], "%03i.jpg", i);
           img = fopen(&jpegs[0], "w");
           fwrite(&buffer[0], 1, 512, img);
           foundTheFile = true;
       }
       // Keep writing to the previous file.
       else {
           if (foundTheFile) {
               fwrite(&buffer[0], 1, 512, img);
           }
       }
   }
   fclose(img);
   fclose(file);
   return 0;
}

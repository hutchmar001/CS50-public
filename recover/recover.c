/*
*open memory card
*repeat until end of card
*   read 512 bytes into a buffer
*   if start of new jpeg
*       if 1st jpeg
           write 000.jpeg and 1st file
       else
           close previous file so you can open new one
   else
       if already found jpeg, keep writing to it
close anything left open
*/


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
   char jpegs[50];
   FILE *img = NULL;
   // if end of file
   while (!feof(file))
   {
       // read 512 bytes.
       if (fread(buffer, 1, 512, file) == 512) {
           // New JPEG found
           if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0) {
               // create first file
               if (i==0) {
                   sprintf(&jpegs[i], "%03i.jpg", i);
                   img = fopen(&jpegs[i], "w");
                   fwrite(&buffer[0], 1, 512, img);
               }
               // write into new file
               else {
                   fclose(img);
                   i++;
                   sprintf(&jpegs[i], "%03i.jpg", i);
                   img = fopen(&jpegs[i], "w");
                   fwrite(&buffer[0], 1, 512, img);
               }
           }
           // Keep writing to the previous file.
           else {
               fwrite(&buffer[0], 1, 512, img);
           }
       }
   }
   fclose(file);
   return 1;
}




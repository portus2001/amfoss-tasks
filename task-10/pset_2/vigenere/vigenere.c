#include <cs50.h>
#include <stdio.h>
#include<ctype.h>
#include<string.h>
#include<stdlib.h>

int main(int argc, char** argv)//argc contains the number of arguements that we have given.each arguement is seperated by a space
{  //argv puts the two arguements in a string where the first element is the first arguement and the second element is the second arguement
    if(argc!=2)
    {
        printf("Usage: ./vigenere k\n");
        return 1;
    }
    char cyphertext[100];
    string key = argv[1];
    int lenkey = 0;
    lenkey = strlen(key);
    for (int i = 0; i < lenkey; i++){
        if (!isalpha(key[i])){
            printf("Usage: ./vigenere k\n");
            return 1;
        }
    }
    string plaintext = get_string("plaintext: ");
    int len = 0;
    len = strlen(plaintext);
    //loops over the plaintext and output ciphertext
    for (int i = 0, index = 0; i < len; i++)
    {//cyphertext[i] = (plaintext[i] - ('a'or 'A') + k) % 26 + ('a'or 'A'))
        if (isalpha(plaintext[i])){
            if (islower(plaintext[i])){
               cyphertext[i] = (plaintext[i] - 'a' + toupper(key[index]) - 'A') % 26 + 'a';

            }
            else if(isupper(plaintext[i])){
                  cyphertext[i] = (plaintext[i] - 'A' + toupper(key[index]) - 'A') % 26 + 'A';
            }
            index = (index + 1) % lenkey;
        }
        else{
            cyphertext[i] = plaintext[i];
        }


    }

    printf("ciphertext: ");
    for(int i=0;i<strlen(cyphertext);i++)
    {
      printf("%c",cyphertext[i]);

    }
    printf("\n");
}
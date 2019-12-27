#include <cs50.h>
#include <stdio.h>
#include<ctype.h>
#include<string.h>
#include<stdlib.h>

int main(int argc, char** argv)//argc contains the number of arguements that we have given.each arguement is seperated by a space
{  //argv puts the two arguements in a string where the first element is the first arguement and the second element is the second arguement
    if(argc!=2)
    {
        printf("Usage: ./caesar k\n");
        return 1;
    }
    char cyphertext[100];
    int key = atoi(argv[1]);//atoi converts a string to an integer type value.
    if (key < 0){
        printf("key should be positive\n");
        return 1;
    }
    string plaintext = get_string("plaintext: ");
    int len = 0;
    len = strlen(plaintext);
    //loops over the plaintext and output ciphertext
    for (int i = 0; i < len; i++)
    {//cyphertext[i] = (plaintext[i] - ('a'or 'A') + k) % 26 + ('a'or 'A'))
        if (islower(plaintext[i])){
            cyphertext[i] = (plaintext[i] - 'a' + key) % 26 + 'a';
        }
        else if(isupper(plaintext[i])){
            cyphertext[i] = (plaintext[i] - 'A' + key) % 26 + 'A';
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
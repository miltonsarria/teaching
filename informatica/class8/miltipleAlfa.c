/*
   Title: Vigenere Cipher
   
   Description: This program taes in a plain text and produces a cipher of that text using the vigenere cipher
   
   Usage:
   Please enter a sentence or word you want to encrypt: defend
   The ciphered text with (Key shift = 'hello') is: kiqpbk
   
   How it works:
   Vigenere Cipher Encryption Formula:
   C[i] = (p[i] + k[i mod klength] ) mod N, C = cipher, k = secret key (word), p = sentence or plainText or word, N = number of letters in the alphabet
   
   Suppose  letter a=0, b=1, c=2, d=3, e=4, f=5, g=6, h=7, i=8, j=9, k=10, l=11, m=12, n=13, o=14, p=15, q=16, .. z=25
            key = 'hello'
            ( (int)Letter + (int)keyLetter) mod 26 ==> return a ciphered letter as a number, aka cipherValue
                                                   ==> (char)cipherValue = '[some letter]'
   
                                                NOTE: ASCII 'a'=97, 'b'=98, 'c'=99 .. (for lower case letters)
                                                      ASCII 'A' = 65, 'B'=66, 'C'=67 .. (for upper case letters)
*/

//Initialze libraries
# include <stdio.h> //fgets() , printf(0, stdin 
# include <string.h> //strlen()
# include <ctype.h> // isupper() , islower() , tolower(), toupper(), isalpha()

//Declare vigenere cipher
void vigenereCipher(char* plainText, char* k);

int main(){
	
	char* k = "hello"; //Assign the key
	char plainText[101]; //Declare a string for a users text to encrypt
	
	//Ask the user for a sentence or word to encrypt
	printf("Please enter a sentence or word you want to encrypt: ");
	
	//Get the users input (the plain text)
	fgets(plainText, sizeof(plainText), stdin);
	
	//print the encrypted plain text
	printf("The ciphered text with (Key shift = '%s') is: ", k);
	
	//Print the actual encryption
	vigenereCipher(plainText, k);
	
	
	return 0;
}

//C[i] = (p[i] + k[i mod klength] ) mod N, C = cipher, k = secret key (word), p = sentence or plainText or word, N = number of letters in the alphabet
void vigenereCipher(char* plainText, char* k){
	
	int i;
	char cipher;
	int cipherValue;
	int len = strlen(k);
	
	//Loop through the length of the plain text string
	for(i=0; i<strlen(plainText); i++){
		
		//if the character is lowercase, where range is [97 -122]
		if(islower(plainText[i]))
		{
			cipherValue = ( (int)plainText[i]-97 + (int)tolower(k[i % len])-97 ) % 26 +97;
			cipher = (char)cipherValue;
		}
		else // Else it's upper case, where letter range is [65 - 90]
		{
			cipherValue = ( (int)plainText[i]-65 + (int)toupper(k[i % len])-65 ) % 26 +65;
			cipher = (char)cipherValue;
		}
		
		//Print the ciphered character if it is alphanumeric (a letter)
		if(isalpha(plainText[i]))
		{
			printf("%c", cipher);
		}
		else //if the character is not a letter then print the character (e.g. space)
		{
			printf("%c", plainText[i]);
		}
	}
	
	
}

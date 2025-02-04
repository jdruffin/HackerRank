#include <math.h>
#include <stdio.h>


int main() {

  /* Enter your code here. Read input from STDIN. Print output to STDOUT */
  char ch;
  scanf("%c", &ch);

  char word[100];
  scanf("%s", word);

  scanf("\n");

  char sentence[100];
  scanf("%[^\n]%*c", sentence);

  printf("%c\n", ch);
  printf("%s\n", word);
  printf("%s\n", sentence);

  return 0;
}
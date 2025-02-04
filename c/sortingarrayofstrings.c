#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int lexicographic_sort(const char *a, const char *b) { return strcmp(a, b); }

int lexicographic_sort_reverse(const char *a, const char *b) {
  return -strcmp(a, b);
}

int sort_by_number_of_distinct_characters(const char *a, const char *b) {
  // Count distinct characters in string a
  int count_a[256] = {0};
  int distinct_count_a = 0;
  for (const char *p = a; *p != '\0'; p++) {
    if (!count_a[(unsigned char)*p]) {
      distinct_count_a++;
      count_a[(unsigned char)*p] = 1;
    }
  }

  // Count distinct characters in string b
  int count_b[256] = {0};
  int distinct_count_b = 0;
  for (const char *p = b; *p != '\0'; p++) {
    if (!count_b[(unsigned char)*p]) {
      distinct_count_b++;
      count_b[(unsigned char)*p] = 1;
    }
  }

  // Compare distinct character counts
  if (distinct_count_a == distinct_count_b) {
    return lexicographic_sort(a, b);
  }
  return distinct_count_a - distinct_count_b;
}

int sort_by_length(const char *a, const char *b) {
  int len_a = strlen(a);
  int len_b = strlen(b);
  if (len_a == len_b) {
    return lexicographic_sort(a, b);
  }
  return len_a - len_b;
}

void string_sort(char **arr, const int len,
                 int (*cmp_func)(const char *a, const char *b)) {

  // bubble sort
  ;
  for (int i = 0; i < len - 1; i++) {
    for (int j = 0; j < len - i - 1; j++) {

      // swap a and b is a is bigger
      if (cmp_func(arr[j], arr[j + 1]) > 0) {

        char *temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
      }
    }
  }
}

int main() {
  int n;
  scanf("%d", &n);

  char **arr;
  arr = (char **)malloc(n * sizeof(char *));

  for (int i = 0; i < n; i++) {
    *(arr + i) = malloc(1024 * sizeof(char));
    scanf("%s", *(arr + i));
    *(arr + i) = realloc(*(arr + i), strlen(*(arr + i)) + 1);
  }

  string_sort(arr, n, lexicographic_sort);
  for (int i = 0; i < n; i++)
    printf("%s\n", arr[i]);
  printf("\n");

  string_sort(arr, n, lexicographic_sort_reverse);
  for (int i = 0; i < n; i++)
    printf("%s\n", arr[i]);
  printf("\n");

  string_sort(arr, n, sort_by_length);
  for (int i = 0; i < n; i++)
    printf("%s\n", arr[i]);
  printf("\n");

  string_sort(arr, n, sort_by_number_of_distinct_characters);
  for (int i = 0; i < n; i++)
    printf("%s\n", arr[i]);
  printf("\n");
}
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main() {
  int n;
  int m;

  float o;
  float p;

  scanf("%d %d", &n, &m);

  scanf("%f %f", &o, &p);

  printf("%d %d\n", n + m, n - m);
  printf("%.1f %.1f", o + p, o - p);

  return 0;
}
#ifndef _LIBRARY_H
#define _LIBRARY_H

/* A C data structure */
typedef struct Point {
    double x, y;
} Point;

int gcd(int x, int y);

int in_mandel(double x0, double y0, int n);

int divide(int a, int b, int *remainder);

double avg(double *a, int n);

double distance(Point *p1, Point *p2);

#endif
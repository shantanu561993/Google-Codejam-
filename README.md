Google-Codejam-
===============
1A.py
=========
You receive a credit C at a local store and would like to buy two items. You first walk through the store and create a list L of all available items. From this list you would like to buy two items that add up to the entire value of the credit. The solution you provide will consist of the two integers indicating the positions of the items in your list (smaller number first).

Input

The first line of input gives the number of cases, N. N test cases follow. For each test case there will be:

    One line containing the value C, the amount of credit you have at the store.
    One line containing the value I, the number of items in the store.
    One line containing a space separated list of I integers. Each integer P indicates the price of an item in the store.
    Each test case will have exactly one solution.

Output

For each test case, output one line containing "Case #x: " followed by the indices of the two items whose price adds up to the store credit. The lower index should be output first.

Limits

5 ≤ C ≤ 1000
1 ≤ P ≤ 1000

Small dataset

N = 10
3 ≤ I ≤ 100

Large dataset

N = 50
3 ≤ I ≤ 2000

Sample

Input
	
Output
3
100
3
5 75 25
200
7
150 24 79 50 88 345 3
8
8
2 1 9 4 4 56 90 3
	Case #1: 2 3
Case #2: 1 4
Case #3: 4 5

https://code.google.com/codejam/contest/351101/dashboard#s=p0

1B.py
==============
Given a list of space separated words, reverse the order of the words. Each line of text contains L letters and W words. A line will only consist of letters and space characters. There will be exactly one space character between each pair of consecutive words.

Input

The first line of input gives the number of cases, N.
N test cases follow. For each test case there will a line of letters and space characters indicating a list of space separated words. Spaces will not appear at the start or end of a line.

Output

For each test case, output one line containing "Case #x: " followed by the list of words in reverse order.

Limits

Small dataset

N = 5
1 ≤ L ≤ 25

Large dataset

N = 100
1 ≤ L ≤ 1000

Sample

Input
	
Output
3
this is a test
foobar
all your base
	Case #1: test a is this
Case #2: foobar
Case #3: base your all

https://code.google.com/codejam/contest/351101/dashboard#s=p1

1C.py
==================
 You are given two vectors v1=(x1,x2,...,xn) and v2=(y1,y2,...,yn). The scalar product of these vectors is a single number, calculated as x1y1+x2y2+...+xnyn.

Suppose you are allowed to permute the coordinates of each vector as you wish. Choose two permutations such that the scalar product of your two new vectors is the smallest possible, and output that minimum scalar product.

Input
The first line of the input file contains integer number T - the number of test cases. For each test case, the first line contains integer number n. The next two lines contain n integers each, giving the coordinates of v1 and v2 respectively.

Output

For each test case, output a line

Case #X: Y

where X is the test case number, starting from 1, and Y is the minimum scalar product of all permutations of the two given vectors.

Limits

Small dataset

T = 1000
1 ≤ n ≤ 8
-1000 ≤ xi, yi ≤ 1000

Large dataset

T = 10
100 ≤ n ≤ 800
-100000 ≤ xi, yi ≤ 100000

Sample

Input
  	
Output
 
2
3
1 3 -5
-2 4 1
5
1 2 3 4 5
1 0 1 0 1

	Case #1: -25
Case #2: 6

https://code.google.com/codejam/contest/32016/dashboard#s=p0

mkdir.py
=============
 On Unix computers, data is stored in directories. There is one root directory, and this might have several directories contained inside of it, each with different names. These directories might have even more directories contained inside of them, and so on.

A directory is uniquely identified by its name and its parent directory (the directory it is directly contained in). This is usually encoded in a path, which consists of several parts each preceded by a forward slash ('/'). The final part is the name of the directory, and everything else gives the path of its parent directory. For example, consider the path:

/home/gcj/finals

This refers to the directory with name "finals" in the directory described by "/home/gcj", which in turn refers to the directory with name "gcj" in the directory described by the path "/home". In this path, there is only one part, which means it refers to the directory with the name "home" in the root directory.

To create a directory, you can use the mkdir command. You specify a path, and then mkdir will create the directory described by that path, but only if the parent directory already exists. For example, if you wanted to create the "/home/gcj/finals" and "/home/gcj/quals" directories from scratch, you would need four commands:

mkdir /home
mkdir /home/gcj
mkdir /home/gcj/finals
mkdir /home/gcj/quals

Given the full set of directories already existing on your computer, and a set of new directories you want to create if they do not already exist, how many mkdir commands do you need to use?
Input

The first line of the input gives the number of test cases, T. T test cases follow. Each case begins with a line containing two integers N and M, separated by a space.

The next N lines each give the path of one directory that already exists on your computer. This list will include every directory already on your computer other than the root directory. (The root directory is on every computer, so there is no need to list it explicitly.)

The next M lines each give the path of one directory that you want to create.

Each of the paths in the input is formatted as in the problem statement above. Specifically, a path consists of one or more lower-case alpha-numeric strings (i.e., strings containing only the symbols 'a'-'z' and '0'-'9'), each preceded by a single forward slash. These alpha-numeric strings are never empty.
Output

For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is the number of mkdir you need.
Limits

1 ≤ T ≤ 100.
No path will have more than 100 characters in it.
No path will appear twice in the list of directories already on your computer, or in the list of directories you wish to create. A path may appear once in both lists however. (See example case #2 below).
If a directory is listed as being on your computer, then its parent directory will also be listed, unless the parent is the root directory.
The input file will be no longer than 100,000 bytes in total.
Small dataset

0 ≤ N ≤ 10.
1 ≤ M ≤ 10.
Large dataset

0 ≤ N ≤ 100.
1 ≤ M ≤ 100.
Sample

Input
  	
Output
 
3
0 2
/home/gcj/finals
/home/gcj/quals
2 1
/chicken
/chicken/egg
/chicken
1 3
/a
/a/b
/a/c
/b/b
	Case #1: 4
Case #2: 0
Case #3: 4

https://code.google.com/codejam/contest/635101/dashboard#s=p0



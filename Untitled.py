Python 3.5.1 (v3.5.1:37a07cee5969, Dec  5 2015, 21:12:44) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
total = 0
>>> for i in range(10):
	print(i)
	print(total)

0
0
1
0
2
0
3
0
4
0
5
0
6
0
7
0
8
0
9
0
>>> for i in range(10):
	total+=i
	print(i)
	print(total)

	
0
0
1
1
2
3
3
6
4
10
5
15
6
21
7
28
8
36
9
45
>>> total = 0
for total in range(10):
	total+=i
	print(i)
	print(total)
	
SyntaxError: multiple statements found while compiling a single statement
>>> total = 0
for total in range(10):
	total = total + 1
	print(i)
	print(total)
	
SyntaxError: multiple statements found while compiling a single statement
>>> total = 0
>>> for i in range(10):
	total = total + 1
	print(i)
	print(total)

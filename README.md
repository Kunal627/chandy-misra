# Chandy Misra Algo implementation
===================================

The program takes to inputs path and initsite.

path:
=====
Is the file path of input graph which is represented as an adjacency matrix where 1 in a column represents a link from row to column site

example of input site matrix:

Input Matrix: Is provided in csv format, where row and columns represent site and 1 in value represents a link 

0,1,0,0,0 <br />
0,0,1,0,0 <br />
0,0,0,1,0 <br />
0,0,0,0,1 <br />
1,0,0,0,0 <br />

is interpreted as following

<pre>
    S1    S2     S3    S4   S5
S1   0     1      0     0    0

S2   0     0      1     0    1

S3   0     0      0     1    0

S4   0     0      0     0    1

S5   1     0      0     0    0

</pre>

This implies there is an edge with start from row site to column site

S1 ---> S2 ---> S3 ---> S4 ---> S5 <br />
^                               |  <br />
|_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|

initsite
========
It is the initiating site. This parameter takes an integer value. If this value is not supplied then the default site is read from initiator.json in data folder.


Examples:
========

EX1: 
====
For the site matrix above the program will flag a Dead lock as site 1 is visited again which forms a loop.

EX2:
====
0,1,0,0,0
0,0,1,0,0
0,0,0,1,0
0,0,0,0,1
0,0,0,1,0

say site 1 is the initiator, this will also result in a deadlock. As there is a cycle formed between site 5 and 4.

S1 --> S2 --> S3 --> S4 --> S5
                      ^      |
                      |_ _ _ |


EX3:
====

0,1,0,0,0
0,0,1,0,0
0,0,0,1,0
0,0,0,0,1
0,0,0,0,0

say site 1 is the initiator, There is no cycle and this will NOT result in Deadlock.

S1 --> S2 --> S3 --> S4 --> S5


How to run the program
======================
1. Prerequisites - Install Python 3.7. 
2. Install dependencies from requirements.txt using following command 
   pip install -r requirements.txt
3. Navigate to the chandy-misra\src directory and run the following command to execute the program 
   python .\chandymisra.py -path <provide input file path here> -initsite <provide initiating site number>

   

This program simulates the Chandy-Misra OR model. The code is implemented in C++. 

Prerequisites: 
=============
* IDE used - Dev C++  <br />

For running the code.
=====================
* copy the files on the local drive  <br />
* click on the exe file  <br />


Example wait for graph
======================

* The code expects number of sites as an input. The number of sites need to be greater than 1.  <br />
* Input the wait for graph in form of adjaceny matrix. where 1 denotes the edge from one process to another  <br />

e.g

<pre>
The following wait for graph 


S1 --->  S2 ---> S3 ---> S4  
^                         |
| _ _ _ _ _ _ _ _ _ _ _ _ |

Is represented by following adjacency matrix

    S1   S2   S3    S4
	
S1  0    1    0     0

S2  0    0    1     0

S3  0    0    0     1

S4  1    0    0     0


The following input is needed for the program:

Enter number of sites(The sites should be greater than 1):
2
Enter number of processes for site1: (The number of processors should be greater than 1)
2
Enter number of processes for site2: (The number of processors should be greater than 1)
2
Total number of sites=2; Total number of processes=4
Enter the wait graph for processes; Enter 1 if the process is dependent and 0 if not.
From Process number 1 to : 1(1/0) :0
From Process number 1 to : 2(1/0) :1
From Process number 1 to : 3(1/0) :0
From Process number 1 to : 4(1/0) :0
From Process number 2 to : 1(1/0) :0
From Process number 2 to : 2(1/0) :0
From Process number 2 to : 3(1/0) :1
From Process number 2 to : 4(1/0) :0
From Process number 3 to : 1(1/0) :0
From Process number 3 to : 2(1/0) :0
From Process number 3 to : 3(1/0) :0
From Process number 3 to : 4(1/0) :1
From Process number 4 to : 1(1/0) :1
From Process number 4 to : 2(1/0) :0
From Process number 4 to : 3(1/0) :0
From Process number 4 to : 4(1/0) :0

Enter the process initiating the probe (The number should be between 1 and number of processes)
1

</pre>


Output of the wait for graph given above with initiator as 1.

<pre>

Initiating Probe.....

DIRECTION        PROBE   MESSAGES        WAIT FLAG
 S1 --> S2     (1,1,2) ,        1 ,     1
 S2 --> S3     (1,2,3) ,         1 ,     1
 S3 --> S4     (1,3,4) ,         1 ,     1
 S4 --> S1     (1,4,1) --------> DEADLOCK DETECTED HERE
Number of deadlocks detected:1
Printing wait message array
1
1
1
1
Number of knots detected:0

</pre>

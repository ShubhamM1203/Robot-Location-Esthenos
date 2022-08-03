# Robot-Location-Esthenos

In this code I set two extreme position
Initial Constraints = (0, 0)
Final Constraints = (3, 4)

M -> Move one unit curresponding direction
N -> Turn North
S -> Turn South
E -> Turn East
W -> Turn West

The move "M" changes either rowwise or coumnwise as per following example;

Input command: "MSMMEMM";
Befor first move
    0       1       2       3       4
0  (pos, N)
1
2
3
First move 'M' :-
    0       1       2       3       4
0  
1  (pos, N)
2
3
Turn South 'S' :-
    0       1       2       3       4
0  
1  (pos, S)
2
3
Second move 'M' towards south :-
    0       1       2       3       4
0  
1  
2  (pos, S)
3
Third move 'M' towards south :-
    0       1       2       3       4
0  
1  
2  
3  (pos, S)
Turn South 'E' :-
    0       1       2       3       4
0  
1  
2
3 (pos, E)
Fourth move towards East :-
    0       1       2       3       4
0  
1  
2
3        (pos, E)
Final move towards East:-
    0       1       2       3       4
0  
1  
2
3                (pos, E)

After final move the coordinates find in the 2D array is:- (3, 2, E);

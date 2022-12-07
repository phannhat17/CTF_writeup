# Shell Maze

## Challenge description:


## Solution description:
Out task is to solve the maze problem. We are in 'X' position and have to go to the bottom right of the maze
I found a Maze Solver writen in python [here](https://gist.github.com/a613/49d65dc30e98c165d567)
Then write a script to re-config the maze from the server to math the format at maze_solver above.
Here is my script:

```python
from pwn import *
import time
from maze_solver import * # The maze_solver is attached in the same folder

def create_maze(a):
    '''
    This function creates a new maze that have the same format with Maza object in maze_solver
    '''
    while('Move: ' in a):
        a.remove('Move: ')
    while("" in a):
        a.remove("")

    for i in a:
        if i[0] == 'X':
            index = a.index(i)

    a = a[index:]

    for i in range(len(a)):
        a[i] = list(a[i])

    a[0][0] = 'S'
    a[-1][-1] = 'E'

    for i in range(len(a)):
        a[i].insert(0, "#")
        a[i].append('#')
    len_ele = len(a[0])
    wall = ['#' for i in range(len_ele)]
    a.insert(0, wall)
    a.append(wall)

    return(a)

def create_path(maze):
    '''
    This function creates a path to solve the maze
    '''
    sol = []
    a = str(maze)
    b = a.split('\n')
    for i in range(len(b)):
        if '<' in b[i]:
            b[i] = b[i][::-1]

    for i in b:
        for j in list(i):
            if '>' in j or '<' in j or 'V' in j:
                sol.append(j)
    path = ''
    path_test = ''.join(sol)
    if b[1][2] == '#':
        path = 'V' + path_test
    else:
        path = '>' + path_test

    c = list(path)
    return(c)



r = remote('chals.tuctf.com', 30204)
i = 0
main_console_3 =[]
while True:
    
    # First maze
    if i == 0:
        console = r.recv().decode()
        print(console+'\n')
        a = console.split("\n")
        print(a)
        maze = Maze(create_maze(a))
        solution = solve(maze)
        print(maze)
        path = create_path(maze)
        print(path)
        len_path = len(path)
    # The other maze
    else:
        print(main_console_3)
        maze = Maze(create_maze(main_console_3))
        solution = solve(maze)
        print(maze)
        path = create_path(maze)
        print(path)
        len_path = len(path)

    i+=1
    # Send the path that solved to the server
    for j in range(len_path):
        c = str(path[j]) + '\n'
        print(f'Solution: {c}')
        r.send(str(c).encode())
        if j == len_path-1:
            time.sleep(1)
        main_console = r.recv().decode()
        print(main_console)
        print(i)
        index_1 = 0
        # Get the next maze
        main_console_3 = main_console.split("\n")
        for k in main_console_3:
            if k == 'Loading next level...':
                index_1 = main_console_3.index(k)

        main_console_3 = main_console_3[index_1+2:]
```

And the flag is:

```
TUCTF{1_4m_4_7ru3_n37_7r4v3l3r_357269}
```
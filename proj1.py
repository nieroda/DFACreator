
import numpy as np


A = np.array([
    [1, 1, 0, 0],
    [1, 0, 1, 0],
    [1, 0, 0, 1],
    [0, 0, 0, 2]
    ], dtype=object)

A_n = A ^ 100

answer = [1, 0, 0, 0] * A_n * [[1], [1], [1], [0]]
#print(answer)
#exit()
# 1
array = np.array([

    # []
    [0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]], dtype=object)

x = array ^ 137
#[print(a) for a in x]
start = np.array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=object)

accepting = np.array([
            [0],
            [0],
            [0],
            [0],
            [0],
            [0],
            [0],
            [0],
            [0],
            [0],
            [0],
            [0],
            [0],
            [1],
            [1],
            [1],
            [1],
            [1],
            [1],
            [1],
            [1],
            [1],
            [1],
            [1],
            [1],
            [1],
            [1],
            [1],
            [1],
            [1],
            [1],
            [1],
            [1],
            [1],
            [1],
            [1],
            [1]
                        

], dtype=object)
answer = start.dot(x).dot(accepting)
#print(start)
#print(x)
print(answer)

#print(len(answer))
exit()
#array = np.array([[1, 2], [2, 1]], dtype=object)
 
 
#a = array ** 300 
#[print(x) for x in a]

def Pop(queue):
    item = queue[0]
    del queue
    return item

def Push(queue, item):

    queue.insert(0, item)
    return queue

def bfs(state_transition_table, start_state, alphabet):

    #[print(a) for a in state_transition_table]
    #quit()
    edge_input = {i:letter for i, letter in enumerate(alphabet)}
    visited = [0] * len(state_transition_table)
    sequences_found_so_far = [(-1, -1)] * len(state_transition_table)
    queue = []
    #print(visited)
    visited[start_state] = 1
    queue = Push(queue, start_state)

    k = 0
    while queue != []:
        current_state = Pop(queue)
        print('current state', current_state)
        #print(state_transition_table[current_state])
        #print('next states')
        #print(state_transition_table[current_state])
        #print('tuple next states')
        #print([(i, next_state) for i, next_state in enumerate(state_transition_table[current_state]) if i > 0])
        next_states = [(i, next_state) for i, next_state in enumerate(state_transition_table[current_state])]
        #print(next_states)

        # also need the edge input value
        for y in next_states:
            # current state could be 0 and one of the next states could be 0
            #i = y[0]
            #next_state = y[1]
            #print(k)
            (i, next_state) = y
            #print(k, next_state)

            # for catching input where there is no solution
            state_changed = False
            if visited[next_state] == 0:
                # they are all new so this happens for all neighbors
                #print(edge_input[i])

                visited[next_state] = 1

                sequences_found_so_far[next_state] = (current_state, edge_input[i])
                #print(next_state, current_state, sequences_found_so_far[next_state])
                if next_state == 0:
                    print('finished')
                    exit()
                queue = Push(queue, next_state)
            # 0 is an accepting state
            if next_state == 0:
                # what happens if current state = 0?
                print(current_state)
                # need the last link so the recovery process can start on the last character found
                sequences_found_so_far[next_state] = (current_state, edge_input[i])
                #print(next_state, current_state, sequences_found_so_far[next_state])

                print('done')
                #print(sequences_found_so_far, current_state, next_state)
                #exit()
                print()
                # traverse sequences_found_so_far backwards to recover the string

                return recover(sequences_found_so_far, next_state, edge_input)
            #print(sequences_found_so_far)
            k += 1
        k = 0
                

def recover(sequences_found_so_far, next_state, edge_input):
    # 31333
    # reversed = 33313
    # 33313 % 7 = 0
    # tested on alphabet = {1, 3, 5}
    # gives back 553
    # 553 % 7 = 0
    sequence = []
    # this sets prev_state as the current_state > 0
    (prev_state, input_index) = sequences_found_so_far[next_state]

    #print((prev_state, input_index))
    sequence.insert(0, str(input_index))
    while prev_state != 0:
        (prev_state, input_index) = sequences_found_so_far[prev_state]
        #print((prev_state, input_index))

        sequence.insert(0, str(input_index))
        #print(sequence)

    return ''.join(sequence)





# 2
def createArray(input_, k):
  
  # next states are remainders
  # can't visit enough of graph if the remainders never reach 26147
  # can use 10 with 7 because 
  # remainder for order
  # make remainder using the remainders from k, each letter in the alphabet
  # why does it travel down the wrong path?
  return [ [ ( i * 10 + item ) % k for item in input_ ] for i in range(k) ]

#print(bfs(createArray([1, 3], 26147), 0))
# gives an infinite loop
# maybe the test cases have no solutions
# case 2 : Input: k = 198217, Digits permitted: 1
# Shortest multiple of k using digits {1}: integer containing 10962 ones (Your output should be a string of this many 1’s.)
alphabet = [1]
print(bfs(createArray(alphabet, 198217), 0, alphabet))
# works: eactly 10962 1's


#node = {'input_digit': 0, 'prev_digit': }
# find shortest path
'''
def manyBFS(graph, start_vertex, verticies):

  # make a multiway tree in with reverse edges only
  # this allows backward traversal to the root to collect the input digits
  # makes all paths at the same time

  root = {'input_digit': 'null', 'prev_digit': 'null'}
  
  tree = [root]
'''
'''
>>> for i, letter in enumerate(['a', 'b', 'c']):
...     print(i, letter)
... 
0 a
1 b
2 c
>>> 
'''
'''
  next_remainders = [i for i in enumerate(verticies)]
  roots = [root]
  current_level = []
  i = 0
  current_vertex = 0
  new_set_of_next_remainders = []
    next_set_of_roots = []
    while i < len(roots):
      for current_vertex in current_level:
        next_remainders = []
        for j, next_remainder in enumerate(verticies[current_vertex]):
          # if next_remainder == 0
            # stop loops and return the dict representing the next item to add to the path
          tree.append({'input_digit': j, 'prev_digit' : roots[i]})
          next_set_of_roots.append({'input_digit': j, 'prev_digit' : roots[i]})
          next_remainders.append(next_remainder)
        # reset roots with new_set_of_roots for connecting to next level of items
        current_level.append(next_remainder)
        #new_set_of_next_remainders.append((verticies[next_remainders[i]]), )
      i += 1


'''
# another function
# start at last path
# traverse using the reference to the next dict
# collect the input digits in reverse using a list
# ''.join(list_name) = answer to problem

# small example
#table = createArray([1, 3], 7)
#[print(i, row) for i, row in enumerate(table)]
#manyBFS(table, 0, table)
#print(1113 % 7)



a = input('COMMAND: ')
constraints = (0, 0, 3, 4)
directions = ('E', 'W', 'N', 'S')
curr_position = [0, 0, 'S']
for command in a:
    if command in directions:
        curr_position[2] = command
    elif command == 'M':
        if curr_position[2] == 'S' and curr_position[0] != constraints[2]:
            curr_position[0] += 1
        elif curr_position[2] == 'E' and curr_position[1] != constraints[3]:
            curr_position[1] += 1
        elif curr_position[2] == 'N' and curr_position[0] != constraints[1]:
            curr_position[0] -= 1
        elif curr_position[2] == 'W' and curr_position[1] != constraints[0]:
            curr_position[1] -= 1
    else:
        print('Invalid command found')
        break
       
print(curr_position)

steps_cnt = 0

curr_command = input()
while curr_command != 'Going home':
    steps = int(curr_command)
    steps_cnt += steps

    if steps_cnt >= 10000:
        break
    curr_command = input()
if curr_command == 'Going home':
    steps_going_home = int(input())
    steps_cnt += steps_going_home

steps_diff = abs(steps_cnt - 10000)

if steps_cnt >= 10000:
    steps_over_reached = steps_cnt - 10000
    print('Goal reached! Good job!')
    print(f'{steps_over_reached} steps over the goal!')
else:
    steps_under_reached = 10000 - steps_cnt
    print(f'{steps_under_reached} more steps to reach goal.')
# How to use Pomodoro/ Tomato timers
# 1. Decide task to be done set timers to 25 minutes for one "Pomodoro"
# 2. Work on task until timer is complete
# 3. After timer completion, put a checkmark on to-do list
# 4. Take a 5 minutes short break
# 5. After four "Pomodoro" take a long break
# 6. Repeat to step 1

import datetime
import time
import tqdm


def main():
    print_header()
    pomodoro_loop()


def print_header():
    print('------------------------')
    print('     POMODORO APP')
    print('------------------------')
    print()


def which_pomodoro():
    user_input = input('''
  1. 25 minute work session 
  2. 5 minute short break 
  3. 15 minute long break 
  4. or exit [x] 
  '''
                       )
    user_input = user_input.strip()

    if user_input not in ['1', '2', '3']:
        print('Exiting app...')
        exit()

    return user_input


def pomodoro_loop():

    print('Which timer would you like to start?')
    type = which_pomodoro()

    while type:

        if type == '1':
            time_window = 25 * 60
            description = '{} minute work session'.format(time_window/60)
        elif type == '3':
            time_window = 15 * 60
            description = '{} minute long break'.format(time_window/60)
        else:
            time_window = 5*60
            description = '{} minute short break'.format(time_window / 60)

        print('Starting {} minute timer... '.format(time_window/60))
        print('')

        for i in tqdm.tqdm(range(time_window)):
            time.sleep(1)

        print('')
        print('Your ' + description + ' is complete. What would you like to do next?')

        type = which_pomodoro()


if __name__ == '__main__':
    main()
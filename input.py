

def wait_frames(pyboy, frames):
    for _ in range(frames):
        pyboy.tick()

def commands(pyboy, command):
    if command == 'a':
        #press A
        pyboy.button('a')
    elif command == 'b':
        #press B
        pyboy.button('b')
    elif command == 'start':
        #press start
        pyboy.button('start')
    elif command == 'select':
        #press select
        pyboy.button('select')
    

def move(pyboy, direction):
    if direction == 'up':
        #press up
        pyboy.button('up')
    elif direction == 'down':
        #press down
        pyboy.button('down')
    elif direction == 'left':
        #press left
        pyboy.button('left')
    elif direction == 'right':
        #press right
        pyboy.button('right')


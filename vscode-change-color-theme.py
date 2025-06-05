# VSCode change color theme from light to dark and the opposite

import time
try:
    from pynput.keyboard import Controller, Key
except ImportError as e:
    print(f"Missing module: {e.name}. Please install it using: pip install pynput")
    exit(1)

print("Change color theme in vscode")
print("1: White to Dark")
print("2: Dark to White")
print("q: Exit")
choice = input("Enter your choice: ")
print(f"Your choice: {choice}")

# Initialize the keyboard controller
keyboard = Controller()

# Switch to Dark Theme
if choice == '1':

    keyboard.press(Key.ctrl)
    keyboard.press(Key.shift)
    keyboard.press('p')

    keyboard.release('p')
    keyboard.release(Key.shift)
    keyboard.release(Key.ctrl)
    
    time.sleep(2) 
    
    keyboard.type('Color Theme')
    
    time.sleep(2)  
    
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    time.sleep(2)
    
    keyboard.type('Dark Modern')
    
    time.sleep(2) 
    
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    
    print("Switched to Dark Modern Theme!")

# Switch to Light Theme
elif choice == '2':

    keyboard.press(Key.ctrl)
    keyboard.press(Key.shift)
    keyboard.press('p')

    keyboard.release('p')
    keyboard.release(Key.shift)
    keyboard.release(Key.ctrl)

    time.sleep(2)

    keyboard.type('Color Theme')

    time.sleep(2)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    time.sleep(2)

    keyboard.type('Light Modern')

    time.sleep(2)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    print("Switched to Light Modern Theme!")

elif choice == 'q':
    print("Exit")
    exit()
else:
    print("Invalid choice. Please enter 1, 2, or q.")


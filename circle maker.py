import pyautogui
import math
import time
pyautogui.FAILSAFE = True
# Function to draw a circle while holding the mouse button
def draw_circle_with_hold(radius, center_x, center_y, steps=1):
    # Calculate the angle step based on the number of points
    angle_step = 2 * math.pi / steps
    pyautogui.moveTo(center_x + radius, center_y)  # Move to the starting position 
    pyautogui.mouseDown()  # Hold down the mouse button

    for i in range(steps + 1):
        angle = i * angle_step
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        pyautogui.dragTo(x, y, duration=0.01)  # Drag to the next point

    pyautogui.mouseUp(0)  # Release the mouse button after completing the circle
    
# Circle parameters
screen_width, screen_height = pyautogui.size()
center_x = screen_width   // 2 # Center of the screen
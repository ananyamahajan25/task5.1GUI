import tkinter as tk
import RPi.GPIO as GPIO

# Pin configuration
LED_PINS = {
    "Red": 17,
    "Green": 22,
    "Blue": 27
}

# GPIO Setup
GPIO.setmode(GPIO.BCM)
for pin in LED_PINS.values():
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

# Functions
def turn_on_led(color):
    for led_color, pin in LED_PINS.items():
        GPIO.output(pin, GPIO.HIGH if led_color == color else GPIO.LOW)

def exit_app():
    GPIO.cleanup()
    root.destroy()

# GUI Setup
root = tk.Tk()
root.title("LED Control")

selected_color = tk.StringVar()
selected_color.set("Red")

# Radio Buttons
for color in LED_PINS:
    tk.Radiobutton(root, text=color, variable=selected_color, value=color,
                   command=lambda: turn_on_led(selected_color.get())).pack(anchor=tk.W)

# Exit Button
tk.Button(root, text="Exit", command=exit_app).pack(pady=10)

# Run the GUI
root.mainloop()
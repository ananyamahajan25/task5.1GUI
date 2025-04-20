import tkinter as tk
import RPi.GPIO as GPIO

# LED pin configuration
LED_PINS = {
    "red": 17,
    "green": 27,
    "blue": 22
}

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
for pin in LED_PINS.values():
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

# Function to turn on the selected LED
def turn_on_led():
    color = color_entry.get().strip().lower()
    if color in LED_PINS:
        for led_color, pin in LED_PINS.items():
            GPIO.output(pin, GPIO.HIGH if led_color == color else GPIO.LOW)
        message_label.config(text=f"{color.capitalize()} LED is ON", fg="green")
    else:
        message_label.config(text="Invalid color. Enter red, green, or blue.", fg="red")

# Exit function to clean up GPIO
def exit_app():
    GPIO.cleanup()
    root.destroy()

# GUI setup
root = tk.Tk()
root.title("SIT730 LED Control")

# Input field
tk.Label(root, text="Enter LED color (red, green, blue):").pack(pady=5)
color_entry = tk.Entry(root)
color_entry.pack(pady=5)

# Submit button
tk.Button(root, text="Submit", command=turn_on_led).pack(pady=5)

# Message label
message_label = tk.Label(root, text="")
message_label.pack(pady=5)

# Exit button
tk.Button(root, text="Exit", command=exit_app).pack(pady=10)

# Start the GUI
root.mainloop()

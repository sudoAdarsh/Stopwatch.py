import customtkinter
import time

# Stopwatch state variables
is_running = False
start_time = 0.0
elapsed_time = 0.0
Lap_counter = 1


def button():
    """Handle Start, Pause, and Resume button actions."""
    global is_running, start_time, elapsed_time

    if not is_running and elapsed_time == 0:
        is_running = True
        start_time = time.time() - elapsed_time
        update()
        button1.configure(text="Pause")

    elif is_running:
        is_running = False
        elapsed_time = time.time() - start_time
        button1.configure(text="Resume")

    elif not is_running and elapsed_time > 0:
        is_running = True
        update()
        start_time = time.time() - elapsed_time
        button1.configure(text="Pause")


def update():
    """Update the stopwatch display every 10ms."""
    global elapsed_time

    if is_running:
        elapsed_time = time.time() - start_time

        h = int(elapsed_time // 3600)
        m = int((elapsed_time % 3600) // 60)
        s = int(elapsed_time % 60)
        ms = int((elapsed_time * 1000) % 1000)

        formatted_time = f"{h:02}:{m:02}:{s:02}:{ms:03}"
        display.configure(text=formatted_time)

        app.after(10, update)


def reset_button():
    """Reset the stopwatch to zero."""
    global is_running, start_time, elapsed_time

    is_running = False
    start_time = 0.0
    elapsed_time = 0.0

    display.configure(text="00:00:00:000")
    button1.configure(text="Start")


def lap_button():
    """Record the current lap time."""
    global elapsed_time, Lap_counter

    if is_running:
        elapsed_time = time.time() - start_time

        h = int(elapsed_time // 3600)
        m = int((elapsed_time % 3600) // 60)
        s = int(elapsed_time % 60)
        ms = int((elapsed_time * 1000) % 1000)

        formatted_time = f"{h:02}:{m:02}:{s:02}:{ms:03}"
        lap_text.insert("end", f"Lap {Lap_counter} - {formatted_time}\n")

        Lap_counter += 1


# --------------------------
# GUI Setup
# --------------------------

app = customtkinter.CTk()
app.title("Stopwatch")
app.geometry("400x400")

# Configure resizing
app.grid_rowconfigure(0, weight=10)
app.grid_rowconfigure(1, weight=1)
for i in range(3):
    app.grid_columnconfigure(i, weight=1)

# Stopwatch display label
display = customtkinter.CTkLabel(
    app,
    text="00:00:00:000",
    font=("Arial", 32, "bold"),
    text_color="white",
    fg_color="transparent",
    anchor="center"
)
display.grid(row=0, column=0, columnspan=3, sticky="nsew")

# Button font
button_font = ("Arial", 18, "bold")

# Start/Pause/Resume button
button1 = customtkinter.CTkButton(app, text="Start", font=button_font, command=button)
button1.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

# Reset button
reset = customtkinter.CTkButton(app, text="Reset", font=button_font, command=reset_button)
reset.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

# Lap button
lap = customtkinter.CTkButton(app, text="Lap", font=button_font, command=lap_button)
lap.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")

# Lap text box
lap_text = customtkinter.CTkTextbox(app, activate_scrollbars=True, height=120, font=("Arial", 23))
lap_text.grid(row=2, column=0, columnspan=3, sticky="nsew")

# Start the application loop
app.mainloop()

# Stopwatch

A Python-based stopwatch application with a graphical interface built using CustomTkinter.
The stopwatch supports Start/Pause/Resume, Reset, and Lap recording functionality.

## Overview

This application provides an interactive stopwatch with millisecond precision.
Features include:

- Start/Pause/Resume functionality for continuous tracking
- Reset to clear the current time
- Lap recording with timestamps
- Millisecond-accurate time display
- Resizable window layout
- The program uses the after() method in Tkinter for smooth real-time updates.

## Requirements

Python 3.7 or newer
The following Python packages:

```python
pip install customtkinter
```

## How to Use

### Clone the repository:

```python
git clone https://github.com/yourusername/stopwatch-app.git
cd Stopwatch
```

### Run the application:

```python
python main.py
```

## Controls:

```
Start: Starts the stopwatch.

Pause: Pauses the stopwatch without resetting the time.

Resume: Continues timing from where it paused.

Reset: Resets the stopwatch to 00:00:00:000.

Lap: Records the current elapsed time in the Lap list.
```

## Notes

The application requires CustomTkinter, which is a modern and customizable version of Tkinter.

The UI adapts to window resizing thanks to grid configuration.

Lap times are recorded only when the stopwatch is running.

## Author

Adarsh Upadhyay

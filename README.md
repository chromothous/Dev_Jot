# Dev Jot

Dev Jot is a lightweight desktop application for managing, editing, and searching reusable code snippets.
It is built in Python using CustomTkinter and designed to prioritize speed, simplicity, and local control.

---

## Why Dev Jot Exists

Developers often accumulate useful code snippets scattered across files, notes, or cloud services.
I built Dev Jot to solve a personal workflow problem: keeping frequently used snippets organized,
searchable, and immediately editable in a single, offline-first desktop tool.

The focus of this project is not only functionality, but also usability, responsiveness,
and clean state management.

---

## Features

- Create, edit, and delete code snippets
- Store snippet metadata (title, description, language)
- Full-text search across titles, descriptions, and code
- Syntax highlighting for common programming constructs
- Keyboard-friendly editing:
  - Tab / Shift+Tab indentation handling
  - Smart backspace behavior
  - Automatic pairing for quotes and brackets
- Responsive, dark-mode GUI
- Local JSON persistence (no accounts, no cloud dependencies)

---

## Tech Stack

- Python
- CustomTkinter (GUI)
- Tkinter (base windowing)
- JSON (local data persistence)
- Regular expressions (syntax highlighting)
- UUID (unique snippet identification)

---

## Running Dev Jot

### Option 1: Prebuilt Executable (Windows)

A prebuilt Windows executable is included in `Dev Jot.zip`.

- Download the ZIP
- Extract the contents
- Run the executable directly

No Python installation or dependencies are required.

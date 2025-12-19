# Dev Jot

Dev Jot is a lightweight desktop application for managing, editing, and searching reusable code snippets.  
It is built in Python using CustomTkinter and designed to prioritize speed, simplicity, and local control.

---

## Why Dev Jot Exists

Developers often accumulate useful code snippets scattered across files, notes, or cloud services.
I built Dev Jot to solve a personal workflow problem:  
keeping frequently used snippets organized, searchable, and immediately editable in a single, offline-first desktop tool.

The focus of this project is not only functionality, but also usability, responsiveness, and clean state management.

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

- **Python**
- **CustomTkinter** for the GUI
- **Tkinter** for base windowing
- **JSON** for local data persistence
- **Regular expressions** for syntax highlighting
- **UUID** for unique snippet identification

---

## Prebuilt Executable

A Windows executable is included in Dev Jot.zip for convenience.
The ZIP contains a bundled build that can be run without installing Python or dependencies.

Let me know what you think at nrda1991@gmail.com

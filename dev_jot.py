# Import for the GUI.
import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter as ctk

# Import for working with JSON.
import json

# Import for working with system.
import os

# Import for unique identifier with cards.
import uuid

# Import for full-feature syntax highlighter.
from pygments import lex
from pygments.lexers import get_lexer_by_name, guess_lexer
from pygments.styles import get_style_by_name
from pygments.token import Token
import re

# ------------------------
# Functions
# ------------------------

# Main hub screen logic.
def main_screen():
    global app, main_area, main_area_2, empty_label, empty_state, top_bar, configure_area, snippets, search_entry

    save_snippets()

    if top_bar.winfo_ismapped():
        top_bar.pack_forget()
    if configure_area.winfo_ismapped():
        configure_area.pack_forget()

    top_bar = ctk.CTkFrame(app, corner_radius=0, fg_color="#1e1e1e")
    top_bar.pack(fill="x", padx=0, pady=0)

    add_button = ctk.CTkButton(
        top_bar, text="+ Add Snippet", width=120, command=lambda: configure_screen(None)
    )
    add_button.pack(side="left", padx=10, pady=10)

    search_entry = ctk.CTkEntry(
        top_bar, placeholder_text="Search snippets...", width=400
    )
    search_entry.pack(side="left", padx=10, pady=10, fill="x", expand=True)
    search_entry.bind("<KeyRelease>", on_search)

    populate_snippets()

    if empty_state == True:
        if main_area_2.winfo_ismapped():
            main_area_2.pack_forget()

        main_area.pack(fill="both", expand=True, padx=10, pady=10)

        empty_label.pack(expand=True)
    else:
        if main_area.winfo_ismapped():
            main_area.pack_forget()

        main_area_2.pack(fill="both", expand=True, padx=10, pady=10)

# Initial populating of the snippets loaded from JSON.
def populate_snippets():
    global empty_state, snippets

    card_width = 250
    card_height = 450

    index = 0

    for widget in main_area_2.winfo_children():
        widget.destroy()

    for key, value in snippets.items():
        card = ctk.CTkFrame(
            main_area_2,
            fg_color="#2d2d30",
            corner_radius=10,
            width=card_width,
            height=card_height,
        )
        card.grid(row=index // 4, column=index % 4, padx=10, pady=10, sticky="nsew")
        card.grid_propagate(False)
        card.pack_propagate(False)

        def on_enter(event, card=card):
            # Always change the parent frame's color.
            card.configure(fg_color="#2A2A2A")

        def on_leave(event, card=card):
            card.configure(fg_color="#2d2d30")

        def on_click(event, card=card):
            original_color = card.cget("fg_color")
            card.configure(fg_color="#3A3A3A")
            card.after(100, lambda: card.configure(fg_color=original_color))

        # Label inside card.
        ctk.CTkLabel(card, text=f"{value["title"]}", font=ctk.CTkFont(size=14)).pack(
            padx=10, pady=10
        )
        ctk.CTkLabel(
            card, text=f"{value["description"]}", font=ctk.CTkFont(size=14)
        ).pack(padx=10, pady=10)
        ctk.CTkLabel(card, text=f"{value["language"]}", font=ctk.CTkFont(size=14)).pack(
            padx=10, pady=10
        )

        # Short code preview.
        ctk.CTkLabel(
            card,
            text=f"{value["code"]}",
            font=ctk.CTkFont(size=12),
            text_color="#aaaaaa",
        ).pack(padx=10, pady=(0, 10))

        empty_state = False

        card.bind("<Button-1>", lambda e, id=key: configure_screen(id))

        index += 1

        widgets_to_bind = [card] + card.winfo_children()

        for widget in widgets_to_bind:
            widget.bind("<Enter>", on_enter)
            widget.bind("<Leave>", on_leave)
            widget.bind("<Button-1>", on_click)

    # Make the grid expand nicely.
    for col in range(len(snippets)):
        main_area_2.grid_columnconfigure(col, weight=1)

# Editing screen logic.
def configure_screen(id):
    global snippets, top_bar, main_area, main_area_2, configure_area, code_box, pairs

    if main_area.winfo_ismapped():
        main_area.pack_forget()
    else:
        main_area_2.pack_forget()

    top_bar.pack_forget()

    top_bar = ctk.CTkFrame(app, corner_radius=0, fg_color="#1e1e1e")
    top_bar.pack(fill="x", padx=0, pady=0)

    back_button = ctk.CTkButton(top_bar, text="< Back", width=120, command=main_screen)
    back_button.pack(side="left", padx=10, pady=10)

    configure_area = ctk.CTkFrame(app, fg_color="#252526")
    configure_area.pack(fill="both", expand=True)

    title_entry = ctk.CTkEntry(configure_area, placeholder_text="Title...", width=400)
    title_entry.pack()

    description_entry = ctk.CTkEntry(
        configure_area, placeholder_text="Description...", width=400
    )
    description_entry.pack()

    language_var = ctk.StringVar(value="Python")
    language_menu = ctk.CTkOptionMenu(
        configure_area,
        values=[
            "Python",
            "JavaScript",
            "Java",
            "C",
            "C++",
            "C#",
            "Ruby",
            "PHP",
            "Swift",
            "Go",
            "Rust",
            "Kotlin",
            "TypeScript",
            "R",
            "SQL",
            "MATLAB",
            "Perl",
            "Lua",
            "Shell",
            "Scala",
            "Objective-C",
            "Dart",
            "Haskell",
            "Julia",
            "Visual Basic",
            "Assembly",
            "Elixir",
            "F#",
            "Groovy",
            "Erlang",
            "COBOL",
            "Fortran",
            "Ada",
            "ActionScript",
            "OCaml",
            "Scheme",
            "Prolog",
            "Solidity",
            "VHDL",
            "Verilog",
            "Tcl",
            "Mercury",
            "Crystal",
            "Nim",
            "Zig",
            "Hack",
            "D",
            "Smalltalk",
            "AutoHotkey",
            "AutoIt",
            "Delphi",
            "Lisp",
            "Awk",
            "Icon",
            "Io",
            "LiveCode",
            "Modula-2",
            "OpenCL",
            "PostScript",
            "REXX",
            "Ring",
            "Seed7",
            "Simula",
            "Turing",
            "Vala",
            "Wolfram",
            "V",
        ],
        variable=language_var,
    )
    language_menu.pack()

    code_box = ctk.CTkTextbox(
        configure_area, width=600, height=300, fg_color="#1e1e1e", text_color="white"
    )
    code_box.pack(padx=10, pady=10, fill="both", expand=True)
    code_box.bind("<Tab>", handle_tab)
    code_box.bind("<Shift-Tab>", handle_shift_tab)
    code_box.bind("<BackSpace>", handle_backspace)
    code_box.bind("<KeyRelease>", lambda e: apply_syntax_highlighting(code_box))

    code_box.after(100, lambda: apply_syntax_highlighting(code_box))

    for key in pairs.keys():
        code_box.bind(key, handle_autocomplete)

    if id == None:
        create_button = ctk.CTkButton(
            top_bar,
            text="Create",
            width=120,
            command=lambda: create_snippet(
                str(uuid.uuid4()),
                title_entry.get(),
                description_entry.get(),
                language_var.get(),
                code_box.get("1.0", "end"),
            ),
        )
        create_button.pack(side="left", padx=10, pady=10)
    else:
        update_button = ctk.CTkButton(
            top_bar,
            text="Update",
            width=120,
            command=lambda: update_snippet(
                id,
                title_entry.get(),
                description_entry.get(),
                language_var.get(),
                code_box.get("1.0", "end"),
            ),
        )
        update_button.pack(side="left", padx=10, pady=10)

        delete_button = ctk.CTkButton(
            top_bar, text="Delete", width=120, command=lambda: delete_snippet(id)
        )
        delete_button.pack(side="left", padx=10, pady=10)

        title_entry.insert(0, f"{snippets[id]["title"]}")
        description_entry.insert(0, f"{snippets[id]["description"]}")
        language_var.set(snippets[id]["language"])
        code_box.insert("1.0", f"{snippets[id]["code"]}")

# For creating code snippets
def create_snippet(id, title, description, language, code):
    global snippets

    snippets[id] = {
        "title": f"{title}",
        "description": f"{description}",
        "language": f"{language}",
        "code": f"{code}",
    }

    main_screen()

# For updating code snippets.
def update_snippet(id, title, description, language, code):
    global snippets

    snippets[id] = {
        "title": f"{title}",
        "description": f"{description}",
        "language": f"{language}",
        "code": f"{code}",
    }

    main_screen()

# Simple deleting of snippets.
def delete_snippet(id):
    global snippets

    del snippets[id]

    main_screen()

# Handles pressing tab in the code box.
def handle_tab(event):
    global code_box

    try:
        start = code_box.index("sel.first linestart")
        end = code_box.index("sel.last lineend")
    except tk.TclError:
        # No selection: insert 8 spaces at cursor
        code_box.insert("insert", "        ")
        return "break"

    line_index = start
    while code_box.compare(line_index, "<=", end):
        code_box.insert(line_index, "        ")
        line_index = code_box.index(f"{line_index} +1line")

    return "break"

# Handles shift + tab within the code box.
def handle_shift_tab(event):
    global code_box

    try:
        start = code_box.index("sel.first linestart")
        end = code_box.index("sel.last lineend")
    except tk.TclError:
        start = code_box.index("insert linestart")
        end = code_box.index("insert lineend")

    line_index = start
    while code_box.compare(line_index, "<=", end):
        # Safely handle lines shorter than 8 spaces.
        line_text = code_box.get(line_index, f"{line_index} lineend")
        spaces_to_remove = min(8, len(line_text) - len(line_text.lstrip(" ")))
        if spaces_to_remove > 0:
            code_box.delete(line_index, f"{line_index} +{spaces_to_remove}c")
        line_index = code_box.index(f"{line_index} +1line")

    return "break"

# Handles backspace being used in the code box.
def handle_backspace(event):
    # Get current cursor position.
    index = code_box.index("insert")
    line_start = code_box.index("insert linestart")

    # Get text from line start up to cursor.
    line_text = code_box.get(line_start, index)

    # check if the last 8 characters before cursor are 8 spaces (a tab).
    if line_text.endswith("        "):
        # Delete the whole tab (8 spaces).
        code_box.delete(f"{index} -8c", index)
        return "break"  # Prevent default backspace.
    # else: Let backspace work normally.

# Does auto complete for coding with "", '', (), [], {}.
def handle_autocomplete(event):
    global pairs

    char = event.char
    if char in pairs:
        # Insert the pair at cursor.
        code_box.insert("insert", char + pairs[char])
        # Move cursor back between the pair.
        code_box.mark_set("insert", f"insert -1c")
        return "break"  # Prevent default typing.

# Saving the snippets created by the user into JSON.
def save_snippets():
    global snippets

    with open("snippets.json", "w", encoding="utf-8") as f:
        json.dump(snippets, f, indent=4)

# Loading the snippets from the JSON file.
def load_snippets():
    global snippets
    if os.path.exists("snippets.json"):
        with open("snippets.json", "r", encoding="utf-8") as f:
            raw_snippets = json.load(f)
            # convert keys back to int
            snippets = {k: v for k, v in raw_snippets.items()}
    else:
        snippets = {}

# Handling the search bar at the main screen.
def on_search(event):
    global search_entry, snippets

    query = search_entry.get().lower()
    filtered = {}

    for key, value in snippets.items():
        if (
            query in value["title"].lower()
            or query in value["description"].lower()
            or query in value["code"].lower()
        ):
            filtered[key] = value

    update_display(filtered)

# Function for updating the main hub from searches.
def update_display(filtered):
    global empty_state, main_area_2

    card_width = 250
    card_height = 450

    index = 0

    for widget in main_area_2.winfo_children():
        widget.destroy()

    for key, value in filtered.items():
        card = ctk.CTkFrame(
            main_area_2,
            fg_color="#2d2d30",
            corner_radius=10,
            width=card_width,
            height=card_height,
        )
        card.grid(row=index // 4, column=index % 4, padx=10, pady=10, sticky="nsew")
        card.grid_propagate(False)
        card.pack_propagate(False)

        def on_enter(event, card=card):
            # Always change the parent frame's color
            card.configure(fg_color="#2A2A2A")

        def on_leave(event, card=card):
            card.configure(fg_color="#2d2d30")

        def on_click(event, card=card):
            original_color = card.cget("fg_color")
            card.configure(fg_color="#3A3A3A")
            card.after(100, lambda: card.configure(fg_color=original_color))

        # Label inside card.
        ctk.CTkLabel(card, text=f"{value["title"]}", font=ctk.CTkFont(size=14)).pack(
            padx=10, pady=10
        )
        ctk.CTkLabel(
            card, text=f"{value["description"]}", font=ctk.CTkFont(size=14)
        ).pack(padx=10, pady=10)
        ctk.CTkLabel(card, text=f"{value["language"]}", font=ctk.CTkFont(size=14)).pack(
            padx=10, pady=10
        )

        # Short code preview.
        ctk.CTkLabel(
            card,
            text=f"{value["code"]}",
            font=ctk.CTkFont(size=12),
            text_color="#aaaaaa",
        ).pack(padx=10, pady=(0, 10))

        empty_state = False

        card.bind("<Button-1>", lambda e, id=key: configure_screen(id))

        index += 1

        widgets_to_bind = [card] + card.winfo_children()

        for widget in widgets_to_bind:
            widget.bind("<Enter>", on_enter)
            widget.bind("<Leave>", on_leave)
            widget.bind("<Button-1>", on_click)

    # Make the grid expand nicely.
    for col in range(len(snippets)):
        main_area_2.grid_columnconfigure(col, weight=1)

# For applying highlighting for syntax in the code box.
def apply_syntax_highlighting(textbox):
    # Remove old tags.
    for tag in textbox.tag_names():
        textbox.tag_remove(tag, "1.0", "end")

    # Define highlighting rules.
    syntax_rules = {
        "keyword": {
            "pattern": r"\b(def|class|return|if|else|elif|for|while|import|from|as|try|except|finally|with|lambda|in|is|and|or|not|pass|break|continue|True|False|None)\b",
            "color": "#569CD6",
        },
        "string": {"pattern": r"(\".*?\"|'.*?')", "color": "#CE9178"},
        "comment": {"pattern": r"#.*", "color": "#6A9955"},
        "number": {"pattern": r"\b\d+(\.\d+)?\b", "color": "#B5CEA8"},
    }

    content = textbox.get("1.0", "end-1c")

    # Apply tags.
    for tag_name, rule in syntax_rules.items():
        pattern = re.compile(rule["pattern"])
        for match in pattern.finditer(content):
            start = f"1.0 + {match.start()} chars"
            end = f"1.0 + {match.end()} chars"

            if tag_name not in textbox.tag_names():
                textbox.tag_config(tag_name, foreground=rule["color"])

            textbox.tag_add(tag_name, start, end)


# ------------------------
# Initial Frames
# ------------------------

app = ctk.CTk()

main_area = ctk.CTkFrame(app, fg_color="#252526")
main_area_2 = ctk.CTkScrollableFrame(app, fg_color="#252526")

empty_label = ctk.CTkLabel(
    main_area, text="You haven't added anything yet.", font=ctk.CTkFont(size=16)
)

top_bar = ctk.CTkFrame(app, fg_color="#252526")
configure_area = ctk.CTkFrame(app, fg_color="#252526")

# ------------------------
# Variables
# ------------------------

snippets = {}
pairs = {'"': '"', "'": "'", "(": ")", "[": "]", "{": "}"}

# ------------------------
# States
# ------------------------

empty_state = True

# ------------------------
# Main
# ------------------------
load_snippets()

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app.title("Dev Jot")

screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
app.geometry(f"{screen_width}x{screen_height}+0+0")
app.resizable(True, True)

main_screen()

app.mainloop()

import os
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox

def main():
    root = tk.Tk()
    root.title("Simple Text Editor")
    root.configure(bg="#1e1e1e")
    root.state('zoomed')

    # --- Sidebar for folders/files ---
    sidebar = tk.Frame(root, bg="#23272e", width=200)
    sidebar.pack(side='left', fill='y')

    sidebar_content = tk.Frame(sidebar, bg="#23272e")
    sidebar_content.pack(expand=True, fill='both')

    opened_folder = {"path": None}
    opened_file = {"path": None}

    def clear_sidebar():
        for widget in sidebar_content.winfo_children():
            widget.destroy()

    def show_empty_sidebar():
        clear_sidebar()
        label = tk.Label(
            sidebar_content,
            text="You have not yet opened a folder.",
            bg="#23272e", fg="#d4d4d4",
            font=("Segoe UI", 10), pady=24
        )
        label.pack(pady=(40, 8), padx=16)
        btn_open_folder = tk.Button(
            sidebar_content, text="Open Folder", font=("Segoe UI", 10, "bold"),
            bg="#0078d4", fg="#fff", activebackground="#005a9e", activeforeground="#fff",
            bd=0, relief="flat", padx=12, pady=8, command=open_folder, cursor="hand2"
        )
        btn_open_folder.pack(pady=8, padx=32, fill="x")

    def show_empty_folder_sidebar(folder_path):
        clear_sidebar()
        header = tk.Frame(sidebar_content, bg="#23272e")
        header.pack(fill="x", pady=(8, 0))
        folder_label = tk.Label(
            header, text=os.path.basename(folder_path), anchor="w",
            bg="#23272e", fg="#d4d4d4", font=("Segoe UI", 10, "bold"), padx=12, pady=8
        )
        folder_label.pack(side="left", fill="x", expand=True)

        # Icon buttons (hidden by default)
        icon_new_file = tk.Label(
            header, text="🗎+", bg="#23272e", fg="#d4d4d4", font=("Segoe UI", 11), cursor="hand2"
        )
        icon_new_folder = tk.Label(
            header, text="📁+", bg="#23272e", fg="#d4d4d4", font=("Segoe UI", 11), cursor="hand2"
        )

        def show_icons(event=None):
            icon_new_file.pack(side="right", padx=(0, 2))
            icon_new_folder.pack(side="right", padx=(0, 8))

        def hide_icons(event=None):
            icon_new_file.pack_forget()
            icon_new_folder.pack_forget()

        header.bind("<Enter>", show_icons)
        header.bind("<Leave>", hide_icons)
        folder_label.bind("<Enter>", show_icons)
        folder_label.bind("<Leave>", hide_icons)

        def create_new_file():
            entry = tk.Entry(sidebar_content, font=("Segoe UI", 10), bg="#23272e", fg="#d4d4d4", insertbackground="#d4d4d4")
            entry.pack(fill="x", padx=24, pady=(2, 0))
            entry.focus_set()
            def save_file(event=None):
                name = entry.get().strip()
                if name:
                    path = os.path.join(folder_path, name)
                    if not os.path.exists(path):
                        with open(path, "w") as f:
                            f.write("")
                        show_folder_sidebar(folder_path)
                        open_file(path)
                entry.destroy()
            entry.bind("<Return>", save_file)
            entry.bind("<FocusOut>", lambda e: entry.destroy())

        def create_new_folder():
            entry = tk.Entry(sidebar_content, font=("Segoe UI", 10), bg="#23272e", fg="#d4d4d4", insertbackground="#d4d4d4")
            entry.pack(fill="x", padx=24, pady=(2, 0))
            entry.focus_set()
            def save_folder(event=None):
                name = entry.get().strip()
                if name:
                    path = os.path.join(folder_path, name)
                    if not os.path.exists(path):
                        os.makedirs(path)
                        show_folder_sidebar(folder_path)
                entry.destroy()
            entry.bind("<Return>", save_folder)
            entry.bind("<FocusOut>", lambda e: entry.destroy())

        icon_new_file.bind("<Button-1>", lambda e: create_new_file())
        icon_new_folder.bind("<Button-1>", lambda e: create_new_folder())

        # Empty folder message
        label = tk.Label(
            sidebar_content,
            text="This folder is empty.",
            bg="#23272e", fg="#d4d4d4",
            font=("Segoe UI", 10), pady=24
        )
        label.pack(pady=(40, 8), padx=16)

    def show_folder_sidebar(folder_path):
        clear_sidebar()
        # Folder header with hover icons
        header = tk.Frame(sidebar_content, bg="#23272e")
        header.pack(fill="x", pady=(8, 0))
        folder_label = tk.Label(
            header, text=os.path.basename(folder_path), anchor="w",
            bg="#23272e", fg="#d4d4d4", font=("Segoe UI", 10, "bold"), padx=12, pady=8
        )
        folder_label.pack(side="left", fill="x", expand=True)

        # Icon buttons (hidden by default)
        icon_new_file = tk.Label(
            header, text="🗎+", bg="#23272e", fg="#d4d4d4", font=("Segoe UI", 11), cursor="hand2"
        )
        icon_new_folder = tk.Label(
            header, text="📁+", bg="#23272e", fg="#d4d4d4", font=("Segoe UI", 11), cursor="hand2"
        )

        def show_icons(event=None):
            icon_new_file.pack(side="right", padx=(0, 2))
            icon_new_folder.pack(side="right", padx=(0, 8))

        def hide_icons(event=None):
            icon_new_file.pack_forget()
            icon_new_folder.pack_forget()

        header.bind("<Enter>", show_icons)
        header.bind("<Leave>", hide_icons)
        folder_label.bind("<Enter>", show_icons)
        folder_label.bind("<Leave>", hide_icons)

        def create_new_file():
            entry = tk.Entry(sidebar_content, font=("Segoe UI", 10), bg="#23272e", fg="#d4d4d4", insertbackground="#d4d4d4")
            entry.pack(fill="x", padx=24, pady=(2, 0))
            entry.focus_set()
            def save_file(event=None):
                name = entry.get().strip()
                if name:
                    path = os.path.join(folder_path, name)
                    if not os.path.exists(path):
                        with open(path, "w") as f:
                            f.write("")
                        show_folder_sidebar(folder_path)
                        open_file(path)
                entry.destroy()
            entry.bind("<Return>", save_file)
            entry.bind("<FocusOut>", lambda e: entry.destroy())

        def create_new_folder():
            entry = tk.Entry(sidebar_content, font=("Segoe UI", 10), bg="#23272e", fg="#d4d4d4", insertbackground="#d4d4d4")
            entry.pack(fill="x", padx=24, pady=(2, 0))
            entry.focus_set()
            def save_folder(event=None):
                name = entry.get().strip()
                if name:
                    path = os.path.join(folder_path, name)
                    if not os.path.exists(path):
                        os.makedirs(path)
                        show_folder_sidebar(folder_path)
                entry.destroy()
            entry.bind("<Return>", save_folder)
            entry.bind("<FocusOut>", lambda e: entry.destroy())

        icon_new_file.bind("<Button-1>", lambda e: create_new_file())
        icon_new_folder.bind("<Button-1>", lambda e: create_new_folder())

        # List files
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        if not files:
            show_empty_folder_sidebar(folder_path)
            return
        for fname in files:
            btn = tk.Button(
                sidebar_content, text="🗎 " + fname, anchor="w",
                bg="#23272e", fg="#d4d4d4", font=("Segoe UI", 10),
                activebackground="#264f78", activeforeground="#fff",
                bd=0, relief="flat", padx=24, pady=6,
                command=lambda f=fname: open_file(os.path.join(folder_path, f))
            )
            btn.pack(fill="x", padx=8, pady=1)

    def show_file_sidebar(file_path):
        clear_sidebar()
        btn = tk.Button(
            sidebar_content, text="🗎 " + os.path.basename(file_path), anchor="w",
            bg="#23272e", fg="#d4d4d4", font=("Segoe UI", 10, "bold"),
            activebackground="#264f78", activeforeground="#fff",
            bd=0, relief="flat", padx=16, pady=12
        )
        btn.pack(fill="x", padx=8, pady=8)

    # --- File/Folder actions ---
    def open_file(path=None):
        if not path:
            file_path = filedialog.askopenfilename()
        else:
            file_path = path
        if file_path:
            with open(file_path, "r", encoding="utf-8") as f:
                text_area.delete("1.0", "end")
                text_area.insert("1.0", f.read())
            opened_file["path"] = file_path
            opened_folder["path"] = None
            show_file_sidebar(file_path)

    def open_folder():
        folder_path = filedialog.askdirectory()
        if folder_path:
            opened_folder["path"] = folder_path
            opened_file["path"] = None
            show_folder_sidebar(folder_path)
            text_area.delete("1.0", "end")

    # --- Show empty sidebar on startup ---
    show_empty_sidebar()

    # --- VS Code-like Top Bar ---
    topbar = tk.Frame(root, bg="#23272e", height=28)
    topbar.pack(side='top', fill='x')

    # VS Code icon (left)
    vscode_icon = tk.Label(topbar, text="🟦", bg="#23272e", fg="#22a6f7", font=("Segoe UI Emoji", 14), padx=8)
    vscode_icon.pack(side="left")

    # File and Run buttons (next to icon)
    menu_btns = {}
    for item in ["File", "Run"]:
        btn = tk.Label(
            topbar, text=item, bg="#23272e", fg="#d4d4d4",
            font=("Segoe UI", 10), padx=10, pady=2, cursor="hand2"
        )
        btn.pack(side="left")
        menu_btns[item] = btn

    # Centered title (like VS Code)
    title_label = tk.Label(
        topbar, text="Byte Code Editor", bg="#23272e", fg="#d4d4d4",
        font=("Segoe UI", 10, "bold")
    )
    title_label.pack(side="top", pady=0, expand=True)

    # Window control icons (right)
    def on_close(): root.destroy()
    def on_minimize(): root.iconify()
    def on_maximize(): root.state('zoomed')

    controls = tk.Frame(topbar, bg="#23272e")
    controls.pack(side="right", padx=4)
    btn_min = tk.Label(controls, text="🗕", bg="#23272e", fg="#d4d4d4", font=("Segoe UI Emoji", 11), padx=6, cursor="hand2")
    btn_max = tk.Label(controls, text="🗖", bg="#23272e", fg="#d4d4d4", font=("Segoe UI Emoji", 11), padx=6, cursor="hand2")
    btn_close = tk.Label(controls, text="🗙", bg="#23272e", fg="#d9534f", font=("Segoe UI Emoji", 11), padx=6, cursor="hand2")
    btn_min.pack(side="left")
    btn_max.pack(side="left")
    btn_close.pack(side="left")
    btn_min.bind("<Button-1>", lambda e: on_minimize())
    btn_max.bind("<Button-1>", lambda e: on_maximize())
    btn_close.bind("<Button-1>", lambda e: on_close())
    for btn in [btn_min, btn_max, btn_close]:
        btn.bind("<Enter>", lambda e, b=btn: b.config(bg="#333344"))
        btn.bind("<Leave>", lambda e, b=btn: b.config(bg="#23272e"))

    # --- Subtle border below menu bar ---
    tk.Frame(root, bg="#333333", height=1).pack(side='top', fill='x')

    # --- Text area ---
    text_area = tk.Text(
        root,
        wrap=tk.WORD,
        font=("Consolas", 12),
        bg="#1e1e1e",
        fg="#d4d4d4",
        insertbackground="#d4d4d4",
        selectbackground="#264f78",
        selectforeground="#ffffff",
        borderwidth=0,
        highlightthickness=0,
        relief="flat"
    )
    text_area.pack(expand=True, fill='both', padx=0, pady=(0,0))

    # Subtle current line highlight
    text_area.tag_configure("current_line", background="#23272e", relief="flat")
    def highlight_current_line(event=None):
        text_area.tag_remove("current_line", "1.0", "end")
        current_index = text_area.index("insert")
        line = current_index.split('.')[0]
        line_start = f"{line}.0"
        line_end = f"{line}.end+1c"
        text_area.tag_add("current_line", line_start, line_end)
    text_area.bind("<KeyRelease>", highlight_current_line)
    text_area.bind("<ButtonRelease>", highlight_current_line)
    highlight_current_line()

    # --- Slim bottom bar ---
    bottom_bar = tk.Frame(root, bg="#23272e", height=18, bd=0, highlightthickness=0)
    bottom_bar.pack(side='bottom', fill='x')
    tk.Frame(root, bg="#333333", height=1).pack(side='bottom', fill='x')

    # Language chooser (modern palette)
    languages = [
        "Plain Text", "Python", "C++", "JavaScript", "HTML", "Java", "C", "C#", "TypeScript", "CSS",
        "PHP", "Ruby", "Go", "Rust", "Kotlin", "Swift", "Scala", "Perl", "Lua", "Shell Script",
        "PowerShell", "Objective-C", "Dart", "R", "MATLAB", "Haskell", "Elixir", "Erlang", "F#"
    ]
    selected_language = tk.StringVar(value=languages[0])

    def set_language(lang):
        selected_language.set(lang)
        # Here you would typically also set the syntax highlighting mode

    language_menu = tk.OptionMenu(
        bottom_bar, selected_language, *languages,
        command=set_language
    )
    language_menu.config(
        bg="#1e1e1e", fg="#d4d4d4",
        font=("Segoe UI", 10),
        borderwidth=0,
        highlightthickness=0
    )
    language_menu.pack(side='right', padx=10, pady=2)

    # --- Status bar (line/column info) ---
    status_bar = tk.Label(
        bottom_bar, text="Ln 1, Col 0", bg="#23272e", fg="#d4d4d4",
        font=("Segoe UI", 10), bd=0, relief="flat", anchor="e", padx=10
    )
    status_bar.pack(side='right', padx=10)  # Move to right side

    def update_status_bar(event=None):
        try:
            row, col = map(int, text_area.index("insert").split("."))
            status_bar.config(text=f"Ln {row}, Col {col}")
        except:
            status_bar.config(text="Ln 0, Col 0")
    text_area.bind("<KeyRelease>", update_status_bar)
    text_area.bind("<ButtonRelease>", update_status_bar)

    # --- Show empty sidebar on startup ---
    show_empty_sidebar()

    root.mainloop()

if __name__ == "__main__":
    main()
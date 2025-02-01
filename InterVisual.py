import customtkinter as ctk
from tkinter import filedialog, ttk
from Lexer import lexer,analyze_code 

def analyze_code_and_display(code, output_table):
    tokens_with_line = analyze_code(code)
    output_table.delete(*output_table.get_children())  
    for token in tokens_with_line:
        output_table.insert("", "end", values=(token[0], token[1], token[2]))   # tipo, valor y num de linea

def open_file(text_area):
    file_path = filedialog.askopenfilename(
        filetypes=[
            ("Todos los archivos", "*.txt;*.java;*.py;*.cpp;*.js"),
            ("Archivos de Texto", "*.txt"),
            ("Archivos de Java", "*.java"),
            ("Archivos de Python", "*.py"),
            ("Archivos de C++", "*.cpp"),
            ("Archivos de JavaScript", "*.js"),
        ]
    )
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            text_area.delete("1.0", "end")
            text_area.insert("1.0", file.read())

def run_app():
    ctk.set_appearance_mode("dark")  
    app = ctk.CTk()
    app.title("Analizador Léxico")
    app.geometry("800x600")

    title_label = ctk.CTkLabel(app, text="Analizador Léxico", font=("Arial", 24, "bold"))
    title_label.pack(pady=10)
    text_area = ctk.CTkTextbox(app, width=700, height=200, font=("Consolas", 12))
    text_area.pack(pady=10)
    open_btn = ctk.CTkButton(app, text="Abrir Archivo", command=lambda: open_file(text_area))
    open_btn.pack()

    analyze_btn = ctk.CTkButton(app, text="Analizar Código", fg_color="blue", command=lambda: analyze_code_and_display(text_area.get("1.0", "end"), output_table))
    analyze_btn.pack(pady=10)
    frame = ctk.CTkFrame(app)
    frame.pack(fill="both", expand=True)

    columns = ("Tipo", "Valor", "Línea")
    output_table = ttk.Treeview(frame, columns=columns, show="headings")
    output_table.heading("Tipo", text="Tipo")
    output_table.heading("Valor", text="Valor")
    output_table.heading("Línea", text="Línea")
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=output_table.yview)
    output_table.configure(yscroll=scrollbar.set)

    output_table.pack(fill="both", expand=True, side="left")
    scrollbar.pack(fill="y", side="right")

    app.mainloop()

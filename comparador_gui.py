import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

def comparar_listas(archivo1, archivo2):
    with open(archivo1, "r", encoding="utf-8") as f1:
        lista1 = set(line.strip() for line in f1 if line.strip())

    with open(archivo2, "r", encoding="utf-8") as f2:
        lista2 = set(line.strip() for line in f2 if line.strip())

    solo_en_1 = sorted(lista1 - lista2)
    solo_en_2 = sorted(lista2 - lista1)

    resultado = "=== SOLO EN ARCHIVO 1 ===\n"
    resultado += "\n".join(solo_en_1)
    resultado += "\n\n=== SOLO EN ARCHIVO 2 ===\n"
    resultado += "\n".join(solo_en_2)

    return resultado


def seleccionar_archivo1():
    archivo = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if archivo:
        entrada_archivo1.set(archivo)


def seleccionar_archivo2():
    archivo = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if archivo:
        entrada_archivo2.set(archivo)


def ejecutar_comparacion():
    archivo1 = entrada_archivo1.get()
    archivo2 = entrada_archivo2.get()

    if not archivo1 or not archivo2:
        messagebox.showerror("Error", "Debes seleccionar ambos archivos.")
        return

    resultado = comparar_listas(archivo1, archivo2)

    # Mostrar diferencias en la caja de texto
    texto_resultado.delete("1.0", tk.END)
    texto_resultado.insert(tk.END, resultado)


def guardar_como():
    contenido = texto_resultado.get("1.0", tk.END).strip()

    if not contenido:
        messagebox.showerror("Error", "No hay nada para guardar. Primero ejecuta la comparación.")
        return

    archivo_guardar = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt")],
        title="Guardar diferencias como..."
    )

    if archivo_guardar:
        with open(archivo_guardar, "w", encoding="utf-8") as out:
            out.write(contenido)
        messagebox.showinfo("Guardado", f"Archivo guardado en:\n{archivo_guardar}")


# ====== INTERFAZ ======
root = tk.Tk()
root.title("Comparador de Archivos TXT (v2)")

entrada_archivo1 = tk.StringVar()
entrada_archivo2 = tk.StringVar()

# Selección de archivos
tk.Label(root, text="Archivo 1:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
tk.Entry(root, textvariable=entrada_archivo1, width=50).grid(row=0, column=1)
tk.Button(root, text="Seleccionar", command=seleccionar_archivo1).grid(row=0, column=2)

tk.Label(root, text="Archivo 2:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
tk.Entry(root, textvariable=entrada_archivo2, width=50).grid(row=1, column=1)
tk.Button(root, text="Seleccionar", command=seleccionar_archivo2).grid(row=1, column=2)

# Botón comparar
tk.Button(root, text="Comparar", command=ejecutar_comparacion,
          bg="#4CAF50", fg="white", width=20).grid(row=2, column=1, pady=10)

# Caja de texto para ver las diferencias
texto_resultado = scrolledtext.ScrolledText(root, width=80, height=25)
texto_resultado.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

# Botón guardar como
tk.Button(root, text="Guardar como...", command=guardar_como,
          bg="#2196F3", fg="white", width=20).grid(row=4, column=1, pady=15)

root.mainloop()
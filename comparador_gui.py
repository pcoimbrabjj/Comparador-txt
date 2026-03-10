import tkinter as tk
from tkinter import filedialog, messagebox
import os

def comparar_listas(archivo1, archivo2, salida):
    with open(archivo1, "r", encoding="utf-8") as f1:
        lista1 = set(line.strip() for line in f1 if line.strip())

    with open(archivo2, "r", encoding="utf-8") as f2:
        lista2 = set(line.strip() for line in f2 if line.strip())

    solo_en_1 = lista1 - lista2
    solo_en_2 = lista2 - lista1

    with open(salida, "w", encoding="utf-8") as out:
        out.write("=== SOLO EN ARCHIVO 1 ===\n")
        for item in sorted(solo_en_1):
            out.write(item + "\n")

        out.write("\n=== SOLO EN ARCHIVO 2 ===\n")
        for item in sorted(solo_en_2):
            out.write(item + "\n")


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

    salida = "diferencias.txt"
    comparar_listas(archivo1, archivo2, salida)

    messagebox.showinfo("¡Listo!", f"Comparación completada.\nArchivo generado: {salida}")


# ====== INTERFAZ ======
root = tk.Tk()
root.title("Comparador de Archivos TXT")

entrada_archivo1 = tk.StringVar()
entrada_archivo2 = tk.StringVar()

tk.Label(root, text="Archivo 1:").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=entrada_archivo1, width=50).grid(row=0, column=1)
tk.Button(root, text="Seleccionar", command=seleccionar_archivo1).grid(row=0, column=2)

tk.Label(root, text="Archivo 2:").grid(row=1, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=entrada_archivo2, width=50).grid(row=1, column=1)
tk.Button(root, text="Seleccionar", command=seleccionar_archivo2).grid(row=1, column=2)

tk.Button(root, text="Comparar", command=ejecutar_comparacion,
          bg="#4CAF50", fg="white", width=20).grid(row=2, column=1, pady=20)

root.mainloop()
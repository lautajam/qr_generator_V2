import qrcode
import os
import re
import tkinter as tk
from tkinter import filedialog, messagebox

# Función para limpiar nombres de archivo
def sanitize_filename(name):
    return re.sub(r'[\\/*?:"<>|]', '_', name)

# Función para generar códigos QR
def generate_qr_codes():
    url_file = filedialog.askopenfilename(
        title="Seleccionar archivo de URLs",
        filetypes=[("Text files", "*.txt")]
    )
    
    if not url_file:
        return
    
    output_folder = filedialog.askdirectory(title="Seleccionar carpeta de salida")
    
    if not output_folder:
        return
    
    try:
        with open(url_file, "r") as file:
            urls = file.readlines()
            for i, line in enumerate(urls):
                line = line.strip()
                if line:
                    if ';' in line:
                        name, url = line.split(';', 1)
                    else:
                        url = line
                        name = url.replace("https://", "").replace("http://", "").replace("/", "_").replace(":", "_")

                    # Limpiar el nombre del archivo
                    name = sanitize_filename(name)

                    # Crear el objeto QR
                    qr = qrcode.QRCode(
                        version=1,
                        error_correction=qrcode.constants.ERROR_CORRECT_L,
                        box_size=10,
                        border=4,
                    )
                    qr.add_data(url)
                    qr.make(fit=True)

                    # Crear la imagen del QR
                    img = qr.make_image(fill_color="black", back_color="white")

                    # Guardar la imagen en la carpeta de salida
                    img_path = os.path.join(output_folder, f"{name}.png")
                    img.save(img_path)

            messagebox.showinfo("Éxito", "Todos los códigos QR han sido generados.")
    
    except Exception as e:
        messagebox.showerror("Error", f"Error al leer el archivo {url_file}: {e}")

# Función para mostrar ayuda
def show_help():
    messagebox.showinfo(
        "Ayuda",
        "Para el archivo del que se saquen las URLs, debe tener el siguiente formato:\n"
        "nombre_para_qr;url\n\n"
        "Si el archivo no sigue este formato, el nombre del código QR será la URL."
    )

# Función principal para configurar y ejecutar la aplicación
def main():
    
    # Configuración de la ventana principal
    root = tk.Tk()
    root.title("Generador de Códigos QR")
    root.geometry("500x150")

    # Impedir el redimensionamiento
    root.resizable(False, False)  # (ancho, alto)

    # Etiquetas y botones
    label = tk.Label(root, text="Generador de Códigos QR desde un archivo de URLs", font=("Arial", 14))
    label.pack(pady=10)

    generate_button = tk.Button(root, text="Generar Códigos QR", command=generate_qr_codes, font=("Arial", 12))
    generate_button.pack(pady=5)

    help_button = tk.Button(root, text="Ayuda", command=show_help, font=("Arial", 12))
    help_button.pack(pady=10)

    # Iniciar la aplicación
    root.mainloop()

# Punto de entrada principal
if __name__ == "__main__":
    main()

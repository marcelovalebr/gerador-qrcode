import tkinter as tk
import qrcode
from tkinter import filedialog
from PIL import Image, ImageTk

# Variável global para armazenar a imagem do QR code
qr_img_display = None
qr_img_save = None

def generate_qr_code():
    global qr_img_display, qr_img_save
    
    url = entry.get()
    
    # Sempre redimensione a imagem para o tamanho pequeno para exibição no aplicativo
    display_size = (200, 200)
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Redimensiona a imagem para exibição
    img = img.resize(display_size, Image.BILINEAR)
    qr_img_display = ImageTk.PhotoImage(img)
    
    qr_label.config(image=qr_img_display)
    
    # Salva a imagem original sem redimensionar para uso posterior no download
    qr_img_save = img
    
    # Aumente o tamanho da janela quando o QR Code for gerado
    window.geometry("400x450")

def save_qr_code():
    url = entry.get()
    size_option = size_var.get()
    
    if size_option == "Pequeno":
        save_size = (100, 100)
    elif size_option == "Médio":
        save_size = (200, 200)
    elif size_option == "Grande":
        save_size = (300, 300)
    else:
        save_size = (200, 200)
    
    # Utiliza a imagem original para o download, redimensionando de acordo com as dimensões escolhidas
    img = qr_img_save.resize(save_size, Image.BILINEAR)
    
    # Abra a caixa de diálogo de salvamento e permita que o usuário escolha onde salvar
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    
    if file_path:
        img.save(file_path)

# Criar janela com tamanho inicial menor
window = tk.Tk()
window.title("Gerador de QR Code")
window.geometry("400x200")  # Defina o tamanho inicial menor

# Caixa de entrada para a URL
url_label = tk.Label(window, text="URL:")
url_label.pack()
entry = tk.Entry(window)
entry.pack()

# Opções de dimensões
size_label = tk.Label(window, text="Tamanho do QR Code:")
size_label.pack()
size_options = ["Pequeno", "Médio", "Grande"]
size_var = tk.StringVar()
size_var.set("Médio")  # Defina o tamanho médio como padrão
size_menu = tk.OptionMenu(window, size_var, *size_options)
size_menu.pack()

# Botão para gerar QR Code
generate_button = tk.Button(window, text="Gerar QR Code", command=generate_qr_code)
generate_button.pack()

# Rótulo para exibir o QR Code
qr_label = tk.Label(window)
qr_label.pack()

# Botão para salvar o QR Code
save_button = tk.Button(window, text="Salvar QR Code", command=save_qr_code)
save_button.pack()

# Iniciar a janela
window.mainloop()

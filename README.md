# Gerador de QR Code

Este é um aplicativo de desktop em Python que gera QR Codes a partir de URLs fornecidas pelos usuários. O QR Code gerado pode ser exibido na tela e salvo em diferentes tamanhos. A interface gráfica foi criada com `tkinter` e a geração de QR Codes com `qrcode`.

## Funcionalidades

- **Gerar QR Codes:** Insira uma URL e o aplicativo gerará um QR Code correspondente.
- **Salvar QR Codes:** Salve o QR Code gerado em diferentes tamanhos (Pequeno, Médio, Grande).

## Tecnologias Utilizadas

- Python
- Tkinter (para interface gráfica)
- Qrcode (para geração de QR Codes)
- PIL/Pillow (para manipulação de imagens)

## Pré-requisitos

- Python 3.x
- Bibliotecas Python:
  - `tkinter` (inclusa por padrão em Python)
  - `qrcode`
  - `Pillow`

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/gerador-de-qr-code.git
    cd gerador-de-qr-code
    ```

2. Instale as dependências:
    ```bash
    pip install qrcode[pil] pillow
    ```

3. Execute o script:
    ```bash
    python gerador_qr_code.py
    ```

## Uso

1. Abra o aplicativo e insira a URL que você deseja converter em QR Code.
2. Selecione o tamanho desejado para o QR Code (Pequeno, Médio ou Grande).
3. Clique no botão "Gerar QR Code" para criar o QR Code.
4. O QR Code gerado será exibido na tela.
5. Para salvar o QR Code, clique no botão "Salvar QR Code" e escolha o local e o nome do arquivo.

## Código Exemplo

```python
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

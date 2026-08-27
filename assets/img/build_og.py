"""Gera imagem Open Graph (1200x630) com fundo navy + logo centralizada."""
from PIL import Image

img_dir = r"C:\Users\lucca.vilarins\Desktop\lianeng\assets\img"

W, H = 1200, 630
bg = Image.new("RGBA", (W, H), (8, 10, 40, 255))

logo = Image.open(f"{img_dir}\\logo-light.png").convert("RGBA")
# Escala a logo para caber com margem confortável
target_w = int(W * 0.72)
ratio = target_w / logo.width
target_h = int(logo.height * ratio)
logo_resized = logo.resize((target_w, target_h), Image.LANCZOS)

x = (W - target_w) // 2
y = (H - target_h) // 2
bg.paste(logo_resized, (x, y), logo_resized)

bg.convert("RGB").save(f"{img_dir}\\og-image.jpg", quality=92)
print("og-image.jpg saved", bg.size)

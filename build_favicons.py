"""Gera favicons e recorta margens transparentes das logos."""
from PIL import Image

img_dir = r"C:\Users\lucca.vilarins\Desktop\lianeng\assets\img"

def trim(im):
    bbox = im.getbbox()
    return im.crop(bbox) if bbox else im

# Recorta a logo completa (remove margem transparente ao redor)
logo = Image.open(f"{img_dir}\\logo.png")
logo_trimmed = trim(logo)
logo_trimmed.save(f"{img_dir}\\logo.png")
print("logo.png trimmed ->", logo_trimmed.size)

# Recorta o símbolo isolado
symbol = Image.open(f"{img_dir}\\favicon-src.png")
symbol_trimmed = trim(symbol)

sizes = [16, 32, 48, 180, 192, 512]
for s in sizes:
    resized = symbol_trimmed.resize((s, s), Image.LANCZOS)
    if s == 180:
        resized.save(f"{img_dir}\\apple-touch-icon.png")
    elif s == 512:
        resized.save(f"{img_dir}\\icon-512.png")
    elif s == 192:
        resized.save(f"{img_dir}\\icon-192.png")
    else:
        resized.save(f"{img_dir}\\favicon-{s}.png")
    print(f"saved size {s}")

# favicon.ico multi-size
symbol_trimmed.save(f"{img_dir}\\favicon.ico", sizes=[(16,16),(32,32),(48,48)])
print("favicon.ico saved")

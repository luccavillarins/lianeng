"""Gera uma versao clara da logo (texto/quadrado navy -> branco) para uso em fundos escuros (header/footer)."""
from PIL import Image
import numpy as np

img_dir = r"C:\Users\lucca.vilarins\Desktop\lianeng\assets\img"

logo = Image.open(f"{img_dir}\\logo.png").convert("RGBA")
arr = np.array(logo)

rgb = arr[:, :, :3].astype(int)
alpha = arr[:, :, 3]

# navy pixels (o quadrado do simbolo + texto "LIAN")
navy_mask = (rgb[:, :, 0] < 60) & (rgb[:, :, 1] < 60) & (rgb[:, :, 2] < 120) & (alpha > 0)

out = arr.copy()
out[navy_mask, 0] = 255
out[navy_mask, 1] = 255
out[navy_mask, 2] = 255

# O "L" branco interno do simbolo precisa virar navy (senao some no fundo branco->branco)
white_mask = (rgb[:, :, 0] > 230) & (rgb[:, :, 1] > 230) & (rgb[:, :, 2] > 230) & (alpha > 200)
out[white_mask, 0] = 9
out[white_mask, 1] = 0
out[white_mask, 2] = 65

Image.fromarray(out, "RGBA").save(f"{img_dir}\\logo-light.png")
print("logo-light.png salvo", out.shape)

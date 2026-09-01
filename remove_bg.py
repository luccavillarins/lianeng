"""
Remove fundo branco de logos LIAN Engenharia via flood-fill a partir das bordas,
preservando detalhes internos brancos (ex.: o "L" vazado dentro do quadrado).
Também aplica anti-aliasing na borda de transparência para evitar serrilhado.
"""
import sys
from collections import deque
import numpy as np
from PIL import Image

def remove_white_background(path_in, path_out, threshold=235, tolerance=18, out_size=None):
    im = Image.open(path_in).convert("RGBA")
    arr = np.array(im)
    h, w = arr.shape[:2]
    rgb = arr[:, :, :3].astype(np.int16)

    # Máscara de pixels "quase brancos"
    near_white = np.all(rgb >= threshold, axis=2)

    visited = np.zeros((h, w), dtype=bool)
    q = deque()

    # Semente: todas as bordas da imagem que sejam quase-brancas
    for x in range(w):
        for y in (0, h - 1):
            if near_white[y, x] and not visited[y, x]:
                visited[y, x] = True
                q.append((y, x))
    for y in range(h):
        for x in (0, w - 1):
            if near_white[y, x] and not visited[y, x]:
                visited[y, x] = True
                q.append((y, x))

    while q:
        y, x = q.popleft()
        for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
            ny, nx = y+dy, x+dx
            if 0 <= ny < h and 0 <= nx < w and not visited[ny, nx] and near_white[ny, nx]:
                visited[ny, nx] = True
                q.append((ny, nx))

    alpha = arr[:, :, 3].copy()
    alpha[visited] = 0
    arr[:, :, 3] = alpha

    # Suaviza a borda de corte (halo) reduzindo alpha de pixels adjacentes claros
    edge = np.zeros((h, w), dtype=bool)
    vis_pad = np.pad(visited, 1, mode="constant", constant_values=False)
    for dy, dx in ((1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)):
        edge |= vis_pad[1+dy:1+dy+h, 1+dx:1+dx+w]
    edge &= ~visited

    bright = np.all(rgb >= 200, axis=2)
    soften = edge & bright
    arr[soften, 3] = (arr[soften, 3].astype(np.float32) * 0.35).astype(np.uint8)

    out = Image.fromarray(arr, "RGBA")
    if out_size:
        out = out.resize(out_size, Image.LANCZOS)
    out.save(path_out, "PNG")
    print(f"OK: {path_out} ({out.size[0]}x{out.size[1]})")

if __name__ == "__main__":
    src_dir = r"C:\Users\lucca.vilarins\Desktop\lian doc\img"
    dst_dir = r"C:\Users\lucca.vilarins\Desktop\lianeng\assets\img"

    # Logo completa (ícone + LIAN ENGENHARIA) -> para o header
    remove_white_background(f"{src_dir}\\logomarca.png", f"{dst_dir}\\logo.png")

    # Símbolo isolado (quadrado com L) -> favicon / apple-touch-icon
    remove_white_background(f"{src_dir}\\MARCA LIAN.png", f"{dst_dir}\\favicon-src.png")

#!/usr/bin/python3

import matplotlib.pyplot as plt
import networkx as nx
import PIL.Image
import requests
from io import BytesIO

# URLs das imagens para os nós do grafo
icons = {
    "router": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Router_symbol-Blue.svg/480px-Router_symbol-Blue.svg.png",
    "switch": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Router_symbol-Blue.svg/480px-Router_symbol-Blue.svg.png",
    "PC": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Router_symbol-Blue.svg/480px-Router_symbol-Blue.svg.png",
}

# Função para baixar e carregar imagens
def load_image_from_url(url):
    response = requests.get(url)
    return PIL.Image.open(BytesIO(response.content))

# Baixar e carregar as imagens
images = {k: load_image_from_url(url) for k, url in icons.items()}

# Criar o grafo de rede de computadores
G = nx.Graph()

G.add_node("router", image=images["router"])
for i in range(1, 4):
    G.add_node(f"switch_{i}", image=images["switch"])
    for j in range(1, 4):
        G.add_node(f"PC_{i}_{j}", image=images["PC"])

# Conectar os nós do grafo
G.add_edge("router", "switch_1")
G.add_edge("router", "switch_2")
G.add_edge("router", "switch_3")
for u in range(1, 4):
    for v in range(1, 4):
        G.add_edge(f"switch_{u}", f"PC_{u}_{v}")

# Gerar layout e criar figura
pos = nx.spring_layout(G, seed=1734289230)
fig, ax = plt.subplots()

# Desenhar as conexões entre os nós
nx.draw_networkx_edges(
    G,
    pos=pos,
    ax=ax,
    arrows=True,
    arrowstyle="-",
    min_source_margin=15,
    min_target_margin=15,
)

# Transformações para posicionar imagens corretamente
tr_figure = ax.transData.transform
tr_axes = fig.transFigure.inverted().transform

# Definir tamanho dos ícones no gráfico
icon_size = (ax.get_xlim()[1] - ax.get_xlim()[0]) * 0.025
icon_center = icon_size / 2.0

# Adicionar imagens nos nós
for n in G.nodes:
    xf, yf = tr_figure(pos[n])
    xa, ya = tr_axes((xf, yf))
    a = plt.axes([xa - icon_center, ya - icon_center, icon_size, icon_size])
    a.imshow(G.nodes[n]["image"])
    a.axis("off")

plt.show()


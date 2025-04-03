import networkx as nx
import matplotlib.pyplot as plt

# Criando o grafo
G = nx.DiGraph()

# Adicionando conexões
edges = [
    ("LaTeX", "Diagramas"),
    ("LaTeX", "Editores"),
    ("Diagramas", "PGFPlo​​ts"),
    ("Diagramas", "TikZ"),
    ("Editores", "Overleaf"),
    ("Editores", "TeXstudio"),
]
G.add_edges_from(edges)

# Definir a posição dos nós manualmente para melhor estética
pos = {
    "LaTeX": (0, 3),
    "Diagramas": (-1, 1.5),
    "Editores": (1, 1.5),
    "PGFPlo​​ts": (-1.5, 0),
    "TikZ": (-0.5, 0),
    "Overleaf": (0.5, 0),
    "TeXstudio": (1.5, 0),
}

# Criando a figura
plt.figure(figsize=(7, 5))
nx.draw(
    G, pos, with_labels=True, node_size=2500, node_color="mediumpurple",
    font_size=10, font_weight="bold", edge_color="black", alpha=0.85,
    arrowsize=15, connectionstyle="arc3,rad=0.2"  # Faz curvas suaves
)

# Exibir o gráfico
plt.show()


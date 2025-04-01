import matplotlib.pyplot as plt
import matplotlib.patches as patches
import textwrap



# Definição dos passos
steps = [
    ("Step 01", "Defining the Objectives of the Event"),
    ("Step 02", "Selecting the Best Venue for the Occasion"),
    ("Step 03", "Developing a Comprehensive Program for Attendees"),
    ("Step 04", "Coordinating Logistics and Ensuring Smooth Operations"),
    ("Step 05", "Evaluating the Success and Gathering Feedback")
]

colors = ["#8ED7C6", "#1E4D7A", "#1DB5A0", "#1E4D7A", "#1DB5A0"]

box_beak = 0.4
box_width = 2.2 # menor ou igual a 2+box_beak
box_height = 0.7
box_fontsize = 12 
box_fontfamily= 'monospace' # {FONTNAME, 'serif', 'sans-serif', 'cursive', 'fantasy', 'monospace'}

delta_boxs = 0.2

extrabox_width = 1.5 # menor a box_width
extrabox_height = 1.0
extrabox_pad = 0.15
extrabox_fontsize = 9
extrabox_fontfamily='monospace' # {FONTNAME, 'serif', 'sans-serif', 'cursive', 'fantasy', 'monospace'}

def wrap_text(text, width=20):
    """Quebra o texto em múltiplas linhas para caber dentro da caixa."""
    return "\n".join(textwrap.wrap(text, width))

# Criando a figura
fig, ax = plt.subplots(figsize=(10, 5))
#ax.set_xlim(0, 10)
#ax.set_ylim(0, 5)
ax.axis('off')

# Desenhando os passos
for i, (step, text) in enumerate(steps):
    x = i * 2
    
    extrabox_y0 = 0.0
    box_y0 = extrabox_y0 + extrabox_pad + extrabox_height + delta_boxs
    

    triangle = patches.Polygon(
        [(x + 0.5 * box_width, box_y0), 
         (x + 0.5 * box_width-delta_boxs, box_y0-delta_boxs), 
         (x + 0.5 * box_width+delta_boxs, box_y0-delta_boxs)],
        closed=True, facecolor=colors[i], edgecolor="black")
    ax.add_patch(triangle)
    
    # Criando as setas como polígonos
    arrow = patches.Polygon(
        [(x, box_y0), 
         (x + box_width - box_beak, box_y0), 
         (x + box_width, box_y0+ 0.5*box_height),
         (x + box_width - box_beak, box_y0 + box_height), 
         (x, box_y0 + box_height), 
         (x + box_beak, box_y0+ 0.5*box_height)],
        closed=True, facecolor=colors[i], edgecolor="black")
    ax.add_patch(arrow)
    
    ax.text(    x + 0.5*(box_width), box_y0+ 0.5*box_height, 
                step, 
                ha="center", 
                va="center", 
                fontsize=box_fontsize,
                fontfamily=box_fontfamily, 
                color="white", 
                fontweight="bold"
                )
    
    # Criando as caixas de texto abaixo
    box = patches.FancyBboxPatch(
        (x + 0.5*box_width-0.5*extrabox_width, extrabox_y0), #(tupla: coordenadas x e y do canto inferior esquerdo da caixa)
        extrabox_width, # largura da caixa
        extrabox_height, # altura da caixa
        boxstyle="round,pad="+str(extrabox_pad), # pad=0.1: Ao redor do texto
        facecolor="white", # cor fundo
        edgecolor="black" # cor borda
        )
    ax.add_patch(box)
    
    # Quebrando o texto para caber na caixa
    wrapped_text = wrap_text(text, width=18)
    ax.text(x + 0.5 * box_width, 
            extrabox_y0+0.5*extrabox_height, 
            wrapped_text, 
            ha="center", 
            va="center", 
            fontfamily=extrabox_fontfamily,
            fontsize=extrabox_fontsize, 
            fontweight="bold"
            )



plt.gca().set_aspect('equal', adjustable='box')
plt.xlim(extrabox_y0, (len(steps)-1) * 2 + box_width)
plt.ylim(extrabox_y0-extrabox_pad, box_y0+box_height)

plt.tight_layout(pad=0.5)  

#plt.savefig("latex_workflow2.eps", bbox_inches='tight', pad_inches=0.1)
#plt.savefig("latex_workflow2.png", dpi=300)
plt.savefig("latex_workflow2.pdf", bbox_inches='tight', pad_inches=0.1, dpi=300)


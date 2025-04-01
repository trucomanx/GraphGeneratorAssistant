import matplotlib.pyplot as plt
from matplotlib.patches import Arrow, Circle
import numpy as np


# Configurações
labels = ["Edit", "pdfLaTeX", "BibTeX", "make\nindex", "pdfLaTeX"]
colors = ["red", "green", "#2222AA", "yellow", "gray"] # plt.cm.tab10.colors

element_alpha   = 1.0
element_radius  = 0.045 
proccess_radius = 0.100

text_fontsize=28
text_weight='bold'
text_color="black"
text_fontfamily='monospace' # {FONTNAME, 'serif', 'sans-serif', 'cursive', 'fantasy', 'monospace'}

arrow_color = "gray"  # arrow color
arrow_thick = 8       # arrow line thickness
arrow_scale = 20      # arrow head scale



fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal', adjustable='box')
plt.axis('off')


# Desenha nós
L = len(labels)
angles = np.linspace(0, 2*np.pi, L, endpoint=False)
for i, (label, color) in enumerate(zip(labels, colors)):
    
    # center of element circle
    x = proccess_radius * np.cos(angles[i])
    y = proccess_radius * np.sin(angles[i])
    
    # add circle
    circle = Circle((x, y), 
                    element_radius,       # circle radius
                    edgecolor=color,      # circle edge color
                    facecolor=color,      # circle face color
                    alpha=element_alpha)
    ax.add_patch(circle)
    
    # add circle text
    ax.text(x, y, 
            label, 
            ha='center', 
            va='center', 
            fontfamily=text_fontfamily,
            fontsize=text_fontsize, 
            weight=text_weight, 
            color=text_color)
    
    # arrow working
    next_i = (i + 1) % L
    x_end = proccess_radius * np.cos(angles[next_i])
    y_end = proccess_radius * np.sin(angles[next_i])
    
    # Start and end of arrows
    start_x = x + (x_end - x) * element_radius / np.hypot(x_end - x, y_end - y)
    start_y = y + (y_end - y) * element_radius / np.hypot(x_end - x, y_end - y)
    end_x = x_end - (x_end - x) * element_radius / np.hypot(x_end - x, y_end - y)
    end_y = y_end - (y_end - y) * element_radius / np.hypot(x_end - x, y_end - y)
    
    # add arrow
    ax.annotate("",
        xy=(end_x, end_y),          # arrow end point
        xytext=(start_x, start_y),  # arrow initial point
        arrowprops=dict(
            arrowstyle="->,head_length=1,head_width=0.5",  # head size 
            color=arrow_color,
            lw=arrow_thick,            # arrow thickness
            shrinkA=arrow_thick,       # Afastamento do ponto inicial
            shrinkB=0,                 # Afastamento do ponto final
            mutation_scale=arrow_scale # head size scale
        )
    )


R = element_radius + proccess_radius

if L % 2 == 0:
    plt.xlim(-R, R)
    plt.ylim(-R, R)
else:
    alpha = np.pi/L
    plt.xlim(-proccess_radius*np.cos(alpha)-element_radius, R)
    plt.ylim(-R, R)
    
plt.tight_layout(pad=0.5)  
plt.savefig("latex_workflow1.pdf", bbox_inches='tight', pad_inches=0.1, dpi=600)
#plt.savefig("latex_workflow1.png", dpi=600)
#plt.savefig("latex_workflow1.eps", bbox_inches='tight')


---
name: system-diagram
description: "Generate high-level system architecture diagrams from text descriptions. Outputs clean PNG files with minimal text and no titles. Splits complex systems into multiple focused diagrams. Use when the user asks to visualize, diagram, or draw a system, architecture, pipeline, or data flow."
---

# System Diagram Generator

Generate clean, high-level system diagrams as PNG from text descriptions.

## Requirements

- **graphviz** system binary and Python package. Check and install if missing:

```bash
# Check
which dot && python3 -c "import graphviz" 2>/dev/null && echo "OK"
# Install if needed
brew install graphviz
pip3 install --break-system-packages graphviz
```

> **Status**: graphviz 15.1.0 (dot) and Python graphviz 0.21 are installed.

If brew/pip are unavailable, fall back to the Pillow-based renderer (see Fallback section).

## Workflow

1. Parse the user's text description into logical components, connections, and data flows.
2. Decide whether to split into multiple diagrams. Split when:
   - The system has 2+ distinct subsystems with different concerns (e.g., training vs serving).
   - A single diagram would exceed ~15 nodes.
   - The user's description naturally segments (e.g., "offline pipeline" and "online serving").
3. For each diagram, generate a self-contained Python script and execute it.
4. Output files as `<topic>.png` in the current working directory (or user-specified path).
5. Show the generated images inline with `![[filename.png]]`.

## Diagram Style Rules

- **No title.** Do not set `label` on the graph.
- **Minimal text.** Node labels: 1-3 words max. Edge labels: 1-2 words or omit.
- **High-level.** Show major components and data flows, not implementation details.
- **Clean layout.** Use `rankdir="LR"` (left-to-right) by default. Switch to `TB` for deep hierarchies.
- **Visual grouping.** Use `subgraph cluster_*` for logical groupings (dashed border, light fill, no bold title — use small italic font for cluster labels if needed).
- **Consistent shapes:**
  - Rounded boxes (`shape="box", style="rounded"`) — services, components
  - Cylinders (`shape="cylinder"`) — databases, storage
  - Parallelogram (`shape="parallelogram"`) — data streams, queues
  - Diamond (`shape="diamond"`) — decision points
  - Ellipse (`shape="ellipse"`) — external systems, users
- **Colors.** Muted, professional palette. Use soft fills (`fillcolor`), not bright colors. Example fills: `"#E8F4FD"` (blue), `"#FFF3E0"` (orange), `"#E8F5E9"` (green), `"#F3E5F5"` (purple), `"#FFEBEE"` (red), `"#F5F5F5"` (gray).
- **Fonts.** `fontname="Helvetica"`, `fontsize="11"` for nodes, `fontsize="9"` for edges.
- **Edges.** Solid arrows for primary data flow. Dashed for async/optional. Use `arrowsize="0.7"`.
- **DPI.** Render at `dpi="150"` for crisp output.

## Script Template

```python
import graphviz

g = graphviz.Digraph(format="png", engine="dot")
g.attr(rankdir="LR", dpi="150", bgcolor="white", pad="0.5",
       nodesep="0.6", ranksep="0.8")
g.attr("node", shape="box", style="rounded,filled", fillcolor="#F5F5F5",
       fontname="Helvetica", fontsize="11", margin="0.2,0.1")
g.attr("edge", fontname="Helvetica", fontsize="9", arrowsize="0.7", color="#666666")

# --- nodes and edges here ---

g.render("<topic>", cleanup=True)  # produces <topic>.png
```

## Naming

- Single diagram: `<topic>.png` (e.g., `rec_system.png`, `training_pipeline.png`)
- Multiple diagrams: `<topic>_<aspect>.png` (e.g., `rec_system_training.png`, `rec_system_serving.png`)
- Use snake_case, no spaces.

## Fallback: Pillow Renderer

If graphviz cannot be installed, use PIL/Pillow to draw:

```python
from PIL import Image, ImageDraw, ImageFont
img = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(img)
# draw.rounded_rectangle, draw.text, draw.line with arrowheads
img.save("<topic>.png")
```

This produces simpler diagrams but avoids install dependencies. Use the same style rules (colors, minimal text).

## Examples

User: "diagram a recommendation system with feature store, model training, and online serving"

Split into 2 diagrams:
- `rec_system_offline.png` — Feature ingestion → Feature Store → Training Data → Model Training → Model Registry
- `rec_system_online.png` — User Request → Feature Lookup → Model Serving → Ranking → Response

User: "draw the transformer architecture"

Single diagram:
- `transformer.png` — Input Embedding → Encoder Stack → Decoder Stack → Output, with attention subgraphs

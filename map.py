import settings as st
import map_generator as mgr

text_map = mgr.map_create()

world_map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == 'W':
            world_map.add((i*st.TILE, j*st.TILE))

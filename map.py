import settings as st
import map_generator as mgr

text_map = mgr.map_create()

world_map = {}
mini_map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char != '.':
            mini_map.add((i*st.MAP_TILE, j*st.MAP_TILE))
            if char == '1':
                world_map[(i*st.TILE, j*st.TILE)] = '1'
            elif char == '2':
                world_map[(i*st.TILE, j*st.TILE)] = '2'

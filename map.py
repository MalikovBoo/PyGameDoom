import settings as st

text_map = [
    'WWWWWWWWWWWW',
    'W..........W',
    'W....WW....W',
    'W......W...W',
    'W..W.......W',
    'W....WW....W',
    'W..........W',
    'WWWWWWWWWWWW'
]

world_map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == 'W':
            world_map.add((i*st.TILE, j*st.TILE))


from math import ceil

def readable_coords(level):
    # TODO: NOT WORKING... see: https://github.com/xivapi/ffxiv-datamining/blob/master/docs/MapCoordinates.md
    tilescale = 50.0
    scale = 1.0
    m = 2048.0 / (scale / 100.0)
    tilecount = m / tilescale
    x = float(level['X'])
    y = float(level['Y'])
    out_x = ceil(round((x / tilescale) + (tilecount / 2.0), 1))
    out_y = ceil(round((y / tilescale) + (tilecount / 2.0), 1))
    return {
        "x": out_x,
        "y": out_y
    }

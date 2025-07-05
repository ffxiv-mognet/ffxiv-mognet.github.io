
from math import ceil, floor


def readable_coords(level, map):
    # adapted from https://github.com/ffxiv-teamcraft/ffxiv-teamcraft/blob/c919ee4/apps/data-extraction/src/abstract-extractor.ts#L110
    x = floor(+float(level['X']) * 100.0) / 100.0
    y = floor(+float(level['Z']) * 100.0) / 100.0
    z = floor(+float(level['Y']) * 100.0) / 100.0
    c = int(map['SizeFactor']) / 100.0
    offset_x = int(map['Offset{X}'])
    offset_y = int(map['Offset{Y}'])

    x1 = (+x + offset_x) * c
    y1 = (+y + offset_y) * c

    def trunc_1(k):
        return int(k * 10)/10.0

    return {
        "x": trunc_1(floor(((41.0 / c) * ((+x1 + 1024.0) / 2048.0) + 1.0) * 100.0) / 100.0),
        "y": trunc_1(floor(((41.0 / c) * ((+y1 + 1024.0) / 2048.0) + 1.0) * 100.0) / 100.0),
        "z": trunc_1(floor(z) / 100.0)
    }

# -*- coding: utf-8 -*-
"""

@author: ncoz

@copyright: ZRC SAZU (Novi trg 2, 1000 Ljubljana, Slovenia)

@history:
    Created on Fri Feb 14 11:27:01 2020
"""

def round_multiple(nr, xL, pix):
    """
    Rounds to the nearest multiple of the pixle resolution
    """
    # nr = 396455.12
    # xL = 348890
    # pix = 10
    return pix * round((nr - xL) / pix) + xL


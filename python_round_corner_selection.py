#!/usr/bin/env python
# -*- coding:utf-8 -*-

from gimpfu import *

def python_round_corner_selection(img, drawable, width, height, radius, x, y, antialias):
    diameter = radius * 2
    pdb.gimp_ellipse_select(img, x, y, diameter, diameter, 2, antialias, False, 0)
    pdb.gimp_ellipse_select(img, x + width - diameter, y, diameter, diameter, 0, antialias, False, 0)
    pdb.gimp_ellipse_select(img, x + width - diameter, y + height - diameter, diameter, diameter, 0, antialias, False, 0)
    pdb.gimp_ellipse_select(img, x, y + height - diameter, diameter, diameter, 0, antialias, False, 0)
    pdb.gimp_rect_select(img, x + radius, y, width - diameter, height, 0, False, 0)
    pdb.gimp_rect_select(img, x, y + radius, width, height - diameter, 0, False, 0)
    img.undo_group_start()
    img.undo_group_end()
    
register(
  "create-rounded-corner-selection",
  "角丸選択範囲を作成します。",
  "角丸選択範囲を作成します。",
  "t87rtp",
  "t87rtp",
  "2012.1.5",
  "<Image>/Python-fu/Selection/角丸選択範囲の作成",
  "*",
  [
   (PF_INT32, "width", "幅", 500),
   (PF_INT32, "height"  ,"高さ", 500),
   (PF_INT32, "radius"  ,"半径", 50),
   (PF_INT32, "offset_x"  ,"横位置", 0),
   (PF_INT32, "offset_y"  ,"縦位置", 0),
   (PF_TOGGLE, "antialias", "アンチエイリアス", True)
   ],
  [],
  python_round_corner_selection)

main()
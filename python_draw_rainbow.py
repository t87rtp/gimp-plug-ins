#!/usr/bin/env python
# -*- coding:utf-8 -*-

from gimpfu import *

def python_draw_rainbow(img, drawable, direction, start_color):
    img.undo_group_start()
    
    def_foreground = gimp.get_foreground()
    
    if direction == 1:
        divsion = img.height / 360
    elif direction == 0:
        divsion = img.width / 360
    x = 0
    y = 0
    i = 0
    
    gimp.set_foreground(start_color) 
    pdb.gimp_drawable_fill(drawable, 0)
    
    while i < 360:
        if direction == 0:
            pdb.gimp_rect_select(img, x, y, divsion, img.height, 2, False, 0)
            x = x + divsion
        elif direction == 1:
            pdb.gimp_rect_select(img, x, y, img.width, divsion, 2, False, 0)
            y = y + divsion
        pdb.gimp_hue_saturation(drawable, 0, i - 180, 50, 50)
        i = i + 1
                
    pdb.gimp_selection_clear(img)
    gimp.set_foreground(def_foreground)
    
    gimp.displays_flush()

    img.undo_group_end()

register(
  "python-fu-draw-rainbow",
  "summary",
  "description",
  "t87rtp",
  "t87rtp",
  "date",
  "<Image>/Python-fu/Filter/虹を描画",
  "*",
  [
   (PF_RADIO, "direction" , "方向", 0, (("縦", 1), ("横", 0))),
   (PF_COLOR ,"start_color" ,"始まりの色" , (255, 0, 0))
   ],
  [],
  python_draw_rainbow)

main()
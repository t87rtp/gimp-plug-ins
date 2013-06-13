#!/usr/bin/env python
# -*- coding:utf-8 -*-

from gimpfu import *

def python_layers_replace_color(img, drawable, c_b, c_a):
    img.undo_group_start()
    
    for layer in img.layers:
        from_red, from_green, from_blue, aaa = c_b
        to_red, to_green, to_blue, aaa = c_a
        pdb.plug_in_exchange(img, layer, from_red, from_green, from_blue, to_red, to_green, to_blue, 0, 0, 0)
    
    gimp.displays_flush()
    img.undo_group_end()

register(
  "python-fu-layers-replace-color",
  "すべてのレイヤーの任意の色を指定した色に置き換えます。",
  "すべてのレイヤーの任意の色を指定した色に置き換えます。",
  "t87rtp",
  "t87rtp",
  "2013.06.12",
  "<Image>/Python-fu/Layer/すべてのレイヤーの色を置き換え",
  "*",
  [
   (PF_COLOR, "color_befor", "変換前の色", (255, 255, 255)),
   (PF_COLOR, "color_after", "変換後の色", (0, 0, 0))
   ],
  [],
  python_layers_replace_color)

main()
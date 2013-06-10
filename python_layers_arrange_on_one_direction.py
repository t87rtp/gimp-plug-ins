#!/usr/bin/env python
# -*- coding:utf-8 -*-

from gimpfu import *

def python_layers_arrange_on_one_direction(img, drawable, direction):
    img.undo_group_start()
    def_active_layer = pdb.gimp_image_get_active_layer(img)

    layers = img.layers
    offset_x = 0
    offset_y = 0
    for layer in layers:
        pdb.gimp_layer_set_offsets(layer, offset_x, offset_y)
        if direction == 1:
            offset_y = offset_y + layer.height
        elif direction == 0:
            offset_x = offset_x + layer.width
    
    pdb.gimp_image_resize_to_layers(img)
        
    pdb.gimp_image_set_active_layer(img, def_active_layer)
    gimp.displays_flush()

    img.undo_group_end()

register(
  "python-fu-layers-arrange-on-one-direction",
  "すべてのレイヤーを並べます",
  "すべてのレイヤーを縦方向または横方向に並べます。",
  "t87rtp",
  "t87rtp",
  "date",
  "<Image>/Python-fu/Layer/すべてのレイヤーを並べる",
  "*",
  [
   (PF_RADIO, "direction" , "方向", 1, (("縦", 1), ("横", 0))),
   ],
  [],
  python_layers_arrange_on_one_direction)

main()
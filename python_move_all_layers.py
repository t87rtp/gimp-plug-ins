#!/usr/bin/env python
# -*- coding:utf-8 -*-

from gimpfu import *

def python_move_all_layers(img, drawable, type, x, y):
    img.undo_group_start()
    def_active_layer = pdb.gimp_image_get_active_layer(img)

    layers = img.layers
    for layer in layers:
        if type == 1:
            offset_x = x
            offset_y = y
        elif type == 0:
            offset_x, offset_y = pdb.gimp_drawable_offsets(layer)
            offset_x = offset_x + x
            offset_y = offset_y + y
        pdb.gimp_layer_set_offsets(layer, offset_x, offset_y)

    pdb.gimp_image_set_active_layer(img, def_active_layer)
    gimp.displays_flush()

    img.undo_group_end()
    
register(
  "python-fu-move-all-layers",
  "すべてのレイヤーを移動します。。",
  "相対位置を指定した場合、各レイヤーの現在位置から指定したピクセル分移動します。絶対位置を指定した場合、キャンパスを基準に指定した座標にすべてのレイヤーが移動します。",
  "t87rtp",
  "t87rtp",
  "2012.1.5",
  "<Image>/Python-fu/Layer/すべてのレイヤーを移動",
  "*",
  [
   (PF_RADIO, "tgt" , "座標の指定方法", 1, (("絶対位置", 1), ("相対位置", 0))),
   (PF_SPINNER, "x", "移動量(x)", 0, (-9999, 9999, 1)),
   (PF_SPINNER, "y", "移動量(y)", 0, (-9999, 9999, 1))
   ],
  [],
  python_move_all_layers)

main()
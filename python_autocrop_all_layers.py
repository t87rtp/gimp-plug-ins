#!/usr/bin/env python
# -*- coding:utf-8 -*-

from gimpfu import *

def python_autocrop_all_layers(img, drawable):
    img.undo_group_start()
    def_active_layer = pdb.gimp_image_get_active_layer(img)

    layers = img.layers
    for layer in layers:
        pdb.gimp_image_set_active_layer(img, layer)
        pdb.plug_in_autocrop_layer(img, layer)
        
    pdb.gimp_image_set_active_layer(img, def_active_layer)
    gimp.displays_flush()

    img.undo_group_end()

register(
  "python-fu-autocrop-all-layers",
  "すべてのレイヤーを自動切り抜きします。",
  "すべてのレイヤーを最小サイズで切り抜きます。",
  "t87rtp",
  "t87rtp",
  "date",
  "<Image>/Python-fu/Layer/すべてのレイヤーを自動切り抜き",
  "RGB*",
  [],
  [],
  python_autocrop_all_layers)

main()
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from gimpfu import *

def python_reversing_the_order_of_layers(img, drawable):
    img.undo_group_start()
    def_active_layer = pdb.gimp_image_get_active_layer(img)

    layers = img.layers
    for layer in layers:
        pdb.gimp_image_raise_layer_to_top(img, layer)
        
    pdb.gimp_image_set_active_layer(img, def_active_layer)
    gimp.displays_flush()

    img.undo_group_end()

register(
  "python-fu-reversing-the-order-of-layers",
  "summary",
  "description",
  "t87rtp",
  "t87rtp",
  "date",
  "<Image>/Python-fu/Layer/レイヤーの順序を反転",
  "*",
  [],
  [],
  python_reversing_the_order_of_layers)

main()
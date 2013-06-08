#!/usr/bin/env python
# -*- coding:utf-8 -*-

from gimpfu import *

def python_resize_all_layers_to_image_size(img, drawable):
    img.undo_group_start()

    layers = img.layers
    for layer in layers:
        pdb.gimp_layer_resize_to_image_size(layer)
    gimp.displays_flush()

    img.undo_group_end()

register(
  "python-fu-resize-all-layers-to-image-size",
  "すべてのレイヤーをキャンパスに合わせます。",
  "すべてのレイヤーのサイズをキャンパスサイズに合わせます。",
  "t87rtp",
  "t87rtp",
  "date",
  "<Image>/Python-fu/Layer/すべてのレイヤーをキャンパスに合わせる",
  "RGB*",
  [],
  [],
  python_resize_all_layers_to_image_size)

main()
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from gimpfu import *

def python_rename_all_layers_to_serial(img, drawable, n, d):
    img.undo_group_start()
    def_active_layer = pdb.gimp_image_get_active_layer(img)
    
    number = int(n)

    layers = img.layers
    for layer in layers:
        pdb.gimp_drawable_set_name(layer, str(number).rjust(d,"0"))
        number = number + 1
        
    pdb.gimp_image_set_active_layer(img, def_active_layer)
    gimp.displays_flush()

    img.undo_group_end()

register(
  "python-fu-rename-all-layers-to-serial",
  "summary",
  "description",
  "t87rtp",
  "t87rtp",
  "date",
  "<Image>/Python-fu/Layer/すべてのレイヤーを連番にリネーム",
  "RGB*",
  [
   (PF_SPINNER, "n", "開始番号", 1, (0, 100, 1)),
   (PF_SPINNER, "d", "桁数", 1, (1, 100, 1))
   ],
  [],
  python_rename_all_layers_to_serial)

main()
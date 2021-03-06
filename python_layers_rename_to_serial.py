#!/usr/bin/env python
# -*- coding:utf-8 -*-

from gimpfu import *

def python_layers_rename_to_serial(img, drawable, n, d):
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
  "python-fu-layers-rename-to-serial",
  "すべてのレイヤー名を連番にリネームします。",
  "すべてのレイヤーを指定開始番号から始まる指定桁数の連番にリネームします。",
  "t87rtp",
  "t87rtp",
  "date",
  "<Image>/Python-fu/Layer/すべてのレイヤーを連番にリネーム",
  "*",
  [
   (PF_SPINNER, "n", "開始番号", 1, (0, 100, 1)),
   (PF_SPINNER, "d", "桁数", 1, (1, 100, 1))
   ],
  [],
  python_layers_rename_to_serial)

main()
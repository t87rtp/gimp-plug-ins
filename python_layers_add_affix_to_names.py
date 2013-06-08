#!/usr/bin/env python
# -*- coding:utf-8 -*-

from gimpfu import *

def python_layers_add_affix_to_names(img, drawable, prefix, suffix):
    img.undo_group_start()
    def_active_layer = pdb.gimp_image_get_active_layer(img)
    
    layers = img.layers
    for layer in layers:
        pdb.gimp_drawable_set_name(layer, prefix + pdb.gimp_drawable_get_name(layer) + suffix)
        
    pdb.gimp_image_set_active_layer(img, def_active_layer)
    gimp.displays_flush()

    img.undo_group_end()

register(
  "python-fu-layers-add-affix-to-names",
  "すべてのレイヤーの名前の前後に文字列を追加します。",
  "すべてのレイヤーの名前の前後に文字列を追加します。",
  "t87rtp",
  "t87rtp",
  "2013.06.08",
  "<Image>/Python-fu/Layer/すべてのレイヤーの名前の前後に文字列を追加",
  "*",
  [
   (PF_STRING, "prefix", "接頭辞", ""),
   (PF_STRING, "suffix", "接尾辞", "")
   ],
  [],
  python_layers_add_affix_to_names)

main()
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from gimpfu import *

def python_scale_all_layers(img, drawable, w, h, keep):
    img.undo_group_start()
    def_active_layer = pdb.gimp_image_get_active_layer(img)

    layers = img.layers
    for layer in layers:
        pdb.gimp_image_set_active_layer(img, layer)
        if keep:
            original_rate = layer.height / layer.width
            target_rate = h / w
            if original_rate > target_rate:
                pdb.gimp_layer_scale_full(layer, w, h, True, 3)
            elif original_rate < target_rate:
                pdb.gimp_layer_scale_full(layer, w, h, True, 3)
            else:
                pdb.gimp_layer_scale_full(layer, w, h, True, 3)
        else:
            pdb.gimp_layer_scale_full(layer, w, h, True, 3)
        
    pdb.gimp_image_set_active_layer(img, def_active_layer)
    gimp.displays_flush()

    img.undo_group_end()

register(
  "python-fu-scale-all-layers",
  "summary",
  "description",
  "t87rtp",
  "t87rtp",
  "date",
  "<Image>/Python-fu/Layer/すべてのレイヤーをリサイズ",
  "RGB*",
  [
   (PF_SPINNER, "w", "幅", 0, (-9999, 9999, 1)),
   (PF_SPINNER, "h", "高さ", 0, (-9999, 9999, 1)),
   (PF_TOGGLE, "keep", "アスペクト比を保持", True)
   ],
  [],
  python_scale_all_layers)

main()
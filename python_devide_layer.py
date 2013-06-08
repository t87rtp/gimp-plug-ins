#!/usr/bin/env python
# -*- coding:utf-8 -*-

from gimpfu import *

def python_devide_layer(img, drawable, h, v):
    img.undo_group_start()
    
    def_active_layer = pdb.gimp_image_get_active_layer(img)
    
    width = pdb.gimp_image_width(img)
    height = pdb.gimp_image_height(img)
    
    width_d = width / h
    height_d = height / v
    
    a = 0
    b = 0
    while b < v:
        while a < h:
            copy_layer = def_active_layer.copy()
            img.add_layer(copy_layer, -1)
            pdb.gimp_layer_resize(copy_layer, width_d, height_d, width_d * a * -1, height_d * b * -1)
            pdb.gimp_drawable_set_name(copy_layer, pdb.gimp_drawable_get_name(def_active_layer) + "_" + str(a + 1) + "-" + str(b + 1))
            a = a + 1
        a = 0
        b = b + 1
    
    gimp.displays_flush()
    img.undo_group_end()

register(
  "python-fu-devide-layer",
  "アクティブなレイヤーを分割します。",
  "アクティブなレイヤーを指定した水平方向・垂直方向に等分割します。",
  "t87rtp",
  "t87rtp",
  "date",
  "<Image>/Python-fu/Layer/レイヤーをタイル状に分割",
  "*",
  [
   (PF_SPINNER, "h", "水平分割数", 1, (1, 100, 1)),
   (PF_SPINNER, "v", "垂直分割数", 1, (1, 100, 1))
   ],
  [],
  python_devide_layer)

main()
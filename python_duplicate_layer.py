#!/usr/bin/env python
# -*- coding:utf-8 -*-

from gimpfu import *

def python_duplicate_layer(img, drawable):
    copy_layer = drawable.copy()
    img.add_layer(copy_layer, -1)
    gimp.displays_flush()

register(
  "python-fu-duplicate-layer",
  "summary",
  "description",
  "t87rtp",
  "t87rtp",
  "date",
  "<Image>/Python-fu/Layer/レイヤーを複製",
  "*",
  [],
  [],
  python_duplicate_layer)

main()
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from gimpfu import *

def python_save_layers_to_each_files(img, drawable, root_dir, format, fit, visible_only):
    layers = img.layers
    img.undo_group_start()

    def save_drawable(drawable):
        if format == 0:
            file_path = root_dir + "\\" + drawable.name + ".jpg"
            pdb.file_jpeg_save(img, drawable, file_path, file_path, 0.85, 0, 1, 0, "", 3, 1, 0, 2)
        elif format == 1:
            file_path = root_dir + "\\" + drawable.name + ".png"
            pdb.file_png_save(img, drawable, file_path, file_path, 0, 9, 0, 0, 0, 0, 0)
        elif format == 2:
            file_path = root_dir + "\\" + drawable.name + ".gif"
            if img.base_type is not INDEXED:
                pdb.gimp_image_convert_indexed(img, 0, 0, 256, False, True, "")
            pdb.file_gif_save(img, drawable, file_path, file_path, 0, 0, 0, 0)
        elif format == 3:
            file_path = root_dir + "\\" + drawable.name + ".bmp"
            pdb.file_bmp_save(img, drawable, file_path, file_path)
    
    def each_layers():
        for layer in layers:
            if fit is False:
                offset_x, offset_y = pdb.gimp_drawable_offsets(layer)
                layer_width, layer_height = layer.width, layer.height
                pdb.gimp_layer_resize_to_image_size(layer)
            
            if visible_only:
                if pdb.gimp_drawable_get_visible(layer):
                    save_drawable(layer)
            else:
                save_drawable(layer)

            if fit is False:
                pdb.gimp_layer_resize(layer, layer_width, layer_height, offset_x * -1, offset_y * -1)
    
    each_layers()
    img.undo_group_end()
    
register(
  "save-layers-to-each-files",
  "画像のすべてのレイヤーを指定された形式でそれぞれ保存します。",
  "画像のすべてのレイヤーを指定された形式でそれぞれ保存します。",
  "t87rtp",
  "t87rtp",
  "2012.1.5",
  "<Image>/Python-fu/File/すべてのレイヤーを個別の画像として保存",
  "*",
  [
   (PF_DIRNAME, "root_dir", "出力先ディレクトリ", ""),
   (PF_OPTION, "format"  ,"出力ファイル形式", 1 ,[".jpg", ".png", ".gif",".bmp"]),
   (PF_TOGGLE, "fit", "レイヤーのサイズを保持", False),
   (PF_TOGGLE, "visible_only", "可視レイヤーのみ", False)
   ],
  [],
  python_save_layers_to_each_files)

main()
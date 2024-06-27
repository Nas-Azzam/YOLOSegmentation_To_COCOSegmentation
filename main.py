import json
from check import creates_categories, creation_json_yolo_to_coco

images_directory = "/media/user/10EE456DEE454BE2/folder/data/train/images"
annotation_directory = "/media/user/10EE456DEE454BE2/folder/data/train/labels"



categorie = ["category1","category2","category3"....]
creation_json_yolo_to_coco(images_directory,annotation_directory, categories=categorie,anno_file_name="train")




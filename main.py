import json
from check import creates_categories, creation_json_yolo_to_coco

images_directory = "/media/contil/10EE456DEE454BE2/Nas/WilDSAM/data/train/images"
annotation_directory = "/media/contil/10EE456DEE454BE2/Nas/WilDSAM/data/train/labels"



categorie = ["Giraffe","Hippo","Wildbeast","warthog","Lion","hyena","Hartebeest","Baboon","buffalo","Elephant","Gazella","Impala","zebra"]
creation_json_yolo_to_coco(images_directory,annotation_directory, categories=categorie,anno_file_name="train")




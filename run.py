from detectron2.structures import BoxMode
import os
import cv2

def get_data(img_dir):
    dataset_dicts = []
    list_cat = []	
    for dir in os.listdir(img_dir):
        list_cat.append(dir)
	for file in os.path.join(img_dir, dir)
            record = {}
            height, width = cv2.imread(filename).shape[:2]     
            record["file_name"] = filename
            record["image_id"] = idx
            record["height"] = height
            record["width"] = width
            record["annotations"] = {
                "bbox": [np.min(px), np.min(py), np.max(px), np.max(py)],
                "bbox_mode": BoxMode.XYXY_ABS,
                "segmentation": [poly],
                "category_id": 0,
            }
    for name in list_cat:
        print(name)	

    dataset_dicts = []
"""
    for idx, v in enumerate(imgs_anns.values()):
        record = {}
        
        filename = os.path.join(img_dir, v["filename"])
        height, width = cv2.imread(filename).shape[:2]
        
        record["file_name"] = filename
        record["image_id"] = idx
        record["height"] = height
        record["width"] = width
      
        annos = v["regions"]
        objs = []
        for _, anno in annos.items():
            assert not anno["region_attributes"]
            anno = anno["shape_attributes"]
            px = anno["all_points_x"]
            py = anno["all_points_y"]
            poly = [(x + 0.5, y + 0.5) for x, y in zip(px, py)]
            poly = [p for x in poly for p in x]
            obj = {
                "bbox": [np.min(px), np.min(py), np.max(px), np.max(py)],
                "bbox_mode": BoxMode.XYXY_ABS,
                "segmentation": [poly],
                "category_id": 0,
            }
            objs.append(obj)
        record["annotations"] = objs
        dataset_dicts.append(record)
    return dataset_dicts
"""
dataset_dicts = get_data("Data")
print(dataset_dicts)

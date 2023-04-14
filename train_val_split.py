import os
import shutil
from sklearn.model_selection import train_test_split

data_dir = 'Data'
train_dir = os.path.join(data_dir, 'train')
val_dir = os.path.join(data_dir, 'val')

if not os.path.exists(train_dir):
    os.makedirs(train_dir)

if not os.path.exists(val_dir):
    os.makedirs(val_dir)

for class_name in os.listdir(data_dir):
    class_dir = os.path.join(data_dir, class_name)
    if os.path.isdir(class_dir):
        train_class_dir = os.path.join(train_dir, class_name)
        val_class_dir = os.path.join(val_dir, class_name)
        if not os.path.exists(train_class_dir):
            os.makedirs(train_class_dir)
        if not os.path.exists(val_class_dir):
            os.makedirs(val_class_dir)
        
        image_paths = [os.path.join(class_dir, f) for f in os.listdir(class_dir) if f.endswith('.png')]
        train_paths, val_paths = train_test_split(image_paths, test_size=0.2)
        
        for path in train_paths:
            filename = os.path.basename(path)
            dst = os.path.join(train_class_dir, filename)
            shutil.copyfile(path, dst)
        
        for path in val_paths:
            filename = os.path.basename(path)
            dst = os.path.join(val_class_dir, filename)
            shutil.copyfile(path, dst)

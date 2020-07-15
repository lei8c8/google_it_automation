#!/usr/bin/env python3

import os
import glob
from PIL import Image
for filename in glob.glob('*'):
    im = Image.open(filename)
    target_abs_path = os.path.join('/opt/icons', filename)
    new_image = im.rotate(270).resize((128,128)).convert('RGB')
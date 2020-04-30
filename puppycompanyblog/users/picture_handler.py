from PIL import Image
import os
from flask import url_for, current_app

### function to add a picture ###
def add_profile_image(pic_upload, username):

    filename = pic_upload.filename
    ext_type = filename.split('.')[-1]
    storage_filename = str(username)+'.'+ext_type

    filepath = os.path.join(current_app.root_path,'static/profile_pics',storage_filename)

    output_size = (200, 200)
    pic = Image.open(pic_upload)
    pic.thumbnail(output_size)
    pic.save(filepath)

    return storage_filename

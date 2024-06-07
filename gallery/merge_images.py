#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from PIL import Image

def merge_images(image1_path, image2_path):
    # 이미지 파일 열기
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)

    # 이미지 크기 맞추기
    image1 = image1.resize(image2.size)

    # 이미지 합성
    blended_image = Image.blend(image1, image2, alpha=0.5)

    return blended_image


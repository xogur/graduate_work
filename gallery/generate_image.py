#!/usr/bin/env python
# coding: utf-8


# In[3]:

from PIL import Image

def generate_image(input_image_path, output_image_path):
    # 이미지 열기
    image = Image.open(input_image_path)
    
    # 이미지를 90도 회전
    generate_image = image.rotate(90, expand=True)
    
    # 이미지를 RGB 모드로 변환
    generate_image = generate_image.convert('RGB')
    
    # 회전된 이미지를 jpg 형식으로 저장
    generate_image.save(output_image_path, format='JPEG')

    return output_image_path
# 입력 이미지 파일 경로와 출력 이미지 파일 경로 설정


# 함수 호출하여 이미지 회전 및 저장


# In[ ]:





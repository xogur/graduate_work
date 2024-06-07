from PIL import Image
import time  # 딜레이를 추가하기 위해 time 모듈을 가져옵니다.
from gallery.merge_images import merge_images

def merge_images(image1_path, image2_path):
    # 이미지 파일 열기
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)

    # 이미지 크기 맞추기
    image1 = image1.resize(image2.size)

    # 이미지 합성
    blended_image = Image.blend(image1, image2, alpha=0.5)

    return blended_image

def merge_and_save_images(image1_path, image2_path):
    # 30초 딜레이 추가
    time.sleep(5)
    
    # 이미지 합성
    merged_image = merge_images(image1_path, image2_path)
    merged_image = merged_image.convert('RGB')

    # 합성된 이미지 저장
    output_image_path = "images2/generate_image.jpg"
    merged_image.save(output_image_path)

    return output_image_path

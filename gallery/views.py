import os
from django.shortcuts import render, redirect
from .forms import MultipleImageForm
from .models import Image
from .generate_image import generate_image  # generate_image.py에서 필요한 함수 import
from .save_merged_image import merge_and_save_images
from .merge_images import merge_images

def save_image_paths_to_txt(image_names, filename):
    with open(filename, 'w') as file:
        for name in image_names:
            file.write(f"{name}\n")

def upload_image(request):
    if request.method == 'POST':
        form = MultipleImageForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            
            # 업로드된 이미지의 원본 이름을 유지
            instance.image.name = request.FILES['image'].name
            instance.image2.name = request.FILES['image2'].name
            
            instance.save()

            # 업로드된 이미지 가져오기
            uploaded_images = Image.objects.order_by('-uploaded_at')[:1] 
            image_names = []
            # 이미지에 대해 generate_image 함수를 호출하여 처리
            for uploaded_image in uploaded_images:
                if uploaded_image.image and uploaded_image.image2:
                    model_image_name = os.path.basename(uploaded_image.image.name)
                    cloth_image_name = os.path.basename(uploaded_image.image2.name)
                    image_names.append(f"{model_image_name} {cloth_image_name}")
            
                    uploaded_image.save()
            save_image_paths_to_txt(image_names, 'C:/Users/X/김민수/졸업작품/VITON-HD-main/VITON-HD/datasets/test_pairs_simple.txt')
        
            return render(request, 'gallery/processing_page.html')
    else:
        form = MultipleImageForm()
    return render(request, 'gallery/upload_image.html', {'form': form})

def show_images(request):
    images = Image.objects.order_by('-uploaded_at')[:1]
    context = {'images': images}
    return render(request, 'gallery/show_images.html', context)

import subprocess
from django.shortcuts import render, redirect
from .models import Image
from .forms import MultipleImageForm
import sys

def processing_page(request):
    uploaded_images = Image.objects.order_by('-uploaded_at')[:1]
    for uploaded_image in uploaded_images:
        if uploaded_image.image and uploaded_image.image2:
            model_image_path = uploaded_image.image.path
            cloth_image_path = uploaded_image.image2.path
            # 가상 환경의 Python 인터프리터 경로
            python_path = sys.executable

            # test.py 파일을 호출하여 처리
            result = subprocess.run(
                [python_path, '../VITON-HD-main/VITON-HD/test.py', '--name', 'test4', '--dataset_list', 'test_pairs_simple.txt'],
                text=True, 
                capture_output=True
    
            )
            print(result.stdout)
            print(result.stderr)
            
            # 여기서 generate_image.jpg 파일을 저장소에 저장한 후 URL을 생성
            image_url = 'C:/Users/X/김민수/졸업작품/image_gallery_project/results/test4/generate_image.jpg'
            uploaded_image.image_url = image_url
            uploaded_image.save()
    
    return redirect('gallery:show_images')

이 프로젝트는 생성형 인공지능(Generative AI) 기술을 활용하여, 사용자의 전신 이미지에 의류 아이템을 자연스럽게 합성하는 패션 시착(Virtual Try-On) 시스템을 구현하는 것을 목표로 한다.
기존의 제한된 온라인 피팅 시스템을 넘어서, 다양한 자세, 배경, 옷 종류에 적응할 수 있는 유연하고 정교한 시착 시스템을 구축한다.

Python, PyTorch

OpenPose: 인체의 관절 위치 추정 (Pose Estimation)

U-Net: 이미지 분할 및 특징 추출

GMM (Geometric Matching Module): 의류와 사람의 자세를 정렬하여 자연스러운 시각적 매칭 구현

IDM-VTON 구조 기반: 딥러닝 기반의 고해상도 의상 합성

Django: 웹 서비스 구현


본 시스템의 동작 과정은 다음 과정을 따른다.

입력 단계(Input Stage) 
- 모델 이미지와 입혀질 의상의 이미지를 입력으로 한다.

전처리 단계(Preprocessing)

- 포즈 추정(Pose Estimation)  : OpenPose를 이용한 신체 자세를 추출한다. 이를 이용하여 착용자의 자세를 Keypoint 데이터(관절 좌표)로 변환하여 옷을 사용자의 자세에 맞게 변형시키는 데 활용 및 가려진 신체 부위를 예측하는데 이용된다. ex) 긴팔 티셔츠 -> 반팔 티셔츠 경우 팔 예측

- 의미적 분할(Semantic Segmentation) : 딥러닝 기반 세그멘테이션 모델로 사용자 이미지를 신체 부위(얼굴, 팔, 다리 등)와 배경, 기존 의상으로 나눈 세그멘테이션 맵을 생성해 가려진 신체 부위를 복원하거나 필요한 영역만 추출한다.

특징 추출 단계(Feature Extraction) 
- 의상의 패턴, 색상, 질감을 CNN 기반 네트워크로 추출하고 세그멘테이션의 픽셀 레벨 정보를 추출해 특징 데이터를 GMM모듈로 전달해 적합한 의상 변형을 수행하도록 해준다.

의상 변형 단계(Clothing Warping)
- GMM모듈로 추출된 의상 특징과 Pose 데이터를 사용해 의상을 사용자의 자세에 맞게 변형된 의상을 Output한다.
결과: 변형된 의상(Warped Clothing).


신체 복원 단계(Body Reconstruction)
- U-Net 기반 네트워크로 가려진 신체 부위를 Pose데이터와 Segmentation데이터를 이용하여 복원하면서 신체의 전체적인 모습을 생성한다.

이미지 합성 단계(Image Composition)
- GMM의 Outpu인 변형된 의상과 복원된 신체 이미지를 결합한다. 그 결과로 가상 시착 결과 이미지를 생성한다.






VITON-HD : https://github.com/shadow2496/VITON-HD


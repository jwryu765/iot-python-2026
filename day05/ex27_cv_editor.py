# ex27_cv_editor.py
# OpenCV 사용 이미지 편집기

import cv2
import numpy as np
import time    # 저장시 시분초를 이미지 이름에 사용

# 이미지 실시간 읽기
from tkinter import Tk, filedialog   # Tkinter 파이썬 기본 GUI 라이브러리

# 5. 편집 이미지 저장
edited_img = None   # 전역변수

# 1. 이미지 로드
img = cv2.imread(filename='./day05/cat01.jpg')
if img is None:
    raise FileNotFoundError('이미지 로딩 실패!')

origin = img.copy()  # 원본이미지 복사
winname = 'Editor'

# 6. 이미지 열기함수
def load_image():
    global origin
    
    root = Tk()
    root.withdraw()   # GUI 창 숨기기

    filepath = filedialog.askopenfilename(
                    title='이미지 열기',
                    filetypes=[('Image files', '*.jpg *.png *.jpeg *.bmp')])
    if filepath:
        img = cv2.imread(filepath)
        if img is None:
            print('이미지 로딩 실패')
            return
        
        origin = img.copy()
        print('이미지 로드 완료')
        update()

# 4. 이미지 변경함수
def update(_=None):
    # 함수 내에서는 전역변수 사용시 global 사용
    # 함수 스코프가 
    global edited_img  # 전역변수를 사용하겠다는 키워드

    alpha = cv2.getTrackbarPos('Contrast', winname) / 50    #이미지 대비
    beta = cv2.getTrackbarPos('Brightness', winname) - 100   # 이미지 밝기
    blur = cv2.getTrackbarPos('Blur', winname)  # 트랙바 이름 Blur에서 데이터 가져오기
    edge = cv2.getTrackbarPos('Edge', winname=winname) # 엣지
    rotate = cv2.getTrackbarPos('Rotate', winname) - 180 # 트랙바 회전 값 가져오기
    threshold = cv2.getTrackbarPos('Threshold', winname)   # 이진화값 가져오기

    # 대비/밝기 조걸
    edited = cv2.convertScaleAbs(origin, alpha=alpha, beta=beta)

    # 블러
    if blur > 0:
        k = blur * 2 + 1  # 홀수 커널
        edited = cv2.GaussianBlur(edited, (k, k), 0)

    # 엣지
    if edge > 0:
        edited = cv2.Canny(edited, edge, edge*2)
        edited = cv2.cvtColor(edited, cv2.COLOR_GRAY2BGR)

    # 이진화
    if threshold > 0:
        gray = cv2.cvtColor(edited, cv2.COLOR_BGR2GRAY) # 그레이스케일
        _, edited = cv2.threshold(gray, threshold, 200, cv2.THRESH_BINARY)
        edited = cv2.cvtColor(edited, cv2.COLOR_GRAY2BGR)

    # 회전
    h, w = edited.shape[:2]
    center = (w // 2, h // 2)  # 이미지 중앙 설정
    M = cv2.getRotationMatrix2D(center, rotate, 1.0)
    edited = cv2.warpAffine(edited, M, (w, h))

    edited_img = edited     # 편집완료된 이미지를 전역변수에 할당
    cv2.imshow('Editor', edited)

# 3. 트랙바 윈도우 생성     
cv2.namedWindow(winname)
cv2.createTrackbar('Contrast', winname, 50, 150, update)  # 이미지 대비 변경
cv2.createTrackbar('Brightness', winname, 100, 200, update)  # 이미지 밝기 변경
cv2.createTrackbar('Blur', winname, 0, 10, update)  # 이미지 블러 변경
cv2.createTrackbar('Edge', winname, 0, 200, update)  # 이미지 엣지 변경
cv2.createTrackbar('Rotate', winname, 180, 360, update)  # 이미지 회전

cv2.createTrackbar('Threshold', winname, 0, 200, update)  # 이미지 이진화 

update()

# 2. 기본동작 처리
while True:
    key = cv2.waitKey(1) & 0xff
    if key == ord('r'):
        cv2.imshow('ImageEditor', origin)
        pass
    elif key == ord('o'):   # 이미지 로드
        load_image()

    elif key == ord('s'):   # 이미지 저장
        if edited_img is None:
            print('저장이미지 없음')
        else:
            filename = f'saved_{time.time()}.jpg'
            cv2.imwrite(f'./day05/{filename}', edited_img)
            print('이미지 저장완료')

    elif key == ord('q'): # 프로그램 종료
        break

    else:
        cv2.imshow('Simple ImageEditor', origin)

cv2.destroyAllWindows()
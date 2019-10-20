# 特征点位置获取以及标定特征点
import numpy as np
import cv2
import dlib

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('./shape_predictor_68_face_landmarks.dat')


# cv2 读取图像
img = cv2.imread('./tim.jpeg')
# 取灰度
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
# 人脸数
rects = detector(img_gray, 0)
print(len(rects)) # 打印人脸个数

for i in range(len(rects)):
    landmarks = np.matrix([[p.x, p.y] for p in predictor(img, rects[i]).parts()])
    for idx, point in enumerate(landmarks):
        # 68点的坐标
        pos = (point[0, 0], point[0, 1])
        print(idx+1, pos)
        
        # 利用cv2.circlr给每个特征点画一个圆，共68个
        cv2.circle(img, pos, 2, color=(0, 255, 0))
#利用cv2.putText在每个特征点上输出1-68
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(idx+1), pos, font, 0.8, (0, 0, 255), 1, cv2.LINE_AA)
# 保存标定特征点后的图
cv2.imshow("img", img)
cv2.imwrite('test.jpg',img,[int(cv2.IMWRITE_JPEG_QUALITY),70])

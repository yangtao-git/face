import numpy as np
import matplotlib.pyplot as plt
import cv2

# 读取图片
image = cv2.imread(r'./datas/image (21).jpg')
# BGR -> RGB
# image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# 灰度图
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# 二值化
ret,binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
# 查找轮廓
contours, hierarchy = cv2.findContours(binary,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
'''
center, radius = cv2.minEnclosingCircle( cnt )
参数：
    cnt 是轮廓。
返回值：
    center 是最小包围圆形的中心。
    radius 是最小包围圆形的半径。
'''
for cnt in contours:
    (x,y),radius = cv2.minEnclosingCircle(cnt)
    if 3.14*radius < 1000: # 过滤掉面积小于1000的圆
        continue
    center = (int(x),int(y))
    radius = int(radius)
    cv2.circle(image,center,radius,(255,0,0),10)
gray = cv2.cvtColor(gray,cv2.COLOR_GRAY2BGR)
binary = cv2.cvtColor(binary,cv2.COLOR_GRAY2BGR)
print("shape image : ",image.shape)
print("shape gray : ",gray.shape)
print("shape binary : ",binary.shape)

result = cv2.hconcat([image, gray, binary])
result = cv2.resize(result, (0,0), fx=0.2, fy=0.2)
cv2.imshow("result",result)
cv2.waitKey(0)
cv2.destroyAllWindows()

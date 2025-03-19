import cv2 as cv

img = cv.imread('tiger.jpg')
#img_grid = [[0] * 3] * 3
img_grid=[]
print(img_grid)
(h, w) = img.shape[:2]
th, tw = h // 3, w // 3
for i in range(3):
    for j in range(3):
        #img_grid[i][j] = img[th * i: th * (i + 1), tw * j: tw * (j + 1)]
        img_grid.append(img[th * i: th * (i + 1), tw * j: tw * (j + 1)])
        # cv.imshow(f'{(i, j)}', img_grid[i][j])
        cv.imshow(f'{(i, j)}', img_grid[-1])
        print(f'{(i, j)}')

cv.imshow('1,1', img_grid[4])

cv.waitKey(0)

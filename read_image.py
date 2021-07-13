import cv2
from PIL import Image
import matplotlib.pyplot as plt
import pytesseract
import os
from wand.image import Image
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

def mark_region(image_path):
    
    im = cv2.imread(image_path)
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (9,9), 0)
    thresh = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,11,30)

    # Dilate to combine adjacent text contours
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9,9))
    dilate = cv2.dilate(thresh, kernel, iterations=10)

    # Find contours, highlight text areas, and extract ROIs
    cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    line_items_coordinates = []
    for c in cnts:
        area = cv2.contourArea(c)
        x,y,w,h = cv2.boundingRect(c)

        if y >= 100 and x <= 1000:
            if area > 10000:
                image = cv2.rectangle(im, (x,y), (2550, y+h), color=(255,0,255), thickness=2)
                line_items_coordinates.append([(x,y), (2550, y+h)])

        if y >= 2400 and x <= 2000:
            image = cv2.rectangle(im, (x,y), (2200, y+h), color=(255,0,255), thickness=2)
            line_items_coordinates.append([(x,y), (2200, y+h)])


    return image, line_items_coordinates

if __name__ == "__main__":
    FILENAME = "/home/milind/Python/Documents/Capital_Gain_Stmt_PY_IP121098392 (002)_NOPASS.pdf-1.png"
    print(FILENAME)
    image, line_items_coordinates = mark_region(FILENAME)
    plt.figure(figsize=(20,20))
    plt.imshow(image)
    plt.savefig("image-with-regions.png")
    # print(line_items_coordinates)

    image = cv2.imread(FILENAME)
    c = line_items_coordinates

    # img = image[c[0][1]:c[1][1], c[0][0]:c[1][0]]   
        # convert_pdf_to_images('example-multipage.pdf')
    # plt.figure(figsize=(20,20))
    # plt.imshow(image[c[0][1]:c[1][1]])
    # plt.savefig("image-with-regions_1.png")
    save_file = True
    i = 0
    for index in c:
        img = image[index[0][1]:index[1][1],index[0][0]:index[1][0]]
        image_name = '/home/milind/Python/Documents/output/Page2/result_image' + '_Part_' + str(i + 1) + '.png'
        plt.figure(figsize=(20,20))
        plt.imshow(img)
        if(save_file==True):
            plt.savefig(image_name)
        ret,thresh1 = cv2.threshold(img,120,255,cv2.THRESH_BINARY)
        text = str(pytesseract.image_to_string(thresh1, config='--psm 6'))
        print('_________________' + 'Start result_image' + '_Part_' + str(i + 1)  + '______________________')
        print(text)
        print('_________________' + 'END   result_image' + '_Part_' + str(i + 1)  + '______________________')
        i = i + 1

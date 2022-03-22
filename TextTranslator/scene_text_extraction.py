import cv2
import pytesseract
from image_preprocess import cv2_imageprocessing as cvimg
from text_detection import east_text_detector as east
from tesseract_processing import tesseract_ocr as tesocr
# pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR'  # your path may be different
def extract_text_from_image(image_path,**kwargs):
    orig,copy = cvimg.load_image(image_path)
    # cv2.imshow('proceprocessed',copy)
    # cv2.imshow('original', orig)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # copy = cv2.merge((copy,copy,copy))
    resized,resized_width,resized_height = cvimg.resize_image(copy)
    text_coordinates = east.east_text_detector(resized,**kwargs)
    east.get_text_bounding_boxes_on_image(orig,text_coordinates, resized_width, resized_height, **kwargs)
    #rois = east.get_text_bounding_boxes_on_image(text_coordinates,resized_width,resized_height,**kwargs)
    # final_extracted_text = tesocr.extract_text_from_image(rois)
    # for text in final_extracted_text:
    #     print(text)
    # text = tesocr.core_tesseract_OCR(copy)
    # print(text)

def main():
    image_path = 'D:\\COLLEGE WORK\\SEM 5\\Mini Project Sem 5\\Resume Ranker\\Sem 5 mini project\\resume\\new.jpeg'
    kwargs = {"min_confidence": 0.5,
              "padding": 0.10}
    extract_text_from_image(image_path ,**kwargs)
if __name__ == '__main__':
    main()





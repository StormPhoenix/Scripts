import argparse
import cv2

def ImageSketch(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_gray = cv2.medianBlur(img_gray, 5)
    edges = cv2.Laplacian(img_gray, cv2.CV_8U, ksize=5)
    ret, threshold = cv2.threshold(edges, 145, 255, cv2.THRESH_BINARY_INV)
    return threshold

def ImageCartonize(img_path, output_path, gray_mode=False):
    cartoonized = None
    img = cv2.imread(img_path)
    threshold = ImageSketch(img)
    filtered = cv2.bilateralFilter(img, 10, 250, 250)
    cartoonized = cv2.bitwise_and(filtered, filtered, mask=threshold)

    if gray_mode:
        cartoonized = cv2.cvtColor(cartoonized, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(output_path, cartoonized)

def ImageStylization(img_path, output_path):
    img = cv2.imread(img_path)
    stylization = cv2.stylization(img, sigma_s=60, sigma_r=0.07) 

    cv2.imwrite(output_path, stylization)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some inputs.')
    parser.add_argument('--file', type=str, required=True)
    parser.add_argument('--output', type=str, required=True)
    args = parser.parse_args()

    ## ImageCartonize(args.file, args.output)
    ImageStylization(args.file, args.output)

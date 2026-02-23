import cv2
import os              # clean & correct filenames on every operating system. Without it, write filenames by hand

from gui_utilities import EdgeDetector


def main():
    file = "yellow.jpg"
    image = cv2.imread(file, 0)         # read the photo whose name is in the args box.

    if image is None:
        print("Cannot find the picture: ", file)
        return
    
    cv2.imshow('Input', image)

    edge_detector = EdgeDetector(image, filter_size=13, threshold1=28, threshold2=115)     # (image, start with three numbers on its sliders)

    print ("Edge parameters:")                          # After the slider window is closed (you pressed any key), write on the black screen:
    print (f"GaussianBlur Filter Size: {edge_detector.filterSize()}")        # then the three numbers you chose with the sliders
    print (f"Threshold1: {edge_detector.threshold1()}")              # what number is on the 1st threshold
    print (f"Threshold2: {edge_detector.threshold2()}")              # what number is on the 2nd?

    (head, tail) = os.path.split(file)             # Take the picture name (example: "pictures/cat.jpg"). Cut it in two pieces: head = "pictures" , tail = "cat.jpg"

    (root, ext) = os.path.splitext(tail)                  # Now, take only "cat.jpg" and split it.

    smoothed_filename = os.path.join("output_images", root + "-smoothed" + ext)         # Glue new names together
    edge_filename = os.path.join("output_images", root + "-edges" + ext)

    cv2.imwrite(smoothed_filename, edge_detector.smoothedImage())         # cv2.imwrite(label , photo )
    cv2.imwrite(edge_filename, edge_detector.edgeImage())

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
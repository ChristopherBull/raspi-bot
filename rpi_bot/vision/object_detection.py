"""Detects objects from a camera (image/video).

Requires: OpenCV (compiled from source for best performance)

Pre-trained models found here:
https://github.com/opencv/opencv/wiki/TensorFlow-Object-Detection-API
https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf1_detection_zoo.md
"""
import cv2
import os.path
import sys
from importlib import import_module
from timeit import default_timer as timer

# Add models to the PATH
# Allows this script to be run standalone or as part of the wiser project
if __name__ == "__main__":
    proj_root_path = os.path.dirname(os.path.abspath(__file__)) + "/../../"
    sys.path.append(proj_root_path)
else:
    proj_root_path = './'
vision_models = import_module('rpi_bot.vision.models')

# Labels for pre-trained models based on COCO
COCO_labels = {0: 'background',
               1: 'person', 2: 'bicycle', 3: 'car', 4: 'motorcycle',
               5: 'airplane', 6: 'bus', 7: 'train', 8: 'truck', 9: 'boat',
               10: 'traffic light', 11: 'fire hydrant', 13: 'stop sign',
               14: 'parking meter', 15: 'bench', 16: 'bird', 17: 'cat',
               18: 'dog', 19: 'horse', 20: 'sheep', 21: 'cow', 22: 'elephant',
               23: 'bear', 24: 'zebra', 25: 'giraffe', 27: 'backpack',
               28: 'umbrella', 31: 'handbag', 32: 'tie', 33: 'suitcase',
               34: 'frisbee', 35: 'skis', 36: 'snowboard', 37: 'sports ball',
               38: 'kite', 39: 'baseball bat', 40: 'baseball glove',
               41: 'skateboard', 42: 'surfboard', 43: 'tennis racket',
               44: 'bottle', 46: 'wine glass', 47: 'cup', 48: 'fork',
               49: 'knife', 50: 'spoon', 51: 'bowl', 52: 'banana', 53: 'apple',
               54: 'sandwich', 55: 'orange', 56: 'broccoli', 57: 'carrot',
               58: 'hot dog', 59: 'pizza', 60: 'doughnut', 61: 'cake',
               62: 'chair', 63: 'couch', 64: 'potted plant', 65: 'bed',
               67: 'dining table', 70: 'toilet', 72: 'tv', 73: 'laptop',
               74: 'mouse', 75: 'remote', 76: 'keyboard', 77: 'mobile phone',
               78: 'microwave', 79: 'oven', 80: 'toaster', 81: 'sink',
               82: 'refrigerator', 84: 'book', 85: 'clock', 86: 'vase',
               87: 'scissors', 88: 'teddy bear', 89: 'hair drier',
               90: 'toothbrush'}


def detect(image_path, save_image=False, display_image=False,
           benchmark=False,
           net_config=vision_models.default_object_detection_config):
    """Detect objects in a given image.

    Loads an image into a Neural Network for object detection.

    Args:
        image_path (str): The path to the image to perform detection on.
        save_image (bool, optional): Whether an annotated copy of the image
            should be saved. Saves to same location as image_path, with an
            updated filename. Defaults to False.
        display_image (bool, optional): Whether to display the results in a
            window. Defaults to False (e.g., for terminal execution).
        benchmark (bool, optional): Whether to record execution time. Times
            are output to terminal and embedded onto images (if save_image is
            enabled). Defaults to False.
        net_config (NeuralNetworkConfig, optional): Additional network
            configuration. This specifies which model to load and provides
            any model/network-specific configuration (such as how to normalise
            inputs). Defaults to models.default_object_detection_config.
    """
    if benchmark:
        print(net_config.model_dirname)
        start = timer()

    # Loading model
    model_dir = net_config.model_dirname
    model = '{}res/models/{}/frozen_inference_graph.pb'.format(
        proj_root_path, model_dir)
    config = '{}res/models/{}/config.pbtxt'.format(
        proj_root_path, model_dir)
    net = cv2.dnn_DetectionModel(model, config)

    # Configure network
    net.setInputSize(net_config.input_size_width, net_config.input_size_height)
    if net_config.input_scale is not None:
        net.setInputScale(net_config.input_scale)
    if net_config.input_mean is not None:
        net.setInputMean(net_config.input_mean)
    net.setInputSwapRB(net_config.input_swap_RB)

    # Input image into network
    image = cv2.imread(image_path)
    if benchmark:
        start_NN = timer()
    classes, confidences, boxes = net.detect(image, confThreshold=0.5)
    if benchmark:
        end_NN = timer()

    # Loop through each potentially detected object
    for class_id, confidence, box in zip(classes.flatten(),
                                         confidences.flatten(),
                                         boxes):
        class_name = COCO_labels[class_id]
        print("{0:>9} {1}".format(str(confidence), class_name))
        if display_image or save_image:
            cv2.rectangle(image, box, color=(0, 255, 0))
            start_y = box[1]
            # Determine if text will be too near top of image
            if start_y > 20:
                text_y = start_y - 10
            else:
                text_y = start_y + 10
            # Draw labels a top of bounding boxes
            cv2.putText(image, class_name,
                        (int(box[0]), int(text_y)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

    if benchmark:
        end = timer()
        time_nn = "{:.2f}s".format(end_NN - start_NN)
        print("Time:      {:.2f}s".format(end - start))
        print("Time (NN): %s\n" % time_nn)
        if display_image or save_image:
            cv2.putText(image, time_nn,
                        (int(5), int(image.shape[0] - 5)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 0), 2)

    # Share outputs
    if save_image:
        cv2.imwrite(append_filename(args.image), image)
    if display_image:
        cv2.imshow('image', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


def append_filename(filename, append_str=".annotated"):
    """Append a string to a filename before the file extension.

    Source: https://stackoverflow.com/a/37487898/508098

    Args:
        filename (str): The filename to update.
        append_str (str, optional): The string to append to the filename.
            Defaults to ".annotated".

    Returns:
        str: The updated filename.
    """
    return "{0}{2}{1}".format(*os.path.splitext(filename) + (append_str,))


if __name__ == "__main__":
    # Parse arguments
    import argparse  # Only import argparse if running as a singular script
    parser = argparse.ArgumentParser(
        description=('Detect objects in a given image or video using '
                     'MobileNet-SSD object detection'))
    parser.add_argument("--image",
                        default="image.jpg",
                        help="Image path to process")
    parser.add_argument("--save",
                        action='store_true',
                        help=("Save the annotated result (adds '.annotated' "
                              "to new file's name)"))
    parser.add_argument("--show",
                        action='store_true',
                        help="Show result in a window")
    parser.add_argument("--benchmark",
                        action='store_true',
                        help="Records time taken to process image")
    parser.add_argument("--benchmark-all-models",
                        action='store_true',
                        help=("Records time taken to process image for all "
                              "available models in the models folder"))
    args = parser.parse_args()

    # Perform object detection
    detect(args.image, args.save, args.show,
           args.benchmark or args.benchmark_all_models)

    if args.benchmark_all_models:
        # TODO dynamically load models by iterating over folder
        import models.ssdlite_mobilenet_v2_coco_2018_05_09.config as v2lite
        other_models = [
            v2lite
        ]
        for model in other_models:
            detect(args.image, args.save, args.show,
                   args.benchmark or args.benchmark_all_models,
                   model.config)

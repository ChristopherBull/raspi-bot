# RPi Bot - Vision

## Object Detection

The object detection code uses Neural Networks to identify objects in a given image or frame of a video.

The currently used model is [MobileNet V3](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf1_detection_zoo.md#mobile-models) (large), an [SSD model (Single Shot object Detection)](https://arxiv.org/abs/1512.02325) trained on the [COCO dataset](https://cocodataset.org/).

The [choice of model is configurable](../../models/) to allow easier integration of future or alternate models, which enables testing and benchmarking of multiple models to determine a best fit for your computational requirements in a resource-constrained environment.

### Testing / Benchmarking Object Detection

The object detection code can be run standalone for testing/benchmarking purposes. Simply call the script directly:

```shell
python3 object_detection.py
```

The script uses reasonable defaults, but configurable parameters are available. Check the help documentation:

```shell
python3 object_detection.py -h
```

A typical command during a non-desktop session (e.g., SSH) would be:

```shell
python3 object_detection.py --image image.jpg --benchmark
```

A typical command during a desktop session would be:

```shell
python3 object_detection.py --image image.jpg --save --show --benchmark
```

If you `--save` or `--show` images, the bounding boxes and labels are baked onto the images. If you also pass `--benchmark`, the neural network inference time is baked onto the image.

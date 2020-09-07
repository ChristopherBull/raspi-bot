# Models

This directory contains the configuration for ML/AI models.

## Object Detection TensorFlow Models

When adding an object detection model, ensure you have the following files:

- `rpi_bot/vision/models/<model_name>/__init__.py`
- `rpi_bot/vision/models/<model_name>/config.py`
- `res/models/<model_name>/config.pbtxt`
- `res/models/<model_name>/frozen_inference_graph.pb`

Information on using object detection TensorFlow models with OpenCV, links to some pre-trained models (and generating a `.pbtxt` config file) can be found at [OpenCV's wiki on the TensorFlow Object Detection API](https://github.com/opencv/opencv/wiki/TensorFlow-Object-Detection-API).

`__init__.py` may be empty.

`config.py` should contain:

```python
from rpi_bot.vision.models.net_config_manager import NeuralNetworkConfig
import os

config = NeuralNetworkConfig()
```

You can then update some default configuration options by, for example, adding:

```python
# Update default values
config.model_dirname = os.path.basename(
    os.path.dirname(os.path.realpath(__file__)))
config.input_size_width = 320
config.input_size_height = 320
config.input_scale = 1.0 / 127.5
config.input_mean = (127.5, 127.5, 127.5)
config.input_swap_RB = True
```

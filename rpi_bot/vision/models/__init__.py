"""Neural Network models."""
from importlib import import_module

# NB import folder like this, as standard import statement throws ImportError.
net_config = import_module(('rpi_bot.vision.models.'
                            'ssd_mobilenet_v3_large_coco_2020_01_14.config'))

default_object_detection_config = net_config.config

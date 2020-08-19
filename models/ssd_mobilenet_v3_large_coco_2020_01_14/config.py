"""
Configuration properties for a Neural Network Model.

Model:
ssd_mobilenet_v3_large_coco_2020_01_14

This model requires images to be normalised before processing.
"""
from models.net_config_manager import NeuralNetworkConfig
import os

config = NeuralNetworkConfig()

# Update default values
config.model_dirname = os.path.basename(
    os.path.dirname(os.path.realpath(__file__)))
config.input_size_width = 320
config.input_size_height = 320
config.input_scale = 1.0 / 127.5
config.input_mean = (127.5, 127.5, 127.5)
config.input_swap_RB = True

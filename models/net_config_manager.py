"""Neural Network model configurations."""
from typing import Tuple


class NeuralNetworkConfig():
    """A data class that defines a Neural Network input configuration.

    Examples include how to normalise input images into the neural network.
    Properties of this class are used, for example, by
    cv2.dnn_DetectionModel().
    """

    model_dirname: str = None
    input_size_width: int = 300
    input_size_height: int = 300
    input_scale: float = None
    input_mean: Tuple[float, float, float] = None
    input_swap_RB: bool = True

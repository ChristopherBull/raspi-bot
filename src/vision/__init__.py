"""Vision Module. Add Models to the PATH."""
import os
import sys

models = os.path.dirname(os.path.abspath(__file__)) + "/../.."
sys.path.append(models)

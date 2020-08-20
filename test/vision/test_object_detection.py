"""Test Object Detection."""
import unittest
import src.vision.object_detection as detection


class TestObjectDetection(unittest.TestCase):
    """TestCase for Object Detection.

    Args:
        unittest (TestCase): TestCase parent.
    """

    def test_append_filename(self):
        """Test filename change utility function."""
        path = "myFile.py"
        to_append = ".abc123"
        expected = "myFile%s.py" % to_append
        self.assertEqual(detection.append_filename(path, to_append), expected)

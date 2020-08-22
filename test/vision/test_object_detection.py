"""Test Object Detection."""
import unittest
import rpi_bot.vision.object_detection as detection


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

    def test_object_detection_defaults(self):
        """
        Test object detection with default configuration.

        No exception should be raised.
        """
        detection.detect("test/res/test-image-1.jpg")

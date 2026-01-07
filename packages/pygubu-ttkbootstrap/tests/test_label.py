import pygubu
import unittest
import ttkbootstrap as ttk

from pathlib import Path
from .support import get_root, TestWidget
from .gcode.create_label import create_label

UI_PATH = Path(__file__).parent / "ui" / "label.ui"


#
class TestLabel(TestWidget):
    def create_widget(self):
        self.widget = create_label(master=get_root())

    def test_class(self):
        self.assertIsInstance(self.widget, ttk.Label)
        self.widget.destroy()


class TestLabelBuilder(TestWidget):
    def create_widget(self):
        self.builder = pygubu.Builder()
        self.builder.add_from_file(UI_PATH)
        self.widget = self.builder.get_object("label1")

    def test_class(self):
        self.assertIsInstance(self.widget, ttk.Label)
        self.widget.destroy()


if __name__ == "__main__":
    unittest.main()

import pygubu
import unittest
import bootstack as ttk

from pathlib import Path
from .support import get_root, TestWidget
from .gcode.create_button import create_button


UI_PATH = Path(__file__).parent / "ui" / "button.ui"


#
class TestLabel(TestWidget):
    def create_widget(self):
        self.widget = create_button(master=get_root())

    def test_class(self):
        self.assertIsInstance(self.widget, ttk.Button)
        self.widget.destroy()


class TestLabelBuilder(TestWidget):
    def create_widget(self):
        self.builder = pygubu.Builder()
        self.builder.add_from_file(UI_PATH)
        self.widget = self.builder.get_object("button1")

    def test_class(self):
        self.assertIsInstance(self.widget, ttk.Button)
        self.widget.destroy()


if __name__ == "__main__":
    unittest.main()

import unittest
import ttkbootstrap as tk

root = None


def get_root():
    global root

    if root is None:
        # create a new master only if there isn't one already
        root = tk.App()

    return root


def root_deiconify():
    root = get_root()
    root.deiconify()


def root_withdraw():
    root = get_root()
    root.withdraw()


def simulate_mouse_click(widget, x, y):
    """Generate proper events to click at the x, y position (tries to act
    like an X server)."""
    widget.event_generate("<Enter>", x=0, y=0)
    widget.event_generate("<Motion>", x=x, y=y)
    widget.event_generate("<ButtonPress-1>", x=x, y=y)
    widget.event_generate("<ButtonRelease-1>", x=x, y=y)


class TestWidget(unittest.TestCase):
    def setUp(self):
        root_deiconify()
        self.create_widget()

    def create_widget(self) -> any:
        raise NotImplementedError()

    def tearDown(self):
        root_withdraw()

#!/usr/bin/python3
import tkinter as tk
from ttkbootstrap.widgets.primitives.label import Label


def i18n_translator_noop(value):
    """i18n - Setup translator in derived class file"""
    return value


def first_object_callback_noop(widget):
    """on first objec callback - Setup callback in derived class file."""
    pass


def image_loader_default(master, image_name: str):
    """Image loader - Setup image_loader in derived class file."""
    return tk.PhotoImage(file=image_name, master=master)


def find_callback(callbacks_bag, callback_uid):
    cb = None

    if isinstance(callbacks_bag, dict):
        if callback_uid in callbacks_bag:
            cb = callbacks_bag[callback_uid]
    elif hasattr(callbacks_bag, callback_uid):
        cb = getattr(callbacks_bag, callback_uid)
    if cb is None:

        def cb_undef(*args):
            print(f"No function defined for {callback_uid}")

        cb = cb_undef
    return cb


def create_label(
    *,
    master=None,
    translator=None,
    on_first_object_cb=None,
    data_pool=None,
    image_loader=None,
    callbacks_bag=None,
):
    if translator is None:
        translator = i18n_translator_noop
    _ = translator  # i18n string marker.
    if image_loader is None:
        image_loader = image_loader_default
    if on_first_object_cb is None:
        on_first_object_cb = first_object_callback_noop

    #
    # Begin UI code
    label1 = Label(master)
    label1.configure(anchor="center", compound="left", icon="gear", text="label1")
    # First object created
    on_first_object_cb(label1)

    label1.pack(expand=True, ipadx=20, ipady=20, side="top")

    return label1


if __name__ == "__main__":
    root = tk.Tk()
    app = create_label(root)
    if isinstance(app, tk.Menu):
        root.configure(menu=app)
    root.mainloop()

#!/usr/bin/python3
"""
Label Test

Test Label code generation

UI source file: label-py.ui
"""

import tkinter as tk
from bootstack.widgets.primitives.label import Label


def safe_i18n_translator(value):
    """i18n - Setup translator in derived class file"""
    return value


def safe_fo_callback(widget):
    """on first objec callback - Setup callback in derived class file."""
    pass


def safe_image_loader(master, image_name: str):
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
    master=None,
    *,
    translator=None,
    on_first_object_cb=None,
    data_pool=None,
    image_loader=None,
    callbacks_bag=None,
):
    if translator is None:
        translator = safe_i18n_translator
    _ = translator  # i18n string marker.
    if image_loader is None:
        image_loader = safe_image_loader
    if on_first_object_cb is None:
        on_first_object_cb = safe_fo_callback

    #
    # Begin UI code
    label1 = Label(master)
    my_text_var = tk.StringVar(value="label1")
    label1.configure(
        anchor="se",
        background="#ffd6ff",
        compound="left",
        cursor="boat",
        foreground="#182400",
        icon="gear",
        icon_only=False,
        justify="center",
        padding="5p 5p 5p 5p",
        relief="solid",
        state="normal",
        takefocus=True,
        text="label1",
        textvariable=my_text_var,
        width=8,
        wraplength=50,
    )
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

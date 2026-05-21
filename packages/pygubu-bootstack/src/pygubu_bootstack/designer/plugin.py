import tkinter as tk
from pygubu.api.v1 import IDesignerPlugin
from pygubu.utils.widget import crop_widget
from ..config import namespace, primitives, windows
from .preview import ToplevelFramePreviewBO
from .properties import plugin_properties as plugin_properties


class ttkbDesignerPlugin(IDesignerPlugin):
    skip_crop = (
        primitives.notebook,
        primitives.notebook_tab,
        primitives.panedwindow,
        primitives.panedwindow_pane,
    )

    def is_toplevel_widget(self, builder_uid: str) -> bool:
        """Return True if builder widget is a toplevel widget.

        Example: for tk.Tk, tk.Toplevel should return True.
        """
        if builder_uid in (windows.app, windows.toplevel):
            return True
        return False

    def get_preview_builder(self, builder_uid: str):
        if builder_uid in (windows.app, windows.toplevel):
            return ToplevelFramePreviewBO
        return None

    def configure_for_preview(self, builder_uid: str, widget):
        if builder_uid.startswith(namespace):
            do_crop = builder_uid not in self.skip_crop and isinstance(
                widget, tk.Widget
            )
            if do_crop:
                crop_widget(widget)

    def ensure_visibility_in_preview(self, builder, selected_uid: str):
        """Ensure visibility of selected_uid in preview.
        Usage example:
            Activate a tab of a Notebook if the selected widget is
            inside the notebook.
        """
        xpath = ".//object[@class='bootstack.notebook_tab']"
        # find all tabs
        tabs = builder.uidefinition.root.findall(xpath)
        if tabs is None:
            return
        for tab in tabs:
            tab_id = tab.get("id")
            # Check if this tab was clicked
            if tab_id == selected_uid:
                xpath = "./child/object[1]"
                child = tab.find(xpath)
                # A tab can be empty, check that.
                if child is not None:
                    child_id = child.get("id")
                    notebook = builder.objects[tab_id].widget
                    current_tab = builder.objects[child_id].widget
                    notebook.select(current_tab)
                    notebook.update()
                    # Found, stop searching
                    break
            # check if selected_uid is inside this tab
            xpath = f".//object[@id='{selected_uid}']"
            o = tab.find(xpath)
            if o is not None:
                # selected_uid is inside, find the tab child
                # and select this tab
                xpath = "./child/object[1]"
                child = tab.find(xpath)
                child_id = child.get("id")
                notebook = builder.objects[tab_id].widget
                current_tab = builder.objects[child_id].widget
                notebook.select(current_tab)
                notebook.update()
                # Found, stop searching
                break

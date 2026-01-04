import tkinter as tk
from pygubu.api.v1 import IDesignerPlugin
from pygubu.utils.widget import crop_widget
from ..config import namespace, primitives


class ttkbDesignerPlugin(IDesignerPlugin):
    skip_crop = (
        primitives.notebook,
        primitives.notebook_tab,
        primitives.panedwindow,
        primitives.panedwindow_pane,
    )

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
        xpath = ".//object[@class='ttkbootstrap.notebook_tab']"
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

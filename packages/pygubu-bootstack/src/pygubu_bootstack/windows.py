from pygubu.api.v1 import BuilderObject, register_widget
from bootstack import App, Toplevel
from .config import windows, windows_ns, tab_group


RESIZABLE = {
    "both": (True, True),
    "horizontally": (True, False),
    "vertically": (False, True),
    "none": (False, False),
}


class ToplevelMixin:
    def realize(self, parent, extra_init_args: dict = None):
        self.parent_bo = parent
        args = self._get_init_args(extra_init_args)
        # master = parent.get_child_master()
        self.widget = self.class_(**args)
        return self.widget

    def code_realize(self, boparent, code_identifier=None):
        self.parent_bo = boparent
        if code_identifier is not None:
            self._code_identifier = code_identifier
        lines = []
        # master = boparent.code_child_master()
        init_args = self._code_get_init_args(self.code_identifier())
        kwargs = self.code_make_kwargs_str(init_args)
        s = f"{self.code_identifier()} = {self._code_class_name()}({kwargs})"
        lines.append(s)
        return lines

    def _process_property_value(self, pname, value):
        if pname in ("maxsize", "minsize"):
            if "|" in value:
                w, h = value.split("|")
                value = (int(w), int(h))
            return value
        elif pname == "resizable":
            return RESIZABLE[value]
        return super()._process_property_value(pname, value)

    def _code_process_property_value(self, targetid, pname, value: str):
        if pname in ("minsize", "maxsize", "resizable"):
            return self._process_property_value(pname, value)
        return super()._code_process_property_value(targetid, pname, value)


class AppBO(ToplevelMixin, BuilderObject):
    class_ = App
    container = True
    layout_required = False
    container_layout = True
    allowed_parents = ("root",)
    properties = (
        "title",
        "minsize",
        "maxsize",
        "resizable",
    )
    ro_properties = properties


register_widget(windows.app, AppBO, "App", tab_group, group=windows_ns.app)


class ToplevelBO(ToplevelMixin, BuilderObject):
    class_ = Toplevel
    container = True
    layout_required = False
    container_layout = True
    allowed_parents = ("root",)
    properties = (
        "title",
        "minsize",
        "maxsize",
        "resizable",
    )
    ro_properties = properties


register_widget(
    windows.toplevel, ToplevelBO, "Toplevel", tab_group, group=windows_ns.toplevel
)


# The commented code bellow needs and advanced preview class. For now just omit them.
# class AppShellBO(AppBO):
#     class_ = AppShell
#
#
# register_widget(windows.appshell, AppShellBO, "AppShell", tab_group, group=windows_ns.appshell)
#
#
# class AppShellPageBO(BuilderObject):
#     layout_required = False
#     allowed_parents = (windows.appshell,)
#
#     def realize(self, parent, extra_init_args: dict = None):
#         self.parent_bo = parent
#         args = self._get_init_args(extra_init_args)
#         master = parent.get_child_master()
#         page_id = self.wmeta.identifier
#         self.widget = master.add_page(page_id, **args)
#         return self.widget
#
# register_widget(windows.appshell_page, AppShellPageBO, "AppShell.Page", tab_group, group=windows_ns.appshell_page)

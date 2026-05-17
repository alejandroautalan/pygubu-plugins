from tkinter import getboolean
from pygubu.api.v1 import BuilderObject, register_widget
from bootstack import (
    Badge,
    Button,
    CheckButton,
    CheckToggle,
    Combobox,
    Entry,
    Frame,
    GridFrame,
    Label,
    LabelFrame,
    MenuButton,
    Notebook,
    OptionMenu,
    PackFrame,
    PanedWindow,
    Progressbar,
    RadioButton,
    RadioToggle,
    Scale,
    Scrollbar,
    Separator,
    SizeGrip,
    Spinbox,
    Switch,
    TreeView,
)
from pygubu.plugins.ttk.ttkstdwidgets import (
    TTKNotebookTab,
    TTKPanedwindowPane,
    TTKTreeviewBO,
    TTKTreeviewColumnBO,
)
from .config import primitives, primitives_ns, tab_group


class ttkbWidgetMixin:
    def _process_property_value(self, pname, value):
        if pname in ("localize", "icon_only"):
            return getboolean(value)
        return super()._process_property_value(pname, value)

    def _code_process_property_value(self, targetid, pname, value):
        if pname == ("localize", "icon_only"):
            return self._process_property_value(pname, value)
        return super()._code_process_property_value(targetid, pname, value)


class LabelBO(ttkbWidgetMixin, BuilderObject):
    class_ = Label
    properties = (
        "class_",
        "cursor",
        "text",
        "textvariable",
        "image",
        "icon",
        "icon_only",
        "compound",
        "anchor",
        "justify",
        "localize",
        "value_format",
        "padding",
        "width",
        "wraplength",
        "font",
        "foreground",
        "background",
        "relief",
        "state",
        "takefocus",
        "style",
        # "color",
        # "variant",
    )
    ro_properties = ("color",)  # FIXME


register_widget(
    primitives.label, LabelBO, "Label", tab_group, group=primitives_ns.label
)


class BadgeBO(LabelBO):
    class_ = Badge


register_widget(
    primitives.badge, BadgeBO, "Badge", tab_group, group=primitives_ns.badge
)


class ButtonBO(ttkbWidgetMixin, BuilderObject):
    class_ = Button
    properties = (
        "text",
        "command",
        "image",
        "icon",
        "icon_only",
        "anchor",
        "compound",
        "padding",
        "width",
        "underline",
        "state",
        "takefocus",
        "localize",
        "style",
        "class_",
        "cursor",
        "default",
        # "name",
        "textvariable",
        # "color",
        # "variant",
    )
    ro_properties = properties
    command_properties = ("command",)


register_widget(
    primitives.button, ButtonBO, "Button", tab_group, group=primitives_ns.button
)


class CheckButtonBO(ttkbWidgetMixin, BuilderObject):
    class_ = CheckButton
    properties = (
        "text",
        "command",
        "image",
        "icon",
        "icon_only",
        "compound",
        "variable",
        # "signal",
        "value",
        "onvalue",
        "offvalue",
        "padding",
        "anchor",
        "width",
        "underline",
        "state",
        "takefocus",
        "style",
        "class_",
        "cur",
        # "name",
        "textvariable",
        # "textsignal",
        # "color",
        # "vari",
        # "surface_color",
        "localize",
    )
    ro_properties = properties
    command_properties = ("command",)


register_widget(
    primitives.checkbutton,
    CheckButtonBO,
    "CheckButton",
    tab_group,
    group=primitives_ns.checkbutton,
)


class CheckToggleBO(CheckButtonBO):
    class_ = CheckToggle


register_widget(
    primitives.checktoogle,
    CheckToggleBO,
    "CheckToggle",
    tab_group,
    group=primitives_ns.checktoogle,
)


class SwitchBO(CheckButtonBO):
    class_ = Switch


register_widget(
    primitives.switch, SwitchBO, "Switch", tab_group, group=primitives_ns.switch
)


class RadioButtonBO(ttkbWidgetMixin, BuilderObject):
    class_ = RadioButton
    properties = (
        "text",
        "command",
        "image",
        "icon",
        "icon_only",
        "compound",
        "variable",
        # "signal",
        "value",
        "padding",
        "anchor",
        "width",
        "underline",
        "state",
        "takefocus",
        "style",
        "class_",
        "cursor",
        # "name",
        "textvariable",
        # "textsignal",
        # "color",
        # "variant",
        # "surface_color",
        "localize",
    )
    ro_properties = properties
    command_properties = ("command",)


register_widget(
    primitives.radiobutton,
    RadioButtonBO,
    "RadioButton",
    tab_group,
    group=primitives_ns.radiobutton,
)


class RadioToggleBO(RadioButtonBO):
    class_ = RadioToggle


register_widget(
    primitives.radiotoggle,
    RadioToggleBO,
    "RadioToggle",
    tab_group,
    group=primitives_ns.radiotoggle,
)


class ComboboxBO(ttkbWidgetMixin, BuilderObject):
    class_ = Combobox
    properties = (
        "values",
        "textvariable",
        "textsignal",
        "state",
        "width",
        "height",
        "postcommand",
        "justify",
        "exportselection",
        "xscrollcommand",
        "font",
        "foreground",
        "background",
        "style",
        "class_",
        "cursor",
        # "name",
        # "color",
        # "surface_color",
    )
    ro_properties = properties
    command_properties = ("postcommand",)


register_widget(
    primitives.combobox, ComboboxBO, "Combobox", tab_group, group=primitives_ns.combobox
)


class EntryBO(ttkbWidgetMixin, BuilderObject):
    class_ = Entry
    properties = (
        "textvariable",
        # "textsignal",
        "show",
        "width",
        "exportselection",
        "justify",
        "validate",
        "validatecommand",
        "invalidcommand",
        "xscrollcommand",
        "font",
        "foreground",
        "background",
        "state",
        "takefocus",
        "style",
        "class_",
        "cursor",
        # "name",
        # "color",
        # "variant",
        # "surface_color",
    )
    ro_properties = properties
    command_properties = ("validatecommand", "invalidcommand", "xscrollcommand")


register_widget(
    primitives.entry, EntryBO, "Entry", tab_group, group=primitives_ns.entry
)


class FrameBO(ttkbWidgetMixin, BuilderObject):
    class_ = Frame
    container = True
    container_layout = True
    properties = (
        "class_",
        "cursor",
        "takefocus",
        "style",
        "borderwidth",
        "relief",
        "padding",
        "height",
        "width",
        "takefocus",
        # "color",
        # "variant",
        "show_border",
    )
    ro_properties = properties


register_widget(
    primitives.frame, FrameBO, "Frame", tab_group, group=primitives_ns.frame
)


class GridFrameBO(FrameBO):
    class_ = GridFrame
    container = True
    container_layout = False  # FIXME: howto handle this widget?


register_widget(
    primitives.gridframe,
    GridFrameBO,
    "GridFrame",
    tab_group,
    group=primitives_ns.gridframe,
)


class PackFrameBO(FrameBO):
    class_ = PackFrame
    container = True
    container_layout = False  # FIXME: howto handle this widget?


register_widget(
    primitives.packframe,
    PackFrameBO,
    "PackFrame",
    tab_group,
    group=primitives_ns.packframe,
)


class LabelFrameBO(ttkbWidgetMixin, BuilderObject):
    class_ = LabelFrame
    container = True
    container_layout = True
    properties = (
        "text",
        "labelanchor",
        "padding",
        "relief",
        "borderwidth",
        "width",
        "height",
        "style",
        "class_",
        "cursor",
        # "name",
        # "color",
        # "surface_color",
        "localize",
    )
    ro_properties = properties


register_widget(
    primitives.labelframe,
    LabelFrameBO,
    "LabelFrame",
    tab_group,
    group=primitives_ns.labelframe,
)


class MenuButtonBO(ttkbWidgetMixin, BuilderObject):
    class_ = MenuButton
    properties = (
        "text",
        "image",
        "icon",
        "icon_only",
        "compound",
        "direction",
        "menu",
        "padding",
        "state",
        "takefocus",
        "style",
        "class_",
        "cursor",
        # "name",
        "textvariable",
        # "textsignal",
        # "color",
        # "variant",
        # "surface_color",
        "localize",
    )
    ro_properties = properties


register_widget(
    primitives.menubutton,
    MenuButtonBO,
    "MenuButton",
    tab_group,
    group=primitives_ns.menubutton,
)


class NotebookBO(ttkbWidgetMixin, BuilderObject):
    class_ = Notebook
    container = True
    allowed_children = (primitives.notebook_tab,)
    virtual_events = (
        "<<NotebookTabChange>>",
        "<<NotebookTabActivate>>",
        "<<NotebookTabDeactivate>>",
    )
    properties = (
        "padding",
        "height",
        "width",
        "style",
        "class_",
        "cursor",
        # "color",
        # "variant",
        # "surface_color",
    )
    ro_properties = properties


register_widget(
    primitives.notebook, NotebookBO, "Notebook", tab_group, group=primitives_ns.notebook
)


class NotebookTabBO(TTKNotebookTab): ...


register_widget(
    primitives.notebook_tab,
    NotebookTabBO,
    "Notebook.Tab",
    tab_group,
    group=primitives_ns.notebook_tab,
)

NotebookTabBO.add_allowed_parent(primitives.notebook)


class OptionMenuBO(ttkbWidgetMixin, BuilderObject):
    class_ = OptionMenu
    properties = (
        "command",
        "image",
        "icon",
        "icon_only",
        "compound",
        "padding",
        "width",
        "underline",
        "state",
        "takefocus",
        "style",
        "class_",
        "cursor",
        "default",
        # "name",
        "textvariable",
        # "textsignal",
        # "color",
        # "variant",
        # "surface_color",
        "show_dropdown_button",
        "dropdown_button_icon",
    )
    ro_properties = properties
    command_properties = ("command",)


register_widget(
    primitives.optionmenu,
    OptionMenuBO,
    "OptionMenu",
    tab_group,
    group=primitives_ns.optionmenu,
)


class PanedWindowBO(ttkbWidgetMixin, BuilderObject):
    class_ = PanedWindow
    container = True
    allowed_children = (primitives.panedwindow_pane,)
    properties = (
        "orient",
        "padding",
        "width",
        "height",
        "style",
        "class_",
        "cursor",
        # "name",
        # "color",
        # "variant",
        # "surface_color",
    )
    ro_properties = properties


register_widget(
    primitives.panedwindow,
    PanedWindowBO,
    "PanedWindow",
    tab_group,
    group=primitives_ns.panedwindow,
)


class PanedWindowPaneBO(TTKPanedwindowPane): ...


register_widget(
    primitives.panedwindow_pane,
    PanedWindowPaneBO,
    "PanedWindow.Pane",
    tab_group,
    group=primitives_ns.panedwindow_pane,
)

PanedWindowPaneBO.add_allowed_parent(primitives.panedwindow)


class ProgressbarBO(ttkbWidgetMixin, BuilderObject):
    class_ = Progressbar
    properties = (
        "mode",
        "orient",
        "length",
        "maximum",
        "value",
        "variable",
        # "signal",  FIXME !
        "phase",
        "style",
        "class_",
        "cursor",
        # "name",
        # "color",
        # "variant",
        # "surface_color",
    )
    ro_properties = properties


register_widget(
    primitives.progressbar,
    ProgressbarBO,
    "Progressbar",
    tab_group,
    group=primitives_ns.progressbar,
)


class ScaleBO(ttkbWidgetMixin, BuilderObject):
    class_ = Scale
    properties = (
        "from_",
        "to",
        "value",
        "variable",
        # "signal",
        "orient",
        "length",
        "command",
        "takefocus",
        "style",
        "class_",
        "cursor",
        # "name",
        # "color",
        # "variant",
        # "surface_color",
    )
    ro_properties = properties
    command_properties = ("command",)


register_widget(
    primitives.scrollbar, ScaleBO, "Scale", tab_group, group=primitives_ns.scrollbar
)


class ScrollbarBO(ttkbWidgetMixin, BuilderObject):
    class_ = Scrollbar
    properties = (
        "orient",
        "command",
        "takefocus",
        "style",
        "class_",
        "cursor",
        # "name",
        # "color",
        # "variant",
        # "surface_color",
    )
    ro_properties = properties


register_widget(
    primitives.scrollbar,
    ScrollbarBO,
    "Scrollbar",
    tab_group,
    group=primitives_ns.scrollbar,
)


class SeparatorBO(ttkbWidgetMixin, BuilderObject):
    class_ = Separator
    properties = (
        "orient",
        "style",
        "class_",
        "cursor",
        # "name",
        # "color",
        # "variant",
        # "surface_color",
    )
    ro_properties = properties


register_widget(
    primitives.separator,
    SeparatorBO,
    "Separator",
    tab_group,
    group=primitives_ns.separator,
)


class SizeGripBO(ttkbWidgetMixin, BuilderObject):
    class_ = SizeGrip
    properties = (
        "style",
        "class_",
        "cursor",
        # "name",
        # "color",
        # "surface_color",
    )
    ro_properties = properties


register_widget(
    primitives.sizegrip, SizeGripBO, "SizeGrip", tab_group, group=primitives_ns.sizegrip
)


class SpinboxBO(ttkbWidgetMixin, BuilderObject):
    class_ = Spinbox
    properties = (
        "from_",
        "to",
        "increment",
        "values",
        "wrap",
        "command",
        "textvariable",
        # "textsignal",  FIXME!
        "format",
        "width",
        "state",
        "takefocus",
        "style",
        "class_",
        "cursor",
        # "name",
        # "color",
        # "surface_color",
    )
    ro_properties = properties
    command_properties = ("command",)


register_widget(
    primitives.spinbox, SpinboxBO, "Spinbox", tab_group, group=primitives_ns.spinbox
)


class TreeViewBO(TTKTreeviewBO):
    class_ = TreeView
    allowed_children = (primitives.treeview_col,)


register_widget(
    primitives.treeview, TreeViewBO, "TreeView", tab_group, group=primitives_ns.treeview
)


class TreeViewColBO(TTKTreeviewColumnBO):
    allowed_parents = (primitives.treeview,)


register_widget(
    primitives.treeview_col,
    TreeViewColBO,
    "TreeView.Column",
    tab_group,
    group=primitives_ns.treeview_col,
)

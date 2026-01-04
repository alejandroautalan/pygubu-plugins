from pygubu.api.v1 import BuilderObject, register_widget
from .config import primitives, tab_group
from ttkbootstrap import (
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


class BadgeBO(BuilderObject):
    class_ = Badge
    properties = ("text",)


register_widget(primitives.badge, BadgeBO, "Badge", tab_group)


class ButtonBO(BuilderObject):
    class_ = Button
    properties = ("text",)


register_widget(primitives.button, ButtonBO, "Button", tab_group)


class CheckButtonBO(BuilderObject):
    class_ = CheckButton
    properties = ("text",)


register_widget(primitives.checkbutton, CheckButtonBO, "CheckButton", tab_group)


class CheckToggleBO(BuilderObject):
    class_ = CheckToggle
    properties = ("text",)


register_widget(primitives.checktoogle, CheckToggleBO, "CheckToggle", tab_group)


class ComboboxBO(BuilderObject):
    class_ = Combobox
    properties = tuple()


register_widget(primitives.combobox, ComboboxBO, "Combobox", tab_group)


class EntryBO(BuilderObject):
    class_ = Entry
    properties = []


register_widget(primitives.entry, EntryBO, "Entry", tab_group)


class FrameBO(BuilderObject):
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
    )


register_widget(primitives.frame, FrameBO, "Frame", tab_group)


class GridFrameBO(BuilderObject):
    class_ = GridFrame
    container = True
    container_layout = True
    properties = ("class_",)


register_widget(primitives.gridframe, GridFrameBO, "GridFrame", tab_group)


class LabelBO(BuilderObject):
    class_ = Label
    properties = ("text",)


register_widget(primitives.label, LabelBO, "Label", tab_group)


class LabelFrameBO(BuilderObject):
    class_ = LabelFrame
    container = True
    container_layout = True
    properties = (
        "text",
        "padding",
    )


register_widget(primitives.labelframe, LabelFrameBO, "LabelFrame", tab_group)


class MenuButtonBO(BuilderObject):
    class_ = MenuButton
    properties = ("text",)


register_widget(primitives.menubutton, MenuButtonBO, "MenuButton", tab_group)


class NotebookBO(BuilderObject):
    class_ = Notebook
    container = True
    allowed_children = (primitives.notebook_tab,)
    properties = (
        "padding",
        "width",
    )


register_widget(primitives.notebook, NotebookBO, "Notebook", tab_group)

Progressbar


class NotebookTabBO(TTKNotebookTab): ...


register_widget(primitives.notebook_tab, NotebookTabBO, "Notebook.Tab", tab_group)

NotebookTabBO.add_allowed_parent(primitives.notebook)


class OptionMenuBO(BuilderObject):
    class_ = OptionMenu
    properties = ("padding",)


register_widget(primitives.optionmenu, OptionMenuBO, "OptionMenu", tab_group)


class PackFrameBO(BuilderObject):
    class_ = PackFrame
    container = True
    container_layout = False
    properties = ("padding",)


register_widget(primitives.packframe, PackFrameBO, "PackFrame", tab_group)


class PanedWindowBO(BuilderObject):
    class_ = PanedWindow
    container = True
    allowed_children = (primitives.panedwindow_pane,)
    properties = ("orient",)
    ro_properties = ("orient",)


register_widget(primitives.panedwindow, PanedWindowBO, "PanedWindow", tab_group)


class PanedWindowPaneBO(TTKPanedwindowPane): ...


register_widget(
    primitives.panedwindow_pane, PanedWindowPaneBO, "PanedWindow.Pane", tab_group
)

PanedWindowPaneBO.add_allowed_parent(primitives.panedwindow)


class ProgressbarBO(BuilderObject):
    class_ = Progressbar
    properties = (
        "mode",
        "orient",
    )


register_widget(primitives.progressbar, ProgressbarBO, "Progressbar", tab_group)


class RadioButtonBO(BuilderObject):
    class_ = RadioButton
    properties = ("text",)


register_widget(primitives.radiobutton, RadioButtonBO, "RadioButton", tab_group)


class RadioToggleBO(RadioButtonBO):
    class_ = RadioToggle


register_widget(primitives.radiotoggle, RadioToggleBO, "RadioToggle", tab_group)


class ScaleBO(BuilderObject):
    class_ = Scale
    properties = (
        "orient",
        "from_",
        "to",
    )


register_widget(primitives.scale, ScaleBO, "Scale", tab_group)


class ScrollbarBO(BuilderObject):
    class_ = Scrollbar
    properties = ("orient",)
    ro_properties = ("orient",)


register_widget(primitives.scrollbar, ScrollbarBO, "Scrollbar", tab_group)


class SeparatorBO(BuilderObject):
    class_ = Separator
    properties = ("orient",)
    ro_properties = ("orient",)


register_widget(primitives.separator, SeparatorBO, "Separator", tab_group)


class SizeGripBO(BuilderObject):
    class_ = SizeGrip
    properties = []


register_widget(primitives.sizegrip, SizeGripBO, "SizeGrip", tab_group)


class SpinboxBO(BuilderObject):
    class_ = Spinbox
    properties = ("from_", "to")


register_widget(primitives.spinbox, SpinboxBO, "Spinbox", tab_group)


class SwitchBO(CheckButtonBO):
    class_ = Switch


register_widget(primitives.switch, SwitchBO, "Switch", tab_group)


class TreeViewBO(TTKTreeviewBO):
    class_ = TreeView
    allowed_children = (primitives.treeview_col,)


register_widget(primitives.treeview, TreeViewBO, "TreeView", tab_group)


class TreeViewColBO(TTKTreeviewColumnBO):
    allowed_parents = (primitives.treeview,)


register_widget(primitives.treeview_col, TreeViewColBO, "TreeView.Column", tab_group)

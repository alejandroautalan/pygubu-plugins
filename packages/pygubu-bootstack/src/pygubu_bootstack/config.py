from pygubu.utils.namespace import walkns, SN


tab_group = ("ttk", "ttkbootstrap Widgets")
namespace = "ttkbootstrap"

CONTAINER = 50
INPUT = 90

windows_ns = SN(
    _name=namespace,
    app=10,
    toplevel=10,
)
windows = walkns(windows_ns)

primitives_ns = SN(
    _name=namespace,
    # containers
    frame=CONTAINER - 5,
    packframe=CONTAINER - 4,
    gridframe=CONTAINER - 3,
    labelframe=CONTAINER - 2,
    notebook=CONTAINER,
    notebook_tab=CONTAINER,
    panedwindow=CONTAINER,
    panedwindow_pane=CONTAINER,
    # input widgets
    label=INPUT - 5,
    badge=INPUT - 5,
    entry=INPUT - 4,
    spinbox=INPUT - 4,
    combobox=INPUT - 4,
    button=INPUT - 3,
    checkbutton=INPUT - 3,
    checktoogle=INPUT - 3,
    radiobutton=INPUT - 3,
    radiotoggle=INPUT - 3,
    switch=INPUT - 3,
    menubutton=INPUT - 3,
    optionmenu=INPUT - 3,
    progressbar=INPUT,
    scale=INPUT,
    scrollbar=INPUT,
    separator=INPUT,
    sizegrip=INPUT,
    treeview=INPUT,
    treeview_col=INPUT,
)

primitives = walkns(primitives_ns)

from pygubu.utils.namespace import walkns, SN


tab_group = ("ttk", "ttkbootstrap Widgets")
namespace = "ttkbootstrap"

primitives_ns = SN(
    _name=namespace,
    frame=1,
    badge=1,
    button=1,
    checkbutton=1,
    checktoogle=1,
    combobox=1,
    entry=1,
    gridframe=1,
    label=1,
    labelframe=1,
    menubutton=1,
    notebook=1,
    notebook_tab=1,
    optionmenu=1,
    packframe=1,
    panedwindow=1,
    panedwindow_pane=1,
    progressbar=1,
    radiobutton=1,
    radiotoggle=1,
    scale=1,
    scrollbar=1,
    separator=1,
    sizegrip=1,
    spinbox=1,
    switch=1,
    treeview=1,
    treeview_col=1,
)

primitives = walkns(primitives_ns)

from pygubu.api.v1 import register_custom_property
from ..config import namespace, windows, primitives

_builder_all = f"{namespace}.*"

plugin_properties = dict(
    auto_flow=dict(
        buid=[primitives.gridframe],
        editor="choice",
        values=("", "row", "column", "row-dense", "column-dense", "none"),
        state="readonly",
    ),
    color=dict(
        buid=_builder_all,
        editor="choice",
        values=("", "primary", "danger", "success"),
        state="readonly",
    ),
    columns=dict(
        buid=primitives.gridframe,
        editor="json_entry",
        help="Number of columns or a list of size specs.",
    ),
    direction=dict(
        buid=[primitives.packframe],
        editor="choice",
        values=(
            "",
            "vertical",
            "horizontal",
            "row",
            "column",
            "row-reverse",
            "column-reverse",
        ),
        state="readonly",
    ),
    gap=dict(
        buid=[primitives.packframe, primitives.gridframe],
        editor="naturalnumber",
    ),
    icon=dict(buid=_builder_all),
    icon_only=dict(
        buid=_builder_all,
        editor="choice",
        values=("True", "False"),
        default_value="False",
        state="readonly",
    ),
    maxsize=dict(
        buid=[windows.app, windows.appshell, windows.toplevel], editor="whentry"
    ),
    minsize=dict(
        buid=[windows.app, windows.appshell, windows.toplevel], editor="whentry"
    ),
    resizable=dict(
        buid=[windows.app, windows.toplevel],
        editor="choice",
        values=("", "both", "horizontally", "vertically", "none"),
        state="readonly",
    ),
    rows=dict(
        buid=primitives.gridframe,
        editor="json_entry",
        help="Number of row or a list of size specs.",
    ),
    state=[
        dict(
            buid=[_builder_all],  # FIXME: for all widgets?
            editor="choice",
            values=("", "normal", "active", "disabled", "readonly"),
            state="readonly",
        ),
        dict(
            buid=[primitives.combobox, primitives.combobox],
            editor="choice",
            values=("", "normal", "disabled", "readonly"),
            state="readonly",
        ),
    ],
    sticky_items=dict(
        buid=primitives.gridframe,
        editor="choice",
        values=(
            "",
            "n",
            "ne",
            "nw",
            "e",
            "w",
            "s",
            "se",
            "sw",
            "center",
        ),
        state="readonly",
    ),
    variant=dict(
        buid=_builder_all,
        editor="choice",
        values=("", "default", "inverse"),
        state="readonly",
    ),
)

for prop in plugin_properties:
    definitions = plugin_properties[prop]
    if isinstance(definitions, dict):
        definitions = [definitions]
    for definition in definitions:
        builders = definition.pop("buid", _builder_all)
        if isinstance(builders, str):
            builders = [builders]
        editor = definition.pop("editor", "entry")
        for builder_uid in builders:
            register_custom_property(builder_uid, prop, editor, **definition)

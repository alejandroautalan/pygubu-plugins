from pygubu.api.v1 import register_custom_property
from ..config import namespace, windows, primitives

_builder_all = f"{namespace}.*"

plugin_properties = dict(
    color=dict(
        buid=_builder_all,
        editor="choice",
        values=("", "primary", "danger", "success"),
        state="readonly",
    ),
    icon=dict(buid=_builder_all),
    maxsize=dict(buid=[windows.app, windows.toplevel], editor="whentry"),
    minsize=dict(buid=[windows.app, windows.toplevel], editor="whentry"),
    resizable=dict(
        buid=[windows.app, windows.toplevel],
        editor="choice",
        values=("", "both", "horizontally", "vertically", "none"),
        state="readonly",
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

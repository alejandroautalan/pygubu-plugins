import importlib
from pygubu.api.v1 import BuilderLoaderPlugin
from .config import namespace, windows, primitives


class ttkbootstrapPlugin(BuilderLoaderPlugin):
    module_map = {
        "pygubu_bootstack.windows": (windows.app, windows.toplevel),
        "pygubu_bootstack.primitives": (
            primitives.frame,
            primitives.labelframe,
            primitives.label,
            primitives.button,
        ),
    }

    def do_activate(self) -> bool:
        spec = importlib.util.find_spec("bootstack")
        return spec is not None

    def get_module_for(self, identifier: str) -> str:
        for module, identifiers in self.module_map.items():
            if identifier in identifiers:
                return module
        return None

    def get_all_modules(self):
        return [m for m in self.module_map.keys()]

    def can_load(self, identifier: str) -> bool:
        return identifier.startswith(f"{namespace}.")

    def get_designer_plugin(self):
        """Load class that implements IDesignerPlugin"""
        from .designer.plugin import ttkbDesignerPlugin

        return ttkbDesignerPlugin()

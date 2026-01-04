import importlib
from pygubu.api.v1 import BuilderLoaderPlugin
from .config import primitives, namespace


class ttkbootstrapPlugin(BuilderLoaderPlugin):
    module_map = {
        "pygubu_ttkbootstrap.windows": (f"{namespace}.Window",),
        "pygubu_ttkbootstrap.primitives": (primitives.frame,),
    }

    def do_activate(self) -> bool:
        spec = importlib.util.find_spec("ttkbootstrap")
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

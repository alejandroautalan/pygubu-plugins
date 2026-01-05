from pygubu.plugins.pygubu.designer.basehelpers import (
    ToplevelPreviewFactory,
    ToplevelPreviewMixin,
    ToplevelPreviewBaseBO,
)
from ttkbootstrap import Frame


ToplevelFramePreview = ToplevelPreviewFactory(
    "ToplevelFramePreview",
    (ToplevelPreviewMixin, Frame, object),
    {},
)


class ToplevelFramePreviewBO(ToplevelPreviewBaseBO):
    class_ = ToplevelFramePreview

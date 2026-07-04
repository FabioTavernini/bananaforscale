import os
import FreeCADGui as Gui

_ADDON_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
_ICON = os.path.join(_ADDON_DIR, "Resources", "Icons", "banana.png")


class BananaForScaleWorkbench(Gui.Workbench):
    MenuText = "Banana For Scale"
    ToolTip = "Adds a banana for scale to your FreeCAD document"
    Icon = _ICON

    def Initialize(self):
        from . import banana_command
        self.appendToolbar("Banana Tools", ["Banana_AddForScale"])
        self.appendMenu("Banana For Scale", ["Banana_AddForScale"])

    def Activated(self):
        pass

    def Deactivated(self):
        pass


Gui.addWorkbench(BananaForScaleWorkbench())

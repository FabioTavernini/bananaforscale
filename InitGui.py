import os
import FreeCADGui as Gui


class BananaForScaleWorkbench(Gui.Workbench):
    MenuText = "Banana For Scale"
    ToolTip = "Adds a banana for scale to your FreeCAD document"
    Icon = os.path.join(os.path.dirname(__file__), "Resources", "media", "screenshot.png")

    def Initialize(self):
        import banana_command
        self.appendToolbar("Banana Tools", ["Banana_AddForScale"])
        self.appendMenu("Banana For Scale", ["Banana_AddForScale"])

    def Activated(self):
        pass

    def Deactivated(self):
        pass


Gui.addWorkbench(BananaForScaleWorkbench())
import os
import FreeCAD as App
import FreeCADGui as Gui

class BananaForScaleWorkbench(Gui.Workbench):
    MenuText = "Banana For Scale"
    ToolTip = "Adds a banana for scale to your FreeCAD document"
    Icon = os.path.join(App.getUserAppDataDir(), "Mod", "bananaforscale", "Resources", "media", "banana.png")

    def Initialize(self):
        import banana_command
        self.appendToolbar("Banana Tools", ["Banana_AddForScale"])
        self.appendMenu("Banana For Scale", ["Banana_AddForScale"])

    def Activated(self):
        pass

    def Deactivated(self):
        pass


try:
    Gui.addWorkbench(BananaForScaleWorkbench())
except Exception as e:
    App.Console.PrintError(f"BananaForScale: failed to register workbench: {e}\n")
import os
import FreeCAD as App
import FreeCADGui as Gui
import Mesh as MeshModule

_ADDON_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MODEL_PATH = os.path.join(_ADDON_DIR, "Resources", "Models", "banana.stl")
ICON_PATH = os.path.join(_ADDON_DIR, "Resources", "Icons", "banana.svg")


class AddBananaForScaleCommand:
    def GetResources(self):
        return {
            "MenuText": "Add Banana for Scale",
            "ToolTip": "Adds a banana for scale to the document",
            "Pixmap": ICON_PATH,
        }

    def Activated(self):
        doc = App.ActiveDocument
        if doc is None:
            doc = App.newDocument("Banana_For_Scale")

        obj = doc.addObject("Mesh::Feature", "Banana_for_scale")
        obj.Mesh = MeshModule.Mesh(MODEL_PATH)
        obj.ViewObject.ShapeColor = (1.0, 0.82, 0.05)

        doc.recompute()
        Gui.SendMsgToActiveView("ViewFit")

        Gui.Selection.clearSelection()
        Gui.Selection.addSelection(doc.Name, obj.Name)
        Gui.runCommand("Std_TransformManip")

    def IsActive(self):
        return True


Gui.addCommand("Banana_AddForScale", AddBananaForScaleCommand())

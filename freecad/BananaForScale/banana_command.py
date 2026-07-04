import os
import FreeCAD as App
import FreeCADGui as Gui
import Part

_ADDON_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
STEP_PATH = os.path.join(_ADDON_DIR, "Resources", "Models", "banana.step")


class AddBananaForScaleCommand:
    def GetResources(self):
        return {
            "MenuText": "Add Banana for Scale",
            "ToolTip": "Adds a banana for scale to the document",
            "Pixmap": "",
        }

    def Activated(self):
        doc = App.ActiveDocument
        if doc is None:
            doc = App.newDocument("Banana_For_Scale")

        shape = Part.Shape()
        shape.read(STEP_PATH)

        obj = doc.addObject("Part::Feature", "Banana_for_scale")
        obj.Shape = shape
        obj.ViewObject.ShapeColor = (1.0, 0.82, 0.05)
        obj.ViewObject.DisplayMode = "Shaded"

        doc.recompute()
        Gui.SendMsgToActiveView("ViewFit")

        Gui.Selection.clearSelection()
        Gui.Selection.addSelection(doc.Name, obj.Name)
        Gui.runCommand("Std_TransformManip")

    def IsActive(self):
        return True


Gui.addCommand("Banana_AddForScale", AddBananaForScaleCommand())

from contextlib import suppress
from typing import ClassVar

import FreeCAD as App

from . import banana_command  # noqa: F401 — registers Banana_AddForScale
from . import can_command  # noqa: F401 — registers Banana_AddCanForScale


class WorkbenchManipulator:
    _instance: ClassVar["WorkbenchManipulator | None"] = None

    def modifyMenuBar(self):
        return []

    def modifyContextMenu(self, recipient):
        return []

    def modifyToolBars(self):
        return [
            {"append": "Banana_AddForScale", "toolBar": "View"},
            {"append": "Banana_AddCanForScale", "toolBar": "View"},
        ]

    @classmethod
    def install(cls):
        if App.GuiUp and cls._instance is None:
            cls._instance = WorkbenchManipulator()
            App.Gui.addWorkbenchManipulator(cls._instance)
            with suppress(Exception):
                App.Gui.activeWorkbench().reloadActive()


WorkbenchManipulator.install()

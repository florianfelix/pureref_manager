import bpy
from bpy.types import AddonPreferences
from bpy.props import StringProperty, IntProperty, BoolProperty


class PureRefAddonPreferences(AddonPreferences):
    bl_idname = __package__

    pureref_executable: StringProperty(
        name="PureRef Executable",
        subtype='FILE_PATH',
    )

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "pureref_executable")

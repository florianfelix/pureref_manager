import bpy
from bpy.types import PropertyGroup
from bpy.props import PointerProperty, BoolProperty, StringProperty


class PureRefManagerSceneSettings(PropertyGroup):
    open_on_load: BoolProperty(
        name='Open on load',
        default=False,
        description='Open the PureRef file for this blender scene on opening the blender file')
    pureref_file: StringProperty(
        name='PureRef File',
        default='',
        subtype='FILE_PATH',
        description='If left empty the alphabetically last found pureref file in the project directory is opened')


def register():
    bpy.types.Scene.pureref_scene_settings = PointerProperty(
        type=PureRefManagerSceneSettings)


def unregister():
    del(bpy.types.Scene.pureref_scene_settings)

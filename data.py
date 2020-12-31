import bpy
from bpy.types import PropertyGroup
from bpy.props import PointerProperty, BoolProperty, StringProperty


class PureRefManagerSceneSettings(PropertyGroup):
    load_on_load: BoolProperty(
        name='Open PureRef on File Load',
        default=False,)
    pureref_file: StringProperty(
        name='PureRef File to Load',
        default='',
        subtype='FILE_PATH',
        description='If left empty the alphabetically last found pureref file is opened')


def register():
    bpy.types.Scene.pureref_scene_settings = PointerProperty(
        type=PureRefManagerSceneSettings)


def unregister():
    del(bpy.types.Scene.pureref_scene_settings)

import bpy
import os
from subprocess import Popen

from bpy.app.handlers import persistent


@persistent
def pureref_load_handler(dummy):
    execute_on_load = bpy.context.scene.pureref_scene_settings.open_on_load
    if execute_on_load:
        pureref_open()


def pureref_open():
    # First try to load PureRef from Filepath in Scene Settings
    filepath = bpy.context.scene.pureref_scene_settings.pureref_file
    filepath = bpy.path.abspath(filepath)
    if filepath:
        open_pureref_file(filepath)

    # Else try finding PureRef File in Project directory
    else:
        if not bpy.data.filepath:
            # print("PureRef: File not saved. Nowhere to look.")
            return

        folder = os.path.dirname(bpy.data.filepath)
        purerefs = sorted([os.path.join(folder, f)
                           for f in os.listdir(folder) if f.endswith(".pur")])

        if purerefs:
            filepath = purerefs[-1]
            open_pureref_file(filepath)
        else:
            print('PureRef: No PureRef Files found in project directory')


def open_pureref_file(path):
    addon_prefs = bpy.context.preferences.addons[__package__].preferences
    pureref_executable = addon_prefs.pureref_executable

    # Check if executable is set
    if not pureref_executable:
        print("PureRef: Executable not set in Addon Preferences, Doing nothing.")
        return

    # Check if file exists and is pureref file
    if not os.path.exists(path) or not os.path.basename(path).endswith('.pur'):
        print('PureRef: ', path, 'not found')
        return

    # Open pureref with file
    command = [pureref_executable, path]
    Popen(command)


class OpenPureRef(bpy.types.Operator):
    bl_idname = "scene.open_pureref"
    bl_label = "Open PureRef"

    def execute(self, context):
        pureref_open()
        return {'FINISHED'}


def register():
    if pureref_load_handler in bpy.app.handlers.load_post:
        bpy.app.handlers.load_post.remove(pureref_load_handler)

    bpy.app.handlers.load_post.append(pureref_load_handler)


def unregister():
    bpy.app.handlers.load_post.remove(pureref_load_handler)

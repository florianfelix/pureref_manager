import bpy


class Show_preferencesOperator(bpy.types.Operator):
    bl_idname = "scene.show_preferences"
    bl_label = "Show Preferences"

    def execute(self, context):
        bpy.ops.screen.userpref_show()
        context.preferences.active_section = 'ADDONS'
        bpy.ops.preferences.addon_show(module="pureref_manager")

        return {'FINISHED'}


from bpy.types import Panel


class VIEW3D_PT_pureref_manager(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "View"
    bl_label = "PureRef"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False  # No animation.

        scene = context.scene
        settings = scene.pureref_scene_settings

        col = layout.column()

        preferences = context.preferences
        addon_prefs = preferences.addons[__package__].preferences
        pureref_executable = addon_prefs.pureref_executable

        if not pureref_executable:
            col.label(text='PureRef executable not set', icon='ERROR')
            col.label(text='Set in Addon Preferences', icon='ERROR')

        col.operator('scene.open_pureref')
        col.prop(settings, 'load_on_load')
        col.prop(settings, 'pureref_file')

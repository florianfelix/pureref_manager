
from bpy.types import Panel


class SCENE_PT_pureref_management(Panel):
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "scene"

    bl_label = "PureRef Management"
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 110

    @classmethod
    def poll(cls, context):
        return True

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
            col.label(text='PureRef executable not set in Addon Preferences', icon='ERROR')

        col.operator('scene.open_pureref')
        col.prop(settings, 'load_on_load')
        col.prop(settings, 'pureref_file')
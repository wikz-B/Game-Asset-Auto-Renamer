bl_info = {
    "name": "Game Asset Auto Renamer",
    "author": "WikzB",
    "version": (1, 0),
    "blender": (3, 0, 0),
    "location": "View3D > Sidebar > Game Tools",
    "description": "Auto rename game assets with proper prefixes",
    "category": "Object",
}

import bpy

PREFIX_MAP = {
    'MESH': 'SM_',
    'ARMATURE': 'SK_',
    'EMPTY': 'EMP_',
    'CAMERA': 'CAM_',
    'LIGHT': 'LGT_',
}

class OBJECT_OT_game_auto_rename(bpy.types.Operator):
    bl_idname = "object.game_auto_rename"
    bl_label = "Auto Rename Assets"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        base_name = context.scene.game_asset_base_name
        index = 1

        for obj in context.selected_objects:
            prefix = PREFIX_MAP.get(obj.type, 'OBJ_')

            if "col" in obj.name.lower():
                prefix = "COL_"

            number = str(index).zfill(2)
            obj.name = f"{prefix}{base_name}_{number}"
            index += 1

        return {'FINISHED'}


class VIEW3D_PT_game_auto_rename_panel(bpy.types.Panel):
    bl_label = "Game Asset Renamer"
    bl_idname = "VIEW3D_PT_game_auto_rename_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Game Tools'

    def draw(self, context):
        layout = self.layout
        layout.prop(context.scene, "game_asset_base_name")
        layout.operator("object.game_auto_rename", icon="SORTALPHA")


def register():
    bpy.types.Scene.game_asset_base_name = bpy.props.StringProperty(
        name="Base Name",
        description="Base name for assets",
        default="Asset"
    )

    bpy.utils.register_class(OBJECT_OT_game_auto_rename)
    bpy.utils.register_class(VIEW3D_PT_game_auto_rename_panel)


def unregister():
    del bpy.types.Scene.game_asset_base_name
    bpy.utils.unregister_class(OBJECT_OT_game_auto_rename)
    bpy.utils.unregister_class(VIEW3D_PT_game_auto_rename_panel)


if __name__ == "__main__":
    register()

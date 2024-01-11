import bpy

class vt_PT_Panel(bpy.types.Panel):

    """Creates a Panel in the N-Panel of the 3D viewport"""
    bl_label = "Voronoi this mesh!"
    bl_idname = "OBJECT_PT_voronoiThis"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Voronoi This'

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        obj = context.object
        box = layout.box()
        box.scale_y = 4
        active_obj = context.view_layer.objects.active

        try:
            active_obj.modifiers['GeoNode']
            box.operator("object.undo_voronoi", text="UNDO")
        except:
            box.operator("object.apply_voronoi", text="ADD MODIFIER")
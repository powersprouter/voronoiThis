import bpy
from . vt_geonodes import voronoi_surface_node_group
from bpy.types import Context, Operator

class vt_OT_Create_Voronoi_Geonode_Operator(Operator):
    bl_idname = "object.create_voronoi_geonode"
    bl_label = "create geonode"
    bl_description = "Installs voronoi geonode group"
    
    def execute(self, context):
        voronoi_surface = voronoi_surface_node_group()

        return {"FINISHED"}


class vt_OT_Apply_Voronoi_Operator(Operator):
    bl_idname = "object.apply_voronoi"
    bl_label = "apply to voronoi object"
    bl_description = "Press to apply voronoi to active object"

    @classmethod
    def poll(cls, context):
        obj = context.object

        if obj is not None:
            if obj.mode == "OBJECT":
                if context.selected_objects:
                    if obj.type == "MESH":
                        return True
            
        return False
    
    def execute(self, context):

        active_obj = context.view_layer.objects.active

        try:
            bpy.data.node_groups['Voronoi Surface']
            print("voronoi already loaded")
        except:   
            bpy.ops.object.create_voronoi_geonode()
            print("voronoi now loaded")

        modifier = active_obj.modifiers.new("GeoNode", "NODES")
        bpy.ops.node.new_geometry_node_group_assign()
        bpy.data.node_groups.remove(modifier.node_group)
        modifier.node_group = bpy.data.node_groups['Voronoi Surface']
    



        return {"FINISHED"}
    
class vt_OT_Undo_Voronoi_Operator(Operator):
    bl_idname = "object.undo_voronoi"
    bl_label = "undo voronoi to object"
    bl_description = "Press to remove voronoi from active"

    @classmethod
    def poll(cls, context):
        obj = context.object

        if obj is not None:
            if obj.mode == "OBJECT":
                if context.selected_objects:
                    if obj.type == "MESH":                
                        return True
            
        return False
    
    def execute(self, context):
        active_obj = context.view_layer.objects.active
        bpy.ops.object.modifier_remove(modifier="GeoNode")


        return {"FINISHED"}

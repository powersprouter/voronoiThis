# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "voronoiThis",
    "author" : "powersprouter",
    "description" : "changes mesh object into voronoi version",
    "blender" : (3, 6, 0),
    "version" : (0, 0, 1),
    "location" : "View3D",
    "warning" : "",
    "category" : "Object"
}
import bpy
from . vt_ops import vt_OT_Apply_Voronoi_Operator, vt_OT_Undo_Voronoi_Operator, vt_OT_Create_Voronoi_Geonode_Operator
from . vt_panel import vt_PT_Panel


classes = (vt_OT_Apply_Voronoi_Operator, vt_OT_Undo_Voronoi_Operator, vt_PT_Panel, vt_OT_Create_Voronoi_Geonode_Operator)

def register():
    for c in classes:
        bpy.utils.register_class(c)

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)

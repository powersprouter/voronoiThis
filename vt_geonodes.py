import bpy
from bpy.types import Context, Operator

#initialize voronoi_surface node group
def voronoi_surface_node_group():
	voronoi_surface= bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Voronoi Surface")

	#initialize voronoi_surface nodes
	#node Frame.002
	frame_002 = voronoi_surface.nodes.new("NodeFrame")
	frame_002.label = "smooth"

	#node Frame.003
	frame_003 = voronoi_surface.nodes.new("NodeFrame")
	frame_003.label = "smooth"

	#node Frame.001
	frame_001 = voronoi_surface.nodes.new("NodeFrame")
	frame_001.label = "create voronoi pattern"

	#node Join Geometry
	join_geometry = voronoi_surface.nodes.new("GeometryNodeJoinGeometry")

	#node Extrude Mesh
	extrude_mesh = voronoi_surface.nodes.new("GeometryNodeExtrudeMesh")
	extrude_mesh.mode = 'FACES'
	#Selection
	extrude_mesh.inputs[1].default_value = True
	#Offset
	extrude_mesh.inputs[2].default_value = (0.0, 0.0, 0.0)
	#Offset Scale
	extrude_mesh.inputs[3].default_value = 0.029999999329447746
	#Individual
	extrude_mesh.inputs[4].default_value = False

	#node Flip Faces
	flip_faces = voronoi_surface.nodes.new("GeometryNodeFlipFaces")
	#Selection
	flip_faces.inputs[1].default_value = True

	#node Blur Attribute
	blur_attribute = voronoi_surface.nodes.new("GeometryNodeBlurAttribute")
	blur_attribute.data_type = 'FLOAT_VECTOR'
	#Value_Int
	blur_attribute.inputs[1].default_value = 0
	#Value_Color
	blur_attribute.inputs[3].default_value = (0.0, 0.0, 0.0, 0.0)
	#Iterations
	blur_attribute.inputs[4].default_value = 10
	#Weight
	blur_attribute.inputs[5].default_value = 1.0

	#node Position.001
	position_001 = voronoi_surface.nodes.new("GeometryNodeInputPosition")

	#node Set Position
	set_position = voronoi_surface.nodes.new("GeometryNodeSetPosition")
	#Selection
	set_position.inputs[1].default_value = True
	#Offset
	set_position.inputs[3].default_value = (0.0, 0.0, 0.0)

	#node Merge by Distance
	merge_by_distance = voronoi_surface.nodes.new("GeometryNodeMergeByDistance")
	merge_by_distance.mode = 'ALL'
	#Selection
	merge_by_distance.inputs[1].default_value = True
	#Distance
	merge_by_distance.inputs[2].default_value = 0.0010000000474974513

	#node Blur Attribute.001
	blur_attribute_001 = voronoi_surface.nodes.new("GeometryNodeBlurAttribute")
	blur_attribute_001.data_type = 'FLOAT_VECTOR'
	#Value_Int
	blur_attribute_001.inputs[1].default_value = 0
	#Value_Color
	blur_attribute_001.inputs[3].default_value = (0.0, 0.0, 0.0, 0.0)
	#Iterations
	blur_attribute_001.inputs[4].default_value = 7
	#Weight
	blur_attribute_001.inputs[5].default_value = 1.0

	#node Position.002
	position_002 = voronoi_surface.nodes.new("GeometryNodeInputPosition")

	#node Set Position.001
	set_position_001 = voronoi_surface.nodes.new("GeometryNodeSetPosition")
	#Selection
	set_position_001.inputs[1].default_value = True
	#Offset
	set_position_001.inputs[3].default_value = (0.0, 0.0, 0.0)

	#voronoi_surface outputs
	#output Geometry
	voronoi_surface.outputs.new('NodeSocketGeometry', "Geometry")
	voronoi_surface.outputs[0].attribute_domain = 'POINT'


	#node Group Output
	group_output = voronoi_surface.nodes.new("NodeGroupOutput")

	#node Set Shade Smooth
	set_shade_smooth = voronoi_surface.nodes.new("GeometryNodeSetShadeSmooth")
	#Selection
	set_shade_smooth.inputs[1].default_value = True
	#Shade Smooth
	set_shade_smooth.inputs[2].default_value = True

	#node Delete Geometry.001
	delete_geometry_001 = voronoi_surface.nodes.new("GeometryNodeDeleteGeometry")
	delete_geometry_001.domain = 'POINT'
	delete_geometry_001.mode = 'ALL'

	#node Voronoi Texture
	voronoi_texture = voronoi_surface.nodes.new("ShaderNodeTexVoronoi")
	voronoi_texture.voronoi_dimensions = '3D'
	voronoi_texture.feature = 'DISTANCE_TO_EDGE'
	voronoi_texture.distance = 'EUCLIDEAN'
	#Vector
	voronoi_texture.inputs[0].default_value = (0.0, 0.0, 0.0)
	#W
	voronoi_texture.inputs[1].default_value = 0.0
	#Smoothness
	voronoi_texture.inputs[3].default_value = 1.0
	#Exponent
	voronoi_texture.inputs[4].default_value = 0.5

	#node Math.001
	math_001 = voronoi_surface.nodes.new("ShaderNodeMath")
	math_001.operation = 'GREATER_THAN'
	#Value_002
	math_001.inputs[2].default_value = 0.5

	#node Subdivide Mesh
	subdivide_mesh = voronoi_surface.nodes.new("GeometryNodeSubdivideMesh")

	#voronoi_surface inputs
	#input Geometry
	voronoi_surface.inputs.new('NodeSocketGeometry', "Geometry")
	voronoi_surface.inputs[0].attribute_domain = 'POINT'

	#input Scale
	voronoi_surface.inputs.new('NodeSocketFloat', "Scale")
	voronoi_surface.inputs[1].default_value = 9.0
	voronoi_surface.inputs[1].min_value = 0.009999999776482582
	voronoi_surface.inputs[1].max_value = 100.0
	voronoi_surface.inputs[1].attribute_domain = 'POINT'

	#input Threshold
	voronoi_surface.inputs.new('NodeSocketFloat', "Threshold")
	voronoi_surface.inputs[2].default_value = 0.20000000298023224
	voronoi_surface.inputs[2].min_value = 0.0
	voronoi_surface.inputs[2].max_value = 10.0
	voronoi_surface.inputs[2].attribute_domain = 'POINT'

	#input Randomness
	voronoi_surface.inputs.new('NodeSocketFloatFactor', "Randomness")
	voronoi_surface.inputs[3].default_value = 1.0
	voronoi_surface.inputs[3].min_value = 0.0
	voronoi_surface.inputs[3].max_value = 1.0
	voronoi_surface.inputs[3].attribute_domain = 'POINT'

	#input SubDiv Level
	voronoi_surface.inputs.new('NodeSocketInt', "SubDiv Level")
	voronoi_surface.inputs[4].default_value = 8
	voronoi_surface.inputs[4].min_value = 0
	voronoi_surface.inputs[4].max_value = 10
	voronoi_surface.inputs[4].attribute_domain = 'POINT'


	#node Group Input
	group_input = voronoi_surface.nodes.new("NodeGroupInput")

	#Set parents
	blur_attribute.parent = frame_002
	position_001.parent = frame_002
	set_position.parent = frame_002
	blur_attribute_001.parent = frame_003
	position_002.parent = frame_003
	set_position_001.parent = frame_003
	delete_geometry_001.parent = frame_001
	voronoi_texture.parent = frame_001
	math_001.parent = frame_001

	#Set locations
	frame_002.location = (0.0, 0.0)
	frame_003.location = (1023.28515625, -113.66104125976562)
	frame_001.location = (0.0, 0.0)
	join_geometry.location = (1609.525146484375, 307.0888671875)
	extrude_mesh.location = (1402.150634765625, 156.93072509765625)
	flip_faces.location = (1375.5, 290.40460205078125)
	blur_attribute.location = (980.8716430664062, 164.03497314453125)
	position_001.location = (813.77392578125, 134.8182830810547)
	set_position.location = (1155.430419921875, 253.48175048828125)
	merge_by_distance.location = (1829.5, 292.4901428222656)
	blur_attribute_001.location = (980.8716430664062, 164.03497314453125)
	position_002.location = (813.77392578125, 134.8182830810547)
	set_position_001.location = (1256.430419921875, 253.48175048828125)
	group_output.location = (2719.498046875, 248.7440643310547)
	set_shade_smooth.location = (2499.5, 229.84994506835938)
	delete_geometry_001.location = (561.5, 351.4587707519531)
	voronoi_texture.location = (121.2535629272461, 538.5966186523438)
	math_001.location = (341.5, 455.728759765625)
	subdivide_mesh.location = (-122.50473022460938, 120.95755004882812)
	group_input.location = (-511.0431213378906, 117.22941589355469)

	#Set dimensions
	frame_002.width, frame_002.height = 544.5, 320.25
	frame_003.width, frame_003.height = 645.5, 319.25
	frame_001.width, frame_001.height = 643.0, 417.75
	join_geometry.width, join_geometry.height = 140.0, 100.0
	extrude_mesh.width, extrude_mesh.height = 140.0, 100.0
	flip_faces.width, flip_faces.height = 140.0, 100.0
	blur_attribute.width, blur_attribute.height = 140.0, 100.0
	position_001.width, position_001.height = 140.0, 100.0
	set_position.width, set_position.height = 140.0, 100.0
	merge_by_distance.width, merge_by_distance.height = 140.0, 100.0
	blur_attribute_001.width, blur_attribute_001.height = 140.0, 100.0
	position_002.width, position_002.height = 140.0, 100.0
	set_position_001.width, set_position_001.height = 140.0, 100.0
	group_output.width, group_output.height = 140.0, 100.0
	set_shade_smooth.width, set_shade_smooth.height = 140.0, 100.0
	delete_geometry_001.width, delete_geometry_001.height = 140.0, 100.0
	voronoi_texture.width, voronoi_texture.height = 140.0, 100.0
	math_001.width, math_001.height = 140.0, 100.0
	subdivide_mesh.width, subdivide_mesh.height = 140.0, 100.0
	group_input.width, group_input.height = 140.0, 100.0

	#initialize voronoi_surface links
	#math_001.Value -> delete_geometry_001.Selection
	voronoi_surface.links.new(math_001.outputs[0], delete_geometry_001.inputs[1])
	#voronoi_texture.Distance -> math_001.Value
	voronoi_surface.links.new(voronoi_texture.outputs[0], math_001.inputs[0])
	#delete_geometry_001.Geometry -> set_position.Geometry
	voronoi_surface.links.new(delete_geometry_001.outputs[0], set_position.inputs[0])
	#position_001.Position -> blur_attribute.Value
	voronoi_surface.links.new(position_001.outputs[0], blur_attribute.inputs[0])
	#position_001.Position -> blur_attribute.Value
	voronoi_surface.links.new(position_001.outputs[0], blur_attribute.inputs[2])
	#blur_attribute.Value -> set_position.Position
	voronoi_surface.links.new(blur_attribute.outputs[2], set_position.inputs[2])
	#set_position.Geometry -> extrude_mesh.Mesh
	voronoi_surface.links.new(set_position.outputs[0], extrude_mesh.inputs[0])
	#extrude_mesh.Mesh -> join_geometry.Geometry
	voronoi_surface.links.new(extrude_mesh.outputs[0], join_geometry.inputs[0])
	#flip_faces.Mesh -> join_geometry.Geometry
	voronoi_surface.links.new(flip_faces.outputs[0], join_geometry.inputs[0])
	#set_position.Geometry -> flip_faces.Mesh
	voronoi_surface.links.new(set_position.outputs[0], flip_faces.inputs[0])
	#join_geometry.Geometry -> merge_by_distance.Geometry
	voronoi_surface.links.new(join_geometry.outputs[0], merge_by_distance.inputs[0])
	#position_002.Position -> blur_attribute_001.Value
	voronoi_surface.links.new(position_002.outputs[0], blur_attribute_001.inputs[0])
	#position_002.Position -> blur_attribute_001.Value
	voronoi_surface.links.new(position_002.outputs[0], blur_attribute_001.inputs[2])
	#blur_attribute_001.Value -> set_position_001.Position
	voronoi_surface.links.new(blur_attribute_001.outputs[2], set_position_001.inputs[2])
	#set_shade_smooth.Geometry -> group_output.Geometry
	voronoi_surface.links.new(set_shade_smooth.outputs[0], group_output.inputs[0])
	#merge_by_distance.Geometry -> set_position_001.Geometry
	voronoi_surface.links.new(merge_by_distance.outputs[0], set_position_001.inputs[0])
	#set_position_001.Geometry -> set_shade_smooth.Geometry
	voronoi_surface.links.new(set_position_001.outputs[0], set_shade_smooth.inputs[0])
	#group_input.Geometry -> subdivide_mesh.Mesh
	voronoi_surface.links.new(group_input.outputs[0], subdivide_mesh.inputs[0])
	#subdivide_mesh.Mesh -> delete_geometry_001.Geometry
	voronoi_surface.links.new(subdivide_mesh.outputs[0], delete_geometry_001.inputs[0])
	#group_input.Scale -> voronoi_texture.Scale
	voronoi_surface.links.new(group_input.outputs[1], voronoi_texture.inputs[2])
	#group_input.Threshold -> math_001.Value
	voronoi_surface.links.new(group_input.outputs[2], math_001.inputs[1])
	#group_input.Randomness -> voronoi_texture.Randomness
	voronoi_surface.links.new(group_input.outputs[3], voronoi_texture.inputs[5])
	#group_input.SubDiv Level -> subdivide_mesh.Level
	voronoi_surface.links.new(group_input.outputs[4], subdivide_mesh.inputs[1])
	return voronoi_surface
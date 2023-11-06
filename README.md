# voronoiThis




This Blender add-on allows you to quickly add a preprogrammed geonode modifier to your mesh that will change it into a voronoi version. Just select your mesh and click APPLY in the 3D viewport side UI panel (the "N-panel").
(Technically speaking, the voronoi is not actually applied - it is sitting as a modifier in your modifier stack that can be undone - click UNDO to clear).

To install the add-on, download the zip, go to user Preferences>Add-ons and install & activate the zip file without unzipping. This add-on requires Blender version 3.6 or more recent.

When you apply a voronoi to your mesh, various key parametors are also shown as group inputs in the modifier. Just go to the modifer stack (the wrench) and you will see the node named "GeoNode" there.
Note that the default setting for subdivisions is at a level of 8. This works well with the default cube and other low poly meshes, but if you are wanting to voronoi something more complicated,
you may want to lower the subdiv level for better performance. Other key parameters are also able to be adjusted right in the GeoNode modifier.





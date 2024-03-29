# voronoiThis


<img width="1215" alt="vor3" src="https://github.com/powersprouter/voronoiThis/assets/96590051/8f476767-d5c9-4d02-a2a6-4533b5ed95d5">

This Blender add-on allows you to quickly add a preprogrammed geometry node to your mesh that will change it into a version that has a voronoi surface. Just select your mesh and click ADD MODIFIER in the 3D viewport side UI panel (the "N-panel").
(The voronoi is not applied - it is non-destructive, sitting as a modifier in your modifier stack that can be undone - click UNDO to clear. Be sure to APPLY the modifier if you want to use it in combination with an animation, otherwise your computer will get bogged down with so many data calculations).

To install the add-on, download the zip, go to user Preferences>Add-ons and install & activate the zip file without unzipping. This add-on requires Blender version 3.6 or more recent.

When you apply a voronoi to your mesh, various key parameters are also shown as group inputs in the modifier. Just go to modifier properties (the wrench) and you will see the node named "GeoNode" there.

Note that the default setting for subdivisions is at a level of 4. This works well with the default cube and other low poly meshes, but if you are wanting to voronoi something more complicated, you may want to lower the subdiv level for better performance, or adjust higher if you want more divisions. Really depends on the level of detail in your underlying mesh and the processing power available to you on your machine. There are other key parameters that are also able to be adjusted right in the GeoNode modifier, as well as in the Voronoi Surface nodegroup itself. Enjoy!

Volumetric voronoi and other parametric structural modifiers, including algorithmic optimizations for engineering constraints, are not difficult - am happy to work on this more if there is sufficient interest.

<img width="437" alt="vorThis1" src="https://github.com/powersprouter/voronoiThis/assets/96590051/f31077d0-48d8-46f6-a56e-012cf6b9dca2">
<img width="427" alt="vorThis2" src="https://github.com/powersprouter/voronoiThis/assets/96590051/d423496a-66b4-430c-83fd-fa76407239d3">
<img width="1235" alt="vor5" src="https://github.com/powersprouter/voronoiThis/assets/96590051/28ab66d9-3be2-4219-89d8-db6bce3c6427">
<img width="354" alt="vor4" src="https://github.com/powersprouter/voronoiThis/assets/96590051/d3a149e5-512a-4733-9452-340a69c02c0e">




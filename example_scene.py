import pypov

scene = pypov.Scene()

scene.elements.append(pypov.Include('colors.inc'))

cam = pypov.Camera()
cam.location = (0, 1, -1)
cam.look_at = (0, 0, 0)
scene.elements.append(cam)

light = pypov.LightSource((-1, 1, -1))
light.parallel = True
light.point_at = (0, 0, 0)
light.color = 'White'
scene.elements.append(light)

sphere = pypov.Sphere((0, 0, 0), 0.2)
sphere.pigment = pypov.Pigment()
sphere.pigment.color = 'Red'
scene.elements.append(sphere)

box = pypov.Box((0.3, 0, 0), (0.5, 0.2, 0.2))
box.pigment = pypov.Pigment()
box.pigment.color = 'Green'
scene.elements.append(box)

plane = pypov.Plane('y', 0)
plane.pigment = pypov.Pigment()
plane.pigment.color = 'Blue'
scene.elements.append(plane)

cylinder = pypov.Cylinder((-0.6, 0, 0), (-0.6, 0.2, 0), 0.2)
cylinder.pigment = pypov.Pigment()
cylinder.pigment.color = 'Yellow'
scene.elements.append(cylinder)

union = pypov.Union()
union.objects.append(pypov.Sphere((0, 0.5, 0), 0.2))
union.objects.append(pypov.Sphere((0.4, 0.5, 0), 0.2))
union.pigment = pypov.Pigment()
union.pigment.color = 'Cyan'
scene.elements.append(union)

print scene.toPovray()

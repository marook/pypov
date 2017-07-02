import pypov

scene = pypov.Scene()

scene.elements.append(pypov.Include('colors.inc'))

cam = pypov.Camera()
cam.location = (0, 1, -1)
cam.look_at = (0, 0, 0)
scene.elements.append(cam)

light = pypov.LightSource()
light.location = (-1, 1, -1)
light.color = 'White'
scene.elements.append(light)

sphere = pypov.Sphere((0, 0, 0), 0.2)
scene.elements.append(sphere)

print scene.toPovray()

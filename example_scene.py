import pypov

scene = pypov.Scene()

cam = pypov.Camera()
cam.location = pypov.V(0, 1, -1)
cam.look_at = pypov.V(0, 0, 0)
scene.elements.append(cam)

print scene.pov

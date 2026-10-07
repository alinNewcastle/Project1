from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor

class WalkingPanda(ShowBase):
    def __init__(self, no_rotate=False, scale=1.0, rotation_speed=6.0, camera_radius=20.0, camera_height=3.0, animation_speed=1.0, volume=0.3):
        ShowBase.__init__(self)

        self.music = self.loader.loadSfx("../sounds/music.ogg") # navigate to root directory, then sounds, and use music file
        self.music.setLoop(True)
        self.music.setVolume(volume)
        self.music.play()

        self.no_rotate = no_rotate
        self.rotation_speed = rotation_speed
        self.camera_radius = camera_radius
        self.camera_height = camera_height

        
        # Load the environment model.
        self.scene = self.loader.loadModel("models/environment")
        self.scene.reparentTo(self.render)
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)

        # Add the spinCameraTask procedure to the task manager.
        self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")

        # Load and transform the panda actor.
        self.pandaActor = Actor(
            "models/panda-model",
            {"walk": "models/panda-walk4"}
        )
        base_scale = 0.005
        self.pandaActor.setScale(base_scale * scale, base_scale * scale, base_scale * scale)
        self.pandaActor.reparentTo(self.render)
        # Loop its animation.
        self.pandaActor.setPlayRate(animation_speed, "walk")
        self.pandaActor.loop("walk")

    # Define a procedure to move the camera.
    def spinCameraTask(self, task):
        if self.no_rotate:
            angleDegrees = 0.0
        else:
            angleDegrees = task.time * self.rotation_speed

        angleRadians = angleDegrees * (pi / 180.0)

        self.camera.setPos(
            self.camera_radius * sin(angleRadians),
            -self.camera_radius * cos(angleRadians),
            self.camera_height,
        )
        self.camera.setHpr(angleDegrees, 0, 0)

        return Task.cont


app = WalkingPanda(
    no_rotate=False, 
    scale=2.0,
    rotation_speed=6.0,
    camera_radius=20.0, 
    camera_height=3.0, 
    animation_speed=1.0,
    volume=0.3
)
app.run()

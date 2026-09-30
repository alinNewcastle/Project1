import panda3d
from direct.showbase.ShowBase import ShowBase

class MyApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        #load environment model
        self.scene = self.loader.loadModel
        self.scene.reparentTo(self.render)
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)
app = MyApp()
app.run()

'''
    import sys
    import platform
    
    print("Hello World")
    
    print( 1, sys.version)
    print( 2, platform.python_implementation())
    print( 3, sys.executable)
    
    if sys.version_info[0] > 2:
        print("\n Good version!")
        sys.exit(1)
'''
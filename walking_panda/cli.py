from . import panda

import argparse

def cli():
    parser = argparse.ArgumentParser(prog="walking_panda")
    # stop rotating the camera around the panda
    parser.add_argument("--no-rotate",help="Suppress Rotation", action="store_true")
    # size of panda haha
    parser.add_argument("--scale", type=float, default=1.0, help="Modify size of panda")
    # camera orbit speed
    parser.add_argument("--rotation-speed", type=float, default=6.0, help="Camera orbit speed in degrees per second")
    # distance of camera from origin
    parser.add_argument("--camera-radius", type=float, default=20.0, help="Distance of the camera from the scene origin")
    # camera view height
    parser.add_argument("--camera-height", type=float, default=3.0, help="Camera height (Z position)")
    # speed of the walk animation
    parser.add_argument("--animation-speed", type=float, default=1.0, help="Walk animation playback rate")
    # music volume
    parser.add_argument("--volume", type=float, default=0.5, help="Background music volume")
    args = parser.parse_args()

    walking = panda.WalkingPanda(**vars(args))
    walking.run()
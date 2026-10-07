from . import panda

import argparse

def cli():
    parser = argparse.ArgumentParser(prog="walking_panda")
    parser.add_argument("--no-rotate",help="Suppress Rotation", action="store_true")
    parser.add_argument("--scale", type=float, default=1.0, help="Modify size of panda")
    parser.add_argument("--rotation-speed", type=float, default=6.0, help="Camera orbit speed in degrees per second")
    parser.add_argument("--camera-radius", type=float, default=20.0, help="Distance of the camera from the scene origin")
    parser.add_argument("--camera-height", type=float, default=3.0, help="Camera height (Z position)")
    parser.add_argument("--animation-speed", type=float, default=1.0, help="Walk animation playback rate")

    args = parser.parse_args()

    walking = panda.WalkingPanda(**vars(args))
    walking.run()
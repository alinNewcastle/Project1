Portfolio 1
===========

# Documentation for Project1: Walking Panda

## Overview

Project1 is a simple Python application built as part of the **CSC1034: Portfolio-1** module at Newcastle University. The package demonstrates a 3D animated scene featuring a "moonwalking panda" using the **Panda3D** game engine. It serves as an educational exercise for creating and controlling 3D actors and camera movement within a real-time rendering environment.

## Requirements

The project depends on the following Python package:

- **Panda3D** version `1.10.16` (as specified in `requirements.txt`).

Ensure you have Python 3.7 or later installed, as Panda3D 1.10.16 supports modern Python versions.

## Installation

1. **Clone the repository**:
   ```
   git clone https://github.com/alinNewcastle/Project1.git
   cd Project1
   ```

2. **Install the dependency**:
   ```
   pip install -r requirements.txt
   ```

   Alternatively, install Panda3D directly:
   ```
   pip install Panda3D==1.10.16
   ```

3. **(Recommended) Create a virtual environment** to isolate the package:
   ```
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

## Usage

Run the main script from the project root directory:

```
python ./walking_panda/panda.py
```

A window will open displaying a 3D environment with a panda model performing a walking animation. The camera automatically rotates around the scene, giving a dynamic view of the panda.

## Code Overview

### `walking_panda/panda.py`

This is the entry point of the application. It defines a class `WalkingPanda` that inherits from `ShowBase` (Panda3D's main application class). Key steps in the code:

1. **Initialize Panda3D**: `ShowBase.__init__(self)` sets up the engine.
2. **Store configuration**: The constructor accepts `no_rotate`, `scale`, `rotation_speed`, `camera_radius`, `camera_height`, and `animation_speed`, storing the ones needed later as instance attributes.
3. **Load environment**: Loads a built‑in environment model, scales it, and positions it in the scene.
4. **Load panda actor**: Loads the `panda-model` with an animation named `walk` (from `panda-walk4`). The actor is scaled by `base_scale * scale` and added to the render tree.
5. **Start animation**: Applies `setPlayRate(animation_speed, "walk")` and then calls `self.pandaActor.loop("walk")` to continuously play the walking animation at the requested speed.
6. **Camera control**: A task `spinCameraTask` is added to the task manager. The camera is always positioned using `camera_radius` and `camera_height`. When `no_rotate` is `False`, the orbit angle advances at `rotation_speed` degrees per second; when `True`, the angle is frozen at `0` so the camera holds a static view in front of the scene.
7. **Run the application**: Creates an instance of `WalkingPanda` and starts the main loop.

### `walking_panda/cli.py`

Provides an `argparse`‑based command‑line interface. The parsed arguments are passed straight into `WalkingPanda` via `vars(args)`, which is why the constructor parameter names use underscores (e.g. `--rotation-speed` becomes `rotation_speed`). If a parameter name doesn't match, Python raises a `TypeError`, so keeping the two in sync matters.

You can run:

```
python -m walking_panda.cli --help
```

to see the available arguments.

## Project Purpose

This project is an **educational exercise** for the CSC1034 module. It demonstrates:

- Loading and displaying 3D models using Panda3D.
- Playing skeletal animations on an actor.
- Controlling the camera programmatically.
- Structuring a small Python package with a clear entry point.

The code is intentionally minimal to focus on the core concepts of 3D scene composition and animation.

## License

The project is licensed under the terms described in the `LICENSE` file.
The code is intended primarily for academic assessment and feedback purposes. Please respect the license when reusing or redistributing the code.

## Contributing

As this is a personal academic project, external contributions are not expected. However, if you have suggestions or find issues, you can:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-idea`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-idea`).
5. Open a Pull Request.

## Contact

For questions or feedback related to this project, please contact me, via GitHub.

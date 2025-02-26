# Black Hole Gravitational Lensing Simulation

This project is a **ray tracing simulation of gravitational lensing** around a black hole. As the black hole's mass increases, the light bending effect intensifies, creating the illusion that the black hole is approaching the observer. The simulation applies **general relativistic lensing** to an image of space, distorting it based on the Schwarzschild metric.

## 🌌 Gravitational Lensing and Ray Tracing
Gravitational lensing is a phenomenon predicted by **Einstein's General Relativity** where massive objects, like black holes, bend the path of light passing near them. This effect can create distorted, magnified, or even multiple images of background objects.

In this simulation, we use **ray tracing techniques** to compute how light paths are deflected by the gravitational field of an increasing-mass black hole. By applying the lensing equation to an image, we simulate how the background would appear if viewed near such a strong gravitational field.

## 🖥️ Simulation Overview
The simulation follows these key steps:
1. **Load a background image** representing distant stars.
2. **Define gravitational lensing equations** to compute the deflection angle of light due to the black hole.
3. **Apply ray tracing to each pixel**, mapping how light would be distorted due to the black hole’s gravitational field.
4. **Increase the black hole's mass over time**, which makes the gravitational bending stronger, creating the impression that the black hole is moving closer.
5. **Animate the effect** to visualize the evolving lensing distortions.

## 📜 Mathematical Model
The deflection angle \( \alpha \) for light passing near a Schwarzschild black hole is given by:

$\alpha = \frac{4 G M}{c^2 r}$

where:
- $G$ is the gravitational constant,
- $M$ is the black hole’s mass,
- $c$ is the speed of light,
- $r$ is the distance from the black hole.

The apparent position of the background light source is computed using:

$\beta = \theta - \alpha \frac{D_s - D_l}{D_s}$

where:
- $\theta$ is the observed angle,
- $D_s$ and $D_l$ are the distances to the source and the lens, respectively.

## 📽️ Running the Simulation
### Requirements
Make sure you have Python installed with the following dependencies:
```bash
pip install numpy matplotlib scipy ffmpeg
```

### Running the Code
1. Clone the repository:
   ```bash
   git clone https://github.com/HugoGW/Black-Hole-Simulation/black-hole-mass.git
   cd black-hole-mass
   ```
2. Run the script:
   ```bash
   python black-hole-mass.py
   ```

The simulation will generate an animation showing the increasing distortion effect as the black hole's mass grows.

## 📂 File Structure
```
📂 black-hole-mass
 ├── black-hole-mass.py  # Main simulation script
 ├── space_background_2.jpg   # Background image (replace with your own)
 ├── README.md              # This documentation
 ├── black_hole_mass.mp4             # Generated animation (if saved)
```

## 🎥 Output
The animation depicts the **gravitational lensing effect** increasing over time. As the black hole's mass grows, light is bent more dramatically, causing stronger distortions.

<p align="center">
  <img src="example.gif" alt="Black hole lensing simulation">
</p>




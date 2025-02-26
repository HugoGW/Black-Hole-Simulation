# Black Hole Ray Tracing Simulation

This project simulates **gravitational lensing** around a black hole using **ray tracing** techniques. The simulation creates a dynamic visualization where the mass of the black hole increases over time, giving the illusion that it is getting closer. The final result is saved as `BH_pic.jpg`, while the background image `space_background_3.jpg` is required for accurate visualization.

## Gravitational Lensing & Ray Tracing

Gravitational lensing is a phenomenon predicted by Einstein's General Relativity, where massive objects like black holes bend light passing near them. This effect alters the apparent position and shape of background stars and galaxies.

To simulate this, we use **ray tracing**, which involves calculating the deflection of light rays due to the gravitational field of the black hole. The amount of bending is given by:

$\alpha = \frac{4GM}{c^2 r}$

where:
- $G$ is the gravitational constant,
- $M$ is the mass of the black hole,
- $c$ is the speed of light,
- $r$ is the distance from the black hole.

### Increasing Mass Effect

As the simulation progresses, the mass of the black hole increases, which amplifies the lensing effect. This gives the illusion that the black hole is moving closer to the observer, distorting more of the background image over time.

## Background Image & Output Result

- **Required Background**: `space_background_3.jpg`
  - This image represents deep space and is essential for visualizing the lensing effect.
  - As light rays bend around the black hole, the stars and celestial objects in the image appear distorted.

- **Final Result**: `BH_pic.jpg`
  - The simulation generates this image as the final visualization of the gravitational lensing effect.

## Running the Simulation

1. Clone this repository.
2. Place `space_background_3.jpg` in the project directory.
3. Run the script in Python:
   ```bash
   python black_hole_pic.py
   ```
4. The final image `BH_pic.jpg` will be generated, showing the gravitational lensing effect around the black hole.

## Dependencies

- Python 3.x
- NumPy
- Matplotlib
- SciPy

## Output

The simulation generates an image where the black hole grows in mass, progressively distorting the background image. The final visualization (`BH_pic.jpg`) exhibits a strong gravitational lensing effect with an event horizon region appearing completely black due to light capture. ![Gravitational Lensing](BH_pic.jpg)




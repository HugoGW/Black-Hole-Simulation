# Black Hole Gravitational Lensing Simulation  

This project simulates **gravitational lensing** caused by a black hole, demonstrating how its intense gravity distorts light from a background image. Using **ray tracing** techniques, it applies Einstein's General Relativity principles to create realistic visual effects.  

## Code Structure  
- **`black-hole-image/`**: Contains code that generates a still image of a black hole, illustrating gravitational lensing effects.  
- **`black-hole-mass/`**: Simulates a black hole with increasing mass over time, creating the illusion that the observer is moving closer to it.  
- **`black-hole-position/`**: Simulates a moving black hole, showing how gravitational lensing dynamically changes as its position shifts.  

## How It Works  
- A space background image is loaded.  
- The Schwarzschild metric and the deflection formula:  
  $\alpha = \frac{4GM}{c^2 r}$  
  are used to compute light bending.  
- The distorted light paths are mapped to a new image using `scipy.ndimage.map_coordinates`.  

## Requirements  
- Python 3.x  
- NumPy, Matplotlib, SciPy  
- FFmpeg (for animations, if needed)  

## Installation  
```sh
pip install numpy matplotlib scipy  
```  

## Usage  
1. Clone the repository:  
```sh
git clone https://github.com/HugoGW/Black-Hole-Simulation.git  
cd Black-Hole-Simulation  
```  
2. Add a background image (`space_background.jpg`, `space_background_2.jpg` or `space_background_3.jpg`).  
3. Run the script in the desired directory.  

## Author  
Created by **Hugo Alexandre** (@HugoGW). Feel free to contribute or reach out for improvements!  

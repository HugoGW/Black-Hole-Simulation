import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import map_coordinates

# Physical constants
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
c = 299792458    # Speed of light (m/s)
M_sun = 1.898e30  # Mass of the Sun (kg)
M = 0.3 * M_sun  # Mass of the black hole (adjustable)
rs = 2 * G * M / c**2  # Schwarzschild radius (m)

# Load background image
image_path = "Your_Path/space_background_3.jpg"  # Update with your actual path
image = plt.imread(image_path)  # Load image (RGB format)

# Distances and scaling
D_lens = 1e06  # Distance to the gravitational lens (black hole) (m)
D_source = 1.001e06  # Distance to the background source (m)
scale = 0.0000118  # Angular scale (radians per pixel)

def beta(theta):
    """
    Compute the image angle β as a function of the incident angle θ using gravitational lensing.
    """
    r = np.maximum(theta * D_lens, 1e-40)  # Distance from the black hole, avoid division by zero
    alpha = 4 * G * M / (c**2 * r)  # Deflection angle due to gravitational lensing
    
    return theta - alpha * (D_source - D_lens) / D_source  # Corrected angle accounting for distances

def raytrace_RGB(channel):
    """
    Apply ray tracing on a given RGB image channel to simulate gravitational lensing.
    """
    height, width = channel.shape
    y, x = np.meshgrid(np.arange(height), np.arange(width), indexing='ij')  # Image grid
    
    # Convert pixel coordinates to angular coordinates
    theta_x, theta_y = (x - width // 2) * scale, (y - height // 2) * scale
    theta = np.hypot(theta_x, theta_y)  # Radial angle from the center
    
    # Compute gravitationally lensed angle β
    beta_angle = beta(theta)
    
    # Identify valid pixels and those inside the Schwarzschild radius (captured by the black hole)
    valid = theta > 1e-20
    schwarzschild = theta * D_lens < rs  # Check if inside the event horizon
    
    # Project β back onto x and y coordinates while avoiding division by zero
    beta_x = np.where(valid, beta_angle * np.divide(theta_x, theta, where=valid), 0)
    beta_y = np.where(valid, beta_angle * np.divide(theta_y, theta, where=valid), 0)
    
    # Convert back to pixel coordinates
    Pix_beta_x = np.clip(beta_x / scale + width // 2, 0, width - 1)
    Pix_beta_y = np.clip(beta_y / scale + height // 2, 0, height - 1)
    
    # Apply coordinate transformation to deform the image
    deformed_channel = map_coordinates(channel, [Pix_beta_y.ravel(), Pix_beta_x.ravel()], order=1, mode='wrap').reshape(height, width)
    
    # Darken pixels that fall within the Schwarzschild radius (event horizon)
    deformed_channel[schwarzschild] = 0
    
    return deformed_channel

def raytrace_image():
    """
    Apply gravitational lensing ray tracing to all three RGB channels.
    """
    return np.stack([raytrace_RGB(image[..., i]) for i in range(3)], axis=-1)

# Generate the gravitationally lensed image
deformed_image = raytrace_image()

# Display the result
plt.imshow(deformed_image)
plt.axis('off')  # Hide axes for a cleaner visualization
plt.title('Gravitational Lensing by a Black Hole')
plt.show()

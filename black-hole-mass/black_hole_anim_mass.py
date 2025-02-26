import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.ndimage import map_coordinates

# Physical constants
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
c = 299792458    # Speed of light (m/s)
M_sun = 1.898e30  # Solar mass (kg)
M_initial = 0.01 * M_sun  # Initial mass of the black hole (10% of the Sun's mass)

# Load background image
image_path = r'Your_Path/space_background_2.jpg'  # Path to the background image
image = plt.imread(image_path)  # Load color image

# Distances and scaling
D_lens = 1e06  # Distance to the lensing object (in meters)
D_source = 1.001e06  # Distance to the light source (in meters)
scale = 0.0000118  # Scale factor (radians per pixel)

def beta(theta, M):
    """
    Computes the image angle beta as a function of the incident angle theta and mass M.
    """
    rs = 2 * G * M / c**2  # Schwarzschild radius
    r = np.maximum(theta * D_lens, 1e-40)  # Distance from the lensing object
    alpha = 4 * G * M / (c**2 * r)  # Gravitational deflection angle
    
    return theta - alpha * (D_source - D_lens) / D_source

def raytrace_RGB(channel, M):
    """
    Applies ray tracing to a given image channel based on gravitational lensing.
    """
    rs = 2 * G * M / c**2  # Update Schwarzschild radius
    height, width = channel.shape
    y, x = np.meshgrid(np.arange(height), np.arange(width), indexing='ij')  # Image grid coordinates
    
    x_center = width // 2
    y_center = height // 2
    
    # Convert to angular coordinates
    theta_x, theta_y = (x - x_center) * scale, (y - y_center) * scale
    theta = np.hypot(theta_x, theta_y)  # Angular distance from the center
    
    # Compute deformed beta angle
    beta_angle = beta(theta, M)
    
    # Identify valid pixels and those captured by the black hole
    valid = theta > 1e-20
    schwarzschild = theta * D_lens < rs  # Pixels falling inside the event horizon
    
    # Projection on axes, avoiding division by zero
    beta_x = np.where(valid, beta_angle * np.divide(theta_x, theta, where=valid), 0)
    beta_y = np.where(valid, beta_angle * np.divide(theta_y, theta, where=valid), 0)
    
    # Convert back to pixel coordinates
    beta_x_pix = np.clip(beta_x / scale + width // 2, 0, width - 1)
    beta_y_pix = np.clip(beta_y / scale + height // 2, 0, height - 1)
    
    # Apply transformation to the channel
    deformed_channel = map_coordinates(channel, [beta_y_pix.ravel(), beta_x_pix.ravel()], order=1, mode='wrap').reshape(height, width)
    
    # Darken pixels that fall inside the black hole
    deformed_channel[schwarzschild] = 0
    
    return deformed_channel

def update(frame):
    """
    Updates the image for each frame of the animation by increasing the black hole's mass.
    """
    M = M_initial * (1 + 0.2 * frame)  # Mass increases by 2% per frame
    
    deformed_red = raytrace_RGB(image[:, :, 0], M)
    deformed_green = raytrace_RGB(image[:, :, 1], M)
    deformed_blue = raytrace_RGB(image[:, :, 2], M)
    
    deformed_image = np.stack([deformed_red, deformed_green, deformed_blue], axis=-1)
    im.set_array(deformed_image)
    return [im]

# Initialize animation
fig, ax = plt.subplots()
im = ax.imshow(image)
ax.axis('off')  # Hide axes
ani = animation.FuncAnimation(fig, update, frames=200, interval=1, blit=True)

# Output path
output_path = r'Your_Path/black_hole_mass.mp4'  # Path to save animation

# Save the animation as an MP4 file
ani.save(output_path, writer='ffmpeg', fps=30)
plt.show()

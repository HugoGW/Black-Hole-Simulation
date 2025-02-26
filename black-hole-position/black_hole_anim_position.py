import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.ndimage import map_coordinates

# Physical constants
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
c = 299792458    # Speed of light (m/s)
M_sun = 1.898e30  # Solar mass (kg)
M = 0.3 * M_sun  # Mass of the black hole (kg)
rs = 2 * G * M / c**2  # Schwarzschild radius (m)

# Load background image
image_path = r'Your_Path/space_background.jpg'  # Replace with your actual path
image = plt.imread(image_path)  # Load the image (assumed to be in color)

# Distances and scale
D_lens = 1e06  # Distance to the lensing object (arbitrary units)
D_source = 1.001e06  # Distance to the background source (arbitrary units)
scale = 0.0000118  # Radians per pixel (angular scale of the image)

# Get image dimensions
height, width, _ = image.shape

def beta(theta):
    """
    Computes the source angle β as a function of the observed angle θ,
    taking into account gravitational lensing.
    """
    r = np.maximum(theta * D_lens, 1e-40)  # Ensure r is nonzero to avoid division errors
    alpha = 4 * G * M / (c**2 * r)  # Gravitational deflection angle
    return theta - alpha * (D_source - D_lens) / D_source  # Compute the lensed position

def raytrace_RGB(channel, center_x):
    """
    Applies gravitational lensing (ray tracing) to a single RGB channel.
    """
    y, x = np.meshgrid(np.arange(height), np.arange(width), indexing='ij')  # Generate coordinate grid
    center_y = height // 2  # Center of the black hole along the y-axis
    
    # Compute angular positions relative to the black hole center
    theta_x, theta_y = (x - center_x) * scale, (y - center_y) * scale
    theta = np.hypot(theta_x, theta_y)  # Compute radial distance in angular space

    # Compute the deflected angle β due to gravitational lensing
    beta_vals = beta(theta)
    valid = theta > 1e-20  # Avoid division by zero
    schwarzschild = theta * D_lens < rs  # Pixels where light is captured by the black hole

    # Compute β components in x and y directions
    beta_x = np.where(valid, beta_vals * np.divide(theta_x, theta, where=valid), 0)
    beta_y = np.where(valid, beta_vals * np.divide(theta_y, theta, where=valid), 0)

    # Convert β to pixel coordinates
    Pix_beta_x = np.clip(beta_x / scale + center_x, 0, width - 1)
    Pix_beta_y = np.clip(beta_y / scale + center_y, 0, height - 1)

    # Apply the coordinate transformation to the image channel
    deformed_channel = map_coordinates(channel, [Pix_beta_y.ravel(), Pix_beta_x.ravel()], order=1, mode='wrap').reshape(height, width)
    
    # Set pixels inside the event horizon to black
    deformed_channel[schwarzschild] = 0
    return deformed_channel

def raytrace_image(center_x):
    """
    Applies gravitational lensing to all three RGB channels.
    """
    return np.stack([raytrace_RGB(image[..., i], center_x) for i in range(3)], axis=-1)

# Create the figure
fig, ax = plt.subplots()
img_display = ax.imshow(image)
ax.axis('off')  # Hide axes for better visualization

# Animation parameters
start_x = width // 10  # Initial position of the black hole (left side)
end_x = width * 10 // 10  # Final position of the black hole (right side)
n_frames = 200  # Number of frames in the animation

def update(frame):
    """
    Updates the animation frame by moving the black hole across the image.
    """
    center_x = start_x + frame * (end_x - start_x) // n_frames  # Compute new black hole position
    deformed_image = raytrace_image(center_x)  # Apply lensing effect
    img_display.set_array(deformed_image)  # Update displayed image
    return img_display,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=n_frames, interval=1, blit=True)

# Save animation as an MP4 file
output_path = r'Your_Path/black_hole_pos.mp4'  # Replace with your actual path
ani.save(output_path, writer='ffmpeg', fps=30)

plt.show()

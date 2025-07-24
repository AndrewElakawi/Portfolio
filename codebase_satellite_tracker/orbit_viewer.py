import numpy as np
import matplotlib.pyplot as plt

#Example values. Currently using hard values for ISS orbit (replace with actual satellite data)

inclination_deg = 51.6
raan_deg = 0
radius = 6771 # in km (approximate radius of Earth + ISS altitude)

# Convert angles to radians

incl = np.deg2rad(inclination_deg)
raan = np.deg2rad(raan_deg)

# Generate points for a circle in the orbital plane

theta = np.linespace(0, 2 * np.pi, 200)
x = radius * np.cos(theta)
y = radius * np.sin(theta)
z = np.zeros_like(theta)


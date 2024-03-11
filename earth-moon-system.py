import matplotlib.pyplot as plt

# Settings
earth_radius_km = 6371
moon_radius_km = 1737
earth_moon_distance_km = 384400
barycenter_distance_from_earth_center_km = 4671

# Scale factors for visualization
scale_factor_earth = 2  # To keep Earth visible but not to scale
scale_factor_moon = 2  # To exaggerate the Moon's size for visibility
scale_factor_barycenter = 10  # To exaggerate the barycenter's location for visibility

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 8))

# Tidal bulges
tidal_bulge_1 = plt.Circle((-barycenter_distance_from_earth_center_km * scale_factor_earth, 0),
                           earth_radius_km * scale_factor_earth, color='cyan', alpha=0.2, label='Tidal bulge')
tidal_bulge_2 = plt.Circle((barycenter_distance_from_earth_center_km * scale_factor_earth, 0),
                           earth_radius_km * scale_factor_earth, color='cyan', alpha=0.2)
ax.add_artist(tidal_bulge_1)
ax.add_artist(tidal_bulge_2)

# Earth
earth = plt.Circle((0, 0), earth_radius_km * scale_factor_earth, color='blue', alpha=0.3, label='Earth')
ax.add_artist(earth)

# Moon
moon = plt.Circle((earth_moon_distance_km, 0), moon_radius_km * scale_factor_moon, color='gray', alpha=0.5,
                  label='Moon')
ax.add_artist(moon)

# Indicate the barycenter with a red dot, inside the Earth but not at its center
barycenter = plt.Circle((barycenter_distance_from_earth_center_km, 0), 100 * scale_factor_barycenter, color='red',
                        alpha=0.7, label='Barycenter')
ax.add_artist(barycenter)

# Adjust the plot
ax.set_aspect('equal')
ax.set_xlim(-2 * earth_radius_km - barycenter_distance_from_earth_center_km,
            earth_moon_distance_km + scale_factor_moon * moon_radius_km + 50 + earth_radius_km)
ax.set_ylim(-10000 * scale_factor_earth, 10000 * scale_factor_earth)
# plt.axis('off')
plt.legend()
plt.savefig('earth-moon.png', format='png', transparent=True)

plt.show()

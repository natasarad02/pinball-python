import matplotlib.pyplot as plt

def linear_motion_euler(m, F, x0, v0, dt, num_steps):
    # Initialize arrays to store position and velocity values
    positions = [x0]
    velocities = [v0]

    # Euler's method loop
    for _ in range(num_steps):
        # Calculate acceleration using Newton's second law
        acceleration = F / m

        # Update velocity and position using Euler's method
        v_new = velocities[-1] + acceleration * dt
        x_new = positions[-1] + v_new * dt

        # Append the new values to the arrays
        velocities.append(v_new)
        positions.append(x_new)

    return positions, velocities

# Parameters
mass = 1.0  # Mass of the object
net_force = 10.0  # Net force acting on the object
initial_position = 0.0  # Initial position
initial_velocity = 0.0  # Initial velocity
time_step = 0.1  # Time step for Euler's method
num_steps = 100  # Number of steps

# Solve the ODE using Euler's method
positions, velocities = linear_motion_euler(mass, net_force, initial_position, initial_velocity, time_step, num_steps)

# Plot the results
time_values = [i * time_step for i in range(num_steps + 1)]

plt.plot(time_values, positions, label='Position')
plt.plot(time_values, velocities, label='Velocity')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.title('Linear Motion ODE Solution using Euler\'s Method')
plt.show()

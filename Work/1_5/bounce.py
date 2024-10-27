# bounce.py
#
# Exercise 1.5
# Constants
INITIAL_HEIGHT = 100
BOUNCE_FACTOR = 0.6
TOTAL_BOUNCES = 10

# Variables
height = INITIAL_HEIGHT
bounce = 0

# Simulation loop
while bounce < TOTAL_BOUNCES:
    bounce += 1
    height *= BOUNCE_FACTOR
    print(f'{bounce:<4} {height:>8.3f}')
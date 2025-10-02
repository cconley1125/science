# Projectile Motion Lab Calculator
# Created by Chris Conley with assistance from ChatGPT (October 2025)

import math
import time

def run_projectile_lab():
    while True:
        print("\n--- Vernier Projectile Motion Lab ---\n")

        # Step 1: Average velocity from trials
        n = int(input("How many test trials will be used to calculate average velocity? "))
        velocities = []
        for i in range(1, n + 1):
            v = float(input(f"Enter velocity for trial {i} (m/s): "))
            velocities.append(v)
        v0 = sum(velocities) / len(velocities)
        print(f"\nAverage initial velocity: {v0:.3f} m/s\n")

        # Step 2: Starting height
        bench_height = float(input("Enter the height from LabQuest to floor (cm): "))
        start_height_cm = bench_height + 14.6
        start_height_m = start_height_cm / 100
        print(f"Starting height: {start_height_cm:.2f} cm ({start_height_m:.3f} m)\n")

        # Step 3: Horizontal offset
        offset_cm = float(input("Enter horizontal offset of launcher from edge (cm): "))
        offset_m = offset_cm / 100
        print(f"Horizontal offset: {offset_cm:.2f} cm ({offset_m:.3f} m)\n")

        # Step 4: Launch angle
        angle_deg = float(input("Enter the launch angle (degrees): "))
        angle_rad = math.radians(angle_deg)
        print(f"Launch angle: {angle_deg:.2f}°\n")

        # Step 5: Break velocity into components
        v0x = v0 * math.cos(angle_rad)
        v0y = v0 * math.sin(angle_rad)
        g = 9.8

        # Calculations
        # Time to max height
        t_up = v0y / g

        # Max height above floor
        max_height_m = start_height_m + (v0y**2) / (2 * g)
        max_height_cm = max_height_m * 100

        # Total flight time: solve y(t) = 0 (floor level)
        a = -0.5 * g
        b = v0y
        c = start_height_m
        disc = b**2 - 4*a*c
        if disc < 0:
            t_total = 0
        else:
            t1 = (-b + math.sqrt(disc)) / (2*a)
            t2 = (-b - math.sqrt(disc)) / (2*a)
            t_total = max(t1, t2)

        # Range
        range_m = v0x * t_total
        range_cm = range_m * 100

        # Distance from bench edge
        distance_from_edge_m = range_m - offset_m
        distance_from_edge_cm = distance_from_edge_m * 100

        # Final vertical velocity
        vy_final = v0y - g * t_total

        # Final total velocity
        v_final = math.sqrt(v0x**2 + vy_final**2)
        angle_final = math.degrees(math.atan2(abs(vy_final), v0x))  # below horizontal

        # Final Results
        print("\n--- Results ---\n")
        print(f"Average initial velocity: {v0:.3f} m/s")
        print(f"Starting height: {start_height_cm:.2f} cm ({start_height_m:.3f} m)")
        print(f"Maximum height: {max_height_cm:.2f} cm ({max_height_m:.3f} m)")
        print(f"Time to max height: {t_up:.3f} s")
        print(f"Total flight time: {t_total:.3f} s")
        print(f"Total range: {range_cm:.2f} cm ({range_m:.3f} m)")
        print(f"Distance from bench edge: {distance_from_edge_cm:.2f} cm ({distance_from_edge_m:.3f} m)")
        print(f"Final velocity: {v_final:.3f} m/s at {angle_final:.2f}° below horizontal\n")

        again = input("Do you want to input another set of data? (y/n): ").strip().lower()
        if again != 'y':
            print("\nThank you for your love of physics, and especially the mechanics of projectile motion.")
            print("Have a wonderful day!\n")
            time.sleep(2)  # brief pause before ending
            break

# Run the lab calculations
run_projectile_lab()

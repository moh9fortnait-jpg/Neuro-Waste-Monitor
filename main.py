# Project 10: Neuro-Waste Monitor
# A utility to visualize and reduce household resource waste

def calculate_waste(liters_per_min, minutes_active, days=365):
    total_waste = liters_per_min * minutes_active * days
    # Logic: 1000 liters = 1 cubic meter
    cubic_meters = total_waste / 1000
    return total_waste, cubic_meters

def main():
    print("--- Neuro-Waste Monitor v1.0 ---")
    print("Visualize your environmental footprint.")
    
    try:
        print("\nExample: A leaking tap or a long shower.")
        rate = float(input("Estimated waste rate (Liters per minute): "))
        duration = float(input("Average duration of use per day (Minutes): "))
        
        daily_l, yearly_l = calculate_waste(rate, duration, 1) # Daily
        total_l, total_m3 = calculate_waste(rate, duration)    # Yearly
        
        print("\n--- Impact Report ---")
        print(f"Daily Waste   : {daily_l:.2f} Liters")
        print(f"Yearly Waste  : {total_l:,} Liters")
        print(f"Volume in M3  : {total_m3:.2f} m³")
        
        # Innovation: Actionable Logic
        if total_m3 > 50:
            print("Status: [Critical] This waste could fill a small swimming pool!")
        else:
            print("Status: [Noticeable] Every drop counts toward a better future.")
            
    except ValueError:
        print("Error: Please enter valid numerical data.")

if __name__ == "__main__":
    main()
def calculate_nrr(total_runs_scored, total_runs_conceded, match_type):
    if match_type == 'ODI':
        entitled_overs = 50  
    elif match_type in ['T20', 'T20I']:
        entitled_overs = 20 
    else:
        return "Invalid match type. Please choose 'ODI', 'T20', or 'T20I'."
    
    nrr = (total_runs_scored / entitled_overs) - (total_runs_conceded / entitled_overs)
    return round(nrr, 2)

def main():
    print("Welcome to NRR Calculator!")
    match_type = input("Enter match type (ODI, T20, or T20I): ").strip().upper()

    if match_type not in ['ODI', 'T20', 'T20I']:
        print("Invalid match type. Please enter 'ODI', 'T20', or 'T20I':")
        return

    total_runs_scored = float(input("Enter the total runs scored by the team: "))
    total_runs_conceded = float(input("Enter the total runs conceded by the team: "))

    nrr = calculate_nrr(total_runs_scored, total_runs_conceded, match_type)
    
    print(f"Net Run Rate for {match_type} match: {nrr}")

if __name__ == "__main__":
    main()

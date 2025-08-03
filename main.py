def main():
    # Individual Person Expenses (Summing up direct spends)
    MukeshSpent = 20500 + 600 + 350 + 2100           # Mukesh's individual expenses
    SubitshaSpent = 2000 + 600                       # Subitsha's individual expenses
    BhaveshSpent = 1205 + 700                        # Bhavesh's individual expenses (Snacks split with Priyesh)
    PriyeshSpent = 1800                              # Priyesh's individual expenses (split amongst Subitsha, Vasavi, Vansi)

    # Total Expenses Calculation
    Total_Money_Spent = MukeshSpent + SubitshaSpent + BhaveshSpent + PriyeshSpent
    print(f"Total Expenses : {Total_Money_Spent}")

    # Calculate shared expenses (per head splits)
    Resort = (20000 - 10000) / 8                     # Resort charge distributed among 8
    Beer = 2100 / 3                                  # Beer shared among 3
    Snacks = (600 + 700) / 9                         # Snacks shared among 9
    Whisky = 1205 / 2                                # Whisky shared among 2
    CabPlus = 600 / 6                                # Cab Plus shared among 6
    CabMinus = 350 / 5                               # Cab Minus shared among 5
    Vodka = 1800 / 3                                 # Vodka shared among 3

    # Calculation for each person, summing up all shared costs for that individual
    Mukesh = Resort + Beer + Snacks + CabPlus + CabMinus
    Goutham = Resort + Snacks + CabPlus + CabMinus
    Vasavi = Resort + Vodka + CabMinus + CabPlus
    Sunil = Resort + Snacks + CabPlus
    Vansi = Resort + Snacks + CabPlus + CabMinus + Vodka
    Bhavesh = Resort + Snacks + Beer + Whisky + 2500   # 2500
    Priyesh = Resort + Snacks + Beer + Whisky
    Subitsha = Resort + Snacks + Vodka + CabMinus + CabPlus

    # Store persons and their expenses in a dictionary for check
    persons = {
        'Mukesh': Mukesh,
        'Goutham': Goutham,
        'Vasavi': Vasavi,
        'Sunil': Sunil,
        'Vansi': Vansi,
        'Bhavesh': Bhavesh,
        'Priyesh': Priyesh,
        'Subitsha': Subitsha
    }

    # Print individual cost breakdowns
    for name, total in persons.items():
        print(f"{name}: {round(total)}")


    # Calculate how much each person needs to get back or pay
    MukeshShare = Mukesh - MukeshSpent
    SubitshaShare = Subitsha - SubitshaSpent
    BhaveshShare = Bhavesh - BhaveshSpent
    PriyeshShare = Priyesh - PriyeshSpent

    print()
    print(f"MukeshShare: {round(MukeshShare)}")
    print(f"SubitshaShare: {round(SubitshaShare)}")
    print(f"BhaveshShare: {round(BhaveshShare)}")
    print(f"PriyeshShare: {round(PriyeshShare)}")


if __name__ == "__main__":
    main()

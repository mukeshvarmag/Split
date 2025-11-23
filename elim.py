def main():
    # Individual Person Expenses (Summing up direct spends)
    MukeshSpent = 25200  + 1000    + 5400     # Resort + snacks

    BhaveshSpent = 780             # Beer

    AdityaSpent = 800

    # Total Expenses Calculation
    Total_Money_Spent = MukeshSpent + AdityaSpent + BhaveshSpent
    print(f"Total Expenses : {Total_Money_Spent}")

    # Calculate shared expenses (per head splits)
    Resort = (25200) / 9
    Beer = 780 / 3
    Snacks = (1000 + 800) / 9
    Whisky = 5400 / 5
    Indri = 3000


    # Calculation for each person, summing up all shared costs for that individual
    Mukesh = Resort + Snacks + Whisky
    Goutham = Resort + Snacks
    Vasavi = Resort + Snacks
    Sunil = Resort + Snacks

    Priyesh = Resort + Snacks + Beer + Whisky
    Subitsha = Resort + Snacks + Whisky
    Aditya = Resort + Snacks + Whisky + Beer

    Bhavesh = 2 * Resort + Snacks + Beer + Whisky + Indri



    # Calculate how much each person needs to get back or pay
    MukeshShare = Mukesh - MukeshSpent
    BhaveshShare = Bhavesh - BhaveshSpent
    AdityaShare = Aditya - AdityaSpent

    print()

    persons = {
        'Mukesh': MukeshShare,
        'Goutham': Goutham,
        'Vasavi': Vasavi,
        'Sunil': Sunil,
        'Bhavesh': BhaveshShare,
        'Priyesh': Priyesh,
        'Subitsha': Subitsha,
        'Aditya' : AdityaShare
    }

    # Print individual cost breakdowns
    print(f"{'Name':<10} {'Total':>10}")
    print("-" * 22)
    for name, total in persons.items():
        print(f"{name:<10} {round(total):>10}")



if __name__ == "__main__":
    main()

# ============================================================
#              ELECTRIC CIRCUIT CALCULATOR
# ============================================================

print("================================================")
print("          ELECTRIC CIRCUIT CALCULATOR")
print("================================================")
print("        Calculate Voltage, Current,")
print("        Resistance and Power")
print("================================================")


while True:

    print("\n------------------- MENU -------------------")
    print("1. Calculate Voltage")
    print("2. Calculate Current")
    print("3. Calculate Resistance")
    print("4. Calculate Power")
    print("5. Calculate Series Resistance")
    print("6. Calculate Parallel Resistance")
    print("7. Exit")
    print("--------------------------------------------")

    choice = input("Enter your choice (1-7): ")

    # --------------------------------------------------------
    # 1. Calculate Voltage
    # Formula: V = I × R
    # --------------------------------------------------------

    if choice == "1":

        print("\n--- Calculate Voltage ---")

        current = float(input("Enter current (I) in Amperes: "))
        resistance = float(input("Enter resistance (R) in Ohms: "))

        voltage = current * resistance

        print("Voltage =", voltage, "Volts")


    # --------------------------------------------------------
    # 2. Calculate Current
    # Formula: I = V / R
    # --------------------------------------------------------

    elif choice == "2":

        print("\n--- Calculate Current ---")

        voltage = float(input("Enter voltage (V) in Volts: "))
        resistance = float(input("Enter resistance (R) in Ohms: "))

        if resistance == 0:
            
            print("Error: Resistance cannot be zero.")
        else:
            current = voltage / resistance
            print("Current =", current, "Amperes")


    # --------------------------------------------------------
    # 3. Calculate Resistance
    # Formula: R = V / I
    # --------------------------------------------------------

    elif choice == "3":

        print("\n--- Calculate Resistance ---")

        voltage = float(input("Enter voltage (V) in Volts: "))
        current = float(input("Enter current (I) in Amperes: "))

        if current == 0:
            print("Error: Current cannot be zero.")
        else:
            resistance = voltage / current
            print("Resistance =", resistance, "Ohms")


    # --------------------------------------------------------
    # 4. Calculate Power
    # Formula: P = V × I
    # --------------------------------------------------------

    elif choice == "4":

        print("\n--- Calculate Power ---")

        voltage = float(input("Enter voltage (V) in Volts: "))
        current = float(input("Enter current (I) in Amperes: "))

        power = voltage * current

        print("Power =", power, "Watts")


    # --------------------------------------------------------
    # 5. Series Resistance
    # Formula: R = R1 + R2 + R3 + ...
    # --------------------------------------------------------

    elif choice == "5":

        print("\n--- Series Resistance ---")

        number = int(input("How many resistors do you have? "))

        total_resistance = 0

        for i in range(1, number + 1):

            resistance = float(
                input("Enter resistance of resistor " + str(i) + " (Ohms): ")
            )

            total_resistance = total_resistance + resistance

        print("Total Series Resistance =", total_resistance, "Ohms")


    # --------------------------------------------------------
    # 6. Parallel Resistance
    # Formula: 1/R = 1/R1 + 1/R2 + ...
    # --------------------------------------------------------

    elif choice == "6":

        print("\n--- Parallel Resistance ---")

        number = int(input("How many resistors do you have? "))

        reciprocal = 0

        for i in range(1, number + 1):

            resistance = float(
                input("Enter resistance of resistor " + str(i) + " (Ohms): ")
            )

            if resistance == 0:
                print("Error: Resistance cannot be zero.")
                break

            reciprocal = reciprocal + (1 / resistance)

        else:

            if reciprocal == 0:
                print("Error: Invalid resistance values.")
            else:
                total_resistance = 1 / reciprocal
                print(
                    "Total Parallel Resistance =",
                    total_resistance,
                    "Ohms"
                )


    # --------------------------------------------------------
    # 7. Exit
    # --------------------------------------------------------

    elif choice == "7":

        print("\nThank you for using Electric Circuit Calculator!")
        print("Program ended.")
        break


    # --------------------------------------------------------
    # Invalid choice
    # --------------------------------------------------------

    else:

        print("\nInvalid choice!")
        print("Please enter a number from 1 to 7.")


    # --------------------------------------------------------
    # Continue message
    # --------------------------------------------------------

    if choice != "7":

        input("\nPress Enter to return to the menu...")
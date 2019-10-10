print("How many bars should be charged?")
max_bars = int(input())
bars_charged = 0


while (max_bars > bars_charged):
    bars_charged = bars_charged + 1
    print("Charging:", "█"*bars_charged)

print("The battery is fully charged.")

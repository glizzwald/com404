print("How many zones must I cross")
zone_count = int(input())
min_zone_count = 0
print("Crossing zones...")

while(zone_count>min_zone_count):
    print("...crossed zone", zone_count)
    zone_count = zone_count - 1

print("Crossed all zones. Jumanji!")
#For Alpha Drone---------------------------

Alpha_starting_battery = 96/100
Alpha_consume_battery_for_camara = 6/100
Alpha_delivery_distance = 20
Alpha_consme_battery_for_reaching_per_km = 2/100
Alpha_consume_battery_for_unload = 4/100
Alpha_consume_battery_for_return_per_km = 1/100
Alpha_complete_mission_time = 34/60

Alpha_consume_battery_for_reaching_total = Alpha_delivery_distance * Alpha_consme_battery_for_reaching_per_km
Alpha_consume_battery_for_return_total = Alpha_delivery_distance * Alpha_consume_battery_for_return_per_km

Alpha_total_battery_consumed_For_mission = Alpha_consume_battery_for_camara + Alpha_consume_battery_for_reaching_total + Alpha_consume_battery_for_unload + Alpha_consume_battery_for_return_total

#For Bravo Drone---------------------------

Bravo_starting_battery = 98/100
Bravo_consume_battery_for_camara = 8/100
Bravo_delivery_distance = 18
Bravo_consme_battery_for_reaching_per_km = 2/100
Bravo_consume_battery_for_unload = 5/100
Bravo_consume_battery_for_return_per_km = 1/100
Bravo_complete_mission_time = 30/60

Bravo_consume_battery_for_reaching_total = Bravo_delivery_distance * Bravo_consme_battery_for_reaching_per_km
Bravo_consume_battery_for_return_total = Bravo_delivery_distance * Bravo_consume_battery_for_return_per_km

Bravo_total_battery_consumed_For_mission = Bravo_consume_battery_for_camara + Bravo_consume_battery_for_reaching_total + Bravo_consume_battery_for_unload + Bravo_consume_battery_for_return_total


#For Charlie Drone---------------------------

Charlie_starting_battery = 94/100
Charlie_consume_battery_for_camara = 7/100
Charlie_delivery_distance = 22
Charlie_consme_battery_for_reaching_per_km = 2/100
Charlie_consume_battery_for_unload = 6/100
Charlie_consume_battery_for_return_per_km = 1/100
Charlie_complete_mission_time = 38/60

Charlie_consume_battery_for_reaching_total = Charlie_delivery_distance * Charlie_consme_battery_for_reaching_per_km
Charlie_consume_battery_for_return_total = Charlie_delivery_distance * Charlie_consume_battery_for_return_per_km

Charlie_total_battery_consumed_For_mission = Charlie_consume_battery_for_camara + Charlie_consume_battery_for_reaching_total + Charlie_consume_battery_for_unload + Charlie_consume_battery_for_return_total

Emargency_battery = 15/100


#Task 1: Calculate the remaining battery after the mission for each drone

remaining_battery_after_mission_Alpha = Alpha_starting_battery - Alpha_total_battery_consumed_For_mission
remaining_battery_after_mission_Bravo = Bravo_starting_battery - Bravo_total_battery_consumed_For_mission
remaining_battery_after_mission_Charlie = Charlie_starting_battery - Charlie_total_battery_consumed_For_mission

print("Remaining battery after mission for Alpha Drone:", remaining_battery_after_mission_Alpha*100, "%")
print("Remaining battery after mission for Bravo Drone:", remaining_battery_after_mission_Bravo*100, "%")
print("Remaining battery after mission for Charlie Drone:", remaining_battery_after_mission_Charlie*100, "%")

#Task 2: usable battary excluding the emergency battery

usable_battery_Alpha = remaining_battery_after_mission_Alpha - Emargency_battery
usable_battery_Bravo = remaining_battery_after_mission_Bravo - Emargency_battery
usable_battery_Charlie = remaining_battery_after_mission_Charlie - Emargency_battery

if usable_battery_Alpha < Emargency_battery:
    print("Alpha Drone has less than emergency battery left after the mission.")
else:
    print("Usable battery for Alpha Drone:", usable_battery_Alpha*100, "%")

if usable_battery_Bravo < Emargency_battery:
    print("Bravo Drone has less than emergency battery left after the mission.")
else:
    print("Usable battery for Bravo Drone:", usable_battery_Bravo*100, "%")

if usable_battery_Charlie < Emargency_battery:
    print("Charlie Drone has less than emergency battery left after the mission.")
else:
    print("Usable battery for Charlie Drone:", usable_battery_Charlie*100, "%")

#task----------------------
alpha = usable_battery_Alpha
bravo = usable_battery_Bravo
charlie = usable_battery_Charlie


if alpha == bravo == charlie:
    print("All drones have the same usable battery after the mission.")

if alpha > bravo and alpha > charlie:
    print("alpha 1st")

    if bravo > charlie:
        print("bravo 2nd")
        print("charlie 3rd")
    else:
        print("bravo 3rd")
        print("charlie 2nd")

elif bravo > alpha and bravo > charlie:
    print("bravo 1st")

    if alpha > charlie:
        print("alpha 2nd")
        print("charlie 3rd")
    else:
        print("alpha 3rd")
        print("charlie 2nd")


elif charlie > alpha and charlie > bravo:
    print("Charlie 1st")
    
    if alpha > bravo:
        print("alpha 2nd")
        print("bravo 3rd")
    else:
        print("alpha 3rd")
        print("bravo 2nd")

    


#Task 4-------------------

Highest_usable_battery = max(usable_battery_Alpha, usable_battery_Bravo, usable_battery_Charlie)

if Highest_usable_battery == usable_battery_Alpha:
    print("Alpha Drone has the highest usable battery after the mission.")

if Highest_usable_battery == usable_battery_Bravo:
    print("Bravo Drone has the highest usable battery after the mission.")

else:
    print("Charlie Drone has the highest usable battery after the mission.")


#Task 5-------------------

if remaining_battery_after_mission_Alpha < 20/100:
    print("Alpha Drone Recharged required.")
else:
        print("Alpha Drone MISSION SUCCESSFULL.")

if remaining_battery_after_mission_Bravo < 20/100:
    print("Bravo Drone Recharged required.")
else:
        print("Bravo Drone MISSION SUCCESSFULL.")

if remaining_battery_after_mission_Charlie < 20/100:
    print("Charlie Drone Recharged required.")
else:
        print("Charlie Drone MISSION SUCCESSFULL.")
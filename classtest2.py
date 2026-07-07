anwer_complete_trips = 18
anwer_earn_per_trips = 420
anwer_bonus = 750
anwer_spent_fuel_tolls_parkings = 2850 + 350 + 450
anwer_work_time = (9*60) + 15


abdullah_complete_trips = 21
abdullah_earn_per_trips = 390
abdullah_bonus = 500
abdullah_spent_fuel_tolls_parkings = 3150 + 500 + 300
abdullah_work_time = (10*60)


jubayer_complete_trips = 16
jubayer_earn_per_trips = 510
jubayer_bonus = 900
jubayer_spent_fuel_tolls_parkings = 2600 + 250 + 550
jubayer_work_time = (8*60) + 30

uber_commision = 22/100

#task 1 --------------

Total_trip_earnings_anwer = anwer_complete_trips * anwer_earn_per_trips
Total_trip_earnings_abdullah = abdullah_complete_trips * abdullah_earn_per_trips
Total_trip_earnings_jubayer = jubayer_complete_trips * jubayer_earn_per_trips

print("Total Trip earnings of Anwer:", Total_trip_earnings_anwer ,"Taka")
print("Total Trip earnings of Abdullah:", Total_trip_earnings_abdullah, "Taka")
print("Total Trip earnings of Jubayer:", Total_trip_earnings_jubayer, "Taka")

#task 2 ----------------

uber_commission_from_anwer = Total_trip_earnings_anwer - uber_commision
uber_commission_from_abdullah = Total_trip_earnings_abdullah - uber_commision
uber_commission_from_jubayer = Total_trip_earnings_jubayer - uber_commision

print("Uber Take Commission From Anwer:" ,uber_commission_from_anwer, "Taka")
print("Uber Take Commission From Abdullah:" ,uber_commission_from_abdullah, "Taka")
print("Uber Take Commission From Jubayer:" ,uber_commission_from_anwer , "Taka")

#task 3 ----------------

total_except_bonus_Commission_anwer =  (anwer_complete_trips * anwer_earn_per_trips) - uber_commision
total_except_bonus_Commission_abdullah =  (abdullah_complete_trips * abdullah_earn_per_trips) - uber_commision
total_except_bonus_Commission_jubayer =  (jubayer_complete_trips * jubayer_earn_per_trips) - uber_commision

print("Anwer Final Earnings:",total_except_bonus_Commission_anwer, "Taka")
print("abdullah Final Earnings:",total_except_bonus_Commission_abdullah, "Taka")
print("Jubayer Final Earnings:",total_except_bonus_Commission_jubayer, "Taka")

#task 4 ----------------

print("Total expence of Anwer:", anwer_spent_fuel_tolls_parkings , "Taka")
print("Total expence of Abdullah:", abdullah_spent_fuel_tolls_parkings , "Taka")
print("Total expence of Jubayer:", jubayer_spent_fuel_tolls_parkings , "Taka")


#task 5 ----------------

net_profit_anwer = total_except_bonus_Commission_anwer - anwer_spent_fuel_tolls_parkings + anwer_bonus

net_profit_abdullah = total_except_bonus_Commission_abdullah - abdullah_spent_fuel_tolls_parkings + abdullah_bonus

net_profit_jubayer = total_except_bonus_Commission_jubayer - jubayer_spent_fuel_tolls_parkings + jubayer_bonus

print("Net Profit of Anwer:",net_profit_anwer, "Taka")
print("Net Profit of Abdullah:",net_profit_abdullah, "Taka")
print("Net Profit of jubayer:",net_profit_jubayer, "Taka")


#task 6-------------------

if net_profit_anwer > net_profit_abdullah and net_profit_anwer > net_profit_jubayer:
    print("Anwer has the highest Net profit")

elif net_profit_abdullah > net_profit_anwer  and net_profit_abdullah > net_profit_jubayer:
    print("Abdullah has the highest net profit")

else:
    print("Jubayer has the highest net profit")


#task 7 -------------------------

if net_profit_anwer > net_profit_abdullah and net_profit_anwer > net_profit_jubayer:
    print("Anwer Ranked 1st By net profit")
    
    if net_profit_abdullah > net_profit_jubayer:
        print("Abdullah Ranked 2nd by net profit")
        print("Jubayer Ranked 3rd by net profit")
    else:
        print("Jubayer Ranked 2nd by net profit")
        print("Abdullah Ranked 3rd by net profit")

elif net_profit_abdullah > net_profit_anwer and net_profit_abdullah > net_profit_jubayer:
    print("Abduillah Ranked 1st By net profit")
    
    if net_profit_anwer > net_profit_jubayer:
        print("Anwer Ranked 2nd by net profit")
        print("Jubayer Ranked 3rd by net profit")
    else:
        print("Jubayer Ranked 2nd by net profit")
        print("Anwer Ranked 3rd by net profit")

else:
    print("Jubayer Ranked 1st By net profit")

    if net_profit_anwer > net_profit_abdullah:
        print("Anwer Ranked 2nd by net profit")
        print("abdullah Ranked 3rd by net profit")
    else:
        print("Abdullah Ranked 2nd by net profit")
        print("Anwer Ranked 3rd by net profit")


#task 8 ------------------------

if anwer_work_time > abdullah_work_time and anwer_work_time > jubayer_work_time:
    print("Anwer worked the Longest Duration")

elif abdullah_work_time > anwer_work_time  and abdullah_work_time > jubayer_work_time:
    print("Abdullah worked the Longest Duration")

else:
    print("Jubayer worked the Longest Duration")


#task 9 ---------------------

if net_profit_anwer >= 6000:
    print("Anwer perfomance : Excellent")
elif 4000 < net_profit_anwer < 5999:
    print("Anwer Performance : Good")
else:
    print("Anwer Needs Improvement")

if net_profit_abdullah >= 6000:
    print("Abdullah perfomance : Excellent")
elif 4000 < net_profit_abdullah < 5999:
    print("Abdullah Performance : Good")
else:
    print("Abdullah Needs Improvement")

if net_profit_jubayer >= 6000:
    print("Jubayer perfomance : Excellent")
elif 4000 < net_profit_jubayer < 5999:
    print("Jubayer Performance : Good")
else:
    print("Jubayer Needs Improvement")
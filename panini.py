
plan = ["reading", "coding", "running", "cooking", "sleeping"]
print("Initial plan:", plan)


print("First activity:", plan[0])
print("Last activity:", plan[-1])


print("Middle three:", plan[1:4])
print("Backwards:", plan[::-1])


plan[1] = "studying"
print("After changing second item:", plan)


plan.append("gaming")         
plan.insert(0, "meditating")  
print("After adding items:", plan)


plan.remove("running")        
weekend = ["hiking", "cinema"]
final_plan = plan + weekend
print("Final combined plan:", final_plan)







city = ("Poznan", "Poland", 52.41, 16.93)


print("Country (second item):", city[1])
print("Longitude (last item):", city[-1])
print("Type of city:", type(city))


name, country, lat, lon = city
print("Unpacked Name:", name)
print("Unpacked Latitude:", lat)


city_list = list(city)
city_list[1] = "Germany"    
city = tuple(city_list)
print("Updated city tuple:", city)

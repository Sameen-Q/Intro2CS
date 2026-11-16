
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








mine = {"pizza", "sushi", "pasta", "soup", "salad"}
friend = {"burger", "sushi", "fries", "soup", "tacos"}

print("All unique foods:", mine | friend)
print("Both like:", mine & friend)
print("Only I like:", mine - friend)
print("Only one likes:", mine ^ friend)









words = {"cat": "kot", "dog": "pies", "house": "dom", "water": "woda"}


print("Translation of 'cat':", words["cat"])
print("Total pairs count:", len(words))


words["book"] = "ksiazka"   
words["dog"] = "szczeniak"  
print("After adding and modifying:", words)


words.update({"apple": "jablko", "sun": "slonce"})
print("After update:", words)


print("Keys list:", list(words.keys()))
print("Values list:", list(words.values()))
print("Pairs list:", list(words.items()))

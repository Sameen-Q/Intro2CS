
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

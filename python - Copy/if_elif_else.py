#w = input("give me w: ")

#if w == "sunny":
  #  print("cricket")
#elif w == "rainy":
 #   print("robot")
#else:
    #print("sleep at home")

w = input("give me w: ")
t_o_d = input("give me t_o_d: ") 
if w == "sunny":
    print("play outside")
elif w == "rainy" and t_o_d == "morning":
    print("play inside ")
elif w == "snow" and t_o_d == "night":
    print("play carroms")
elif w == "snow" and t_o_d == "evening":
    print("play u r choice")
else:
    print("your time is over!!")

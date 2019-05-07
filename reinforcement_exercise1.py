# Think of a documentary, a drama, a comedy, and a dramedy. Store the titles of these films in variables. Ask the user if they enjoy 1. documentaries 2. dramas 3. comedies. If they answer yes to documentaries, display a message recommending the documentary to them. If they answer no to documentaries but yes to dramas and comedies, recommend the dramedy. If they answer yes to only dramas, recommend the drama. If they say yes to only comedies, recommend the comedy. If they answer no to all three, recommend a good book instead.

documentary = "climate changing!"
drama = "joker"
comedy = "sonic"
dramedy = "meet the parents"

print("Do you enjoy watching documentary? Respond in yes or no")
response1 = input()
print("Do you enjoy watching drama? Respond in yes or no")
response2 = input()
print("Do you enjoy watching comedy? Respond in yes or no")
response3 = input()

if response1 == "yes" and response2 == "no" and response3 == "no":
    print("I recommend you to watch {}.".format(documentary))
elif response1 == "no" and response2 == "yes" and response3 == "yes":
    print("I recommend you to watch {}.".format(dramedy))
elif response1 == "no" and response2 == "yes" and response3 == "no":
    print("I recommend you to watch {}.".format(drama)) 
elif response3 == "yes" and response1 == "no" and response2 == "no":
    print("I recommend you to watch {}.".format(comedy))
else:
    print("Just read a book dude")


# Let's take a different approach to film recommendations: create the same variables containing your potential film recommendations and then ask the user to rate their appreciation for 1. documentaries 2. dramas 3. comedies on a scale from one to five. If they rate documentaries four or higher, recommend the documentary. If they rate documentaries 3 or lower but both comedies and dramas 4 or higher, recommend the dramedy. If they rate only dramas 4 or higher, recommend the drama. If they rate just comedies 4 or higher, recommend the comedy. Otherwise, recommend a good book.

documentary = "climate changing!"
drama = "joker"
comedy = "sonic"
dramedy = "meet the parents"

print("Please rate from one to five, your appreciation for documentary")
response1 = int(input())
print("Please rate from one to five, your appreciation for dramas")
response2 = int(input())
print("Please rate from one to five, your appreciation for comedy")
response3 = int(input())

if response1 >= 4:
    print("I recommend you to watch {}.".format(documentary))
elif response1 <= 3 and response2 >= 4 and response3 >= 4:
    print("I recommend you to watch {}.".format(dramedy))
elif response2 >= 4 and response1 <= 3 and response3 <= 3:
    print("I recommend you to watch {}.".format(drama))
elif response3 >= 4 and response1 <= 3 and response2 <=3:
    print("I recommend you to watch {}.".format(comedy))

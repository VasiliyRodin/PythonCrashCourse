bicycles = ['bike one', 'canno ndale', 're dline', 'specialized']
mesage = "My first bicycle was a " + bicycles[0].title()
print(mesage)



friends = ["bob bobington" , "lisa lisanton", "fred fredington"]
print(friends[1] + " " + friends[2].title() + " " + friends[0])

friends.append("bart bartington")
print(friends)

friends.insert(2, "ned nedington")
print (friends)

del friends[3]
print (friends)

popped_friend= friends.pop()
print(popped_friend)

friends.remove("bob bobington")
print(friends)



guests = ["bobby bob", "susie sue", "fred fredricks", "ricky bobby"]
removed_guests = guests.pop(0)
print(removed_guests)
guests.append("Jerry reid")
print(guests)

guests.insert(1,"rock monster")
guests.append("some person")

print(sorted(guests))
#guests.sort
print(guests)

#guests.reverse()
print(guests)

print(len(guests))

print(guests[-1])
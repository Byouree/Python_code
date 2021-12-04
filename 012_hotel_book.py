def hotel_book(arr, dep, k):
    event = []
    """
    for i in range(0, len(arr)):
        t_arrive = ()
        t_arrive = (arr[i], "RED")
        event.append(t_arrive)
    print(t_arrive)
    print(event)

    for i in range(0, len(dep)):
        t_departure = ()
        t_departure = (dep[i], "BLUE")
        event.append(t_departure)
    """
    event = [(t,"RED") for t in arr] + [(t, "BlUE") for t in dep]

    event = sorted(event)
    print(event)

    guest = 0

    for t in event:
        if t[1] == "RED":
            guest += 1
        else:
            guest -= 1
        if guest > k:
            return 0

    return 1

arr = [1,3,5]
dep = [2,6,8]
k = 1
print(hotel_book(arr, dep, k))



def findItinerary(tickets):
    adjacency = build_adjacency_list(tickets)
    sort_adjacency_lists(adjacency)

    itinerary = ["JFK"]  # Start with JFK
    num_tickets = len(tickets)  # Total number of tickets

    dfs("JFK", adjacency, itinerary, num_tickets)

    return itinerary

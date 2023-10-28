def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    # Create pairs of position and speed
    pair = [(p, s) for p, s in zip(position, speed)]
    # Sort pairs in reverse order based on position
    pair.sort(reverse=True)
    stack = []  # Stack to track arrival times
    
    for p, s in pair:  # Iterate in reverse sorted order
        time_to_destination = (target – p) / s  # Calculate time to reach destination
        if not stack or time_to_destination > stack[-1]:
            # If the stack is empty or this car does not collide with the car ahead, add it to the stack
            stack.append(time_to_destination)
    
    return len(stack)  # The length of the stack represents the number of car fleets

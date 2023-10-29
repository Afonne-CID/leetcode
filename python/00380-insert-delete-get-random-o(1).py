class RandomizedSet:
    def __init__(self):
        # Initialize an empty dictionary to store values and their indexes.
        self.num_map = {}
        
        # Initialize an empty list to store values.
        self.num_list = []

    def insert(self, val: int) -> bool:
        # Check if the value is already in the dictionary.
        if val in self.num_map:
            return False

        # If the value is not present, add it to the dictionary and list.
        self.num_map[val] = len(self.num_list)
        self.num_list.append(val)

        return True

    def remove(self, val: int) -> bool:
        # Check if the value exists in the dictionary.
        if val not in self.num_map:
            return False

        # Get the index of the value in the list.
        idx, last_element = self.num_map[val], self.num_list[-1]

        # Move the last element to the index of the element we want to remove.
        self.num_list[idx], self.num_map[last_element] = last_element, idx

        # Remove the value from the list and dictionary.
        self.num_list.pop()
        del self.num_map[val]

        return True

    def getRandom(self) -> int:
        # Return a random element from the list.
        return choice(self.num_list)
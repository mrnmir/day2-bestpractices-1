class Fish:
    def __init__(self):
        """Constructor for Fish class"""
        self.members = ["Salmon", "Trout", "Goldfish", "Catfish"]

    def print_members(self):
        print("Members of the Fish class:")
        for member in self.members:
            print(member)

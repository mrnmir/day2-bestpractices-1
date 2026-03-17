class Mammals:
    def __init__(self):
        """Constructor for Mammals class"""
        self.members = ["Tiger", "Elephant", "Whale", "Human"]

    def print_members(self):
        print("Members of the Mammals class:")
        for member in self.members:
            print(member)

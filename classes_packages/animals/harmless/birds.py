class Birds:
    def __init__(self):
        """Constructor for Birds class"""
        self.members = ["Sparrow", "Eagle", "Parrot", "Penguin"]

    def print_members(self):
        print("Members of the Birds class:")
        for member in self.members:
            print(member)

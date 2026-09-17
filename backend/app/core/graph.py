"""Graph data structure used by RouteRU."""


class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_location(self, location):
        if location not in self.adjacency_list:
            self.adjacency_list[location] = []

    def add_connection(
        self,
        location1,
        location2,
        travel_time,
        mode="Walk",
        route=None
    ):
        self.add_location(location1)
        self.add_location(location2)

        connection1 = {
            "location": location2,
            "travel_time": travel_time,
            "mode": mode,
            "route": route
        }

        connection2 = {
            "location": location1,
            "travel_time": travel_time,
            "mode": mode,
            "route": route
        }

        self.adjacency_list[location1].append(connection1)
        self.adjacency_list[location2].append(connection2)

    def get_neighbors(self, location):
        return self.adjacency_list.get(location, [])
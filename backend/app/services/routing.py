import heapq

from app.core.graph import Graph


def build_campus_graph():
    graph = Graph()

    # Livingston
    graph.add_connection(
        "livingston_plaza",
        "livingston_student_center",
        2,
        "Walk"
    )

    graph.add_connection(
        "livingston_student_center",
        "quads",
        2,
        "Walk"
    )

    # Busch
    graph.add_connection(
        "hill_center",
        "allison_road",
        2,
        "Walk"
    )

    graph.add_connection(
        "allison_road",
        "busch_student_center",
        2,
        "Walk"
    )

    graph.add_connection(
        "busch_student_center",
        "werblin",
        4,
        "Walk"
    )

    graph.add_connection(
        "werblin",
        "stadium_west",
        3,
        "Walk"
    )

    # College Avenue
    graph.add_connection(
        "college_ave_student_center",
        "the_yard",
        2,
        "Walk"
    )

    graph.add_connection(
        "the_yard",
        "student_activities_center",
        3,
        "Walk"
    )

    # Cook / Douglass
    graph.add_connection(
        "red_oak_lane",
        "lipman_hall",
        2,
        "Walk"
    )

    graph.add_connection(
        "lipman_hall",
        "biel_road",
        2,
        "Walk"
    )

    graph.add_connection(
        "biel_road",
        "henderson",
        1,
        "Walk"
    )

    graph.add_connection(
        "henderson",
        "gibbons",
        2,
        "Walk"
    )

    graph.add_connection(
        "gibbons",
        "college_hall",
        3,
        "Walk"
    )

    # Livingston <-> Busch
    graph.add_connection(
        "livingston_plaza",
        "busch_student_center",
        5,
        "Bus",
        "B / BL"
    )

    # Livingston <-> College Avenue
    graph.add_connection(
        "livingston_plaza",
        "college_ave_student_center",
        8,
        "Bus",
        "LX"
    )

    # Busch <-> College Avenue
    graph.add_connection(
        "busch_student_center",
        "college_ave_student_center",
        8,
        "Bus",
        "A / H"
    )

    # College Avenue <-> Cook/Douglass
    graph.add_connection(
        "college_ave_student_center",
        "college_hall",
        8,
        "Bus",
        "EE / F"
    )

    # Busch <-> Cook/Douglass
    graph.add_connection(
        "busch_student_center",
        "red_oak_lane",
        12,
        "Bus",
        "REXB"
    )

    # Livingston <-> Cook/Douglass
    graph.add_connection(
        "livingston_plaza",
        "red_oak_lane",
        12,
        "Bus",
        "REXL"
    )

    return graph


def find_shortest_route(graph, start, destination):
    if start == destination:
        return {
            "route": [start],
            "travel_time": 0,
            "steps": []
        }

    priority_queue = [(0, start, [], [])]
    visited = set()

    while priority_queue:
        (
            travel_time,
            current_location,
            path,
            steps
        ) = heapq.heappop(priority_queue)

        if current_location in visited:
            continue

        visited.add(current_location)
        new_path = path + [current_location]

        if current_location == destination:
            return {
                "route": new_path,
                "travel_time": travel_time,
                "steps": steps
            }

        for connection in graph.get_neighbors(current_location):
            neighbor = connection["location"]

            if neighbor in visited:
                continue

            new_step = {
                "from": current_location,
                "to": neighbor,
                "travel_time": connection["travel_time"],
                "mode": connection["mode"],
                "route": connection["route"]
            }

            heapq.heappush(
                priority_queue,
                (
                    travel_time + connection["travel_time"],
                    neighbor,
                    new_path,
                    steps + [new_step]
                )
            )

    return None
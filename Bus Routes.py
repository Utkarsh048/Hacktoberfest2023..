from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes, source, target):
        if source == target:
            return 0
        
        stop_to_routes = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].add(i)
        
        visited_stops = set()
        queue = deque([(source, 0)])
        visited_routes = set()

        while queue:
            current_stop, num_buses = queue.popleft()

            if current_stop == target:
                return num_buses

            for route_index in stop_to_routes[current_stop]:
                if route_index not in visited_routes:
                    visited_routes.add(route_index)
                    for next_stop in routes[route_index]:
                        if next_stop != current_stop and next_stop not in visited_stops:
                            visited_stops.add(next_stop)
                            queue.append((next_stop, num_buses + 1))

        return -1


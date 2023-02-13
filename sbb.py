import json
import operator
import math


class TrainLine:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.hubs = []
        self.hub_location = dict()

    def add_hub_at_km(self, hub, km):
        self.hubs.append(hub)
        self.hub_location[hub.name] = km

    def get_sorted_hubs(self):
        return sorted(self.hub_location.items(), key=operator.itemgetter(1))


class Hub:

    def __init__(self, name="", x=0, y=0):
        self.name = name
        self.x = x
        self.y = y

    def get_coordinates(self):
        return self.x, self.y


class SBB:
    def __init__(self):
        self.hubs = dict()
        self._train_lines = dict()

    def import_data(self, json_file_name):
        with open(json_file_name) as f:
            lines = json.load(f)
        for j in lines:
            if 'fields' not in j:
                continue
            train_line_id = j['fields']['linie']
            if train_line_id not in self._train_lines:
                train_line_name = j['fields']['linienname']
                self._train_lines[train_line_id] = TrainLine(train_line_id, train_line_name)
            hub = Hub()
            hub.name = treat_string(j['fields']['bezeichnung_bpk'])
            hub.x = j['fields']['geopos'][0]
            hub.y = j['fields']['geopos'][1]
            km = j['fields']['km']

            self._train_lines[train_line_id].add_hub_at_km(hub, km)
            self.hubs[hub.name] = hub

        print('successfully imported ' + str(len(self.hubs)) + ' hubs')
        print('successfully imported ' + str(len(self._train_lines)) + ' train lines')

    def create_map(self):
        map = dict()
        for line in self._train_lines:
            previous_hub_name = ""
            previous_km = -1
            for h in self._train_lines[line].get_sorted_hubs():
                hub_name = h[0]
                km = h[1]
                if previous_hub_name:
                    distance = abs(km - previous_km)
                    map.setdefault(hub_name, dict())
                    map.setdefault(previous_hub_name, dict())
                    map[hub_name].setdefault(previous_hub_name)
                    map[previous_hub_name].setdefault(hub_name)
                    map[hub_name][previous_hub_name] = distance
                    map[previous_hub_name][hub_name] = distance
                previous_hub_name = hub_name
                previous_km = km
        return map

    def get_hub_locations(self):
        locations = dict()
        for h in self.hubs:
            locations[h] = self.hubs[h].get_coordinates()
        return locations

    def get_distance_between(self, h1, h2):
        return math.sqrt((self.hubs[h1].x - self.hubs[h2].x) ** 2 + (self.hubs[h1].y - self.hubs[h2].y) ** 2) * 100


def treat_string(name):
    name = name.replace(" ", "_")
    name = name.replace('(', "")
    return name.replace(')', "")

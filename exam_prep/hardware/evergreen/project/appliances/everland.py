from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_cost = sum([room.cost for room in self.rooms])
        return f'Monthly consumption : {total_cost:.2f}$.'

    def pay(self):
        fmt = []
        for room in self.rooms:
            if room.budget >= room.cost:
                room.budget -= room.cost
                fmt.append(f"{room.family_name} paid {room.cost:.2f}$ and have {room.budget:.2f}$ left.")
            else:
                fmt.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
                self.rooms.remove(room)
        return '\n'.join(fmt)

    def status(self):
        total_people = 0
        '\n'.join([
            f'Total population: {total_people}'])
        #TODO FORMATING

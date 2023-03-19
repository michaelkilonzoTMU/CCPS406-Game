class Room:
    def __init__(self, id, name, visited, adjRooms, firstMessage, secondMessage):
        self.id = id
        self.name = name
        self.visited = visited
        self.adjRooms = adjRooms
        self.firstMessage = firstMessage
        self.secondMessage = secondMessage

    def __repr__(self):
        return f'<Room: {self.name}>'
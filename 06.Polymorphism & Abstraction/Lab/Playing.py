class Guitar:
    def play(self):
        return "Playing the guitar"


class Children:
    def play(self):
        return "Children are playing"


def start_playing(obj):
    return obj.play()


piano = Children()
start_playing(piano)
guitar = Guitar()
start_playing(guitar)

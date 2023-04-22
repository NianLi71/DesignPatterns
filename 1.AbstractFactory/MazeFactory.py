from Maze import Maze, Wall, Room, Door, Direction

class MazeFactory:
    def __init__(self) -> None:
        pass

    def MakeMaze(self):
        return Maze()

    def MakeWall(self):
        return Wall()

    def MakeRoom(self, roomNo: int) -> Room:
        return Room(roomNo)

    def MakeDoor(self, room1, room2) -> Door:
        return Door(room1, room2)


# Enchanted Maze components
class EnchantedRoom(Room):
    def __init__(self, roomNo: int, spell):
        super().__init__(roomNo)
        self._spell = spell


class Spell:
    def __init__(self, words) -> None:
        self._words = words


class EnchantedMazeFactory(MazeFactory):
    def __init__(self) -> None:
        super().__init__()

    def MakeRoom(self, roomNo: int):
        print('Making a enchanted room.')
        return EnchantedRoom(roomNo, self.CastSpell())
    
    def CastSpell(self):
        print('Cast a spell.')
        return Spell('This is a spell.')


# BombedMaze component
class BombedWall:
    def __init__(self) -> None:
        print('Making a BombedWall.')


class RoomWithABomb(Room):
    def __init__(self, roomNo: int):
        print('Making a RoomWithABomb.')
        super().__init__(roomNo)


class BombedMazeFactory(MazeFactory):
    def __init__(self) -> None:
        super().__init__()

    def MakeWall(self):
        return BombedWall()

    def MakeRoom(self, roomNo: int) -> Room:
        return RoomWithABomb(roomNo)


# The Maze Game
class MazeGame:
    def CreateMaze(self, factory: MazeFactory):
        aMaze = factory.MakeMaze()

        r1 = factory.MakeRoom(1)
        r2 = factory.MakeRoom(2)
        aDoor = factory.MakeDoor(r1, r2)

        aMaze.AddRoom(r1)
        aMaze.AddRoom(r2)

        r1.SetSide(Direction.North, factory.MakeWall());
        r1.SetSide(Direction.East, aDoor);
        r1.SetSide(Direction.South, factory.MakeWall());
        r1.SetSide(Direction.West, factory.MakeWall());
        r2.SetSide(Direction.North, factory.MakeWall());
        r2.SetSide(Direction.East, factory.MakeWall());
        r2.SetSide(Direction.South, factory.MakeWall());
        r2.SetSide(Direction.West, aDoor);

        return aMaze


if __name__ == '__main__':
    game = MazeGame()
    # game.CreateMaze(MazeFactory())
    # game.CreateMaze(EnchantedMazeFactory())
    game.CreateMaze(BombedMazeFactory())
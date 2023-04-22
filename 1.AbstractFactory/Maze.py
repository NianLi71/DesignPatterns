from __future__ import annotations
from enum import Enum


class Direction(Enum):
    North, South, East, West = range(0, 4)


class MapSite:
    def Enter():
        pass


class Room(MapSite):
    def __init__(self, roomNo: int):
        self.roomNo = roomNo
        self._sides: dict[Direction, MapSite] = {}

    def GetSide(self, direction: Direction) -> MapSite:
        return self._sides[direction]

    def SetSide(self, direction: Direction, mapSite: MapSite) -> None:
        self._sides[direction] = mapSite

    def GetRoomNo(self):
        return self.roomNo


class Wall(MapSite):
    def __init__(self) -> None:
        pass


class Door(MapSite):
    def __init__(self, room1: Room, room2: Room) -> None:
        self._room1 = room1
        self._room2 = room2
        self._isOpen = False

    def OtherSideFrom(self, room: Room) -> Room:
        if room is self._room1:
            return self._room2
        elif room is self._room2:
            return self._room1
        else:
            return None


class Maze:
    def __init__(self) -> None:
        self._rooms_dict = {}

    def AddRoom(self, room: Room):
        self._rooms_dict[room.GetRoomNo()] = room

    def RoomNo(self, number: int) -> Room:
        return self._rooms_dict[number]

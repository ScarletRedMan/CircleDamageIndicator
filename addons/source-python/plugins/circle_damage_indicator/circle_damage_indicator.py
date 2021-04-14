from players.entity import Player
from players.helpers import index_from_userid
from events import Event
from colors import Color
from messages import HudMsg
import math


COLOR_START = (124, 173, 255)
COLOR_END = (212, 66, 34)
PLAYERS = dict()


class Vector3:
    def __init__(self, x: int, y: int, z: int):
        self.x, self.y, self.z = x, y, z

    def linear_interpolate(self, target, t: float):
        x = int((target.x - self.x) * t) + self.x
        y = int((target.y - self.y) * t) + self.y
        z = int((target.z - self.z) * t) + self.z
        return Vector3(x, y, z)

    def get_as_tuple(self) -> tuple:
        return self.x, self.y, self.z


@Event('player_hurt')
def on_damage(event):
    if event['attacker'] in (0, event['userid']):
        return

    global PLAYERS
    key = str(event['attacker'])
    damager = index_from_userid(event['attacker'])
    damage = event['dmg_health']

    if key not in PLAYERS:
        PLAYERS[key] = 0
    x = math.cos(math.pi/6 * PLAYERS[key] - math.pi/2) / 15 + 0.5
    y = math.sin(math.pi/6 * PLAYERS[key] - math.pi/2) / 15 + 0.5
    PLAYERS[key] += 1

    player = Player(index_from_userid(event['userid']))
    color = Vector3(*COLOR_START).linear_interpolate(Vector3(*COLOR_END), 1 - player.health/100.0)

    HudMsg(
        message=str(damage),
        hold_time=1,
        fade_out=1,
        x=x,
        y=y,
        color1=Color(*color.get_as_tuple()),
        channel=PLAYERS[key]
    ).send(damager)


@Event('round_start')
def round_start(_):
    global PLAYERS
    PLAYERS = dict()

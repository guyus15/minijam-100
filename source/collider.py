import pygame

from enum import Enum
from source.vector import Vector


class ColliderTypes(Enum):
    CIRCLE = 0,
    RECTANGLE = 1


class ColliderException(Exception):
    pass


class Collider:
    def __init__(self, shape, pos, radius=None, width=None, height=None):
        self.shape = shape
        self.pos = pos
        self.vel = Vector()

        # Initialise circle collider
        if self.shape is ColliderTypes.CIRCLE:
            if radius is None:
                # If a circle collider is created without a radius we will throw an error.
                raise ColliderException("A circle collider requires a radius parameter.")

            self.radius = radius

        # Initialise rectangle collider
        if self.shape is ColliderTypes.CIRCLE:
            if width is None or height is None:
                # If a rectangle collider is created without a width and a height, throw an error.
                raise ColliderException("A rectangle collider requires a width and height parameter.")

            self.width = width
            self.height = height

        self.collision_list = []

    def hit(self, collider):
        if self.shape is ColliderTypes.CIRCLE:
            # Collision between a circle and a rectangles
            if collider.shape is ColliderTypes.RECTANGLE:
                return collider.hit(self)
            # Collision between two circles
            return collider.pos.copy().subtract(self.pos).length() <= collider.radius + self.radius

        if self.shape is ColliderTypes.RECTANGLE:
            if collider.shape is ColliderTypes.CIRCLE:
                # Collision between a circle and a rectangle
                return (abs(collider.pos.x - self.pos.x) <= collider.radius + self.width / 2) \
                       and (abs(collider.pos.y - self.pos.y) <= collider.radius + self.height / 2)

            # Collision between two rectangles
            return (abs(collider.pos.x - self.pos.x) <= collider.width / 2 + self.width / 2) \
                and (abs(collider.pos.y - self.pos.y) <= collider.height / 2 + self.height / 2)

    def add_collision(self, collider):
        self.collision_list.append(collider)

    def remove_collision(self, collider):
        self.collision_list.remove(collider)

    def in_collision(self, collider):
        return collider in self.collision_list

    # Bouncing with zero mass
    def bounce_zero_mass(self, collider):
        if collider.shape == ColliderTypes.RECTANGLE:
            self.vel.reflect(collider.normal)
        else:
            self.vel.reflect(self.pos.copy().subtract(collider.pos).normalize())

    # Bouncing with mass
    def bounce_momentum(self, collider):
        connect = self.pos.copy().subtract(collider.pos)

        normal = connect.copy().normalize()
        v1_parallel = self.vel.get_proj(normal)
        v1_perpendicular = self.vel.copy().subtract(v1_parallel)
        v2_parallel = collider.getVel().get_proj(normal)
        v2_perpendicular = collider.getVel().copy().subtract(v2_parallel)

        self.vel = v2_parallel + v1_perpendicular
        collider.set_velocity(v1_parallel + v2_perpendicular)

    def get_velocity(self):
        return self.vel

    def set_velocity(self, velocity):
        self.vel = velocity


class PlayerCollider(Collider):
    def __init__(self, position, movement, dimensions):
        Collider.__init__(self, ColliderTypes.RECTANGLE, position, width=dimensions[0], height=dimensions[1])
        self.movement = movement

    def bounce_player(self, collider):
        if collider.shape is ColliderTypes.CIRCLE:
            self.movement.vel_vector.add(
                self.pos.copy().subtract(collider.pos).normalise().multiply(self.movement.speed)
            )
        elif collider.shape is ColliderTypes.RECTANGLE:
            normal = self.pos.copy().subtract(collider.pos).normalise()
            if abs(normal.x) > abs(normal.y):
                normal = Vector(normal.x, 0).normalise()
            else:
                normal = Vector(0, normal.y).normalise()
            self.movement.vel_vector.add(normal.multiply(self.movement.speed * 5))

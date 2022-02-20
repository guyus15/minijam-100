import pygame
import math

from source.vector import Vector


class Movement:
    def __init__(self, speed, pos_vector):
        self.speed = speed
        self.pos_vector = pos_vector
        self.vel_vector = Vector(0, 0)
        self.rotation = 0

    def move_horizontal(self, direction):
        """
        Handles horizontal movement
        Direction -1 = move left
        Direction 1 = move right
        :param direction: The direction to go in the horizontal direction.
        """

        if direction < 0:
            self.vel_vector.add(Vector(-self.speed, self.vel_vector.y))  # Move left
        elif direction > 0:
            self.vel_vector.add(Vector(self.speed, self.vel_vector.y))  # Move right

    def move_vertical(self, direction):
        """
        Handles vertical movement
        Direction -1 = move down
        Direction 1 = move up
        :param direction: The direction to go in the vertical direction.
        """

        if direction > 0:
            self.vel_vector.add(Vector(self.vel_vector.x, -self.speed))  # Move down
        elif direction < 0:
            self.vel_vector.add(Vector(self.vel_vector.x, self.speed))  # Move up

    def check_out_range(self, value):
        """
        A clamping function which will ensure that the speed of the player does not exceed the defined
        speed variable.
        :param value: The value to clamp.
        """

        if value > self.speed:
            return self.speed
        elif value < -self.speed:
            return -self.speed
        else:
            return value

    def rotate(self):
        """
        Rotates the player based off their velocity vector.
        """

        if self.vel_vector.x < -0.1:  # Moving right
            self.rotation = math.pi / 2

            if self.vel_vector.y > 0.1:  # Moving down right
                self.rotation = (3 / 4) * math.pi
            elif self.vel_vector.y < -0.1:  # Moving down left
                self.rotation = math.pi / 4

        elif self.vel_vector.x > 0.1:  # Moving left
            self.rotation = (3 / 2) * math.pi

            if self.vel_vector.y > 0.1:  # Moving down left
                self.rotation = (5 / 4) * math.pi
            elif self.vel_vector.y < -0.1:  # Moving up left
                self.rotation = (7 / 4) * math.pi

        elif self.vel_vector.y > 0.1:  # Moving down
            self.rotation = math.pi
        elif self.vel_vector.y < -0.1:  # Moving up
            self.rotation = 0

    def get_pos(self):
        return self.pos_vector

    def get_rotation_rad(self):
        return self.rotation

    def get_rotation(self):
        return self.rotation * (180 / math.pi)

    def set_speed(self, speed):
        self.speed = speed

    def update(self):
        self.vel_vector = Vector(self.check_out_range(self.vel_vector.x), self.check_out_range(self.vel_vector.y))
        self.rotate()
        self.pos_vector.add(self.vel_vector)
        self.vel_vector.multiply(0.3)  # Dampens movement when coming to a stop


class TrashMovement(Movement):
    def __init__(self, speed, pos_vector, target=None):
        super().__init__(speed, pos_vector)
        self.target = target

    def move_towards_target(self):
        """
        Moves the trash towards a particular target.
        """

        delta_x = self.target.x - self.pos_vector.x
        delta_y = self.target.y - self.pos_vector.y

        # Ensures there are no division by zero errors when normalising
        if delta_x == 0 and delta_y == 0:
            return

        magnitude = Vector(delta_x, delta_y).length()

        # Normalised vector from delta x & delta y
        target_vector = Vector(delta_x, delta_y).normalise()
        self.vel_vector.add(target_vector.multiply(self.speed / (magnitude)))

    def get_distance_to_target(self):
        """
        Gets the distance from the trash item to the target.
        :return: The distance between the trash item and the target.
        """

        delta_x = self.target.x - self.pos_vector.x
        delta_y = self.target.y - self.pos_vector.y

        magnitude = Vector(delta_x, delta_y).length()

        return magnitude

    def set_position(self, position):
        self.pos_vector = position

from source.vector import Vector


class Movement:
    def __init__(self, speed, pos_vector):
        self.speed = speed
        self.pos_vector = pos_vector
        self.vel_vector = Vector()
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


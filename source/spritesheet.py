import pygame


class Spritesheet:
    def __init__(self, file_path, num_rows, num_cols):
        self.num_rows = num_rows
        self.num_cols = num_cols

        self.spritesheet = pygame.image.load(file_path).convert_alpha()
        self.spritesheet_dimensions = [self.spritesheet.get_width(), self.spritesheet.get_height()]

        self.frame_width = self.spritesheet_dimensions[0] / num_cols
        self.frame_height = self.spritesheet_dimensions[1] / num_rows

        self.current_frame = 1  # Sets the initial animation frame
        self.current_col = 1

    def draw(self, screen, pos_vector, rotation=0, frame_index=None, size=None):

        if frame_index is not None:
            self.current_frame = frame_index

        # Finding the current frame dimensions

        while self.current_frame > self.num_rows:
            self.current_frame -= self.num_rows
            self.current_col += 1

        # Selecting the current frame in the image

        location = pygame.Rect(self.frame_width * (self.current_col - 1),
                               self.frame_height * (self.current_frame - 1),
                               self.frame_width,
                               self.frame_height
                               )

        cropped = pygame.Surface((self.frame_width, self.frame_height))
        cropped.blit(self.spritesheet, (0, 0), location)

        cropped = pygame.transform.rotate(cropped, rotation)

        if size is not None:
            cropped = pygame.transform.scale(cropped, (int(size[0]), int(size[1])))

        corrected_rotations = [45, 135, 225, 315]

        if int(rotation) in corrected_rotations:
            cropped = pygame.transform.scale(cropped, (int(cropped.get_width() * 1.4), int(cropped.get_height() * 1.4)))

        pygame.Surface.set_colorkey(cropped, (0, 0, 0))

        screen.blit(cropped, (pos_vector.x, pos_vector.y))

    # Increments the sprite's frame
    def next_frame(self):
        # Resets the current frame if the current frame exceeds the total number of frames
        if (self.current_frame * self.current_col) + 1 > self.num_rows * self.num_cols:
            self.current_frame = 1
            self.current_col = 1
        else:
            self.current_frame += 1

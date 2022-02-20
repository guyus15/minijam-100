class TimeManager:
    time = 0  # The initial clock time

    @classmethod
    def tick(cls):
        cls.time += 1

    @classmethod
    def transition(cls, frame_duration):
        # Used to check if a sufficient amount of time has passed

        if cls.time % frame_duration == 0:
            return True
        else:
            return False

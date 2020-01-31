from repairship.graphics import graphics_utils


class Animation:
    def __init__(self, sheet, frame_width, speed):
        """

        :type sheet: pygame.Surface
        :param frame_width:
        """
        self.sheet = sheet
        self.frame_width = frame_width
        self.speed = speed

        self.frames_amount = int(self.sheet.get_width() / self.frame_width)

        self.frames = self.init_fames()

    def init_fames(self):
        frames = list()
        frames_rects = graphics_utils.slice_animation(self.frame_width, self.frame_width, self.frames_amount)

        for rect in frames_rects:
            frame = graphics_utils.image_at(self.sheet, rect)
            frames.append(frame)

        return frames

    def get_frame_idx_at(self, time):
        return int(time / self.speed) % self.frames_amount

    def get_frame_at(self, time):
        idx = self.get_frame_idx_at(time)
        frame = self.frames[idx]
        return frame

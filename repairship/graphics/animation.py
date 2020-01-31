from repairship.graphics import graphics_utils


class Animation:
    def __init__(self, sheet, size, speed):
        """

        :type sheet: pygame.Surface
        :param size:
        """
        self.sheet = sheet
        self.size = size
        self.speed = speed

        self.frames_amount = int(self.sheet.get_width() / self.size.width)

        self._frames = self.init_fames()

    def init_fames(self):
        frames = list()
        frames_rects = graphics_utils.slice_animation(self.size.width, self.size.height, self.frames_amount)

        for rect in frames_rects:
            frame = graphics_utils.image_at(self.sheet, rect)
            frames.append(frame)

        return frames

    def get_frame(self, idx):
        return self._frames[idx]

    def get_frame_idx_at(self, time):
        return int(time / self.speed) % self.frames_amount

    def get_frame_at(self, time):
        idx = self.get_frame_idx_at(time)
        frame = self.get_frame(idx)
        return frame

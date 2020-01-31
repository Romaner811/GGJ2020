
import abc
import collections
import pygame
from pygame.locals import *


DEFAULT_FPS = 60

EVENT_ID_ANY = USEREVENT + 1
EVENT_ID_FRAME = USEREVENT + 2
EVENT_ID_UPDATE = USEREVENT + 3
EVENT_ID_SONG_END = USEREVENT + 4


class GameApp(abc.ABC):
    def __init__(self, size, fps=None):
        if fps is None:
            fps = DEFAULT_FPS

        self.size = size
        self.tick_interval = int(1000 / fps)

        self._is_running = False
        self._listeners = collections.defaultdict(list)

        self.event_subscribe(EVENT_ID_ANY, self.on_event)
        self.event_subscribe(EVENT_ID_FRAME, self.on_frame)

        pygame.init()
        self.screen = pygame.display.set_mode(size.get_pair())

    def event_subscribe(self, event_type, handler_func):
        self._listeners[event_type].append(handler_func)

    @abc.abstractmethod
    def on_frame(self, event):
        pass

    def on_event(self, event):
        pass

    def on_exit(self, event):
        return True

    def flush_screen(self):
        pygame.display.flip()

    def _execute_event_handlers(self, handlers, event):
        if handlers is None:
            return

        for handler in handlers:
            try:
                handler(event)
            except RuntimeError as e:
                # TODO: exc handling
                pass

    def _handle_event(self, event):
        if event.type == pygame.QUIT:
            if self.on_exit(event):
                self._is_running = 0

        any_event_handlers = self._listeners.get(EVENT_ID_ANY)
        handlers = self._listeners.get(event.type)

        self._execute_event_handlers(handlers, event)
        self._execute_event_handlers(any_event_handlers, event)

    def start(self):
        pygame.time.set_timer(EVENT_ID_FRAME, self.tick_interval)
        self._is_running = True

    def stop(self):
        pygame.time.set_timer(EVENT_ID_FRAME, 0)
        self._is_running = False

    def run(self):
        try:
            self.start()
            while self._is_running:
                event = pygame.event.wait()
                self._handle_event(event)
        finally:
            self.stop()

    def __del__(self):
        pygame.quit()

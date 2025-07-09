class Todo:
    def __init__(self, title: str, is_completed: bool = False) -> None:
        self.title = title
        self.is_completed = is_completed

    def set_completed(self) -> None:
        self.is_completed = True
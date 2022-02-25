class Book:
    title: str
    page: int

    def __init__(self, title: str, page: int = 0) -> None:
        self.title = title
        self.page = page
    def __str__(self) -> str:
        return f"Title: {self.title}\nPage: {self.page}"

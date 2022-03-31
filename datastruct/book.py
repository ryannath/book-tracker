class Book:
    title: str
    author: str
    cur_page: int
    rating: int    

    def __init__(
        self, title: str = "Unknown Book", author:str = "unknown",
        page: int = 0, rating: int = 0
        ) -> None:

        self.title = title
        self.author = "unknown"
        self.page = page
        self.rating = rating

    def __str__(self) -> str:
        return f"Title: {self.title}\nPage: {self.page}\nRating: {self.rating}"

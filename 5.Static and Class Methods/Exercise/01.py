class PhotoAlbum:
    PAGE_PHOTOS = 4
    SUCCESS = 'photo added successfully on page'
    FAILED = 'No more free slots'
    DASHES = f'{11 * "-"}\n'

    def __init__(self, pages: int):
        self.pages = int(pages)
        self.photos = [[] for _ in range(pages)]
        self.pindex = 0

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = int(photos_count) // cls.PAGE_PHOTOS
        return cls(pages)

    def is_space(self):
        return self.pindex < self.pages and len(self.photos[self.pindex]) < self.PAGE_PHOTOS

    def page_new(self):
        if len(self.photos[self.pindex]) == self.PAGE_PHOTOS:
            self.pindex += 1
        return self.pindex

    def add_photo(self, label) -> str:
        if not self.is_space():
            return self.FAILED
        self.photos[self.pindex].append(str(label))
        p_added = f'{label} photo added successfully on page {self.pindex + 1} slot {len(self.photos[self.pindex])}'
        self.page_new()
        return p_added

    def display(self) -> str:
        displ = self.DASHES
        if self.photos:
            for _ in self.photos:
                if _:
                    displ += ''.join('[] ' for p in range(len(_))).strip()
                displ += f'\n{self.DASHES}'
            return displ


import unittest


class TestsPhotoAlbum(unittest.TestCase):
    def test_init_creates_all_attributes(self):
        album = PhotoAlbum(2)
        self.assertEqual(album.pages, 2)
        self.assertEqual(album.photos, [[], []])

    def test_from_photos_should_create_instace(self):
        album = PhotoAlbum.from_photos_count(12)
        self.assertEqual(album.pages, 3)
        self.assertEqual(album.photos, [[], [], []])

    def test_add_photo_with_no_free_spots(self):
        album = PhotoAlbum(1)
        album.add_photo("baby")
        album.add_photo("first grade")
        album.add_photo("eight grade")
        album.add_photo("party with friends")
        result = album.add_photo("prom")
        self.assertEqual(result, "No more free slots")

    def test_add_photo_with_free_spots(self):
        album = PhotoAlbum(1)
        album.add_photo("baby")
        album.add_photo("first grade")
        album.add_photo("eight grade")
        album.add_photo("party with friends")
        self.assertEqual(album.photos, [['baby', 'first grade', 'eight grade', 'party with friends']])

    def test_display_with_one_page(self):
        album = PhotoAlbum(1)
        album.add_photo("baby")
        album.add_photo("first grade")
        album.add_photo("eight grade")
        album.add_photo("party with friends")
        result = album.display().strip()
        self.assertEqual(result, "-----------\n[] [] [] []\n-----------")

    def test_display_with_three_pages(self):
        album = PhotoAlbum(3)
        for _ in range(8):
            album.add_photo("asdf")
        result = album.display().strip()
        self.assertEqual(result, "-----------\n[] [] [] []\n-----------\n[] [] [] []\n-----------\n\n-----------")


if __name__ == "__main__":
    unittest.main()
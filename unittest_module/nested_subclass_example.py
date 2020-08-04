class TestAddUnmarkedChild(unittest.TestCase):
    """Tests for the method that adds a copy of the parent's board as a
    child."""

    def setUp(self):
        self.tree = GameTree()

    class TestTwoMarksOnRoot:

        def setUp(self):
            self.tree._add_root("test")

        def testplaceholder(self):
            print("placeholder")

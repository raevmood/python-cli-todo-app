import unittest
from task import Task

class TestTask(unittest.TestCase):
    def test_mark_complete(self):
        task = Task(1, "Test", "Desc")
        self.assertFalse(task.completed)
        task.mark_complete()
        self.assertTrue(task.completed)

    def test_to_dict(self):
        task = Task(1, "T", "D", "2025-12-25")
        expected = {
            "id": 1,
            "title": "T",
            "description": "D",
            "due_date": "2025-12-25",
            "completed": False
        }
        self.assertEqual(task.to_dict(), expected)

if __name__ == "__main__":
    unittest.main()
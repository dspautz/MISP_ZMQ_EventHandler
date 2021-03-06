from src.models.status import Status
import unittest
import json
import os


class StatusModelTest(unittest.TestCase):
    """Status Model test cases."""

    @classmethod
    def setupClass(cls):
        try:
            status = open(os.path.abspath(os.path.join(os.path.dirname(__file__), '../templates/models/status.json')))
            cls.status = json.load(status)
        except NameError as e:
            raise Exception('No Status Model Class defined!')

    @classmethod
    def teardownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass  # clean up

    def test_from_json(self):
        status = Status.from_json(self, self.status)
        self.assertIsInstance(status, Status)
        self.assertTrue(hasattr(status, "status"))
        self.assertEqual(status.status, "I'm doing science and I'm still alive.")
        self.assertTrue(hasattr(status, "uptime"))
        self.assertEqual(status.uptime, 9170)

    def test_to_json(self):
        status = Status.from_json(self, self.status)
        self.assertDictEqual(status.to_json(), self.status)

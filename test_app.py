#https://jobs.github.com/api

import unittest
from unittest.mock import patch, Mock
from job_search_app import Job_engine


class Test_app(unittest.TestCase):

    def test_get_position(self):
        mock_get_patcher = patch('job_search_app.requests.get')

        fake_json = [{
            "company": "WELL Health",
            "company_url": "null",
            "created_at": "Fri Jan 22 02:23:54 UTC 2021",
            "description": "null",
            "how_to_apply": "follow the link and fill in the form",
            "id": "98701506-35a3-4490-807c-73e5f4066d45",
            "location": "United States",
            "title": "Senior Backend Software Engineer",
            "type": "Full Time",
            "url": "https://jobs.github.com/positions/98701506-35a3-4490-807c-73e5f4066d45"
        }]

        mock_get = mock_get_patcher.start()

        mock_get.return_value = Mock(status_code=200)
        mock_get.return_value.json.return_value = fake_json

        obj = Job_engine()
        response = obj.get_positions("java, python", "true", "usa")

        self.assertEqual(response.json(), fake_json)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()

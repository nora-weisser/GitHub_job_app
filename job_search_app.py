import requests
import json


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)
    return text

class Job_engine():
    def get_positions(self, description, full_time, location):

        parameters = {
            'description': description,
            'full_time': full_time,
            'location': location
        }
        job_search = requests.get('https://jobs.github.com/positions.json', params=parameters)
        return job_search

def main():
    print('Please, enter key words sepasrated by comma')
    description = input()

    print('If you need to find full-time job, enter "true", if not - "false"')
    full_time = input()

    print('Please, enter desired location')
    location = input()

    find_process = Job_engine()
    result = find_process.get_positions(description, full_time, location)
    jprint(result.json())

if __name__ == "__main__":
    main()

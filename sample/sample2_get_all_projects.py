from decouple import config

import todoist

TODOIST_API_KEY = config("TODOIST_API_KEY")

def main():
    api = todoist.TodoistAPI(TODOIST_API_KEY)
    api.sync()

    for project in api.state['projects']:
        # see: project object document.
        # https://developer.todoist.com/sync/v8/#projects

        print(project['name'])

if __name__ == "__main__":
    main()

from decouple import config

import todoist

TODOIST_API_KEY = config("TODOIST_API_KEY")

def main():
    api = todoist.TodoistAPI(TODOIST_API_KEY)
    api.sync()

    for item in api.state['items']:
        # see: item object document.
        # https://developer.todoist.com/sync/v8/#items

        print(item['content'])

if __name__ == "__main__":
    main()

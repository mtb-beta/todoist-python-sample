from decouple import config

import todoist

TODOIST_API_KEY = config("TODOIST_API_KEY")

class TodoistApp():

    def __init__(self):
        self.api = todoist.TodoistAPI(TODOIST_API_KEY)
        self.api.sync()

    @property
    def projects(self):
        return self.api.state['projects']

    @property
    def inbox(self):
        for project in self.projects:
            if project['name'] == "Inbox":
                return project

    @property
    def items(self):
        return self.api.state['items']

    def get_items(self, project=None):
        items = []
        for item in self.items:
            if item['project_id'] == self.inbox['id']:
                items.append(item)
        return items

def main():
    app = TodoistApp()
    
    items = app.get_items(project=app.inbox)

    for item in items:
        print(item['content'])

if __name__ == "__main__":
    main()

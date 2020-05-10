from decouple import config

import todoist

TODOIST_API_KEY = config("TODOIST_API_KEY")


class ItemList:
    def __init__(self, items):
        self.items = items

    def all(self):
        return self.items

    def is_display(self):
        return [
            item for item in self.items
            if not item['checked'] and not item['is_deleted']
        ]

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
        self._items = ItemList(self.api.state['items'])
        return self._items.is_display()

    def get_items(self, project=None):
        if not project:
            self.items

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

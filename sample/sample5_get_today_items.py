from datetime import date, datetime

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

    def filter_project(self, project):
        return [
            item for item in self.items
            if item['project_id'] == project['id']
        ]

    def filter_date(self, date):
        result = []
        for item in self.items:
            if not 'due' in item or not item['due']:
                continue

            item_due_date = datetime.strptime(item['due']['date'], '%Y-%m-%d').date()
            if item_due_date == date:
                result.append(item)
        return result

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

    def get_items(self, project=None, date=None):
        items = ItemList(self.items)
        if project:
            items = items.filter_project(project)

        if date:
            items = items.filter_date(date)

        return items

def main():
    app = TodoistApp()
    items = app.get_items(date=date.today())

    for item in items:
        print(item['content'])

if __name__ == "__main__":
    main()

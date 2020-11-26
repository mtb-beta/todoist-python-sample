from decouple import config

import todoist

TODOIST_API_KEY = config("TODOIST_API_KEY")


def main():
    """
    全てのプロジェクトを表示するサンプル
    """
    api = todoist.TodoistAPI(TODOIST_API_KEY)
    api.sync()

    for project in api.state["projects"]:
        # see: project object document.
        # https://developer.todoist.com/sync/v8/#projects

        # アーカイブされているものは飛ばす
        if project["is_archived"]:
            continue

        # 削除されているものも飛ばす
        if project["is_deleted"]:
            continue

        print(project["id"], project["name"])


if __name__ == "__main__":
    main()

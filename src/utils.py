import os

DATASHEET_ID_PATH = "../secrets/datasheet_id.txt"


def get_datasheet_id():
    if os.path.exists(DATASHEET_ID_PATH):
        print("Using Datasheet ID from file")
        with open(DATASHEET_ID_PATH, "r") as f:
            datasheet_id = f.read()
    elif "DATASHEET_ID" in os.environ:
        print("Using Datasheet ID from environment")
        datasheet_id = os.environ["DATASHEET_ID"]
    else:
        raise Exception("No Datasheet ID found")
    return datasheet_id


def remove_html_margins(path):
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    with open(path, "w", encoding="utf-8") as f:
        for line in lines:
            if "<head>" in line:
                f.write(
                    line.replace("<head>", "<head><style>body { margin: 0; }</style>")
                )
            else:
                f.write(line)

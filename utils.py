import os

DATASHEET_ID_PATH = "secrets/datasheet_id.txt"

colors_dict = {
    "red": "#e41a1c",
    "orange": "#ff7f00",
    "blue": "#377eb8",
    "pink": "#f781bf",
    "yellow": "#dede00",
    "green": "#4daf4a",
    "grey": "#999999",
    "purple": "#984ea3",
}
COLORS = ["blue", "orange", "red", "green", "pink", "yellow", "purple"]
COLORS = [colors_dict[i] for i in COLORS]


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


def flatten(list_of_lists):
    flattened_list = []
    for i in list_of_lists:
        if isinstance(i, list):
            flattened_list += i
        else:
            flattened_list.append(i)
    return flattened_list

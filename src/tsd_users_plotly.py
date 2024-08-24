from utils import get_datasheet_id, remove_html_margins, COLORS, flatten
import pandas as pd
import requests
import plotly.express as px

DATASET_PATH = "../data/tsd-users.csv"

datasheet_id = get_datasheet_id()
r = requests.get(
    f"https://docs.google.com/spreadsheet/ccc?key={datasheet_id}&output=csv"
)
with open(DATASET_PATH, "wb") as f:
    f.write(r.content)

users = pd.read_csv(DATASET_PATH)
users = users[users["Active"]]


def generate_tsd_reach_plot():
    hover_data = {"Name": False, "Link": True}
    fig = px.bar(
        users[users["Total reach"] > 0],
        x="Name",
        y="Total reach",
        color="Type",
        hover_data=hover_data,
        hover_name="Name",
        template="plotly_dark",
        log_y=True,
        color_discrete_sequence=COLORS,
    )

    fig.update_layout(
        title_text="<b>Global reach of The Space Devs users</b>"
        + r"<br><sup>Limited to known users who agreed to share their analytics</sup>",
        xaxis_title=None,
        yaxis_title="Total users worldwide across all platforms",
    )

    fig.write_html("../plots/users_ranking.html")
    remove_html_margins("../plots/users_ranking.html")


def generate_tsd_user_types_plot():
    unique_types = list(
        set(
            [
                s.strip()
                for s in flatten(
                    [s.split(",") for s in users["Type"].unique().tolist()]
                )
            ]
        )
    )
    type_counts = {}
    type_users_list = {}
    for unique_type in unique_types:
        type_counts[unique_type] = 0
        type_users_list[unique_type] = []

    for index, row in users.iterrows():
        user_types = row["Type"].split(",")
        for user_type in user_types:
            type_counts[user_type.strip()] += 1
            type_users_list[user_type.strip()].append(row["Name"])

    for user_type in type_users_list:
        type_users_list[user_type] = "<br>".join(type_users_list[user_type])

    df = pd.DataFrame(
        {
            "type": type_counts.keys(),
            "count": type_counts.values(),
            "users": type_users_list.values(),
        }
    ).sort_values("count", ascending=False)
    fig = px.pie(
        df,
        values="count",
        names="type",
        title="<b>Known services using The Space Devs data</b>",
        template="plotly_dark",
        hole=0.6,
        hover_data="users",
        color_discrete_sequence=COLORS,
    )
    fig.update_traces(textposition="inside", textinfo="value+label")

    fig.write_html("../plots/user_types.html")
    remove_html_margins("../plots/user_types.html")

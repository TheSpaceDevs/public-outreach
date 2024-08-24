from utils import get_datasheet_id, remove_html_margins
import pandas as pd
import requests
import plotly.express as px

DATASET_PATH = "../data/tsd-users.csv"

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

# def get_dataset():
datasheet_id = get_datasheet_id()

# Get dataset and save to file
r = requests.get(
    f"https://docs.google.com/spreadsheet/ccc?key={datasheet_id}&output=csv"
)
with open(DATASET_PATH, "wb") as f:
    f.write(r.content)

users = pd.read_csv(DATASET_PATH)

hover_data = ["Link"]
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
    # updatemenus=[
    #     dict(
    #         type="buttons",
    #         direction="up",
    #         xanchor="right",
    #         x=1,
    #         pad={"r": 10, "t": 10},
    #         buttons=list(
    #             [
    #                 dict(
    #                     args=[{"yaxis.type": "log"}],
    #                     label="Log Scale",
    #                     method="relayout",
    #                     # make it better for dark theme
    #                 ),
    #                 dict(
    #                     args=[{"yaxis.type": "linear"}],
    #                     label="Linear Scale",
    #                     method="relayout",
    #                 ),
    #             ]
    #         ),
    #     ),
    # ],
)

fig.write_html("../plots/users_ranking.html")
remove_html_margins("../plots/users_ranking.html")

# return pd.read_csv(DATASET_PATH)

# def generate_plots():
# dataset = get_dataset()
# dataset.plot(x="Date", y="Users")

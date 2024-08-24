from utils import get_datasheet_id, remove_html_margins
import pandas as pd
import plotly.express as px
import requests

DATASET_PATH = "../data/tsd-users.csv"

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
    log_y=True,
)
# fig = px.histogram(
#     users,
#     x="Total reach",
#     color="Type",
#     marginal="rug",
#     hover_data=hover_data,
#     hover_name="Name",
#     template="plotly_dark",
#     # nbins=int(number_of_bins),
#     # color_discrete_sequence=colors[:-1],
# )
# fig.update_layout(
#     yaxis_title="Total launches per year",
#     xaxis_range=[
#         datetime(1957, 1, 1, 0, 0, 0),
#         datetime(datetime.now().year, 12, 31, 23, 59, 59),
#     ],
#     yaxis_range=[0, ceil(data.Date.dt.year.value_counts().max() / 10) * 10 + 27],
#     title_text="Orbital launch attempts per country since "
#     + str(PastT0s.net.dt.year.min())
#     + subtitle_html,
#     legend_title="Launch Country",
# )

fig.update_layout(
    xaxis_title=None,
    updatemenus=[
        dict(
            type="buttons",
            direction="up",
            xanchor="right",
            x=1,
            pad={"r": 10, "t": 10},
            buttons=list(
                [
                    dict(
                        args=[{"yaxis.type": "log"}],
                        label="Log Scale",
                        method="relayout",
                    ),
                    dict(
                        args=[{"yaxis.type": "linear"}],
                        label="Linear Scale",
                        method="relayout",
                    ),
                ]
            ),
        ),
    ],
)

fig.write_html("../plots/test.html")
remove_html_margins("../plots/test.html")

# return pd.read_csv(DATASET_PATH)


# def generate_plots():
# dataset = get_dataset()
# dataset.plot(x="Date", y="Users")

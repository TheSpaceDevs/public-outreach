from src.tsd_users_plotly import generate_tsd_reach_plot, generate_tsd_user_types_plot

if __name__ == "__main__":
    generate_tsd_reach_plot()
    generate_tsd_user_types_plot()

    # Exit successfully
    print("All done!")
    exit(code=0)

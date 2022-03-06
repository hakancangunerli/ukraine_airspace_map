import plotly.express as px
import plotly.graph_objects as go


def visualize(flight_df,x):

    fig = px.scatter_geo(flight_df, lat="lat", lon="long", hover_name="callsign", color = "lat", color_continuous_scale=px.colors.sequential.RdBu)
    fig.update_geos(lataxis_showgrid=True, lonaxis_showgrid=True)

    fig.update_layout(height=300, width=600)

    fig.update_layout(
        geo_scope=str(x),
        title_text="Flights in " + str(x),
        autosize=True,
        width=1000,
        height=1000,
        margin=dict(
            l=50,
            r=50,
            b=100,
            t=100,
            pad=4
        ),
    ),

    
    fig.write_image("./fig.png")
    
    return fig
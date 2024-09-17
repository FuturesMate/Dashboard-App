import streamlit as st
import pandas as pd
import altair as alt

# Sidebar with selection
category = st.sidebar.selectbox(
    "Choose category",
    ("NQ Session Ranges", "Midnight Retracement", "Other")
)

# Display the chosen category
st.write(f"{category}")

# Add logic for each category
if category == "NQ Session Ranges":

    # Create tabs for different sessions
    tab1, tab2, tab3, tab4 = st.tabs(["New York", "London", "Tokyo", "Daily"])

    # Define the custom sorting order for days of the week
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

    # Set the Y-axis max scale to 500 points
    y_axis_avg_scale = alt.Scale(domain=[0, 350])
    y_axis_max_scale = alt.Scale(domain=[0, 1000])
    y_axis_min_scale = alt.Scale(domain=[0, 200])

    # New York Session Tab
    with tab1:
        st.write("### New York Session Stats")

        # Load data for New York session
        df_ny = pd.read_csv('data_new_york_session.csv')

        # Filter out any unnecessary rows if needed
        df_ny = df_ny[df_ny['Day'] != 'New York Session']

        # Create a bar chart for the Average points
        chart_avg = alt.Chart(df_ny).mark_bar().encode(
            x=alt.X('Day:N', title='', sort=day_order, axis=alt.Axis(labelAngle=0)),
            y=alt.Y('Average:Q', title='Average Points'),
            color=alt.value('#089981'),  # Consistent color for all bars
            tooltip=['Day', 'Average']  # Tooltip for more details
        ).properties(
            width=600
        )

        # Create a bar chart for the Max points
        chart_max = alt.Chart(df_ny).mark_bar().encode(
            x=alt.X('Day:N', title='', sort=day_order, axis=alt.Axis(labelAngle=0)),
            y=alt.Y('Max:Q', title='Max Points'),
            color=alt.value('#F39C12'),  # Consistent color for all bars
            tooltip=['Day', 'Max']  # Tooltip for more details
        ).properties(
            width=600
        )

        # Create a bar chart for the Min points
        chart_min = alt.Chart(df_ny).mark_bar().encode(
            x=alt.X('Day:N', title='', sort=day_order, axis=alt.Axis(labelAngle=0)),
            y=alt.Y('Min:Q', title='Min Points'),
            color=alt.value('#E74C3C'),  # Consistent color for all bars
            tooltip=['Day', 'Min']  # Tooltip for more details
        ).properties(
            width=600
        )

        # Display the charts in a vertical sequence
        st.altair_chart(chart_avg, use_container_width=True)
        st.altair_chart(chart_max, use_container_width=True)
        st.altair_chart(chart_min, use_container_width=True)

    # London Session Tab
    with tab2:
        st.write("### London Session Stats")

        # Load data for London session
        df_london = pd.read_csv('data_london_session.csv')
        # Filter out any unnecessary rows if needed
        df_london = df_london[df_london['Day'] != 'London Session']

        # Create a bar chart for the London session
        chart_avg = alt.Chart(df_london).mark_bar().encode(
            x=alt.X('Day:N', title='', sort=day_order, axis=alt.Axis(labelAngle=0)),
            y=alt.Y('Average:Q', title='Average Points'),
            color=alt.value('#089981'),  # Consistent color for all bars
            tooltip=['Day', 'Average']  # Tooltip for more details
        ).properties(
            width=600
        )

        # Create a bar chart for the Max points
        chart_max = alt.Chart(df_london).mark_bar().encode(
            x=alt.X('Day:N', title='', sort=day_order, axis=alt.Axis(labelAngle=0)),
            y=alt.Y('Max:Q', title='Max Points'),
            color=alt.value('#F39C12'),  # Consistent color for all bars
            tooltip=['Day', 'Max']  # Tooltip for more details
        ).properties(
            width=600
        )

        # Create a bar chart for the Min points
        chart_min = alt.Chart(df_london).mark_bar().encode(
            x=alt.X('Day:N', title='', sort=day_order, axis=alt.Axis(labelAngle=0)),
            y=alt.Y('Min:Q', title='Min Points'),
            color=alt.value('#E74C3C'),  # Consistent color for all bars
            tooltip=['Day', 'Min']  # Tooltip for more details
        ).properties(
            width=600
        )
        # Display the chart
        st.altair_chart(chart_avg, use_container_width=True)
        st.altair_chart(chart_max, use_container_width=True)
        st.altair_chart(chart_min, use_container_width=True)

    # Tokyo Session Tab
    with tab3:
        st.write("### Tokyo Session Stats")

        # Load data for Tokyo session
        df_tokyo = pd.read_csv('data_tokyo_session.csv')

        # Create a bar chart for the Tokyo session
        chart_tokyo = alt.Chart(df_tokyo).mark_bar().encode(
            x=alt.X('Day:N', title='', sort=day_order, axis=alt.Axis(labelAngle=0)),
            y=alt.Y('Average:Q', title='Average Points', scale=y_axis_avg_scale),
            color=alt.value('#E74C3C'),  # Consistent color for all bars
            tooltip=['Day', 'Average']  # Tooltip for more details
        ).properties(
            width=600
        )

        # Display the chart
        st.altair_chart(chart_tokyo, use_container_width=True)

    # Daily Session Tab
    with tab4:
        st.write("### Daily Session Stats (coming soon!)")

else:
    st.write(f"### {category} Data (coming soon!)")

import os
port = os.environ.get('PORT', 8501)  # Default to 8501 if no PORT is set


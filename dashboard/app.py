# Dashboard app
import streamlit as st
import time
import pandas as pd
import plotly.express as px
from queries import get_recent_logs, get_stats

st.set_page_config(page_title="Heartbeat Monitor", layout="wide")

def main():
    st.title("💓 Heartbeat Monitor Dashboard")
    st.markdown("Real-time monitoring of customer heart rate data via Kafka and PostgreSQL.")

    # Sidebar for control
    st.sidebar.header("Settings")
    refresh_rate = st.sidebar.slider("Refresh rate (seconds)", 1, 10, 2)
    
    # Placeholder for status indicators
    col1, col2, col3 = st.columns(3)
    
    # Main content
    data_container = st.empty()
    stats_container = st.empty()

    while True:
        df = get_recent_logs(50)
        stats_df = get_stats()

        with data_container.container():
            if not df.empty:
                # Metrics
                avg_hr = df['heart_rate'].mean()
                total_logs = len(df)
                anomalies = len(df[df['status'] != 'NORMAL'])
                
                m1, m2, m3 = st.columns(3)
                m1.metric("Avg Heart Rate", f"{avg_hr:.1f} BPM")
                m2.metric("Total Logs (Recent)", total_logs)
                m3.metric("Anomalies", anomalies, delta=anomalies, delta_color="inverse")
                
                # Charts
                c1, c2 = st.columns(2)
                
                with c1:
                    st.subheader("Heart Rate over Time")
                    fig_line = px.line(df, x='timestamp', y='heart_rate', color='customer_id', 
                                     title="Recent Heartbeat Trends")
                    st.plotly_chart(fig_line, use_container_width=True)
                
                with c2:
                    st.subheader("Status Distribution")
                    if not stats_df.empty:
                        fig_pie = px.pie(stats_df, values='count', names='status', title="Overall Health Status")
                        st.plotly_chart(fig_pie, use_container_width=True)
                
                # Table
                st.subheader("Recent Logs")
                st.dataframe(df.style.applymap(
                    lambda x: 'background-color: #ffcccc' if x in ['BRADYCARDIA', 'TACHYCARDIA'] else '',
                    subset=['status']
                ), use_container_width=True)
            else:
                st.info("Waiting for data... Make sure the pipeline/pipeline_runner.py is running.")
        
        time.sleep(refresh_rate)

if __name__ == "__main__":
    main()

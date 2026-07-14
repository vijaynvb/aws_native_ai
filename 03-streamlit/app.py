import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(
    page_title="Marketing Campaigns",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main {
        padding-top: 0;
    }
    
    .header-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 30px;
        border-radius: 10px;
        color: white;
        margin-bottom: 30px;
    }
    
    .header-title {
        font-size: 32px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    
    .campaign-card {
        background: #f8f9fa;
        padding: 15px;
        border-radius: 8px;
        border-left: 4px solid #667eea;
        margin-bottom: 10px;
    }
    
    .status-badge {
        padding: 5px 10px;
        border-radius: 4px;
        font-size: 12px;
        font-weight: bold;
        display: inline-block;
        margin-right: 5px;
        margin-bottom: 5px;
    }
    
    .status-in-progress {
        background-color: #667eea;
        color: white;
    }
    
    .status-youtube {
        background-color: #FF0000;
        color: white;
    }
    
    .status-linkedin {
        background-color: #0A66C2;
        color: white;
    }
    
    .status-instagram {
        background-color: #E1306C;
        color: white;
    }
    
    .status-confirmed {
        background-color: #28a745;
        color: white;
    }
    
    .status-podcast {
        background-color: #FF6B35;
        color: white;
    }
    
    .profile-section {
        background: linear-gradient(135deg, #F093FB 0%, #F5576C 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
    
    .metric-box {
        background: white;
        padding: 15px;
        border-radius: 8px;
        text-align: center;
        border: 1px solid #e0e0e0;
    }
    
    .campaign-table {
        font-size: 14px;
    }
</style>
""", unsafe_allow_html=True)

# Sample data for campaigns
campaigns_data = {
    "Campaign": ["Holiday Push", "UGC Drive", "Black Friday Promo", "Partner Collaboration", "Retargeting Campaign", "End of Year Push", "Feature Spotlight", "Fall Launch", "Q3 Awareness", "Fall Launch"],
    "Brief": ["✓", "✓", "✓", "✓", "✓", "✓", "✓", "✓", "✓", "✓"],
    "Creatives": ["✓", "✓", "✓", "✓", "✓", "✓", "✓", "✓", "✓", "✓"],
    "Status": ["In progress", "In progress", "In progress", "In progress", "Planning", "In progress", "Draft", "Confirmed", "Confirmed", "Confirmed"],
    "Channel": ["YouTube", "LinkedIn", "Instagram", "Multiple", "Email", "YouTube", "Social", "YouTube", "Podcast", "Instagram"],
    "Date": ["Nov 02", "Nov 06", "Nov 22", "Oct 15", "Oct 28", "Dec 20", "Nov 10", "Oct 02", "Oct 06", "Oct 22"],
    "Campaign Type": ["Video production", "Brand awareness", "Social media", "Partnership", "Retargeting", "Year-end promo", "Product launch", "Video production", "Paid campaign", "Lead generation"]
}

df_campaigns = pd.DataFrame(campaigns_data)

# Header
with st.container():
    st.markdown("""
    <div class="header-container">
        <div class="header-title">📊 Marketing Campaigns</div>
        <p style="font-size: 16px; margin: 0;">Manage and track all your marketing campaigns in one place</p>
    </div>
    """, unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3 = st.tabs(["📋 Main Table", "📊 Gantt Chart", "🎯 Dashboard"])

with tab1:
    # Filters
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        status_filter = st.multiselect(
            "Filter by Status",
            options=df_campaigns["Status"].unique(),
            default=df_campaigns["Status"].unique()
        )
    
    with col2:
        channel_filter = st.multiselect(
            "Filter by Channel",
            options=df_campaigns["Channel"].unique(),
            default=df_campaigns["Channel"].unique()
        )
    
    with col3:
        sort_by = st.selectbox("Sort by", ["Campaign", "Date", "Status"])
    
    with col4:
        st.write("")
        st.write("")
        if st.button("🔄 Refresh", use_container_width=True):
            st.rerun()
    
    # Filter data
    filtered_df = df_campaigns[
        (df_campaigns["Status"].isin(status_filter)) &
        (df_campaigns["Channel"].isin(channel_filter))
    ]
    
    # Sort data
    if sort_by == "Date":
        filtered_df = filtered_df.sort_values("Date")
    elif sort_by == "Status":
        filtered_df = filtered_df.sort_values("Status")
    else:
        filtered_df = filtered_df.sort_values("Campaign")
    
    # Display table with custom styling
    st.markdown("### Active Campaigns")
    
    # Create custom table display
    for idx, row in filtered_df.iterrows():
        col1, col2, col3, col4, col5 = st.columns([2, 1, 2, 2, 1.5])
        
        with col1:
            st.markdown(f"**{row['Campaign']}**")
        
        with col2:
            # Status badge
            status = row["Status"]
            if "progress" in status.lower():
                badge_class = "status-in-progress"
            elif "confirmed" in status.lower():
                badge_class = "status-confirmed"
            else:
                badge_class = "status-in-progress"
            st.markdown(f'<span class="status-badge {badge_class}">{status}</span>', unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"🎯 {row['Campaign Type']}")
        
        with col4:
            st.markdown(f"📱 {row['Channel']}")
        
        with col5:
            st.markdown(f"📅 {row['Date']}")
        
        st.divider()

with tab2:
    st.markdown("### Gantt Chart Timeline")
    
    # Create sample gantt-like visualization
    gantt_data = []
    start_date = datetime.now()
    
    for idx, row in df_campaigns.iterrows():
        duration = np.random.randint(10, 30)
        gantt_data.append({
            "Campaign": row["Campaign"],
            "Start": start_date + timedelta(days=np.random.randint(0, 30)),
            "Duration": duration
        })
    
    # Display as a simple timeline
    for item in gantt_data:
        progress_percent = np.random.randint(20, 100)
        st.write(f"{item['Campaign']}")
        st.progress(progress_percent / 100)

with tab3:
    st.markdown("### Campaign Dashboard")
    
    # Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Campaigns", len(df_campaigns))
    
    with col2:
        in_progress = len(df_campaigns[df_campaigns["Status"].str.contains("progress", case=False)])
        st.metric("In Progress", in_progress)
    
    with col3:
        confirmed = len(df_campaigns[df_campaigns["Status"].str.contains("Confirmed", case=False)])
        st.metric("Confirmed", confirmed)
    
    with col4:
        planning = len(df_campaigns[df_campaigns["Status"].str.contains("Planning|Draft", case=False)])
        st.metric("Planning", planning)
    
    st.divider()
    
    # Status breakdown
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Status Distribution")
        status_counts = df_campaigns["Status"].value_counts()
        st.bar_chart(status_counts)
    
    with col2:
        st.markdown("### Channel Distribution")
        channel_counts = df_campaigns["Channel"].value_counts()
        st.bar_chart(channel_counts)
    
    st.divider()
    
    # Profile section
    st.markdown("""
    <div class="profile-section">
        <h3>✨ AI Brief Creator</h3>
        <p style="font-size: 18px; margin: 10px 0;">Rose, Brief Creator</p>
        <p style="font-size: 14px;">Generated 7 briefs</p>
    </div>
    """, unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("### 🎛️ Controls")
    
    with st.expander("Add New Campaign"):
        campaign_name = st.text_input("Campaign Name")
        campaign_type = st.selectbox("Campaign Type", ["Video production", "Brand awareness", "Social media", "Partnership", "Retargeting"])
        channel = st.multiselect("Channels", ["YouTube", "LinkedIn", "Instagram", "Podcast", "Email"])
        status = st.selectbox("Status", ["Planning", "In progress", "Confirmed", "Completed"])
        date = st.date_input("Target Date")
        
        if st.button("Create Campaign", use_container_width=True):
            st.success("✅ Campaign created successfully!")
    
    st.divider()
    
    with st.expander("Team Members"):
        st.markdown("""
        - 👤 Rose (Brief Creator)
        - 👤 Alex (Creative Lead)
        - 👤 Jordan (Campaign Manager)
        - 👤 Sam (Analyst)
        """)
    
    st.divider()
    
    with st.expander("About"):
        st.markdown("""
        **Marketing Campaign Manager**
        
        A comprehensive tool to manage marketing campaigns with real-time tracking, 
        team collaboration, and AI-powered brief generation.
        
        Built with Streamlit & AWS Services
        """)

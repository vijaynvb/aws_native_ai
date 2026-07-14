import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(
    page_title="Ness, AI Services",
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
        <div class="header-title">📊 Ness, AI Services</div>
        <p style="font-size: 16px; margin: 0;">Manage and track all your marketing campaigns in one place</p>
    </div>
    """, unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["🎯 Dashboard", "📋 Analyze Sentiment", "📊 PII Data Extraction", "Transcribe Audio File"])

with tab1:

    # Display table with custom styling
    st.markdown("### Quick links for the services")
    


with tab2:
    st.markdown("### Analyze Sentiment given text")
    
    user_input = st.text_input("Enter text to analyze sentiment", key="sentiment_input")

    import boto3

    comprehend = boto3.client('comprehend', region_name='us-east-1')

    

    if st.button("Analyze Sentiment", key="analyze_sentiment_button"):
        if user_input.strip() == "":
            st.warning("Please enter some text to analyze.")
        else:
            # Placeholder for sentiment analysis logic
            response = comprehend.detect_sentiment(Text=user_input, LanguageCode='en')
            st.success(f"Sentiment Analysis Result: **{response['Sentiment']}**")

with tab3:
    st.markdown("### Extract PII Data from text")
    
    pii_input = st.text_area("Enter text to extract PII data", key="pii_input")

    if st.button("Extract PII Data", key="extract_pii_button"):
        if pii_input.strip() == "":
            st.warning("Please enter some text to extract PII data.")
        else:
            # Placeholder for PII extraction logic
            pii_result = {
                "Names": ["John Doe"],
                "Emails": ["john.doe@example.com"]
            }
            st.success("PII Data Extraction Result:")
            for category, items in pii_result.items():
                st.write(f"**{category}:** {', '.join(items)}")

# Sidebar
with st.sidebar:
    st.markdown("### 🎛️ Controls")
    
    

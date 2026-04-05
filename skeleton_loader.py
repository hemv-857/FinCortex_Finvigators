"""
Skeleton loading screen component for CFO OS dashboard.
Displays placeholder UI while content is loading.
"""
import streamlit as st


def inject_skeleton_css():
    """Inject CSS for skeleton loading animation."""
    st.markdown("""
    <style>
    @keyframes skeleton-shimmer {
        0% {
            background-position: -1000px 0;
        }
        100% {
            background-position: 1000px 0;
        }
    }

    .skeleton-loader {
        background: linear-gradient(
            90deg,
            rgba(125, 211, 252, 0.1) 0%,
            rgba(125, 211, 252, 0.2) 20%,
            rgba(125, 211, 252, 0.1) 40%,
            rgba(125, 211, 252, 0.1) 100%
        );
        background-size: 1000px 100%;
        animation: skeleton-shimmer 2s infinite;
        border-radius: 12px;
        height: 20px;
        margin: 10px 0;
    }

    .skeleton-title {
        height: 32px;
        margin-bottom: 16px;
        border-radius: 8px;
    }

    .skeleton-text {
        height: 16px;
        margin-bottom: 8px;
        border-radius: 4px;
    }

    .skeleton-paragraph {
        display: flex;
        flex-direction: column;
        gap: 8px;
        margin-bottom: 16px;
    }

    .skeleton-paragraph .skeleton-text:last-child {
        width: 80%;
    }

    .skeleton-card {
        position: relative;
        overflow: hidden;
        background: linear-gradient(145deg, rgba(16, 37, 61, 0.72), rgba(7, 17, 31, 0.52));
        border: 1px solid rgba(255, 255, 255, 0.14);
        border-radius: 28px;
        padding: 24px;
        margin-bottom: 16px;
        box-shadow: 0 24px 60px rgba(0, 0, 0, 0.28);
        backdrop-filter: blur(22px);
    }

    .skeleton-metric {
        display: flex;
        flex-direction: column;
        gap: 12px;
    }

    .skeleton-metric-value {
        height: 40px;
        border-radius: 8px;
    }

    .skeleton-metric-label {
        height: 14px;
        border-radius: 4px;
        width: 60%;
    }

    .skeleton-chart {
        height: 300px;
        border-radius: 12px;
        margin: 16px 0;
    }

    .skeleton-table {
        width: 100%;
        margin-top: 16px;
    }

    .skeleton-table-row {
        display: flex;
        gap: 12px;
        margin-bottom: 12px;
    }

    .skeleton-table-cell {
        flex: 1;
        height: 16px;
        border-radius: 4px;
    }

    .loading-container {
        display: flex;
        flex-direction: column;
        gap: 24px;
        padding: 0;
    }

    .pulse {
        animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
    }

    @keyframes pulse {
        0%, 100% {
            opacity: 1;
        }
        50% {
            opacity: 0.5;
        }
    }

    .loading-header {
        text-align: center;
        margin-bottom: 32px;
        color: var(--text-muted);
    }

    .loading-spinner {
        display: inline-block;
        width: 32px;
        height: 32px;
        border: 3px solid rgba(125, 211, 252, 0.2);
        border-top-color: #7dd3fc;
        border-radius: 50%;
        animation: spin 1s linear infinite;
        margin-right: 12px;
    }

    @keyframes spin {
        to {
            transform: rotate(360deg);
        }
    }

    .loading-text {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 12px;
        font-size: 16px;
        color: var(--text-base);
    }
    </style>
    """, unsafe_allow_html=True)


def render_skeleton_metric(width: float = 1.0):
    """Render a skeleton placeholder for a metric card."""
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown(
            '<div class="skeleton-loader skeleton-metric-label"></div>',
            unsafe_allow_html=True
        )
    with col2:
        st.markdown(
            '<div class="skeleton-loader skeleton-metric-value" style="width: 60%;"></div>',
            unsafe_allow_html=True
        )


def render_skeleton_chart(height: int = 300):
    """Render a skeleton placeholder for a chart."""
    st.markdown(
        f'<div class="skeleton-loader skeleton-chart" style="height: {height}px;"></div>',
        unsafe_allow_html=True
    )


def render_skeleton_card(num_metrics: int = 3):
    """Render a skeleton placeholder for a content card."""
    with st.container():
        st.markdown(
            '<div class="skeleton-loader skeleton-title"></div>',
            unsafe_allow_html=True
        )
        for _ in range(num_metrics):
            st.markdown(
                '<div class="skeleton-loader skeleton-text"></div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div class="skeleton-loader skeleton-text" style="width: 80%;"></div>',
                unsafe_allow_html=True
            )
        st.divider()


def render_full_skeleton_screen():
    """Render a complete skeleton loading screen matching the dashboard layout."""
    inject_skeleton_css()

    # Header
    st.markdown(
        '<div class="loading-header"><div class="loading-text"><span class="loading-spinner" style="margin-right: 16px;"></span>Analyzing financial data...</div></div>',
        unsafe_allow_html=True
    )

    # Metrics row
    metric_cols = st.columns(4)
    for col in metric_cols:
        with col:
            st.markdown(
                '<div class="skeleton-card"><div class="skeleton-metric"><div class="skeleton-loader skeleton-metric-label"></div><div class="skeleton-loader skeleton-metric-value"></div></div></div>',
                unsafe_allow_html=True
            )

    # Charts section
    st.markdown('<h3 class="skeleton-text" style="height: 24px; width: 200px; margin-bottom: 16px;"></h3>', unsafe_allow_html=True)
    chart_cols = st.columns(2)
    for col in chart_cols:
        with col:
            st.markdown(
                '<div class="skeleton-card"><div class="skeleton-loader skeleton-chart" style="height: 250px;"></div></div>',
                unsafe_allow_html=True
            )

    # Content cards
    st.markdown('<h3 class="skeleton-text" style="height: 24px; width: 250px; margin-bottom: 16px;"></h3>', unsafe_allow_html=True)
    for _ in range(2):
        st.markdown('<div class="skeleton-card">', unsafe_allow_html=True)
        for _ in range(3):
            st.markdown(
                '<div class="skeleton-loader skeleton-text"></div>',
                unsafe_allow_html=True
            )
        st.markdown('</div>', unsafe_allow_html=True)


def show_loading_spinner(message: str = "Processing..."):
    """Show a simple loading spinner with message."""
    inject_skeleton_css()
    st.markdown(
        f'<div style="text-align: center; padding: 32px;"><div class="loading-text"><span class="loading-spinner"></span>{message}</div></div>',
        unsafe_allow_html=True
    )

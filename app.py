import streamlit as st
from aquaguard_agent import run_telemetry

st.set_page_config(page_title="AquaGuard AI", page_icon="💧")

st.title("💧 AquaGuard AI Dashboard")

tds = st.slider("TDS Level (ppm)", 0, 1000, 120)
filter_life = st.slider("Filter Life (%)", 0, 100, 80)

col1, col2 = st.columns(2)

with col1:
    st.metric("TDS", f"{tds} ppm")

with col2:
    st.metric("Filter Life", f"{filter_life}%")

if st.button("Analyze Water"):

    try:
        with st.spinner("Analyzing telemetry..."):

            result = run_telemetry(
                tds=tds,
                filter_life=filter_life,
                customer_id="CUST101",
                phone="whatsapp:+919811922549"
            )

        st.success("Analysis Completed")

        st.subheader("🤖 AquaGuard AI Decision")

        if tds > 500:
            st.error(result)

        elif filter_life <= 5:
            st.warning(result)

        else:
            st.success(result)

    except Exception as e:
        st.error(f"Error: {e}")
        st.exception(e)
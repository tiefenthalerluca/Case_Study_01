
import streamlit as st

st.title("Geräteverwaltung")

# Aktuell ausgewähltes Gerät
if "current_device" not in st.session_state:
    st.session_state.current_device = "Kein Gerät ausgewählt"

# Geräteübersicht
st.header("Geräteübersicht")

geraete = [
    {"ID": 1, "Name": "Bohrmaschine", "Status": "Verfügbar"},
    {"ID": 2, "Name": "Akkuschrauber", "Status": "Ausgeliehen"},
    {"ID": 3, "Name": "Multimeter", "Status": "Verfügbar"}
]

st.table(geraete)

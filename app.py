import sqlite3
from datetime import date
import pandas as pd
import streamlit as st
from pathlib import Path
import os

DB_NAME = "hotel.db"

# ---------- helper layer ----------
#Rebuild hotel.db from schema & sample data if it doesn't exist
if not Path("hotel.db").exists():
    try:
        from create_db import execute_script
        execute_script("schema_sqlite.sql")
        execute_script("sample_data.sql")
    except Exception as e:
        import streamlit as st
        st.error("Failed to create hotel.db on Streamlit Cloud.")
        st.exception(e)

@st.cache_resource(show_spinner=False)
def get_connection():
    return sqlite3.connect(DB_NAME, check_same_thread=False)

def fetch_df(query, params=None):
    conn = get_connection()
    if params:
        return pd.read_sql_query(query, conn, params=params)
    else:
        return pd.read_sql_query(query, conn)

def execute(query, params=None):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(query, params or {})
    conn.commit()
    return cur

# ---------- UI blocks ----------
def list_reservations():
    st.subheader("Liste des réservations")
    df = fetch_df("""
        SELECT R.id,
               C.nom           AS client,
               H.ville         AS ville_hotel,
               R.date_debut,
               R.date_fin,
               Ch.numero       AS chambre
        FROM Reservation R
        JOIN Client   C  ON C.id  = R.id_client
        JOIN Chambre  Ch ON Ch.id = R.id_chambre
        JOIN Hotel    H  ON H.id  = Ch.id_hotel
        ORDER BY R.date_debut;
    """)
    st.dataframe(df, hide_index=True)

def list_clients():
    st.subheader("Clients")
    df = fetch_df("SELECT id, nom, email, telephone, ville FROM Client;")
    st.dataframe(df, hide_index=True)

def search_rooms():
    st.subheader("Chambres disponibles")
    col1, col2 = st.columns(2)
    with col1:
        start = st.date_input("Date d’arrivée", value=date.today())
    with col2:
        end   = st.date_input("Date de départ", value=date.today())
    if start > end:
        st.error("La date d’arrivée doit précéder la date de départ.")
        return
    if st.button("Rechercher"):
        df = fetch_df("""
            SELECT Ch.id,
                   Ch.numero,
                   T.libelle       AS type,
                   T.prix_nuit,
                   H.ville         AS hotel
            FROM Chambre Ch
            JOIN TypeChambre T ON T.id = Ch.id_type_chambre
            JOIN Hotel       H ON H.id = Ch.id_hotel
            WHERE Ch.id NOT IN (
                SELECT id_chambre
                FROM Reservation
                WHERE NOT (:end < date_debut OR :start > date_fin)
            );
        """, {"start": str(start), "end": str(end)})
        st.success(f"{len(df)} chambre(s) libre(s).")
        st.dataframe(df, hide_index=True)

def add_client():
    st.subheader("Ajouter un client")
    with st.form("form_client"):
        nom       = st.text_input("Nom complet")
        adresse   = st.text_input("Adresse")
        ville     = st.text_input("Ville")
        cp        = st.number_input("Code postal", step=1, format="%d")
        email     = st.text_input("E-mail")
        tel       = st.text_input("Téléphone")
        submitted = st.form_submit_button("Enregistrer")
    if submitted:
        execute("""
            INSERT INTO Client(nom, adresse, ville, code_postal, email, telephone)
            VALUES(:nom, :adresse, :ville, :cp, :email, :tel);
        """, locals())
        st.success("Client ajouté.")

def add_reservation():
    st.subheader("Ajouter une réservation")
    clients = fetch_df("SELECT id, nom FROM Client;")
    rooms   = fetch_df("""
        SELECT Ch.id,
               printf('%s – %s (%s)', H.ville, Ch.numero, T.libelle) AS label
        FROM Chambre Ch
        JOIN Hotel       H ON H.id = Ch.id_hotel
        JOIN TypeChambre T ON T.id = Ch.id_type_chambre
        ORDER BY H.ville, Ch.numero;
    """)
    if clients.empty or rooms.empty:
        st.info("Il faut au moins un client et une chambre dans la base.")
        return
    client_dict = dict(zip(clients.nom, clients.id))
    room_dict   = dict(zip(rooms.label, rooms.id))

    with st.form("form_resa"):
        client_name  = st.selectbox("Client", list(client_dict.keys()))
        room_label   = st.selectbox("Chambre", list(room_dict.keys()))
        start = st.date_input("Date d’arrivée", value=date.today())
        end   = st.date_input("Date de départ", value=date.today())
        submit = st.form_submit_button("Réserver")
    if submit:
        if start > end:
            st.error("Dates invalides.")
            return
        execute("""
            INSERT INTO Reservation(date_debut, date_fin, id_client, id_chambre)
            VALUES(:start, :end, :client, :room);
        """, {
            "start": str(start),
            "end":   str(end),
            "client": client_dict[client_name],
            "room":   room_dict[room_label]
        })
        st.success("Réservation enregistrée.")

# ---------- main ----------
PAGES = {
    "Réservations": list_reservations,
    "Clients":       list_clients,
    "Disponibilité": search_rooms,
    "Ajouter client": add_client,
    "Ajouter réservation": add_reservation,
}

def main():
    st.set_page_config(page_title="Gestion Hôtel", page_icon="🏨", layout="wide")
    st.sidebar.title("Menu")
    choice = st.sidebar.radio("", list(PAGES.keys()))
    PAGES[choice]()

if __name__ == "__main__":
    main()

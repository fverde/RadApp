import streamlit as st
import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS mytable(name TEXT, date TEXT, ct TEXT, mri TEXT, plain_film TEXT, us TEXT)')

def add_data(name: object, date: object, ct: object, mri: object, plain_film: object, us: object) -> object:
    c.execute('INSERT INTO mytable(name,date,ct,mri,plain_film,us) VALUES (?,?,?,?,?,?)',
              (name,date.strftime('%Y-%m-%d'),ct,mri,plain_film,us))
    conn.commit()

create_table()

name = st.text_input("Enter your name")
date = st.date_input("Enter date")
ct = st.number_input("CT", min_value=0)
mri = st.number_input("MRI", min_value=0)
plain_film = st.number_input("Plain Film", min_value=0)
us = st.number_input("US", min_value=0)

if st.button("Submit"):
    add_data(name,date,int(ct),int(mri),int(plain_film),int(us))

st.write("Data entered:")
c.execute('SELECT * FROM mytable')
data = c.fetchall()
for row in data:
    st.write(row)

daily_rvu = mri * 90 + ct * 60 + us * 30 + plain_film * 10
st.sidebar.write(f"Daily RVU = {daily_rvu}")
import streamlit as st
import pyodbc

def get_tables(server, database, username, password):
    # Build connection string
    conn_str = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"UID={username};"
        f"PWD={password};"
    )
    
    # Connect to Azure SQL
    with pyodbc.connect(conn_str) as conn:
        cursor = conn.cursor()
        
        # Query to get list of tables (via INFORMATION_SCHEMA)
        cursor.execute("SELECT TABLE_SCHEMA, TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE';")
        
        # Fetch all tables
        tables_data = cursor.fetchall()
        
        # Convert to a list of tuples or list of dicts
        tables_list = [f"{row[0]}.{row[1]}" for row in tables_data]
        
    return tables_list

def main():
    st.title("Azure Sandbox Test")
    
    # Collect Azure SQL credentials (for demonstration; in a real app you’d store these securely)
    server = st.text_input("Azure SQL Server (e.g. yourserver.database.windows.net)")
    database = st.text_input("Database Name")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("List Tables"):
        if server and database and username and password:
            try:
                tables = get_tables(server, database, username, password)
                if tables:
                    st.write("**Tables found in the database:**")
                    st.table(tables)
                else:
                    st.write("No tables found or insufficient permissions.")
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please fill in all required fields.")

if __name__ == "__main__":
    main()

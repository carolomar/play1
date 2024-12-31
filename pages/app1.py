import streamlit as st
import pandas as pd
from datetime import datetime

# Initialize session states
if 'todos' not in st.session_state:
    st.session_state.todos = pd.DataFrame(columns=['Task', 'Status', 'Created Date'])
if 'completed_todos' not in st.session_state:
    st.session_state.completed_todos = pd.DataFrame(columns=['Task', 'Status', 'Created Date', 'Completed Date'])
if 'show_completed' not in st.session_state:
    st.session_state.show_completed = False

st.title('Todo App')

# Input for new todo with return key handling
def add_todo():
    if st.session_state.new_todo:
        new_row = pd.DataFrame({
            'Task': [st.session_state.new_todo],
            'Status': ['Pending'],
            'Created Date': [datetime.now().strftime("%Y-%m-%d %H:%M")]
        })
        st.session_state.todos = pd.concat([st.session_state.todos, new_row], ignore_index=True)
        st.session_state.new_todo = ''  # Clear input
        st.success('Task added!')

new_todo = st.text_input('Add a new task', key='new_todo', on_change=add_todo)

# Toggle completed tasks view
st.sidebar.header('Options')
st.session_state.show_completed = st.sidebar.checkbox('Show Completed Tasks')

# Display active todos
if not st.session_state.todos.empty:
    st.subheader('Active Tasks')
    for idx, row in st.session_state.todos.iterrows():
        col1, col2, col3 = st.columns([3, 1, 1])
        
        with col1:
            st.write(row['Task'])
        with col2:
            if st.button('Complete', key=f'complete_{idx}'):
                completed_row = row.copy()
                completed_row['Status'] = 'Completed'
                completed_row['Completed Date'] = datetime.now().strftime("%Y-%m-%d %H:%M")
                st.session_state.completed_todos = pd.concat([st.session_state.completed_todos, 
                                                            pd.DataFrame([completed_row])], 
                                                            ignore_index=True)
                st.session_state.todos = st.session_state.todos.drop(idx)
                st.rerun()
        with col3:
            if st.button('Delete', key=f'delete_{idx}'):
                st.session_state.todos = st.session_state.todos.drop(idx)
                st.rerun()

# Display completed todos if toggled
if st.session_state.show_completed and not st.session_state.completed_todos.empty:
    st.subheader('Completed Tasks')
    for _, row in st.session_state.completed_todos.iterrows():
        st.write(f"{row['Task']} (Completed: {row['Completed Date']})")

# Show statistics
st.sidebar.header('Statistics')
total_active = len(st.session_state.todos)
total_completed = len(st.session_state.completed_todos)
st.sidebar.write(f'Active tasks: {total_active}')
st.sidebar.write(f'Completed tasks: {total_completed}')
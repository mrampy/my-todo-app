import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo_new = st.session_state["new_todo"] + "\n"
    todos.append(todo_new)
    functions.write_todos(todos)


st.title("ToDo App")
st.write("AMP enterprises")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st._rerun()


st.text_input(label=" ", placeholder="Enter your todo item", on_change=add_todo, key="new_todo")
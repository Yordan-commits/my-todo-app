import streamlit as st
import function

todos = function.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    function.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app")
st.text("This app is in increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        function.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter a todo", placeholder="Add a new todo....",
              on_change=add_todo, key='new_todo')


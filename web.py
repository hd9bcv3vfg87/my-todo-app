import streamlit as st
import functions

css = """
    <style>
        h3 {
            margin-bottom: 15px;
        }
        .stTextInput {
            margin-top: -30px;
        }
    </style>
"""

st.markdown(css, unsafe_allow_html=True)

todos = functions.get_todos()


def add_todo():
    new_todo = st.session_state['new_todo'] + '\n'
    todos.append(new_todo)
    functions.write_todos(todos)


st.session_state['new_todo'] = ''

st.title('Что мне нужно сделать:')
st.subheader('Хоть что-то одно бы...')

for i, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=str(i) + 'c1')
    if checkbox:
        todos.pop(i)
        functions.write_todos(todos)
        del st.session_state[str(i) + 'c1']
        st.experimental_rerun()

st.markdown("""---""")

st.subheader('Добавить боли')

text_input = st.text_input(label='',
                           placeholder='Пишем боль здесь и жмём Enter',
                           on_change=add_todo,
                           key='new_todo')

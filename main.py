import streamlit as st
import json
 
 #load & saved data of library
def load_library():
    try:
        with open("library.json", "r")as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_library():
    with open("library.json", "w")as file:
        json.dump(library,file,indent=4)

#initialize library
library= load_library()

st.title("Panda's Personal Library Manager")
menu = st.sidebar.radio("Select an option", ["View Library","Add Book", "Remove Book", "Search Book", "Save and Exit"])
if menu == "View Library":
    st.sidebar.header("Your Library")
if library:
        st.table(library)
else:
        st.markdown("""
                    <div style="background-color:#90EE90; padding:15px; border-radius:5px; text-align:center; display:flex; justify-content:center; align-items:center;">
            <h4 style="color:black;">Your Library is Empty.Start Adding Books!</h4>
        </div>
    """, unsafe_allow_html=True)


#Add book
if menu == "Add Book":
    st.sidebar.header("Add a new book")
    title = st.text_input("Title")
    author = st.text_input("Author")
    year = st.number_input("Year", min_value=1900, max_value=2100, step=1)
    genre = st.text_input("Genre")
    read_status = st.checkbox("Mark as Read")

    if st.button("Add Book"):
        library.append({"title": title, "author": author, "year": year, "genre": genre, "read_status": read_status})
        save_library()
        st.success("Book added successfully!")
        st.rerun()

elif menu == "Remove Book":
    st.sidebar.header("Remove a book")
    book_titles = [book["title"] for book in library]

    if book_titles:
         selected_book = st.selectbox("select a book to remove", book_titles)
         if st.button("Remove Book"):
              library = [book for book in library if book ["title"] != selected_book]
              save_library()
              st.success("Book removed successfully!")
              st.rerun()
         else:
              st.warning("No book in your library. Add some book!")

#search book
elif menu == "Search Book":
     st.sidebar.header("Search a book")
     search_term = st.text_input("Enter title or author name")

     if st.button("Search"):
          results = [book for book in library if search_term.lower () in book ["title"].lower() or search_term.lower() in book["author"].lower()]
          if results:
               st.table(results)
          else:
               st.warning("No books found!")

#save and exit
elif menu == "Save and Exit":
     save_library()
     st.success("Library saved successfully!")
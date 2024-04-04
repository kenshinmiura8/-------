# app.py
import streamlit as st
from page import home, login ,spotify,todo

def main():
    st.sidebar.title("メニュー")
    
    # ログイン状態を保持するセッションステート
    if "is_logged_in" not in st.session_state:
        st.session_state.is_logged_in = False

    if not st.session_state.is_logged_in:
        username = login.show()
        if username:
            st.session_state.username = username
            st.session_state.is_logged_in = True
    else:
        page = {
            "ホーム(運動記録)": home,
            "spotify(playlistを選ぼう)":spotify,
            "やるべきリスト":todo
            # ここに他のページを追加できます
        }

        selection = st.sidebar.radio("ページを選択", list(page.keys()))

        page = page[selection]
        page.show()

if __name__ == '__main__':
    main()




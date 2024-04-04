# login.py
import streamlit as st
import sqlite3 
import hashlib


def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password, hashed_text):
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False

def create_user():
    # ユーザー・テーブルが存在しない場合は作成
    with sqlite3.connect('database.db') as conn:
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT, password TEXT)')
        conn.commit()

def add_user(username, password):
    # 新規ユーザーの挿入
    with sqlite3.connect('database.db') as conn:
        c = conn.cursor()
        c.execute('INSERT INTO userstable(username, password) VALUES (?, ?)', (username, password))
        conn.commit()

def login_user(username, password):
    # ユーザーが存在するかどうかをチェック
    with sqlite3.connect('database.db') as conn:
        c = conn.cursor()
        c.execute('SELECT * FROM userstable WHERE username = ? AND password = ?', (username, password))
        data = c.fetchall()
        if data:
            # ログインが成功した場合、セッションステート内にusernameを設定
            st.session_state.username = username
            return True
        else:
            return False

def show():
    st.title("ログイン画面")
    if st.session_state.is_logged_in:
        st.success("既にログイン済みです")
        return 
    # ユーザー名の入力欄に一意のキーを設定する
    username = st.text_input("ユーザー名:", key="username_input")
    
    # パスワードの入力欄に一意のキーを設定する
    password = st.text_input("パスワード:", type="password", key="password_input")
    
    login_button = st.button("ログイン")
    
    st.title("サインアップ")
    
    # 新しいユーザー名の入力欄に一意のキーを設定する
    new_user = st.text_input("ユーザー名:", key="new_username_input")
    
    # 新しいパスワードの入力欄に一意のキーを設定する
    new_password = st.text_input("パスワード:", type="password", key="new_password_input")
    
    signup_button = st.button("サインアップ")
    
    # Initialize session_state if not already initialized
    if 'query_params' not in st.session_state:
        st.session_state.query_params = {'logged_in': False}

    if login_button:
        create_user()
        hashed_pswd = make_hashes(password)
        result = login_user(username, check_hashes(password, hashed_pswd))

        if result:
            st.success("{}さんでログインしました".format(username))
            st.session_state.is_logged_in = True

            # ログイン成功後、ページを遷移
            st.session_state.query_params['logged_in'] = True
            
    if signup_button:
        create_user()
        add_user(new_user, make_hashes(new_password))
        st.success("アカウントの作成に成功しました")
        st.session_state.is_logged_in = True
        st.session_state.username = new_user
            # ログイン成功後、ページを遷移
        st.session_state.query_params['logged_in'] = True

    # ログイン成功後、ユーザーをリダイレクト
    if st.session_state.is_logged_in:
        st.rerun()

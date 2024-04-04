# home.py
import streamlit as st
import pandas as pd
import datetime
import sqlite3

def create_user_data_table(username):
    # 各ユーザーのuser_dataテーブルを作成する。
    with sqlite3.connect('database.db') as conn:
        c = conn.cursor()
        c.execute(f'CREATE TABLE IF NOT EXISTS {username}_todo (column1 TEXT,column2 TEXT)')
        conn.commit()

def add_data(username, column1, column2):
    # user_dataテーブルにデータを追加
    with sqlite3.connect('database.db') as conn:
        c = conn.cursor()
        c.execute(f'INSERT INTO {username}_todo (column1, column2) VALUES (?, ?)', (column1, column2))
        conn.commit()

def get_data(username):
    #  user_dataテーブルからデータを取得し、カラム1（日付）でソートする。 
    with sqlite3.connect('database.db') as conn:
        c = conn.cursor()
        c.execute(f'SELECT * FROM {username}_todo ORDER BY column1 ASC')
        data = c.fetchall()
        return data


def remove_data_by_date(username, target_date):
#  user_dataテーブルから指定された日付に基づいてデータを削除する。    
    with sqlite3.connect('database.db') as conn:
        c = conn.cursor()

        # DELETE文を作成してレコードを削除
        delete_query = f'''
        DELETE FROM {username}_todo
        WHERE column1 = ?;
        '''

        c.execute(delete_query, (target_date,))

        # データベースへの変更をコミット
        conn.commit()

def show():
    st.title("ホーム画面")
    st.write("今日運動した詳細を書いてみましょう！")


    # ユーザーごとに異なるデータベーステーブルを作成
    create_user_data_table(st.session_state.username)

    # データの入力フォーム
    with st.form("data_form"):
        formatted_time = st.date_input("削除する日付を選択:", key="formated_date_input")
        text_input = st.text_input("やるべきこと:", key="text_input")
        confirmation_checkbox = st.checkbox("データを追加しますか？",value=False)
        if st.form_submit_button("データ追加") and confirmation_checkbox:
            add_data(st.session_state.username, formatted_time, text_input)

    data = get_data(st.session_state.username)
    st.title("やるべきリスト")
    st.dataframe(pd.DataFrame(data, columns=["日付", "やるべきこと"]))

    st.write("また入力しなおしたい人は↓")
    target_date_input = st.date_input("削除する日付を選択:", key="target_date_input")
    confirmation_checkbox2 = st.checkbox("データを削除しますか？",value=False)
    if confirmation_checkbox2:
        remove_button = st.button("指定した日付のデータを削除", disabled=False)
    else:
        remove_button = st.button("指定した日付のデータを削除", disabled=True)


    # ボタンが押された場合の処理
    if remove_button:
        # 選択された日付に一致するデータを削除
        remove_data_by_date(st.session_state.username, str(target_date_input))
        st.success(f"{target_date_input} のデータが削除されました。")
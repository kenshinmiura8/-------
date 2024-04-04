# home.py
import streamlit as st
import pandas as pd
import datetime
import sqlite3

def create_user_data_table(username):
    # ユーザー・テーブルが存在しない場合は作成
    with sqlite3.connect('database.db') as conn:
        c = conn.cursor()
        c.execute(f'CREATE TABLE IF NOT EXISTS {username}_data (column1 TEXT, column2 INT, column3 INT,column4 INT,column5 INT,column6 INT)')
        conn.commit()

def add_data(username, column1, column2, column3,column4,column5,column6):
    # ユーザー・テーブルに挿入
    with sqlite3.connect('database.db') as conn:
        c = conn.cursor()
        c.execute(f'INSERT INTO {username}_data (column1, column2, column3,column4,column5,column6) VALUES (?, ?, ?,?,?,?)', (column1, column2, column3,column4,column5,column6))
        conn.commit()

def get_data(username):
    # user_dataテーブルからデータを取得し、カラム1（日付）でソートする。
    with sqlite3.connect('database.db') as conn:
        c = conn.cursor()
        c.execute(f'SELECT * FROM {username}_data ORDER BY column1 ASC')
        data = c.fetchall()
        return data


def remove_data_by_date(username, target_date):
#user_dataテーブルから指定された日付に基づいてデータを削除する。    
    with sqlite3.connect('database.db') as conn:
        c = conn.cursor()

        # DELETE文を作成してレコードを削除
        delete_query = f'''
        DELETE FROM {username}_data
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
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime('%Y-%m-%d')
        formatted_time = st.date_input("日付を選択:", key="formatted_time")
        column2_input = st.number_input("歩いた距離:", key="column2_input")
        column3_input = st.number_input("歩いた時間:", key="column3_input")
        column4_input = st.number_input("走った距離:", key="column4_input")
        column5_input = st.number_input("走った時間:", key="column5_input")
        column6_input = st.number_input("体重:", key="column6_input")
        confirmation_checkbox = st.checkbox("データを追加しますか？",value=False)
        if st.form_submit_button("データ追加") and confirmation_checkbox:
            add_data(st.session_state.username, formatted_time, column2_input, column3_input,column4_input,column5_input,column6_input)

    

    # 特定の日付に基づいてデータを削除する
    st.write("同じ日付で書いてしまった、また入力しなおしたい人は↓")
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
    data = get_data(st.session_state.username)
    st.title("運動の詳細")
    st.dataframe(pd.DataFrame(data, columns=["日付", "歩いた距離", "歩いた時間","走った距離","走った時間","体重"]))
    graph = pd.DataFrame(data, columns=["日付", "歩いた距離", "歩いた時間","走った距離","走った時間","体重"])
    # グラフの描画
    show_graph1 = st.checkbox("歩いた距離のグラフを表示")

    if show_graph1:
        # グラフを表示
        st.write('歩いた距離:')
        st.line_chart(graph.set_index("日付")["歩いた距離"])
    show_graph2= st.checkbox("歩いた時間のグラフを表示")
    if show_graph2:
            # グラフを表示
            st.write('歩いた時間:')
            st.line_chart(graph.set_index("日付")["歩いた時間"])
    show_graph3 = st.checkbox("走った距離のグラフを表示")
    if show_graph3:
            # グラフを表示
            st.write('走った距離:')
            st.line_chart(graph.set_index("日付")["走った距離"])
    show_graph4 = st.checkbox("走った時間のグラフを表示")
    if show_graph4:
            # グラフを表示
            st.write('走った時間:')
            st.line_chart(graph.set_index("日付")["走った時間"])
    show_graph5 = st.checkbox("体重のグラフを表示")
    if show_graph5:
            # グラフを表示
            st.write('体重:')
            st.line_chart(graph.set_index("日付")["体重"])

        
        
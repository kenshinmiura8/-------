import numpy as np
import pandas as pd
import streamlit as st


# streamlit 表示画面
def show():
    st.title("あなたに最適なプレイリストを!")
    st.markdown("ウォーキングやランニング中に最適な音楽を選んでください。まず、好きな国のチェックボックスをクリック、好みのジャンルのボタンをクリックしてください。")

    show_playlist1 = st.checkbox("日本に関連したプレイリスト")

    if show_playlist1:
        # グラフを表示
        col1, col2, col3,col4,col5 = st.columns(5)
        with col1:
                st.link_button("日本 話題曲", "https://open.spotify.com/playlist/37i9dQZF1DX9vYRBO9gjDe?si=a535868cae1e4192")
        with col2:
                st.link_button("日本 TOP50", "https://open.spotify.com/playlist/37i9dQZEVXbKXQ4mDTEBXq?si=f061835f5ff54d6a")
        with col3:
                st.link_button("昭和POP", "https://open.spotify.com/playlist/37i9dQZF1DX2QCBqV8Ylrq?si=18725f4c1c6b4aee")
        with col4:
                st.link_button("平成POP", "https://open.spotify.com/playlist/37i9dQZF1DWYQelb54GZmT?si=fd76e1f07c2a4d3d")
        with col5:
                st.link_button("令和POP", "https://open.spotify.com/playlist/37i9dQZF1DXdurasRmJgpJ?si=e6df58c4c23c4388")
        with col1:
                st.link_button("J-Rock 話題曲", "https://open.spotify.com/playlist/37i9dQZF1DX6ntWKaOqGAp?si=cfc91801733949de")
        with col2:
                st.link_button("J-Rock MIX", "https://open.spotify.com/playlist/37i9dQZF1EIhJROHjsowE8?si=8242acef7bc84207")
        with col3:
                st.link_button("J-Rock 1990年代", "https://open.spotify.com/playlist/37i9dQZF1DXcpehQnGbWYD?si=203d4575296b4c81")
        with col4:
                st.link_button("J-Rock 2000年代", "https://open.spotify.com/playlist/37i9dQZF1DWV48gEMVy7G8?si=93d86e52e843407f")
        with col5:
                st.link_button("J-Rock 2010年代", "https://open.spotify.com/playlist/37i9dQZF1DWVCWq6ehLoH4?si=2f3bc0110a074558")
        with col1:
                st.link_button("アニソン 話題曲", "https://open.spotify.com/playlist/37i9dQZF1DWT8aqnwgRt92?si=0fe67bded14c46ea")
        with col2:
                st.link_button("アニソン ロングヒット", "https://open.spotify.com/playlist/37i9dQZF1DX0hAXqBDwvwI?si=43a56c894ade436e")
        with col3:
                st.link_button("J-HipHop", "https://open.spotify.com/playlist/37i9dQZF1DX0Eftsfm2dbT?si=649f15da849147f9")
    show_playlist2 = st.checkbox("韓国に関連したプレイリスト")
    if show_playlist2:
        # グラフを表示
        col1, col2 = st.columns(2)
        with col1:
            st.link_button("90's-10'sのK-pop", "https://open.spotify.com/playlist/37i9dQZF1DX14fiWYoe7Oh?si=13ff12e6b35940c3")
        with col2:
            st.link_button("K-pop 急上昇", "https://open.spotify.com/playlist/37i9dQZF1DX9tPFwDMOaN1?si=852e974deff447bb")
    show_playlist3 = st.checkbox("US,他海外に関連したプレイリスト")
    if show_playlist3:
        # グラフを表示
        col1, col2 = st.columns(2)
        with col1:
            st.link_button("USのレジェンドバンド", "https://open.spotify.com/playlist/37i9dQZF1DWXRqgorJj26U?si=904bfaba448044a3")
        with col2:
            st.link_button("US TOP50", "https://open.spotify.com/playlist/37i9dQZEVXbLRQDuF5jeBp?si=b625ee2d922e4c83")
    
   
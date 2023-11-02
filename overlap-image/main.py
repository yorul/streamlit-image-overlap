import streamlit as st
import numpy as np
import cv2

def main():
    """Streamlit application
    """

    st.title("画像の重畳表示アプリ")
    expander1 = st.expander('ベース画像のアップロード')
    uploaded_file_1 = expander1.file_uploader("画像を選択してください｀", key="base_image")
    if uploaded_file_1 is not None:
        # 画像をOpencvで読み込む
        file_bytes = np.asarray(bytearray(uploaded_file_1.read()), dtype=np.uint8)
        opencv_image_1 = cv2.imdecode(file_bytes, 1)

        st.image(opencv_image_1, channels="BGR")

    expander2 = st.expander('重畳画像のアップロード')
    uploaded_file_2 = expander2.file_uploader("画像を選択してください", key="overlay_image")
    if uploaded_file_2 is not None:
        # 画像をOpencvで読み込む
        file_bytes = np.asarray(bytearray(uploaded_file_2.read()), dtype=np.uint8)
        opencv_image_2 = cv2.imdecode(file_bytes, 1)

        st.image(opencv_image_2, channels="BGR")

if __name__ == "__main__":
    main()
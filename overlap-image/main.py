import streamlit as st
import numpy as np
import cv2
from streamlit_image_coordinates import streamlit_image_coordinates
from PIL import Image
import io
import os

def main():
    """Streamlit application
    """
    st.title("画像の重畳表示アプリ")

    # Session Stateで入力された数値を管理
    if "coord_lst" not in st.session_state:
        # 初期化。初期値は空のリスト
        st.session_state["coord_lst"] = []

    expander1 = st.expander('ベース画像のアップロード')
    uploaded_file_1 = expander1.file_uploader("画像を選択してください", key="base_image")
    if uploaded_file_1 is not None:
        # 画像をOpencvで読み込む
        file_bytes = np.asarray(bytearray(uploaded_file_1.read()), dtype=np.uint8)
        opencv_image_2 = cv2.imdecode(file_bytes, 1)
        #st.image(opencv_image_2)
        img_base = cv2.cvtColor(opencv_image_2, cv2.COLOR_RGB2BGR)
        height_img_base, width_img_base, channels = img_base.shape[:3]
        # streamlit-image-coordinatesコンポーネントを呼び出す
        value = streamlit_image_coordinates(img_base)

        # クリックした座標をリストに保存する
        if value is not None:
            st.write("左上、右上、右下、左下の順でクリックしてください。")
            if len(st.session_state["coord_lst"]) < 4:
                coordinates = value["x"], value["y"]
                st.write(coordinates)
                st.session_state["coord_lst"].append(coordinates)
                #st.write(st.session_state["coord_lst"])
                if len(st.session_state["coord_lst"]) == 4:
                    st.success('座標の入力が完了しました。次は重畳表示したい画像をアップロードしてください。', icon="✅")
                    st.warning('やり直しがしたい場合はResetボタンをクリックしてください。', icon="⚠️")
                    if st.button("Reset", type="primary"):
                        st.session_state["coord_lst"] = []
            else:
                st.warning('座標が４個以上入力されました。Resetボタンをクリックしてください。', icon="⚠️")
                if st.button("Reset", type="primary"):
                    st.session_state["coord_lst"] = []

    expander2 = st.expander('重畳画像のアップロード')
    uploaded_file_2 = expander2.file_uploader("画像を選択してください", key="overlay_image")
    if uploaded_file_2 is not None:
        # 画像をOpencvで読み込む
        file_bytes = np.asarray(bytearray(uploaded_file_2.read()), dtype=np.uint8)
        opencv_image_1 = cv2.imdecode(file_bytes, 1)
        st.image(opencv_image_1, channels="BGR")
        img_overlay = cv2.cvtColor(opencv_image_1, cv2.COLOR_RGB2BGR)
        height_img_overlay, width_img_overlay, channels = img_overlay.shape[:3]
        img_overlay_coord = np.array([[0, 0], [width_img_overlay, 0], [width_img_overlay, height_img_overlay], [0, height_img_overlay]], dtype=np.float32)

    # 画像の重畳表示
    #if img_overlay_coord is not None and len(st.session_state["coord_lst"]) == 4:
    if st.button("Combine", type="primary"):
        coord_lst = np.array(st.session_state["coord_lst"], dtype=np.float32)
        mat = cv2.getPerspectiveTransform(img_overlay_coord, coord_lst)
        perspective_image = cv2.warpPerspective(img_overlay, mat, (width_img_base, height_img_base))

        perspective_image = cv2.cvtColor(perspective_image, cv2.COLOR_BGR2BGRA)
        perspective_image[np.all(perspective_image == [0, 0, 0, 255], axis=2)] = [0, 0, 0, 0]
        test = Image.fromarray(perspective_image).convert("RGBA")
        #st.image(test)

        bg = Image.fromarray(img_base).convert("RGBA")
        #st.image(bg)

        img_clear = Image.new("RGBA", bg.size, (255, 255, 255, 0))
        img_clear.paste(test)
        
        final = Image.alpha_composite(bg, img_clear)
        st.image(final)
        #result = cv2.addWeighted(img_base, 1, perspective_image, 1, 0)
        #st.image(result)

if __name__ == "__main__":
    main()
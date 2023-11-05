# 画像の重畳表示アプリ

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://app-image-overlap-8nawuvdelmjb5xfgk9z7bj.streamlit.app/)

[![Qiita](https://simpleicons.org/icons/qiita.svg)](https://qiita.com/yorul/items/d1b0a6a774499ced21ef)

## アプリの概要
ユーザーは2枚の画像をアップロードし、ベース画像上で4点を選択することで、2枚目の画像を変形し、その領域に配置します。
Photoshopなどの画像編集ソフトを使えば同様のことは可能ですが、このアプリはより直感的で簡単に操作できます（画像をアップロードし、4点をクリックするだけです）。
また、定点カメラのような場合では、4点を事前に指定することで一定の自動化も可能となり、特定の用途においては意外と需要があるかもしれません（？）


## 使い方

まずはベース画像を選択し、アップロードします。

<img width="400" alt="sample1.png" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3501427/8f862138-969e-3f8b-6b5c-a091393074fd.png">

アップロードされた画像の４点、いわゆる左上、右上、右下、左下の順でクリックします。
ここではモニタ画面の４点を指定しました。

<img width="400" alt="sample2.png" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3501427/447b2f99-b53c-cc8e-1451-8d21f3b43a75.png">

もしミスった場合は一応Resetボタンを押せばやり直せます。

<img width="400" alt="sample3.png" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3501427/ec65a758-e5e0-8551-2518-11201c6683be.png">

次は重畳表示したい画像をアップロードし、Combineボタンを押せば完了です。

<img width="400" alt="sample4.png" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3501427/32d490bf-9543-e673-81ec-ed0b7818ce42.png">

以下のような画像が生成されます！

<img width="400" alt="sample5.png" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3501427/32fca43d-9a33-6740-053d-c3af60bfe3c2.png">

## 開発環境
Python
Streamlit
Visual Studio Code


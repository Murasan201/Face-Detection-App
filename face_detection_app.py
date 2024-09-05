import cv2  # OpenCVをインポート
import tkinter as tk  # tkinterでGUIを作成
from tkinter import filedialog  # ファイルダイアログを使用
from PIL import Image, ImageTk  # Pillowを使って画像を処理

# ファイル選択ダイアログを開いて、画像ファイルを選択させる関数
def select_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.tiff")]
    )  # ユーザーにファイルを選択させる
    if file_path:
        detect_faces(file_path)  # 画像が選択されたら顔検出を実行

# 顔検出を行う関数
def detect_faces(image_path):
    # OpenCVで画像を読み込む
    image = cv2.imread(image_path)

    # Haar Cascade分類器を使って顔検出を行う
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    # グレースケールに変換
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 顔を検出 (scaleFactor=1.1, minNeighbors=5は標準的な値)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # 検出された顔の周りに四角形を描画
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # 結果をウィンドウに表示する
    display_image(image)

# 画像をウィンドウに表示する関数
def display_image(image):
    # OpenCVの画像をPillow形式に変換
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    im_pil = Image.fromarray(image_rgb)

    # 画像をtkinterウィジェットに表示できるように変換
    imgtk = ImageTk.PhotoImage(image=im_pil)

    # ラベルに画像を設定して表示
    image_label.config(image=imgtk)
    image_label.image = imgtk  # ガベージコレクションされないように参照を保持

# GUIアプリケーションの作成
root = tk.Tk()
root.title("顔認識アプリケーション")

# 画像表示用のラベルを作成
image_label = tk.Label(root)
image_label.pack()

# 画像を選択するボタンを作成
btn = tk.Button(root, text="画像を選択", command=select_image)
btn.pack()

# GUIを開始
root.mainloop()

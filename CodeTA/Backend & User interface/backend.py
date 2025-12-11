from ultralytics import YOLO
import cv2 #opecCv bgr>rgb
import tempfile
import os #operating system

model = YOLO("bestfinal.pt")

def detect_image(image_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
        tmp_file.write(image_file.read())
        tmp_path = tmp_file.name

    results = model.predict(source=tmp_path, save=False, conf=0.25)

    # Gambar hasil prediksi (BGR → RGB)
    result_bgr = results[0].plot()
    result_rgb = cv2.cvtColor(result_bgr, cv2.COLOR_BGR2RGB)

    # Ambil label unik (tidak ada duplikat)
    label_names = []
    for box in results[0].boxes:
        cls_id = int(box.cls[0])
        class_name = model.names[cls_id] #mengambil id kelas diubah ke int
        label_names.append(class_name)

    unique_labels = list(dict.fromkeys(label_names))  # urutkan dan hilangkan duplikat

    os.remove(tmp_path) #hapus foto sebelumnya
    return result_rgb, unique_labels

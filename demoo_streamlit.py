import streamlit as st
import string
import ast

def dem_tan_suat_tu(text):
    text = text.lower().translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

def main():
    st.title("Ứng dụng đếm từ và đọc tần suất")

    tab1, tab2 = st.tabs([" Đếm từ từ file văn bản", " Đọc từ file tần suất"])

    with tab1:
        st.header("1. Tải lên file văn bản (.txt)")
        uploaded_file = st.file_uploader("Chọn file văn bản", type=["txt"])
        if uploaded_file is not None:
            text = uploaded_file.read().decode("utf-8")
            freq = dem_tan_suat_tu(text)

            st.subheader("Tần suất xuất hiện:")
            st.write(freq)

            # Ghi kết quả xuống file
            output_filename = "tan_suat_tu.txt"
            with open(output_filename, "w", encoding="utf-8") as f:
                f.write(str(freq))

            with open(output_filename, "rb") as f:
                st.download_button("Tải file kết quả", f, file_name=output_filename)

    with tab2:
        st.header("2. Tải lên file tần suất (kiểu dictionary)")
        freq_file = st.file_uploader("Chọn file tần suất", type=["txt"], key="freq")
        if freq_file is not None:
            try:
                content = freq_file.read().decode("utf-8")
                freq_dict = ast.literal_eval(content)  # Chuyển từ chuỗi sang dict an toàn
                st.subheader("Nội dung dictionary:")
                st.write(freq_dict)
            except Exception as e:
                st.error(f"Lỗi khi đọc file: {e}")

if __name__ == "__main__":
    main()

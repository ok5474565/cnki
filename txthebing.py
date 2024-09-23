import streamlit as st
import tempfile
import os

def merge_files(file_paths):
    """合并多个txt文件的内容"""
    merged_content = ""
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            merged_content += file.read() + "\n"  # 添加换行符以分隔文件内容
    return merged_content

def main():
    st.title('合并TXT文件应用')

    # 创建文件上传器
    uploaded_files = st.file_uploader("上传TXT文件", type=['txt'], accept_multiple_files=True)

    # 检查是否有文件被上传
    if uploaded_files is not None:
        # 创建临时目录
        with tempfile.TemporaryDirectory() as temp_dir:
            # 保存上传的文件到临时目录
            file_paths = []
            for file in uploaded_files:
                file_path = os.path.join(temp_dir, file.name)
                with open(file_path, 'wb') as f:
                    f.write(file.getvalue())  # 将上传的文件内容写入临时文件
                file_paths.append(file_path)

            # 合并文件
            merged_content = merge_files(file_paths)

            # 显示合并后的内容
            st.text_area("合并后的内容", value=merged_content, height=300)

            # 提供下载合并后的文件
            st.download_button(
                label="下载合并后的文件",
                data=merged_content.encode('utf-8'),
                file_name="merged_file.txt",
                mime="text/plain"
            )

if __name__ == "__main__":
    main()
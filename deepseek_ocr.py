from ocr import upload_image_and_get_analysis

file_path = 'test.png'
ask_content = '总结'

print(upload_image_and_get_analysis(file_path, ask_content))
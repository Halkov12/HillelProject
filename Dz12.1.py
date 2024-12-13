import codecs
def delete_html_tags(html_file, result_file='cleaned.txt'):
      with codecs.open(html_file, 'r', 'utf-8') as file:
           html = file.read()
      txt = ""
      tag = False
      for i in html:
          if i == '<':
              tag = True
          elif i == '>':
              tag = False
          elif not tag:
              txt += i
      with codecs.open(result_file, 'w', 'utf-8') as file:
          file.write(txt.strip())
      print("Оk")
      with codecs.open(result_file, 'r', 'utf-8') as file:
          lines = file.readlines()
      non_lines = [i for i in lines if i.strip()]
      with codecs.open(result_file, 'w', 'utf-8') as file:
          file.writelines(non_lines)
      print('Ok')

input_path = "draft.html"
output_path = "cleaned.txt"
delete_html_tags(input_path, output_path)
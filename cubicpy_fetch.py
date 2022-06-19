# name: cubicpy_fetch.py, version: 0.1.0, author: paoyung.chang@gmail.com
# Released under the MIT License (MIT). See LICENSE link:
# https://gist.github.com/paoyung/7e465ad984a6cf24024508831ec54516
# Copyright (c) 2022 Paoyung Chang

from cubicpy import chinese

def fetch(word_list, output_file):
	# collect
	words = {' ',}	# 把半型空格檔作預設字詞之一
	exclude = []
	for w in word_list:
		try:
			words[w] = chinese[w]
		except:
			exclude.append(w)
	if len(exclude):
		print('本字庫不包含:', exclude)
	# save file
	try:
		with open(output_file, 'w') as f:
			f.write('words=')
			f.write(str(words))
	except:
		print(f'{output_file} 建立或寫入發生異常！')
	else:
		print(f'{output_file} 建立完成！')


## example:
## fetch(word_list, output_filename)
# >>> word_list = 'Hello，大家好。向各位介紹免費、開源可商用自由改造及衍生的中文點陣字體 -『俐方體11號』'
# >>> fetch(word_list, 'my_font.py')

image = Image.open(img_path)
# 转化为灰度图
imgry = image.convert('L')

table = get_bin_table()
out = imgry.point(table, '1')
#由PIL转化后变成二值图片:0表示黑色,1表示白色。二值化后带噪点的 6937 的像素点输出后如下图
'''
1111000111111000111111100001111100000011
1110111011110111011111011110111100110111
1001110011110111101011011010101101110111
1101111111110110101111110101111111101111
1101000111110111001111110011111111101111
1100111011111000001111111001011111011111
1101110001111111101011010110111111011111
1101111011111111101111011110111111011111
1101111011110111001111011110111111011100
1110000111111000011101100001110111011111
'''
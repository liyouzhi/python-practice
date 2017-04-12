
def fenbiejisuan(max):
	a = 0
	b = 0
	for i in range(0, max+1):
		if i % 2 == 0:
			print("%d is a oushu" % i)
			a = a + i
		else:
			print("%d is a jishu" % i)
			b = b + i
	return a, b


jishu, oushu = fenbiejisuan(100)
print(jishu)
print(oushu)


# pid = "a_1.jpeg"
# thumb_id = pid + ".thumb"
#
# # "a_1.jpeg.thumb"
#
# thumbdata = mysql_get(thumb_id)
# if thumbdata:
# 	return thumbdata
#
# pdata = mysql_get(pid)
# thumbnail = resize(pdata, width, height)
# mysql_set(thumb_id, thumbnail)
# return thumbnail
#
#
# data_path = "/pic_data/"
# pid = data_path + file_name
# thumb_id = pid + ".thumb"
# t_data = fopen(thumb_id)
# if t_data:
# 	return t_data
# p_data = fopen(pid)
# t_data = resize(p_data, width, height)
#
# f = fnew(thumb_id)
# f.write(t_data)
# return t_data
#
#
# PIL

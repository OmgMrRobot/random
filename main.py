import eel
from datetime import datetime

##int(datetime.now().microsecond/100)


def parser(str):
	str = str.split(' ')
	return int(str[0]), int(str[1])

eel.init('web')

@eel.expose
def random_(str):

	a, b = parser(str)

	lamda = 5
	z = 7
	M = 2 ** 16

	for _ in range(int(datetime.now().microsecond/100)):

		z = (z * lamda) % M
		x = z / M

	return f"{a + (b - a) * x}"



eel.start('main2.html', size=(500, 500))



	
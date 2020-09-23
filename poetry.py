import requests

url = 'https://poetrydb.org/random'

def show_poem():
	r = requests.get(url)
	data = r.json()

	print('\n' + data['title'])
	print('By ' + data['author'] + '\n')
	print('\n'.join(data['lines']) + '\n')

show_poem()
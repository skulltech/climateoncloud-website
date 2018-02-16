import json

cards = [
	{
		'image': 'https://placehold.it/318x180',
		'title': 'Card title',
		'text': "Some quick example text to build on the card title and make up the bulk of the card's content.",
		'button': {
			'text': 'Button',
			'link': '#'
		}
	},
	{
		'image': 'https://placehold.it/318x180',
		'title': 'Card title',
		'text': "Some quick example text to build on the card title and make up the bulk of the card's content.",
		'button': {
			'text': 'Button',
			'link': '#'
		}
	},
	{
		'image': 'https://placehold.it/318x180',
		'title': 'Card title',
		'text': "Some quick example text to build on the card title and make up the bulk of the card's content.",
		'button': {
			'text': 'Button',
			'link': '#'
		}
	},
	{
		'image': 'https://placehold.it/318x180',
		'title': 'Card title',
		'text': "Some quick example text to build on the card title and make up the bulk of the card's content.",
		'button': {
			'text': 'Button',
			'link': '#'
		}
	},
	{
		'image': 'https://placehold.it/318x180',
		'title': 'Card title',
		'text': "Some quick example text to build on the card title and make up the bulk of the card's content.",
		'button': {
			'text': 'Button',
			'link': '#'
		}
	},
	{
		'image': 'https://placehold.it/318x180',
		'title': 'Card title',
		'text': "Some quick example text to build on the card title and make up the bulk of the card's content.",
		'button': {
			'text': 'Button',
			'link': '#'
		}
	},
	{
		'image': 'https://placehold.it/318x180',
		'title': 'Card title',
		'text': "Some quick example text to build on the card title and make up the bulk of the card's content.",
		'button': {
			'text': 'Button',
			'link': '#'
		}
	}
]

with open('cards.json', 'w') as f:
	json.dump(cards, f, indent=2)

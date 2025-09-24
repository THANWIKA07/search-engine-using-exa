from exa_py import Exa

exa = Exa('404fd3ba-534d-4c3f-a3d0-b565cca88074')

query = input('Search here: ')

response = exa.search(
  query,
  num_results=5,
  type='keyword',
  ##include_domains=['https://www.youtube.com/'],
  include_domains=['https://www.google.com/'],


)

for result in response.results:
  print(f'Title: {result.title}')
  print(f'URL: {result.url}')
  print()

  
from django.shortcuts import render
# from bs4 import BeautifulSoup
# from urllib.request import urlopen


def music_tracks_all(request):
  # url = "https://soundcloud.com/shona-lowden/tracks"
  # page = urlopen(url)
  # html = page.read().decode("utf-8")
  # soup = BeautifulSoup(html, "html.parser")
  # list = soup.find_all("li", class_="soundList__item")

  context = {}
  return render(request, 'music/tracks_summary.html', context)

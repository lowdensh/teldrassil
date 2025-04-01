from django.shortcuts import render


def music_tracks_all(request):
  context = {}
  return render(request, 'music/tracks_summary.html', context)

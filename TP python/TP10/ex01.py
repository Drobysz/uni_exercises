from beatles import dico_beatles
from albums import dico_albums

if __name__ == '__main__':
    # a)
	song = '12-Bar Original'
	year = dico_beatles[song]
	album = dico_albums[song]

	print(f"a)\nPrefered song: {song} {year} ({album})")
	
	# b) 
	songs = [title for title, yr in dico_beatles.items() if yr == year]
	ln = len(songs)
 
	print(f"\nb)\nThe sons released at the same year as \"{song}\": ", end='')
 
	for idx, ch in enumerate(songs):
		sep = ', '

		if ch == song:
			continue
		if idx == ln - 1:
			sep = '.'
		print(f"\"{ch}\"", end=sep)
  

	# c
	print(f"\n\nc)\nTotal number of songs {len(dico_beatles)}")
 
	# d + e
	song_yr_before_1970 = sorted({ yr for yr in dico_beatles.values() if yr <= 1970 })
	ln = len(song_yr_before_1970)
	
	print("\n\nd + e)\nYears of releases: { ", end='')
 
	for idx, yr in enumerate(song_yr_before_1970):
		sep = ', '
		if idx == ln - 1:
			sep = ''
		print(yr, end=sep)

	print(" }", end='')
 
 
	# f
	print(f"\n\nf)\nList of published songs by year:")
	year_songs = dict()

	for name, yr in dico_beatles.items():
		if yr not in year_songs.keys():
			year_songs[yr] = []
		year_songs[yr].append(name)

	sorted_yrs = sorted({yr for yr in year_songs.keys()})
 
	for yr in sorted_yrs:
		print(f"\n\nSongs for the year {yr}: ")

		for song in year_songs[yr]:
			print(song)


	# g
 
	print(f"\n\ng)\nSongs released at the same year as {song}: ")

	for s in year_songs[dico_beatles[song]]:
		if s != song:
			print(s, end=' ')

	# h
	yrs = sorted({ yr for yr in dico_beatles.values() })
	yr_alb_sg = {year: dict() for year in yrs}

	for name, yr in dico_beatles.items():
		album = dico_albums[name]
  
		if album not in yr_alb_sg[yr].keys():
			yr_alb_sg[yr][album] = list()
		yr_alb_sg[yr][album].append(name)
 
	# i
	song = 'Lucy in the Sky with Diamonds'
	year = dico_beatles[song]
	album = dico_albums[song]
	songs = yr_alb_sg[year][album]
	ln = len(songs)
 
	print(f"\n\ni)\nSongs from the same album as \"{song}\" ({album}): ", end=' ')
 
	for idx, s in enumerate(songs):
		sep = ', '
  
		if idx == ln - 1:
			sep = ';'
		print(f"\"{s}\"", end=sep)
  
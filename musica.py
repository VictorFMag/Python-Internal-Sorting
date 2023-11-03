class Musica:
    def __init__(self, track_name, artist_name, artist_count, released_year, released_month, released_day, in_spotify_playlists, in_spotify_charts, streams, in_apple_playlists, 
        in_apple_charts, in_deezer_playlists, in_deezer_charts, in_shazam_charts, bpm, key, mode, danceability, valence, energy, acousticness, instrumentalness, liveness, speechiness):
        self.track_name = track_name
        self.artist_name = artist_name
        self.artist_count = artist_count
        self.released_year = released_year
        self.released_month = released_month
        self.released_day = released_day
        self.in_spotify_playlists = in_spotify_playlists
        self.in_spotify_charts = in_spotify_charts
        self.streams = streams
        self.in_apple_playlists = in_apple_playlists
        self.in_apple_charts = in_apple_charts
        self.in_deezer_playlists = in_deezer_playlists
        self.in_deezer_charts = in_deezer_charts
        self.in_shazam_charts = in_shazam_charts
        self.bpm = bpm
        self.key = key
        self.mode = mode
        self.danceability = danceability
        self.valence = valence
        self.energy = energy
        self.acousticness = acousticness
        self.instrumentalness = instrumentalness
        self.liveness = liveness
        self.speechiness = speechiness
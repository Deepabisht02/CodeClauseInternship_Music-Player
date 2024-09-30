# CodeClauseInternship_Music Player
The user select a folder using the "select folder" button.
The "select folder" method opens a file dialog to select a folder and then calls "play_songs_in_folder" with the selected folder path.
The "play_songs_in_folder" method gets a list of all audio files in the folder and plays each song using the "play_music" method.
The "play_music" method initilizes the pygame mixer, loads and plays the music file and updates the song label.
The user can play, stop or pause the music using the respective buttons.

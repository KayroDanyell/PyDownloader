from pytube import YouTube
from pytube import Playlist

link = list()
confirma = 'S'

selecao = int(input(('''O que você deseja fazer?
1 - Para baixar musicas únicas, Você pode baixar mais de uma música de uma vez!
2 - Para baixar Playlists Youtube(Você pode baixar mais de uma playlist!)
Selecione:''')))

url = ''
while url != '0':
    url = input('Coloque o link Aqui:')
    link.append(url)

if selecao == 1:
    print(f'== Estas são as urls:{link} ==')
    for video in link:
        print(f'== Baixando: ({video}) ==')
        try:
            youtube = YouTube(video)
            print(youtube.streams)
            youtube.streams.get_audio_only('mp4').download('Downloads')
        
        finally:
            print(f'Houve algum erro com o link "{video}" e não terminou o Download')
            continue
from pytube import YouTube


link = list()
confirma = 'S'


url = ''
while url != '0':
    url = input('Coloque o link Aqui:')
    link.append(url)
    
    
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

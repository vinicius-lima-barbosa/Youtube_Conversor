import pathlib
import os
from pytubefix import YouTube # type: ignore
from pytubefix.cli import on_progress # type: ignore

folderDownload = pathlib.Path.home() / "Downloads"

def download():
    url = input("Digite a url: ")
    yt = YouTube(url, on_progress_callback=on_progress)
    print(yt.title)
    name="".join((yt.title).split())

    ys = yt.streams.get_highest_resolution()
    ys.download(output_path=folderDownload, filename=f'{name}.mp4')
    
    print('Concluido!')

def conversor():
    url = input("Digite a url: ")
    yt = YouTube(url, on_progress_callback=on_progress)
    print(yt.title)
    
    name="".join((yt.title).split())
    
    ys = yt.streams.get_audio_only()
    ys.download(output_path=folderDownload, filename=f'{name}.mp4')
    mp4_file = folderDownload/f'{name}.mp4'
    mp3_file = folderDownload/f'{name}.mp3'
    
    os.system(f'ffmpeg -i {mp4_file} -f mp3 -ab 192000 -vn {mp3_file}')
    os.remove(mp4_file)
    print('Conversao concluida!')

if __name__ == "__main__":
    print("Bem vindo ao conversor!\n") 
    while (True):
        print("Escolha sua opcao\n[1] - Baixar Vídeo\n[2] - Converter para mp3\n[3] - Sair")
        escolha = input()
        
        if (escolha == '1'):
            download()
        
        if (escolha == '2'):
            conversor()
        
        if (escolha == '3'):
            break
        
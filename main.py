import pathlib
from pytubefix import YouTube # type: ignore
from pytubefix.cli import on_progress # type: ignore

folderDownload = pathlib.Path.home() / "Downloads"

def download():
    url = input("Digite a url: ")
    yt = YouTube(url, on_progress_callback = on_progress)
    print(yt.title)

    ys = yt.streams.get_highest_resolution()
    ys.download(output_path=folderDownload)

def conversor():
    url = input("Digite a url: ")
    yt = YouTube(url, on_progress_callback = on_progress)
    print(yt.title)
    
    ys = yt.streams.get_audio_only()
    ys.download(output_path=folderDownload, mp3=True)

if __name__ == "__main__":
    
    print("Bem vindo ao conversor!\n")    
    print("Escolha sua opcao\n[1] - Baixar Vídeo\n[2] - Converter para mp3\n")
    
    while (True):
        escolha = input()
    
        if (escolha == '1'):
            download()
            break
        elif (escolha == '2'):
            conversor()
            break
        else:
            print("Erro ao escolher a opcao! Tente de novo.")
## YouTube Downloader & MP3 Converter

Este projeto é uma ferramenta simples em Python que permite baixar vídeos do YouTube ou converter vídeos em arquivos de áudio MP3. A aplicação utiliza a biblioteca pytubefix para baixar vídeos e ffmpeg para realizar a conversão de vídeos MP4 para MP3.

## Funcionalidades

**Download de vídeos:** Permite baixar vídeos do YouTube na mais alta resolução disponível.
**Conversão para MP3:** Converte vídeos do YouTube para arquivos de áudio MP3 de alta qualidade (192kbps).
**Interface em linha de comando:** Simples e direta, com menu interativo.

## Tecnologias Utilizadas

**Python 3.12.4:** Linguagem principal do projeto.
**pytubefix:** Biblioteca usada para interagir com a API do YouTube e baixar vídeos.
**FFmpeg:** Utilizado para converter arquivos MP4 baixados para MP3.
**OS:** Biblioteca nativa para operações de sistema, como mover e remover arquivos.
**pathlib:** Biblioteca para trabalhar com caminhos de diretórios de forma eficiente e multiplataforma.

## Pré-requisitos

Antes de começar, você precisará ter o seguinte instalado no seu ambiente:

**Python** 3.12.4
**FFmpeg** (para a conversão de MP4 para MP3)
**pytubefix** (pode ser instalada via pip)
**Sistema operacional compatível** (Windows, Linux, MacOS)

## Dependências

**pytubefix:** Usada para baixar vídeos do YouTube.
**ffmpeg:** Para conversão de vídeos MP4 para MP3.
**pathlib:** Para manipulação de caminhos de arquivos e diretórios.

## Problemas Conhecidos

Certifique-se de que o ffmpeg está corretamente instalado no seu sistema.
O nome do arquivo baixado ou convertido pode ser alterado se contiver caracteres especiais que não são suportados pelo sistema de arquivos.

##

Este README explica como instalar e usar o programa, além de listar as dependências e fornecer instruções sobre como executar o script.

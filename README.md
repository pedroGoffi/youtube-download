
# Downloader de Músicas do YouTube 🎶

Um script simples em Python para baixar vídeos do YouTube ou convertê-los em arquivos MP3. Fácil de usar, suporta links individuais e playlists.

---

## Funcionalidades
- **Baixar Vídeos:** Salve vídeos do YouTube na resolução desejada.
- **Baixar Músicas:** Extraia áudio em MP3 de alta qualidade dos vídeos do YouTube.
- **Suporte a Playlists:** Baixe playlists inteiras ou links individuais.
- **Diretório Personalizado:** Escolha onde salvar seus downloads.

---

## Instalação

### Pré-requisitos
1. **Python 3.7 ou superior**: Certifique-se de que o Python está instalado. [Baixe aqui](https://www.python.org/downloads/)
2. **FFmpeg**: Necessário para extrair áudio. Instale via:
   - **Windows:** [Baixe o FFmpeg](https://ffmpeg.org/download.html)
   - **Linux/macOS:** Use o gerenciador de pacotes do sistema, por exemplo:
     ```bash
     sudo apt install ffmpeg  # Linux
     brew install ffmpeg      # macOS
     ```

### Passos
1. Clone ou baixe este repositório:
   ```bash
   git clone https://github.com/seu-repo/downloader-youtube.git
   cd downloader-youtube
   ```
2. Instale as dependências do Python:
   ```bash
   pip install yt-dlp
   ```

---

## Como Usar

### Sintaxe Básica
```bash
python downloader.py [OPÇÕES]
```

### Opções
| Opção             | Descrição                                                                                          |
|--------------------|----------------------------------------------------------------------------------------------------|
| `--src`           | Link para um vídeo/playlist do YouTube ou caminho para um arquivo `.txt` com múltiplos links.      |
| `-o, --output`    | Diretório onde os downloads serão salvos. Padrão: `C:\\Users\\<USUARIO>\\Music\\`.                     |
| `--qualidade`     | Resolução do vídeo (ex.: `360`, `720`, `1080`). Ignorado para downloads de música. Padrão: `720`.   |
| `--playlist`      | Ativa o modo playlist para baixar todos os itens da playlist. Padrão: modo de link único.          |
| `--musica`        | Baixa como MP3 (música). Padrão: modo vídeo.                                                       |

### Exemplos

#### Baixar um Vídeo
```bash
python downloader.py --src https://www.youtube.com/watch?v=exemplo
```

#### Baixar como MP3
```bash
python downloader.py --src https://www.youtube.com/watch?v=exemplo --musica
```

#### Baixar uma Playlist em MP3
```bash
python downloader.py --src https://www.youtube.com/playlist?list=exemplo --musica --playlist
```

#### Salvar Downloads em uma Pasta Específica
```bash
python downloader.py --src https://www.youtube.com/watch?v=exemplo -o D:\\Downloads
```

---

## Observações
- **Modo Playlist:** Utilize a flag `--playlist` para baixar playlists inteiras. Caso contrário, apenas o link fornecido será processado.
- **Pasta Padrão:** Se nenhum diretório de saída for especificado, os downloads serão salvos em:
  ```plaintext
  C:\Users\pedro\Music\
  ```

---

## Solução de Problemas
- Certifique-se de que o FFmpeg está instalado e acessível no PATH do sistema.
- Verifique o formato do link do YouTube.
- Confirme que a versão do Python é 3.7 ou superior.

---

## Licença
Este projeto é open-source e está disponível sob a [Licença MIT](LICENSE).

---

Aproveite seus downloads! 🎉
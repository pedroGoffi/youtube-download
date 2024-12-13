import os
import sys
import argparse
import yt_dlp as youtube_dl
import re
from typing import Optional

# Regex para verificar links do YouTube
YTB_REG: re.Pattern = re.compile(r"^(https?:\/\/)?(www\.)?(youtube\.com|youtu\.be)\/")
DEFAULT_DOWNLOAD_PATH: str = os.path.join(os.environ['USERPROFILE'], "Music")

# Logo para o programa
LOGO = """
==================================================
    DOWNLOADER YOUTUBE 🎥 | Pedro Henrique Goffi de Paulo
==================================================
"""

def print_separador() -> None:
    """Exibe um separador para organizar as mensagens no console."""
    print("=" * 50)

def baixar_video(link: str, pasta_saida: str, qualidade: str, playlist: bool) -> None:
    """Baixa vídeos de um link individual ou playlist."""
    try:
        print_separador()
        print(f"🔗 Processando {'playlist' if playlist else 'vídeo'}: {link}")
        with youtube_dl.YoutubeDL({
            'format': f'bestvideo[height<={qualidade}]+bestaudio/best',
            'outtmpl': os.path.join(pasta_saida, '%(playlist_title)s/%(title)s.%(ext)s') if playlist else os.path.join(pasta_saida, '%(title)s.%(ext)s'),
            'noplaylist': not playlist
        }) as ydl:
            ydl.download([link])
        print(f"✅ {'Playlist' if playlist else 'Vídeo'} baixado com sucesso para {pasta_saida}")
    except Exception as e:
        print(f"❌ Erro ao baixar {'playlist' if playlist else 'vídeo'}: {e}")

def baixar_musica(link: str, pasta_saida: str, playlist: bool) -> None:
    """Baixa músicas de um link individual ou playlist."""
    try:
        print_separador()
        print(f"🔗 Processando {'playlist' if playlist else 'música'}: {link}")
        with youtube_dl.YoutubeDL({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': os.path.join(pasta_saida, '%(playlist_title)s/%(title)s.%(ext)s') if playlist else os.path.join(pasta_saida, '%(title)s.%(ext)s'),
            'noplaylist': not playlist
        }) as ydl:
            ydl.download([link])
        print(f"✅ {'Playlist' if playlist else 'Música'} baixada com sucesso para {pasta_saida}")
    except Exception as e:
        print(f"❌ Erro ao baixar {'playlist' if playlist else 'música'}: {e}")

def is_youtube_link(link: str) -> bool:
    """Verifica se o link é um URL válido do YouTube."""
    return YTB_REG.match(link) is not None

def main() -> None:
    print(LOGO)
    parser = argparse.ArgumentParser(description="🎉 Baixe vídeos ou músicas do YouTube com facilidade!")
    parser.add_argument("--src", help="🔗 Link do YouTube ou caminho para um arquivo .txt com links.", required=False)
    parser.add_argument("-o", "--output", default=DEFAULT_DOWNLOAD_PATH, help="📁 Pasta de saída para salvar os arquivos (padrão: 'download').")
    parser.add_argument("--qualidade", default="720", help="📹 Qualidade do vídeo em resolução (ex: 360, 720, 1080). Ignorado para músicas.")
    parser.add_argument("--playlist", action="store_true", help="📂 Baixar como playlist (padrão: apenas o link fornecido).")
    parser.add_argument("--musica", action="store_true", help="🎵 Baixar como música (padrão: vídeo).")


    args, _     = parser.parse_known_args()
    pasta_saida = args.output
    qualidade   = args.qualidade
    playlist    = args.playlist
    modo        = "musica" if args.musica else "video"

    # Cria a pasta de saída se não existir
    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)
        print(f"📁 Pasta de saída criada: {pasta_saida}")

    if not args.src and len(sys.argv) >= 2:        
        if is_youtube_link(sys.argv[1]):

           args.src = sys.argv[1]
           print(f"✅ Encontrado link para realizar download: {args.src}")
        else:
            print("❌ ⚠️ Erro: Esperado link como primeiro argumento. Por favor, forneça um link com a flag `--src`.")
            sys.exit(1)

    
    # Verifica se o link é válido
    if not args.src or not is_youtube_link(args.src):
        print("❌ Erro: O link fornecido não é válido para o YouTube.")
        return

    # Decide entre vídeo ou música
    if modo == "video":
        baixar_video(args.src, pasta_saida, qualidade, playlist)
    elif modo == "musica":
        baixar_musica(args.src, pasta_saida, playlist)

    print_separador()
    print("🎉 Downloads concluídos! Obrigado por usar o Downloader YouTube.")
    print_separador()

if __name__ == "__main__":
    main()

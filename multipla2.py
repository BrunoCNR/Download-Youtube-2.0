from PySimpleGUI import PySimpleGUI as sgs
from pytube import YouTube, Playlist


def janela():
    sgs.theme('Reddit')
    layout = [
        [sgs.Button('Download de video unico')],
        [sgs.Button('Deseja fazer download de varios videos ?')]
    ]
    return sgs.Window('Opções de Download', layout=layout, finalize=True)


def janela_opcoes():
    sgs.theme('Reddit')
    layout = [
        [sgs.Text('Local de destino: '), sgs.Input(key='loc')],
        [sgs.Text('Link do video:'), sgs.Input(key='url')],
        [sgs.Button('Enviar')],
        [sgs.Button('Voltar')],
        [sgs.Output(size=(70, 20))]
    ]

    return sgs.Window('Informações de download', layout=layout, finalize=True)


def janela_multipla():
    sgs.theme('Reddit')
    layout = [
        [sgs.Text('Local de destino: '), sgs.Input(key='loc')],
        [sgs.Text('Link do video:'), sgs.Input(key='url')],
        [sgs.Button('Enviar')],
        [sgs.Button('Voltar')],
        [sgs.Output(size=(70, 20))]
    ]

    return sgs.Window('Download de PlayList', layout=layout, finalize=True)


janela1, janela2, janela3 = janela(), None, None

while True:
    window, event, values = sgs.read_all_windows()
    if window == janela1 and event == sgs.WIN_CLOSED:
        break
    if window == janela1 and event == 'Download de video unico':
        janela2 = janela_opcoes()
        janela1.hide()
    if window == janela2 and event == sgs.WIN_CLOSED:
        break
    if window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()
    if window == janela2 and event == 'Enviar':
        loc = values['loc']
        url = values['url']
        youtube = YouTube(url)
        video = youtube.streams.get_highest_resolution()
        video.download('{}'.format(loc))
        print(F"Finalizado --- ", video.title)
    if window == janela1 and event == 'Deseja fazer download de varios videos ?':
        janela3 = janela_opcoes()
        janela1.hide()
    if window == janela3 and event == sgs.WIN_CLOSED:
        break
    if window == janela3 and event == 'Voltar':
        janela3.hide()
        janela1.un_hide()
    if window == janela3 and event == 'Enviar':
        loc = values['loc']
        url = values['url']
        youtube_playlist = Playlist(url)
        for video in youtube_playlist.videos:
            video.streams.get_highest_resolution().download('{}'.format(loc))
            print(F"Finalizado --- ", video.title)

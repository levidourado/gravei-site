"""Gera as páginas de política de privacidade e suporte do Gravei.

Uso: python3 site/gerar_site.py site
"""
import os
import sys

OUT = sys.argv[1]
EMAIL = "contato@compusoft.com.br"
MAIL = f'<a href="mailto:{EMAIL}">{EMAIL}</a>'
LANGS = ["pt", "en", "es", "fr", "de", "it"]
LABEL = {"pt": "PT", "en": "EN", "es": "ES", "fr": "FR", "de": "DE", "it": "IT"}
HTML_LANG = {"pt": "pt-BR", "en": "en", "es": "es", "fr": "fr", "de": "de", "it": "it"}

P = {}

P["pt"] = dict(
    title="Política de privacidade do Gravei",
    date="Última atualização: 10 de outubro de 2026",
    support="Suporte",
    body=f"""
<p class="lead">O Gravei é um teleprompter para iPhone, iPad e Android. Você cola o roteiro, lê enquanto a câmera grava, e o texto pode acompanhar a sua voz. Esta página explica o que acontece com as suas informações quando você usa o app.</p>

<h2>Resumo</h2>
<p>O Gravei não coleta dados pessoais. Não tem cadastro, anúncios, ferramentas de análise nem rastreamento. Nada do que você escreve, fala ou grava chega até nós.</p>

<h2>Quem é o responsável</h2>
<p>O Gravei é publicado pela CompuSoft Computadores e Sistemas Ltda. Dúvidas ou pedidos sobre privacidade: {MAIL}.</p>

<h2>O que fica guardado no seu aparelho</h2>
<ul>
<li>O último roteiro que você escreveu ou colou e os seus ajustes (velocidade, fonte, idioma, espelhamento e outros). Ficam só no armazenamento do app, para o texto não se perder quando você fecha.</li>
<li>O vídeo do take, enquanto você está na prévia. Se você salva, ele vai para a galeria do aparelho, no álbum "Gravei", e a cópia temporária é apagada. Se descarta, ele é apagado.</li>
</ul>
<p>Para apagar o roteiro, use o botão de limpar ou desinstale o app. Os vídeos salvos ficam na sua galeria e são apagados por lá, como qualquer outro vídeo.</p>

<h2>Permissões que o app pede</h2>
<ul>
<li><strong>Câmera:</strong> gravar você enquanto lê.</li>
<li><strong>Microfone:</strong> gravar o áudio do vídeo e, com a rolagem por voz ligada, acompanhar o que você fala.</li>
<li><strong>Reconhecimento de fala</strong> (iPhone e iPad, nas versões do sistema que pedem essa permissão): fazer o texto seguir a sua voz.</li>
<li><strong>Fotos:</strong> salvar os vídeos no álbum "Gravei" da galeria.</li>
</ul>
<p>Cada permissão é pedida só quando você usa o recurso e pode ser retirada a qualquer momento nos ajustes do aparelho. Sem câmera e microfone o app não grava, mas você continua escrevendo e editando o roteiro.</p>

<h2>Como funciona a rolagem por voz</h2>
<p><strong>iPhone e iPad com iOS ou iPadOS 26 ou mais novo:</strong> o reconhecimento de fala roda no próprio aparelho, pelo sistema da Apple. Na primeira vez que você usa um idioma, o sistema pode baixar da Apple o modelo de voz desse idioma.</p>
<p><strong>Versões anteriores do iOS:</strong> o app usa o reconhecimento de fala da Apple e pede que ele rode no aparelho sempre que o idioma estiver disponível offline. Quando não está, o áudio vai para a Apple para ser transcrito, de acordo com a <a href="https://www.apple.com/br/legal/privacy/">política de privacidade da Apple</a>. Nós não recebemos esse áudio.</p>
<p><strong>Android:</strong> o reconhecimento usa o Vosk e roda inteiro no aparelho. Na primeira vez que você usa um idioma, o app baixa o modelo de voz dele (entre 31 e 47 MB) do site do projeto Vosk, alphacephei.com. Esse download é a única conexão do app com a internet. Como em qualquer download, o servidor vê o endereço IP do aparelho. Nenhum áudio ou texto é enviado.</p>

<h2>Compartilhamento</h2>
<p>Não vendemos nem compartilhamos dados, e não temos acesso aos seus roteiros, gravações ou ajustes.</p>

<h2>Crianças</h2>
<p>O app não é feito para crianças e não coleta dados de ninguém, de qualquer idade.</p>

<h2>Seus direitos (LGPD)</h2>
<p>Como não guardamos dados seus fora do aparelho, não há nada nosso para consultar, corrigir ou apagar. Se ainda assim tiver uma dúvida ou um pedido, escreva para {MAIL}.</p>

<h2>Mudanças nesta política</h2>
<p>Se o app passar a tratar dados de outro jeito, esta página muda antes, com a nova data no topo.</p>
""",
)

P["en"] = dict(
    title="Gravei privacy policy",
    date="Last updated: October 10, 2026",
    support="Support",
    body=f"""
<p class="lead">Gravei is a teleprompter for iPhone, iPad and Android. You paste your script, read it while the camera records, and the text can follow your voice. This page explains what happens to your information when you use the app.</p>

<h2>Summary</h2>
<p>Gravei does not collect personal data. There is no sign-up, no ads, no analytics and no tracking. Nothing you write, say or record reaches us.</p>

<h2>Who is responsible</h2>
<p>Gravei is published by CompuSoft Computadores e Sistemas Ltda (Brazil). Privacy questions or requests: {MAIL}.</p>

<h2>What is stored on your device</h2>
<ul>
<li>The last script you typed or pasted and your settings (speed, font, language, mirroring and so on). They stay in the app's storage so your text is still there when you come back.</li>
<li>The video of each take while you are on the preview screen. If you save it, it goes to your photo library in the "Gravei" album and the temporary copy is deleted. If you discard it, it is deleted.</li>
</ul>
<p>To delete the script, use the clear button or uninstall the app. Saved videos live in your photo library and you delete them there, like any other video.</p>

<h2>Permissions the app asks for</h2>
<ul>
<li><strong>Camera:</strong> to record you while you read.</li>
<li><strong>Microphone:</strong> to record the video's audio and, with voice scrolling on, to follow what you say.</li>
<li><strong>Speech recognition</strong> (iPhone and iPad, on system versions that ask for it): to make the text follow your voice.</li>
<li><strong>Photos:</strong> to save your videos to the "Gravei" album.</li>
</ul>
<p>Each permission is requested only when you use the feature, and you can turn it off at any time in your device settings. Without camera and microphone the app cannot record, but you can still write and edit your script.</p>

<h2>How voice scrolling works</h2>
<p><strong>iPhone and iPad on iOS or iPadOS 26 or later:</strong> speech recognition runs on the device, using Apple's system. The first time you use a language, the system may download Apple's speech model for it.</p>
<p><strong>Earlier iOS versions:</strong> the app uses Apple's speech recognition and asks for it to run on the device whenever the language is available offline. When it is not, the audio is sent to Apple to be transcribed, under <a href="https://www.apple.com/legal/privacy/">Apple's privacy policy</a>. We never receive that audio.</p>
<p><strong>Android:</strong> recognition uses Vosk and runs entirely on the device. The first time you use a language, the app downloads its speech model (31 to 47 MB) from the Vosk project's website, alphacephei.com. That download is the app's only internet connection. As with any download, the server sees your device's IP address. No audio or text is sent.</p>

<h2>Sharing</h2>
<p>We do not sell or share data, and we have no access to your scripts, recordings or settings.</p>

<h2>Children</h2>
<p>The app is not directed at children and does not collect data from anyone, of any age.</p>

<h2>Your rights</h2>
<p>Because we keep no data about you outside your device, there is nothing on our side to access, correct or delete. If you still have a question or request, write to {MAIL}.</p>

<h2>Changes to this policy</h2>
<p>If the app ever starts handling data differently, this page will be updated first, with the new date at the top.</p>
""",
)

P["es"] = dict(
    title="Política de privacidad de Gravei",
    date="Última actualización: 10 de octubre de 2026",
    support="Soporte",
    body=f"""
<p class="lead">Gravei es un teleprompter para iPhone, iPad y Android. Pegas tu guion, lo lees mientras la cámara graba y el texto puede seguir tu voz. Esta página explica qué pasa con tu información cuando usas la app.</p>

<h2>Resumen</h2>
<p>Gravei no recopila datos personales. No tiene registro, anuncios, herramientas de análisis ni seguimiento. Nada de lo que escribes, dices o grabas llega a nosotros.</p>

<h2>Responsable</h2>
<p>Gravei es publicada por CompuSoft Computadores e Sistemas Ltda (Brasil). Dudas o solicitudes sobre privacidad: {MAIL}.</p>

<h2>Qué se guarda en tu dispositivo</h2>
<ul>
<li>El último guion que escribiste o pegaste y tus ajustes (velocidad, fuente, idioma, espejo y otros). Quedan en el almacenamiento de la app para que el texto siga ahí cuando vuelvas.</li>
<li>El video de cada toma mientras estás en la vista previa. Si lo guardas, va a tu fototeca, en el álbum "Gravei", y la copia temporal se borra. Si lo descartas, se borra.</li>
</ul>
<p>Para borrar el guion, usa el botón de limpiar o desinstala la app. Los videos guardados están en tu fototeca y se borran allí, como cualquier otro video.</p>

<h2>Permisos que pide la app</h2>
<ul>
<li><strong>Cámara:</strong> grabarte mientras lees.</li>
<li><strong>Micrófono:</strong> grabar el audio del video y, con el desplazamiento por voz activado, seguir lo que dices.</li>
<li><strong>Reconocimiento de voz</strong> (iPhone y iPad, en las versiones del sistema que lo piden): hacer que el texto siga tu voz.</li>
<li><strong>Fotos:</strong> guardar los videos en el álbum "Gravei".</li>
</ul>
<p>Cada permiso se pide solo cuando usas la función y puedes retirarlo cuando quieras en los ajustes del dispositivo. Sin cámara ni micrófono la app no graba, pero puedes seguir escribiendo y editando el guion.</p>

<h2>Cómo funciona el desplazamiento por voz</h2>
<p><strong>iPhone y iPad con iOS o iPadOS 26 o posterior:</strong> el reconocimiento de voz se hace en el propio dispositivo, con el sistema de Apple. La primera vez que usas un idioma, el sistema puede descargar de Apple el modelo de voz de ese idioma.</p>
<p><strong>Versiones anteriores de iOS:</strong> la app usa el reconocimiento de voz de Apple y pide que funcione en el dispositivo siempre que el idioma esté disponible sin conexión. Cuando no lo está, el audio se envía a Apple para transcribirlo, según la <a href="https://www.apple.com/es/legal/privacy/">política de privacidad de Apple</a>. Nosotros nunca recibimos ese audio.</p>
<p><strong>Android:</strong> el reconocimiento usa Vosk y funciona por completo en el dispositivo. La primera vez que usas un idioma, la app descarga su modelo de voz (de 31 a 47 MB) del sitio del proyecto Vosk, alphacephei.com. Esa descarga es la única conexión de la app a internet. Como en cualquier descarga, el servidor ve la dirección IP del dispositivo. No se envía audio ni texto.</p>

<h2>Compartir datos</h2>
<p>No vendemos ni compartimos datos, y no tenemos acceso a tus guiones, grabaciones ni ajustes.</p>

<h2>Niños</h2>
<p>La app no está dirigida a niños y no recopila datos de nadie, de ninguna edad.</p>

<h2>Tus derechos</h2>
<p>Como no guardamos datos tuyos fuera del dispositivo, no hay nada nuestro que consultar, corregir o borrar. Si aun así tienes una duda o una solicitud, escribe a {MAIL}.</p>

<h2>Cambios en esta política</h2>
<p>Si la app empieza a tratar datos de otra forma, esta página se actualizará antes, con la nueva fecha arriba.</p>
""",
)

P["fr"] = dict(
    title="Politique de confidentialité de Gravei",
    date="Dernière mise à jour : 10 octobre 2026",
    support="Assistance",
    body=f"""
<p class="lead">Gravei est un téléprompteur pour iPhone, iPad et Android. Vous collez votre texte, vous le lisez pendant que la caméra filme, et le texte peut suivre votre voix. Cette page explique ce qu'il advient de vos informations quand vous utilisez l'app.</p>

<h2>En bref</h2>
<p>Gravei ne collecte aucune donnée personnelle. Pas de compte, pas de publicité, pas d'outils d'analyse, pas de suivi. Rien de ce que vous écrivez, dites ou filmez ne nous parvient.</p>

<h2>Responsable</h2>
<p>Gravei est publiée par CompuSoft Computadores e Sistemas Ltda (Brésil). Questions ou demandes sur la confidentialité : {MAIL}.</p>

<h2>Ce qui est enregistré sur votre appareil</h2>
<ul>
<li>Le dernier texte que vous avez saisi ou collé et vos réglages (vitesse, police, langue, miroir, etc.). Ils restent dans le stockage de l'app pour que votre texte soit toujours là à votre retour.</li>
<li>La vidéo de chaque prise tant que vous êtes sur l'aperçu. Si vous l'enregistrez, elle va dans votre photothèque, dans l'album « Gravei », et la copie temporaire est supprimée. Si vous la rejetez, elle est supprimée.</li>
</ul>
<p>Pour effacer le texte, utilisez le bouton d'effacement ou désinstallez l'app. Les vidéos enregistrées sont dans votre photothèque et se suppriment depuis celle-ci, comme toute autre vidéo.</p>

<h2>Autorisations demandées</h2>
<ul>
<li><strong>Caméra :</strong> vous filmer pendant que vous lisez.</li>
<li><strong>Micro :</strong> enregistrer le son de la vidéo et, avec le défilement à la voix activé, suivre ce que vous dites.</li>
<li><strong>Reconnaissance vocale</strong> (iPhone et iPad, sur les versions du système qui la demandent) : faire suivre votre voix au texte.</li>
<li><strong>Photos :</strong> enregistrer les vidéos dans l'album « Gravei ».</li>
</ul>
<p>Chaque autorisation n'est demandée que lorsque vous utilisez la fonction, et vous pouvez la retirer à tout moment dans les réglages de l'appareil. Sans caméra ni micro, l'app ne peut pas filmer, mais vous pouvez toujours écrire et modifier votre texte.</p>

<h2>Fonctionnement du défilement à la voix</h2>
<p><strong>iPhone et iPad sous iOS ou iPadOS 26 ou plus récent :</strong> la reconnaissance vocale se fait sur l'appareil, par le système d'Apple. La première fois que vous utilisez une langue, le système peut télécharger le modèle vocal d'Apple pour cette langue.</p>
<p><strong>Versions antérieures d'iOS :</strong> l'app utilise la reconnaissance vocale d'Apple et lui demande de fonctionner sur l'appareil chaque fois que la langue est disponible hors ligne. Sinon, l'audio est envoyé à Apple pour être transcrit, selon la <a href="https://www.apple.com/fr/legal/privacy/">politique de confidentialité d'Apple</a>. Nous ne recevons jamais cet audio.</p>
<p><strong>Android :</strong> la reconnaissance utilise Vosk et fonctionne entièrement sur l'appareil. La première fois que vous utilisez une langue, l'app télécharge son modèle vocal (de 31 à 47 Mo) depuis le site du projet Vosk, alphacephei.com. Ce téléchargement est la seule connexion de l'app à internet. Comme pour tout téléchargement, le serveur voit l'adresse IP de l'appareil. Aucun son ni texte n'est envoyé.</p>

<h2>Partage</h2>
<p>Nous ne vendons ni ne partageons de données, et nous n'avons accès ni à vos textes, ni à vos vidéos, ni à vos réglages.</p>

<h2>Enfants</h2>
<p>L'app ne s'adresse pas aux enfants et ne collecte les données de personne, quel que soit l'âge.</p>

<h2>Vos droits</h2>
<p>Comme nous ne conservons aucune donnée vous concernant hors de votre appareil, il n'y a rien chez nous à consulter, corriger ou supprimer. Pour toute question ou demande, écrivez à {MAIL}.</p>

<h2>Modifications</h2>
<p>Si l'app traite un jour les données autrement, cette page sera mise à jour avant, avec la nouvelle date en haut.</p>
""",
)

P["de"] = dict(
    title="Datenschutzerklärung von Gravei",
    date="Zuletzt aktualisiert: 10. Oktober 2026",
    support="Support",
    body=f"""
<p class="lead">Gravei ist ein Teleprompter für iPhone, iPad und Android. Du fügst dein Skript ein, liest es, während die Kamera aufnimmt, und der Text kann deiner Stimme folgen. Diese Seite erklärt, was mit deinen Informationen passiert, wenn du die App nutzt.</p>

<h2>Kurz gesagt</h2>
<p>Gravei erhebt keine personenbezogenen Daten. Es gibt keine Registrierung, keine Werbung, keine Analysetools und kein Tracking. Nichts von dem, was du schreibst, sagst oder aufnimmst, erreicht uns.</p>

<h2>Verantwortlich</h2>
<p>Gravei wird von CompuSoft Computadores e Sistemas Ltda (Brasilien) veröffentlicht. Fragen oder Anfragen zum Datenschutz: {MAIL}.</p>

<h2>Was auf deinem Gerät gespeichert wird</h2>
<ul>
<li>Das zuletzt geschriebene oder eingefügte Skript und deine Einstellungen (Geschwindigkeit, Schrift, Sprache, Spiegelung usw.). Sie bleiben im Speicher der App, damit dein Text noch da ist, wenn du zurückkommst.</li>
<li>Das Video der jeweiligen Aufnahme, solange du in der Vorschau bist. Wenn du es sicherst, landet es in deiner Mediathek im Album „Gravei“ und die temporäre Kopie wird gelöscht. Wenn du es verwirfst, wird es gelöscht.</li>
</ul>
<p>Um das Skript zu löschen, nutze die Schaltfläche zum Leeren oder deinstalliere die App. Gesicherte Videos liegen in deiner Mediathek und werden dort gelöscht, wie jedes andere Video.</p>

<h2>Berechtigungen</h2>
<ul>
<li><strong>Kamera:</strong> dich aufnehmen, während du liest.</li>
<li><strong>Mikrofon:</strong> den Ton des Videos aufnehmen und, bei aktivem Scrollen per Stimme, deinem Sprechen folgen.</li>
<li><strong>Spracherkennung</strong> (iPhone und iPad, bei Systemversionen, die danach fragen): den Text deiner Stimme folgen lassen.</li>
<li><strong>Fotos:</strong> Videos im Album „Gravei“ sichern.</li>
</ul>
<p>Jede Berechtigung wird erst angefragt, wenn du die Funktion nutzt, und lässt sich jederzeit in den Geräteeinstellungen entziehen. Ohne Kamera und Mikrofon kann die App nicht aufnehmen, du kannst dein Skript aber weiter schreiben und bearbeiten.</p>

<h2>So funktioniert das Scrollen per Stimme</h2>
<p><strong>iPhone und iPad mit iOS oder iPadOS 26 oder neuer:</strong> Die Spracherkennung läuft auf dem Gerät, über das System von Apple. Wenn du eine Sprache zum ersten Mal nutzt, kann das System das Sprachmodell dafür von Apple laden.</p>
<p><strong>Ältere iOS-Versionen:</strong> Die App nutzt die Spracherkennung von Apple und verlangt, dass sie auf dem Gerät läuft, wann immer die Sprache offline verfügbar ist. Ist sie das nicht, wird der Ton zur Transkription an Apple gesendet, gemäß der <a href="https://www.apple.com/de/legal/privacy/">Datenschutzrichtlinie von Apple</a>. Wir erhalten diesen Ton nie.</p>
<p><strong>Android:</strong> Die Erkennung nutzt Vosk und läuft vollständig auf dem Gerät. Wenn du eine Sprache zum ersten Mal nutzt, lädt die App das Sprachmodell dafür (31 bis 47 MB) von der Website des Vosk-Projekts, alphacephei.com. Dieser Download ist die einzige Internetverbindung der App. Wie bei jedem Download sieht der Server die IP-Adresse des Geräts. Es werden weder Ton noch Text gesendet.</p>

<h2>Weitergabe</h2>
<p>Wir verkaufen und teilen keine Daten und haben keinen Zugriff auf deine Skripte, Aufnahmen oder Einstellungen.</p>

<h2>Kinder</h2>
<p>Die App richtet sich nicht an Kinder und erhebt von niemandem Daten, egal welchen Alters.</p>

<h2>Deine Rechte</h2>
<p>Da wir außerhalb deines Geräts keine Daten über dich speichern, gibt es bei uns nichts einzusehen, zu berichtigen oder zu löschen. Bei Fragen oder Anliegen schreib an {MAIL}.</p>

<h2>Änderungen</h2>
<p>Falls die App Daten jemals anders verarbeitet, wird diese Seite vorher aktualisiert, mit dem neuen Datum oben.</p>
""",
)

P["it"] = dict(
    title="Informativa sulla privacy di Gravei",
    date="Ultimo aggiornamento: 10 ottobre 2026",
    support="Assistenza",
    body=f"""
<p class="lead">Gravei è un teleprompter per iPhone, iPad e Android. Incolli il copione, lo leggi mentre la fotocamera registra e il testo può seguire la tua voce. Questa pagina spiega cosa succede alle tue informazioni quando usi l'app.</p>

<h2>In breve</h2>
<p>Gravei non raccoglie dati personali. Niente registrazione, pubblicità, strumenti di analisi o tracciamento. Niente di ciò che scrivi, dici o registri arriva a noi.</p>

<h2>Titolare</h2>
<p>Gravei è pubblicata da CompuSoft Computadores e Sistemas Ltda (Brasile). Domande o richieste sulla privacy: {MAIL}.</p>

<h2>Cosa resta salvato sul dispositivo</h2>
<ul>
<li>L'ultimo copione che hai scritto o incollato e le tue impostazioni (velocità, carattere, lingua, specchio e altre). Restano nella memoria dell'app, così ritrovi il testo quando torni.</li>
<li>Il video di ogni ripresa finché sei nell'anteprima. Se lo salvi, va nella tua libreria foto, nell'album "Gravei", e la copia temporanea viene cancellata. Se lo scarti, viene cancellato.</li>
</ul>
<p>Per cancellare il copione usa il pulsante per svuotarlo oppure disinstalla l'app. I video salvati sono nella tua libreria foto e si cancellano da lì, come qualsiasi altro video.</p>

<h2>Autorizzazioni richieste</h2>
<ul>
<li><strong>Fotocamera:</strong> registrarti mentre leggi.</li>
<li><strong>Microfono:</strong> registrare l'audio del video e, con lo scorrimento vocale attivo, seguire ciò che dici.</li>
<li><strong>Riconoscimento vocale</strong> (iPhone e iPad, sulle versioni del sistema che lo richiedono): far seguire al testo la tua voce.</li>
<li><strong>Foto:</strong> salvare i video nell'album "Gravei".</li>
</ul>
<p>Ogni autorizzazione viene chiesta solo quando usi la funzione e puoi revocarla in qualsiasi momento nelle impostazioni del dispositivo. Senza fotocamera e microfono l'app non registra, ma puoi continuare a scrivere e modificare il copione.</p>

<h2>Come funziona lo scorrimento vocale</h2>
<p><strong>iPhone e iPad con iOS o iPadOS 26 o successivi:</strong> il riconoscimento vocale avviene sul dispositivo, tramite il sistema di Apple. La prima volta che usi una lingua, il sistema può scaricare da Apple il relativo modello vocale.</p>
<p><strong>Versioni precedenti di iOS:</strong> l'app usa il riconoscimento vocale di Apple e chiede che funzioni sul dispositivo ogni volta che la lingua è disponibile offline. Quando non lo è, l'audio viene inviato ad Apple per la trascrizione, secondo l'<a href="https://www.apple.com/it/legal/privacy/">informativa sulla privacy di Apple</a>. Noi non riceviamo mai quell'audio.</p>
<p><strong>Android:</strong> il riconoscimento usa Vosk e funziona interamente sul dispositivo. La prima volta che usi una lingua, l'app scarica il relativo modello vocale (da 31 a 47 MB) dal sito del progetto Vosk, alphacephei.com. Quel download è l'unica connessione a internet dell'app. Come per qualsiasi download, il server vede l'indirizzo IP del dispositivo. Non vengono inviati né audio né testo.</p>

<h2>Condivisione</h2>
<p>Non vendiamo né condividiamo dati e non abbiamo accesso ai tuoi copioni, alle registrazioni o alle impostazioni.</p>

<h2>Minori</h2>
<p>L'app non è rivolta ai minori e non raccoglie dati di nessuno, di qualsiasi età.</p>

<h2>I tuoi diritti</h2>
<p>Poiché non conserviamo tuoi dati fuori dal dispositivo, da parte nostra non c'è nulla da consultare, correggere o cancellare. Per domande o richieste scrivi a {MAIL}.</p>

<h2>Modifiche</h2>
<p>Se un giorno l'app tratterà i dati in modo diverso, questa pagina verrà aggiornata prima, con la nuova data in alto.</p>
""",
)


def page(lang, title, body, langs_html, depth):
    up = "../" * depth
    return f"""<!doctype html>
<html lang="{HTML_LANG[lang]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="color-scheme" content="light dark">
<link rel="stylesheet" href="{up}style.css">
</head>
<body>
<main>
<div class="top">
<a class="brand" href="{up}">Gravei<span>.</span></a>
<nav class="langs">{langs_html}</nav>
</div>
{body}
<footer>Gravei · CompuSoft Computadores e Sistemas Ltda · {MAIL}</footer>
</main>
</body>
</html>
"""


def privacy_langs(cur):
    return "".join(
        f'<a href="../{l}/"' + (' aria-current="page"' if l == cur else "") + f">{LABEL[l]}</a>"
        for l in LANGS
    )


for lang in LANGS:
    d = P[lang]
    body = f"<h1>{d['title']}</h1>\n<p class=\"date\">{d['date']}</p>\n{d['body']}"
    path = os.path.join(OUT, "privacy", lang)
    os.makedirs(path, exist_ok=True)
    with open(os.path.join(path, "index.html"), "w") as f:
        f.write(page(lang, d["title"], body, privacy_langs(lang), 2))

links = "".join(f'<li><a href="privacy/{l}/">{P[l]["title"]}</a></li>' for l in LANGS)
home = f"""<h1>Gravei</h1>
<p class="date">Teleprompter para iPhone, iPad e Android</p>
<p class="lead">Cole o roteiro, grave com a câmera frontal e deixe o texto acompanhar a sua voz.</p>

<h2>Suporte</h2>
<p>Encontrou um problema ou tem uma sugestão? Escreva para {MAIL} contando o modelo do aparelho, a versão do sistema e o que aconteceu. Respondemos em português, inglês ou espanhol.</p>

<h2>Support (English)</h2>
<p>Found a bug or have a suggestion? Email {MAIL} with your device model, system version and what happened.</p>

<h2>Privacidade · Privacy</h2>
<p>O Gravei não coleta dados pessoais. Gravei does not collect personal data.</p>
<ul>{links}</ul>
"""
with open(os.path.join(OUT, "index.html"), "w") as f:
    f.write(page("pt", "Gravei: suporte", home, "", 0))

open(os.path.join(OUT, ".nojekyll"), "w").close()
print("ok")

# ============================================================
# TAHUN TERAKHIR DI NUSA BANGSA
# Visual Novel - Ren'Py
# ============================================================

define config.name = "Tahun Terakhir di Nusa Bangsa"
define config.window_title = "Tahun Terakhir di Nusa Bangsa"

# ------------------------------------------------------------
# KARAKTER
# ------------------------------------------------------------

define p = Character("[player_name]", color="#c8e6ff")
define adelia = Character("Adelia", color="#ffb7cb")
define raka = Character("Raka", color="#ffc879")
define maya = Character("Bu Maya", color="#b8d9ff")
define revan = Character("Kak Revan", color="#c8b8ff")
define narator = Character(None)

# ------------------------------------------------------------
# LATAR SEMENTARA
# Bisa diganti dengan gambar latar nanti.
# ------------------------------------------------------------

image bg classroom = Solid("#a8bac8")
image bg corridor = Solid("#8da5b8")
image bg window = Solid("#8298a9")
image bg musicroom = Solid("#655d68")
image bg library = Solid("#777d88")
image bg home = Solid("#5c5963")
image bg schoolyard = Solid("#9cabb1")
image bg stage = Solid("#292b43")
image bg graduation = Solid("#788b9c")
image bg black = Solid("#101116")

# ------------------------------------------------------------
# STAT DAN FLAG
# ------------------------------------------------------------

default player_name = "Kamu"

default prestasi = 0
default pertemanan = 0
default passion = 0

default ekskul = ""
default helped_raka = False
default reported_raka = False
default ignored_raka = False

default raka_secret = False
default raka_trust = 0

default supported_adelia = False
default supported_revan = False
default supported_friends = False

default noticed_absences = False
default joined_performance = False
default applied_scholarship = False

# ------------------------------------------------------------
# HUD STAT
# ------------------------------------------------------------

screen stats_hud():

    frame:
        xalign 0.98
        yalign 0.02
        background "#171b24dd"
        padding (18, 12)

        vbox:
            spacing 5

            text "STATUS" size 18 color "#ffffff"
            text "Prestasi: [prestasi]" size 15 color "#b9d9ff"
            text "Pertemanan: [pertemanan]" size 15 color "#ffc9d9"
            text "Passion: [passion]" size 15 color "#d5c3ff"

# ============================================================
# PEMBUKAAN
# ============================================================

label start:

    $ player_name = renpy.input(
        "Siapa namamu?",
        default="Kamu",
        length=20
    ).strip()

    if not player_name:
        $ player_name = "Kamu"

    show screen stats_hud

    scene bg black
    with fade

    narator "Tahun Terakhir di Nusa Bangsa"

    narator "Katanya, tahun terakhir di SMA adalah waktu untuk mempersiapkan masa depan."

    narator "Memilih universitas. Menentukan cita-cita. Menyelesaikan hal-hal yang belum sempat dilakukan."

    narator "Semua orang sepertinya sudah punya rencana."

    narator "Sementara itu, kamu bahkan belum yakin harus memulai dari mana."

    narator "Hari ini, kamu resmi menjadi murid pindahan kelas dua belas di SMA Nusa Bangsa."

    narator "Dan satu tahun dari sekarang, semuanya akan berubah."

    jump chapter_1


# ============================================================
# BAB 1: HARI PERTAMA
# ============================================================

label chapter_1:

    scene bg corridor
    with fade

    narator "BAB 1: HARI PERTAMA"

    narator "Langkah kakimu semakin cepat ketika melihat jam di ponsel."

    p "Aduh, hari pertama malah telat."

    narator "Kamu berhenti di depan sebuah kelas. Dari balik pintu terdengar suara guru sedang menjelaskan pelajaran."

    scene bg classroom
    with dissolve

    maya "Kamu pasti murid pindahan yang Ibu tunggu."

    maya "Silakan masuk. Perkenalkan dirimu sebentar."

    p "Nama saya [player_name]. Saya murid pindahan dan mulai belajar di sini hari ini."

    maya "Baik. Semoga kamu bisa beradaptasi dengan teman-teman baru."

    maya "Sekarang, cari tempat duduk yang masih kosong."

    narator "Ada beberapa tempat yang bisa kamu pilih."

    menu:

        "Duduk di sebelah Adelia":

            $ prestasi += 1

            narator "Seorang siswi dengan catatan pelajaran yang tersusun rapi menggeser tasnya."

            adelia "Di sini masih kosong. Kamu bisa duduk."

            p "Terima kasih."

            adelia "Kalau ada materi yang tertinggal, nanti aku bisa bantu. Tapi sebaiknya kamu segera mengejar pelajaran."

            p "Baik. Aku akan berusaha."

            adelia "Bagus. Kita punya banyak materi yang harus diselesaikan tahun ini."

            $ supported_adelia = True

        "Duduk di sebelah Raka":

            $ pertemanan += 1

            narator "Seorang siswa mengangkat tasnya dari kursi kosong."

            raka "Wah, murid baru. Selamat datang di kelas paling normal di sekolah ini."

            p "Memangnya kelas lain seperti apa?"

            raka "Rahasia. Kamu harus bertahan di sini dulu sebelum mengetahuinya."

            p "Kamu selalu begini?"

            raka "Baru lima menit kenal sudah menilai orang. Kejam sekali."

            narator "Raka tertawa kecil. Suasana yang semula canggung terasa sedikit lebih santai."

        "Duduk sendirian di dekat jendela":

            $ passion += 1

            narator "Kamu memilih kursi kosong di dekat jendela."

            narator "Dari sana, kamu bisa melihat lapangan sekolah dan gedung di sebelahnya."

            p "Sepertinya aku butuh waktu untuk terbiasa."

            narator "Kamu membuka buku catatan. Untuk sementara, kamu memilih mengamati semuanya dari kejauhan."

    scene bg classroom
    with dissolve

    maya "Baik, semuanya. Kita lanjutkan pelajaran."

    narator "Hari pertama berjalan lebih cepat daripada yang kamu perkirakan."

    scene bg corridor
    with dissolve

    narator "Saat istirahat, kamu melewati lorong di dekat ruang musik."

    narator "Sebuah melodi gitar terdengar dari balik pintu."

    p "Siapa yang main gitar?"

    narator "Kamu berhenti sejenak untuk mendengarkan."

    narator "Ada sesuatu dari melodi itu yang membuatmu ingin tahu lebih jauh."

    jump chapter_2


# ============================================================
# BAB 2: PILIH EKSKUL
# ============================================================

label chapter_2:

    scene bg schoolyard
    with fade

    narator "BAB 2: PILIH EKSKUL"

    narator "Beberapa hari berlalu. Kamu mulai mengenali wajah-wajah di kelas, tetapi belum menemukan kegiatan yang benar-benar ingin kamu tekuni."

    narator "Pendaftaran ekstrakurikuler dibuka minggu ini."

    maya "Pilih kegiatan yang sesuai dengan minat kalian. Jangan memilih hanya karena teman kalian ikut."

    maya "Kalian akan menghabiskan banyak waktu di sana, jadi pikirkan baik-baik."

    menu:

        "Bergabung dengan Klub Olimpiade":

            $ ekskul = "olimpiade"
            $ prestasi += 2

            scene bg library
            with dissolve

            narator "Kamu memutuskan bergabung dengan Klub Olimpiade."

            adelia "Kamu juga mendaftar di sini?"

            p "Iya. Aku ingin meningkatkan kemampuan akademikku."

            adelia "Kalau begitu, kita mungkin akan sering bertemu."

            adelia "Aku biasanya menyusun jadwal belajar setiap minggu. Kalau kamu mau, kita bisa bertukar catatan."

            p "Kedengarannya bagus."

            adelia "Pastikan kamu konsisten. Hasil yang baik perlu usaha yang teratur."

            narator "Sejak hari itu, Adelia menjadi salah satu orang yang paling sering kamu temui."

        "Menjadi panitia OSIS":

            $ ekskul = "osis"
            $ pertemanan += 2

            scene bg schoolyard
            with dissolve

            narator "Kamu memilih bergabung dengan kepanitiaan OSIS."

            raka "Jadi, kamu bakal ikut rapat juga?"

            p "Sepertinya begitu. Kenapa?"

            raka "Karena aku juga kadang bantu acara sekolah. Setidaknya sekarang ada orang yang bisa diajak mengeluh soal rapat."

            p "Baru bergabung sudah mau mengeluh?"

            raka "Aku menyebutnya persiapan mental."

            narator "Kamu mulai mengenal lebih banyak siswa dan terlibat dalam kegiatan sekolah."

            narator "Raka menjadi salah satu teman yang paling sering bekerja bersamamu."

        "Bergabung dengan Klub Musik":

            $ ekskul = "musik"
            $ passion += 2

            scene bg musicroom
            with dissolve

            narator "Kamu membuka pintu ruang musik."

            narator "Seorang siswa yang lebih tua sedang menyetel gitar."

            revan "Kamu anggota baru?"

            p "Iya. Aku tertarik setelah mendengar seseorang bermain gitar beberapa hari lalu."

            revan "Mungkin aku orangnya."

            p "Mungkin?"

            revan "Kalau aku mengaku, nanti kamu langsung menganggapku hebat."

            narator "Ia tersenyum dan meletakkan gitarnya."

            revan "Aku Revan. Panggil saja Kak Revan."

            revan "Di sini, kamu boleh belajar dari awal. Yang penting kamu mau latihan."

            p "Aku akan mencoba."

            revan "Bagus. Kita lihat sejauh mana kamu bisa berkembang tahun ini."

            narator "Sejak itu, ruang musik menjadi tempat yang sering kamu kunjungi."

    jump chapter_3


# ============================================================
# BAB 3: UTS
# ============================================================

label chapter_3:

    scene bg classroom
    with fade

    narator "BAB 3: UTS"

    narator "Waktu berjalan. Tanpa terasa, ujian tengah semester sudah di depan mata."

    narator "Tugas menumpuk, kegiatan ekstrakurikuler semakin sibuk, dan kamu harus menentukan prioritas."

    if ekskul == "olimpiade":

        adelia "Jangan lupa, kita masih punya beberapa materi yang belum dibahas."

        adelia "Kalau kamu mau mengejar nilai tinggi, kita harus mulai belajar lebih awal."

    elif ekskul == "osis":

        raka "Aku baru selesai mengurus daftar perlengkapan acara."

        raka "Dan sekarang kita harus belajar buat UTS. Hidup memang penuh kejutan."

    elif ekskul == "musik":

        revan "Kamu sudah berkembang sejak pertama datang."

        revan "Tapi UTS juga penting. Jangan sampai latihan membuatmu melupakan sekolah."

    narator "Malam sebelum ujian, kamu harus menentukan cara menghabiskan waktumu."

    menu:

        "Belajar sendiri sampai malam":

            $ prestasi += 2
            $ pertemanan -= 1

            scene bg library
            with dissolve

            narator "Kamu memilih belajar sendiri hingga larut malam."

            p "Kalau aku bisa memahami semua materi ini, setidaknya aku tidak akan terlalu khawatir besok."

            narator "Pesan dari teman-temanmu terus berdatangan, tetapi kamu memilih menyelesaikan latihan soal."

            adelia "Kamu masih belajar?"

            p "Iya. Aku belum selesai."

            adelia "Jangan lupa istirahat. Kamu tetap perlu menjaga kondisi saat ujian."

            p "Aku tahu. Terima kasih."

            narator "Kamu merasa lebih siap menghadapi ujian, meskipun malam itu kamu hampir tidak punya waktu untuk berbincang dengan teman-teman."

        "Belajar kelompok bersama Raka":

            $ pertemanan += 2

            scene bg library
            with dissolve

            narator "Kamu memutuskan belajar bersama Raka."

            raka "Oke, siapa yang siap menghadapi soal-soal yang ditulis oleh orang yang membenci murid?"

            p "Baca soalnya dulu."

            raka "Aku sedang membangun suasana."

            narator "Kalian tertawa sebelum mulai mengerjakan soal."

            raka "Kalau ada yang tidak kamu mengerti, bilang saja."

            p "Kamu yakin bisa menjelaskan?"

            raka "Aku bisa menjelaskan dengan percaya diri. Soal benar atau salah, itu urusan lain."

            narator "Meski beberapa kali bercanda, kalian berhasil menyelesaikan banyak soal bersama."

            $ noticed_absences = True

            narator "Namun, kamu menyadari bahwa Raka beberapa kali melihat ponselnya dengan wajah cemas."

            p "Ada masalah?"

            raka "Nggak. Cuma urusan rumah."

            narator "Ia segera mengalihkan pembicaraan."

        "Latihan band dan pasrah":

            $ passion += 2
            $ prestasi -= 1

            scene bg musicroom
            with dissolve

            narator "Kamu memilih datang ke ruang musik."

            revan "Bukannya besok ujian?"

            p "Aku tahu. Aku cuma ingin latihan sebentar."

            revan "Sebentar itu bisa berubah menjadi tiga jam kalau kamu tidak hati-hati."

            p "Aku akan mengatur waktunya."

            narator "Kamu berlatih bersama anggota klub musik."

            revan "Kamu punya kemajuan. Tapi jangan abaikan hal lain yang juga penting."

            p "Aku mengerti, Kak."

            narator "Kamu pulang dengan melodi yang terus terngiang di kepala, meskipun masih ada beberapa materi ujian yang belum kamu kuasai."

            $ noticed_absences = True

    scene bg classroom
    with dissolve

    narator "Hari ujian akhirnya tiba."

    narator "Setelah ujian selesai, kamu kembali memperhatikan sesuatu yang terasa janggal."

    narator "Raka semakin sering tidak masuk sekolah."

    jump chapter_4


# ============================================================
# BAB 4: MASALAH RAKA
# ============================================================

label chapter_4:

    scene bg classroom
    with fade

    narator "BAB 4: MASALAH RAKA"

    narator "Kursi Raka kosong lagi."

    narator "Awalnya kamu mengira ia hanya sakit atau memiliki urusan pribadi. Namun, ketidakhadirannya semakin sering terjadi."

    if pertemanan >= 3:

        scene bg corridor
        with dissolve

        raka "Kamu memperhatikan aku sering nggak masuk, ya?"

        p "Iya. Aku mulai khawatir."

        raka "Sebenarnya ada masalah di rumah."

        raka "Usaha orang tuaku sedang kesulitan. Aku harus membantu mereka, jadi kadang aku nggak bisa datang ke sekolah."

        p "Kenapa kamu tidak cerita dari awal?"

        raka "Aku nggak mau semua orang memperlakukanku secara berbeda."

        raka "Aku masih ingin menjalani hari-hari sekolah seperti biasanya."

        $ raka_trust += 2
        $ raka_secret = True

    else:

        narator "Kamu memutuskan mencari tahu dengan bertanya kepada Bu Maya."

        scene bg classroom
        with dissolve

        p "Bu, saya mau bertanya tentang Raka."

        maya "Ada apa dengannya?"

        p "Dia semakin sering tidak masuk sekolah. Saya khawatir."

        maya "Kamu benar untuk memperhatikannya."

        maya "Kondisi keluarganya sedang sulit. Usaha orang tuanya mengalami masalah, dan Raka berusaha membantu mereka."

        p "Jadi, itu sebabnya dia sering absen?"

        maya "Iya. Ibu sedang berusaha mencari cara agar dia bisa tetap mengikuti pelajaran."

        $ noticed_absences = True

    scene bg corridor
    with dissolve

    narator "Sekarang kamu tahu bahwa Raka sedang menghadapi masalah yang jauh lebih besar daripada yang ia tunjukkan di sekolah."

    narator "Kamu bisa memilih untuk membantunya, meminta bantuan guru, atau membiarkannya menyelesaikan masalah sendiri."

    menu:

        "Membantu Raka secara diam-diam":

            $ helped_raka = True
            $ pertemanan += 2
            $ raka_trust += 2

            scene bg home
            with dissolve

            narator "Kamu menghubungi Raka dan menawarkan bantuan."

            p "Kalau ada tugas yang tertinggal, aku bisa membantu mencatatkan materi untukmu."

            raka "Kamu serius?"

            p "Iya. Kamu tetap harus mengerjakan tugasnya, tapi setidaknya kamu tidak perlu mengejar semuanya dari nol."

            raka "Terima kasih."

            raka "Aku sebenarnya takut bakal tertinggal terlalu jauh."

            p "Kita cari cara supaya kamu tetap bisa mengikuti pelajaran."

            narator "Kamu mulai membagikan catatan pelajaran dan membantu Raka mengejar tugas yang tertinggal."

            narator "Kamu tidak bisa menyelesaikan masalah keluarganya, tetapi kamu bisa membantunya menghadapi sekolah."

        "Melaporkan situasinya kepada Bu Maya":

            $ reported_raka = True
            $ prestasi += 1
            $ raka_trust += 1

            scene bg classroom
            with dissolve

            p "Bu, saya rasa Raka membutuhkan bantuan."

            maya "Terima kasih sudah memberi tahu Ibu."

            maya "Ibu akan mencoba berbicara dengannya dan mencari jalan keluar yang tepat."

            narator "Bu Maya kemudian menghubungi Raka untuk membicarakan keadaannya."

            raka "Kamu yang memberi tahu Bu Maya?"

            p "Iya. Aku khawatir kamu semakin tertinggal."

            raka "Aku mengerti. Aku cuma berharap urusan ini tidak menjadi pembicaraan semua orang."

            p "Aku juga tidak ingin itu terjadi."

            raka "Terima kasih sudah peduli."

        "Berpura-pura tidak mengetahui masalahnya":

            $ ignored_raka = True
            $ pertemanan -= 1

            scene bg classroom
            with dissolve

            narator "Kamu memilih untuk tidak ikut campur."

            p "Mungkin dia punya alasan sendiri."

            narator "Kamu melanjutkan kegiatan seperti biasa."

            narator "Namun, setiap kali melihat kursi Raka kosong, kamu kembali teringat percakapan kalian."

            narator "Ada banyak hal yang tidak bisa kamu ketahui hanya dengan melihat seseorang dari luar."

    jump chapter_5


# ============================================================
# BAB 5: BENTROK JADWAL
# ============================================================

label chapter_5:

    scene bg classroom
    with fade

    narator "BAB 5: BENTROK JADWAL"

    narator "Semester terakhir semakin dekat."

    narator "Suatu pagi, tiga kesempatan datang hampir bersamaan."

    if ekskul == "olimpiade":

        scene bg library
        with dissolve

        adelia "Ada seleksi beasiswa yang akan dibuka minggu ini."

        adelia "Aku ingin mendaftar. Kamu mau ikut?"

        p "Aku akan mempertimbangkannya."

        adelia "Ini kesempatan bagus untuk kita."

    elif ekskul == "osis":

        scene bg schoolyard
        with dissolve

        raka "Panitia pensi butuh bantuan tambahan."

        raka "Aku tahu kamu juga punya banyak urusan, tapi aku ingin kamu ikut membantu."

        p "Aku akan melihat jadwalku."

        raka "Oke. Aku cuma berharap kita bisa menyelesaikan acara ini bersama."

    elif ekskul == "musik":

        scene bg musicroom
        with dissolve

        revan "Pentas seni tinggal beberapa minggu lagi."

        revan "Aku ingin kamu ikut tampil."

        p "Aku belum yakin sudah cukup bagus."

        revan "Kamu tidak akan pernah tahu kalau terus menunggu sampai merasa sempurna."

        p "Aku akan memikirkannya, Kak."

    scene bg classroom
    with dissolve

    narator "Di hari yang sama, kamu mengetahui bahwa seleksi beasiswa, persiapan pentas seni, dan kebutuhan Raka untuk mendapatkan dukungan terjadi dalam waktu yang berdekatan."

    narator "Kamu ingin membantu semuanya, tetapi waktumu terbatas."

    narator "Kamu harus memilih satu hal untuk diprioritaskan."

    menu:

        "Mengikuti seleksi beasiswa bersama Adelia":

            $ prestasi += 2
            $ applied_scholarship = True
            $ supported_adelia = True

            scene bg library
            with dissolve

            adelia "Kamu jadi ikut mendaftar!"

            p "Iya. Aku ingin mencoba kesempatan ini."

            adelia "Bagus. Kita bisa mempersiapkan dokumen dan belajar bersama."

            p "Tapi aku mungkin tidak bisa membantu banyak untuk kegiatan lain."

            adelia "Aku mengerti. Kita semua sedang mengejar sesuatu."

            adelia "Yang penting, kita berusaha sebaik mungkin."

            narator "Kamu menghabiskan sebagian besar waktumu untuk mempersiapkan seleksi."

            narator "Namun, kamu juga menyadari bahwa ada beberapa hal lain yang harus kamu tunda."

        "Mempersiapkan pentas seni bersama Kak Revan":

            $ passion += 2
            $ joined_performance = True
            $ supported_revan = True

            scene bg musicroom
            with dissolve

            revan "Jadi, kamu memutuskan untuk tampil?"

            p "Iya. Aku ingin tahu sejauh mana kemampuanku."

            revan "Bagus. Kita akan mulai latihan lebih serius."

            p "Aku mungkin tidak punya banyak waktu untuk kegiatan lain."

            revan "Kalau begitu, kita harus mengatur jadwal dengan baik."

            narator "Kamu mulai berlatih untuk pentas seni."

            narator "Ada banyak hal yang harus dipelajari, tetapi kamu merasa semakin dekat dengan sesuatu yang ingin kamu lakukan."

        "Mendampingi Raka":

            $ pertemanan += 2
            $ supported_friends = True
            $ raka_trust += 1

            scene bg corridor
            with dissolve

            p "Raka, kamu ada waktu?"

            raka "Ada apa?"

            p "Aku ingin memastikan kamu baik-baik saja."

            raka "Aku masih berusaha mengurus semuanya."

            p "Kamu tidak harus menghadapi semuanya sendirian."

            raka "Aku tahu. Terima kasih sudah datang."

            narator "Kamu menghabiskan waktu untuk mendengarkan Raka dan membantunya menyusun cara agar ia tetap bisa mengikuti kegiatan sekolah."

            narator "Kamu mungkin melewatkan sebagian persiapan lain, tetapi kamu tahu bahwa keputusanmu berarti bagi seseorang."

    narator "Hari-hari berikutnya berlalu dengan cepat."

    narator "Kamu mulai memahami bahwa setiap pilihan membawa konsekuensi. Waktu yang diberikan kepada satu hal berarti waktu yang berkurang untuk hal lainnya."

    jump chapter_6


# ============================================================
# BAB 6: MALAM SEBELUM LULUS
# ============================================================

label chapter_6:

    scene bg graduation
    with fade

    narator "BAB 6: MALAM SEBELUM LULUS"

    narator "Tahun ajaran hampir berakhir."

    narator "Dalam beberapa hari, kamu akan meninggalkan SMA Nusa Bangsa."

    narator "Kamu mengingat hari pertama ketika datang terlambat, belum mengenal siapa pun, dan belum tahu apa yang ingin kamu lakukan."

    narator "Sekarang, kamu sudah sampai di penghujung perjalanan."

    if ekskul == "olimpiade":

        adelia "Kamu ingat waktu pertama kali datang ke kelas?"

        p "Aku ingat. Aku bahkan terlambat."

        adelia "Sekarang kita sudah hampir lulus."

        adelia "Aku masih ingin mendapatkan hasil terbaik, tetapi aku juga mulai memahami bahwa tidak semua hal bisa berjalan sesuai rencana."

        p "Kamu terdengar berbeda dari dulu."

        adelia "Mungkin karena tahun ini mengajarkanku banyak hal."

    elif ekskul == "osis":

        raka "Aneh, ya. Rasanya baru kemarin kita sibuk mengurus kegiatan sekolah."

        p "Dan sekarang semuanya hampir selesai."

        raka "Aku akan merindukan masa-masa ini."

        p "Termasuk rapat yang panjang?"

        raka "Jangan merusak momen ini."

        narator "Kalian tertawa, mengingat semua hal yang pernah terjadi."

    elif ekskul == "musik":

        scene bg musicroom
        with dissolve

        revan "Kamu sudah banyak berkembang sejak pertama datang."

        p "Aku masih punya banyak hal untuk dipelajari."

        revan "Semua musisi juga begitu."

        revan "Yang penting, kamu tahu apa yang ingin kamu lakukan berikutnya."

        p "Aku akan mencoba terus."

        revan "Kalau begitu, jangan berhenti hanya karena kamu belum tahu hasil akhirnya."

    scene bg graduation
    with dissolve

    narator "Sebelum hari kelulusan, kamu kembali bertemu Raka."

    if helped_raka:

        raka "Aku ingin berterima kasih sekali lagi."

        raka "Kamu membantuku ketika semuanya terasa berat."

        p "Aku senang bisa membantu."

        raka "Aku belum bisa menyelesaikan semuanya, tapi sekarang aku merasa lebih siap."

        p "Kamu sudah berusaha sejauh ini. Teruskan saja."

    elif reported_raka:

        raka "Bu Maya sudah banyak membantuku mengatur tugas yang tertinggal."

        p "Syukurlah."

        raka "Terima kasih karena sudah peduli."

    elif ignored_raka:

        raka "Akhirnya kita sampai di penghujung tahun."

        p "Iya. Banyak hal yang terjadi."

        raka "Semoga setelah ini semuanya menjadi lebih baik."

    else:

        raka "Setahun ini terasa cepat sekali."

        p "Benar."

        raka "Aku senang kita bisa melewati semuanya."

    narator "Malam itu, kamu memikirkan semua keputusan yang telah kamu ambil."

    narator "Ada hal-hal yang berhasil kamu capai, ada kesempatan yang terlewat, dan ada hubungan yang menjadi lebih dekat."

    narator "Sekarang, satu pertanyaan tersisa."

    narator "Siapa dirimu setelah satu tahun ini?"

    jump determine_ending


# ============================================================
# PENENTU ENDING
# ============================================================

label determine_ending:

    # Ending rahasia diperiksa terlebih dahulu.
    # Selisih maksimal antara stat tertinggi dan terendah: 2.

    $ highest_stat = max(prestasi, pertemanan, passion)
    $ lowest_stat = min(prestasi, pertemanan, passion)

    if helped_raka and (highest_stat - lowest_stat <= 2):

        jump ending_together

    # Ending utama berdasarkan stat tertinggi.
    # Jika ada nilai yang sama, urutan prioritas:
    # Prestasi, lalu Pertemanan, lalu Passion.

    if prestasi >= pertemanan and prestasi >= passion:

        jump ending_juara

    elif pertemanan >= prestasi and pertemanan >= passion:

        jump ending_rumah

    else:

        jump ending_nada


# ============================================================
# ENDING 1: JUARA
# ============================================================

label ending_juara:

    scene bg library
    with fade

    narator "ENDING: JUARA"

    narator "Hari pengumuman beasiswa akhirnya tiba."

    if applied_scholarship:

        narator "Kamu membuka pengumuman dengan tangan sedikit gemetar."

        narator "Namamu tercantum dalam daftar penerima beasiswa."

        p "Aku berhasil..."

    else:

        narator "Sepanjang tahun, kamu berusaha menjaga nilai dan meningkatkan kemampuan akademik."

        narator "Kamu belum mendapatkan semua kesempatan yang kamu inginkan, tetapi usahamu membuka jalan menuju masa depan."

        p "Setidaknya, aku tahu aku sudah berusaha."

    adelia "Selamat!"

    p "Terima kasih, Adelia."

    adelia "Aku tahu kamu sudah bekerja keras."

    adelia "Kita akhirnya bisa melangkah menuju masa depan."

    p "Iya. Aku harap kita tetap bisa saling mendukung."

    adelia "Tentu saja."

    narator "Kamu berhasil mendapatkan kesempatan untuk melanjutkan pendidikan ke kampus impianmu."

    narator "Namun, ketika mengingat kembali tahun terakhir di SMA, kamu juga teringat pada waktu yang pernah kamu habiskan untuk belajar."

    narator "Ada percakapan yang terlewat. Ada kegiatan yang tidak sempat kamu ikuti. Ada momen bersama teman-teman yang tidak bisa diulang."

    scene bg graduation
    with dissolve

    narator "Kamu tidak menyesali kerja kerasmu."

    narator "Kamu hanya berharap bisa menemukan keseimbangan yang lebih baik pada perjalanan berikutnya."

    narator "Masa depanmu terbuka lebar."

    narator "Dan kali ini, kamu tahu bahwa keberhasilan juga membutuhkan orang-orang yang berjalan bersamamu."

    jump game_credits


# ============================================================
# ENDING 2: RUMAH
# ============================================================

label ending_rumah:

    scene bg schoolyard
    with fade

    narator "ENDING: RUMAH"

    narator "Hari kelulusan tiba."

    narator "Kamu mungkin bukan siswa dengan nilai tertinggi atau pencapaian paling besar."

    narator "Namun, ketika kamu tiba di sekolah, beberapa teman langsung memanggil namamu."

    raka "Hei! Akhirnya datang juga."

    p "Memangnya kalian sudah menunggu lama?"

    raka "Tentu saja. Kita harus mengambil foto bersama."

    narator "Satu per satu teman sekelas berkumpul."

    narator "Di antara keramaian itu, kamu melihat Raka tersenyum dengan lebih tenang daripada sebelumnya."

    raka "Aku masih punya banyak masalah yang harus diselesaikan."

    raka "Tapi sekarang aku merasa bisa menghadapinya."

    p "Kamu pasti bisa."

    raka "Dan kalau aku butuh bantuan?"

    p "Kamu tahu harus mencari siapa."

    raka "Baiklah. Tapi jangan harap aku akan berhenti membuat lelucon."

    p "Aku sudah menduganya."

    narator "Kalian tertawa."

    narator "Adelia datang membawa beberapa foto kelas yang baru dicetak."

    adelia "Kalian harus ikut berfoto. Ini hari terakhir kita sebagai siswa di sini."

    p "Baik. Aku datang."

    narator "Kamu melihat orang-orang yang telah menemanimu selama setahun."

    narator "Mereka memiliki impian dan masalah masing-masing, tetapi kalian telah melewati banyak hal bersama."

    narator "Kamu tidak tahu apa yang akan terjadi setelah lulus."

    narator "Namun, kamu tahu bahwa kenangan ini akan selalu menjadi bagian dari dirimu."

    narator "Di SMA Nusa Bangsa, kamu menemukan sesuatu yang lebih besar daripada sekadar teman sekelas."

    narator "Kamu menemukan tempat untuk pulang."

    jump game_credits


# ============================================================
# ENDING 3: NADA PERTAMA
# ============================================================

label ending_nada:

    scene bg stage
    with fade

    narator "ENDING: NADA PERTAMA"

    narator "Lampu panggung menyala."

    narator "Suara penonton memenuhi halaman sekolah."

    revan "Sudah siap?"

    p "Sejujurnya, tidak."

    revan "Bagus. Berarti kamu masih punya alasan untuk merasa gugup."

    p "Kak, itu tidak membantu."

    revan "Kalau begitu, anggap saja semua orang di depan sana datang untuk mendengarkanmu."

    narator "Kamu menarik napas panjang."

    narator "Lalu, musik dimulai."

    narator "Pada awalnya, tanganmu terasa kaku. Namun, perlahan kamu mulai menikmati setiap nada."

    narator "Ketika lagu berakhir, tepuk tangan memenuhi halaman sekolah."

    p "Kita berhasil."

    revan "Kamu berhasil. Aku hanya membantu sedikit."

    narator "Beberapa hari kemudian, sebuah pesan masuk ke ponselmu."

    narator "Seseorang dari label musik independen kecil melihat penampilanmu dan ingin berbicara tentang kemungkinan kerja sama."

    p "Serius?"

    narator "Kamu membaca pesan itu berulang kali."

    narator "Kamu tahu kesempatan ini belum menjamin kesuksesan. Industri musik penuh persaingan, dan perjalananmu masih panjang."

    revan "Apa pun keputusanmu, jangan lupa alasan kamu mulai bermusik."

    p "Aku hanya ingin terus membuat musik."

    revan "Kalau begitu, teruslah belajar."

    scene bg graduation
    with dissolve

    narator "Pada hari kelulusan, kamu membawa pulang lebih dari sekadar ijazah."

    narator "Kamu membawa keberanian untuk mencoba sesuatu yang belum pasti."

    narator "Kamu belum tahu ke mana musik akan membawamu."

    narator "Tetapi untuk pertama kalinya, kamu ingin mencari tahu."

    narator "Ini bukan akhir perjalananmu."

    narator "Ini adalah nada pertama."

    jump game_credits


# ============================================================
# ENDING RAHASIA: SEMUA BERSAMA
# ============================================================

label ending_together:

    scene bg stage
    with fade

    narator "ENDING RAHASIA: SEMUA BERSAMA"

    narator "Pentas seni sekolah akhirnya dimulai."

    narator "Kamu berdiri di belakang panggung bersama anggota klub musik."

    revan "Kamu sudah siap?"

    p "Aku rasa begitu."

    revan "Bagus. Ada sesuatu yang perlu kamu tahu."

    p "Apa?"

    revan "Musik bukan hanya soal siapa yang paling hebat di atas panggung."

    revan "Kadang, yang membuat penampilan berarti adalah orang-orang yang berdiri bersamamu."

    narator "Kamu mengangguk."

    narator "Ketika musik dimulai, beberapa temanmu ikut naik ke panggung."

    narator "Raka berdiri di dekatmu, sementara Adelia membantu mengatur bagian penampilan yang belum selesai."

    p "Kalian benar-benar ikut?"

    raka "Tentu saja. Masa kami membiarkanmu tampil sendirian?"

    adelia "Jangan salah mengira ini berarti aku akan berhenti mengejar prestasi."

    p "Aku tidak pernah berpikir begitu."

    adelia "Bagus. Sekarang fokus ke penampilanmu."

    narator "Kalian mulai bermain."

    narator "Ada bagian yang tidak sempurna. Ada nada yang terdengar sedikit terlambat."

    narator "Namun, kalian terus bermain sampai lagu berakhir."

    narator "Tepuk tangan terdengar dari seluruh penjuru halaman sekolah."

    scene bg graduation
    with dissolve

    narator "Pada hari kelulusan, kamu kembali memandang sekolah yang telah menjadi bagian penting dari hidupmu."

    raka "Kita benar-benar sudah selesai, ya?"

    adelia "Setidaknya untuk urusan SMA."

    revan "Setelah ini, kalian semua punya jalan masing-masing."

    p "Tapi kita masih bisa bertemu lagi."

    raka "Tentu. Kita harus mengadakan reuni."

    adelia "Jangan membicarakan reuni sebelum kita benar-benar lulus."

    narator "Kalian tertawa bersama."

    narator "Selama setahun, kamu telah belajar, membangun hubungan, dan mengejar hal yang kamu sukai."

    narator "Kamu tidak harus memilih hanya satu hal untuk menjadi bagian dari dirimu."

    narator "Kamu boleh berusaha menjadi lebih baik, menjaga orang-orang yang berarti, dan tetap mengejar impianmu."

    narator "Saat meninggalkan SMA Nusa Bangsa, kamu tidak membawa semua jawaban."

    narator "Namun, kamu tidak lagi merasa harus menghadapi masa depan sendirian."

    narator "Karena perjalanan ini telah mengajarkanmu bahwa terkadang, hal terbaik yang bisa kamu capai adalah tumbuh bersama."

    jump game_credits


# ============================================================
# KREDIT DAN MAIN ULANG
# ============================================================

label game_credits:

    scene bg black
    with fade

    hide screen stats_hud

    narator "TAHUN TERAKHIR DI NUSA BANGSA"

    narator "Terima kasih sudah memainkan cerita ini."

    narator "Setiap pilihan membentuk perjalananmu."

    narator "Dan setiap perjalanan memiliki cerita yang berbeda."

    menu:

        "Mainkan lagi":

            jump restart_game

        "Keluar dari cerita":

            return


label restart_game:

    $ prestasi = 0
    $ pertemanan = 0
    $ passion = 0

    $ ekskul = ""
    $ helped_raka = False
    $ reported_raka = False
    $ ignored_raka = False

    $ raka_secret = False
    $ raka_trust = 0

    $ supported_adelia = False
    $ supported_revan = False
    $ supported_friends = False

    $ noticed_absences = False
    $ joined_performance = False
    $ applied_scholarship = False

    jump start

# Config of Ghost BSD

```
==> /etc/rc.conf <==
background_dhclient="YES"
wlans_iwm0="wlan0"
ifconfig_wlan0="WPA SYNCDHCP powersave"
vboxnet_enable="YES"
root_rw_mount="NO"
sendmail_enable="NONE"
sendmail_submit_enable="NO"
sendmail_outbound_enable="NO"
sendmail_msp_queue_enable="NO"
devfs_system_ruleset="devfsrules_common"
kld_list="geom_mirror geom_journal geom_eli linux /boot/modules/i915kms.ko"
rc_interactive="YES"
ntpd_enable="YES"
ntpd_sync_on_start="YES"
keymap="us.iso"
hostname="ghostbsd-pc"
zfs_enable="YES"
ifconfig_wlan0_ipv6="inet6 accept_rtadv"
linux_enable="YES"
#microcode_update_enable="YES"
kldload_vbox="vboxdrv"

==> /boot/loader.conf <==
loader_brand="gbsd"
loader_logo="gbsd"
hw.psm.synaptics_support="1"
# boot_mute="YES"
crypto_load="YES"
aesni_load="YES"
geom_eli_load="YES"
zfs_load="YES"
if_iwm_load="YES"
iwm8265fw_load="YES"
wlan_ccmp_load="YES"
wlan_tkip_load="YES"
vboxdrv_load="YES"
vm.kmem_size="330M"
vm.kmem_size_max="330M"
vfs.zfs.arc_max="40M"
vfs.zfs.vdev.cache.size="5M"
                              
```
Oh my zsh 
```
git clone https://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh
cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc
```
```
ZSH_THEME="bureau"
```
pkg info 
```
CoinMP-1.8.3_1                 Optimization library with support for COIN-OR CLP, CBC, and CGL
GentiumBasic-1102              Gentium Basic and Gentium Book Basic TrueType fonts
GeoIP-1.6.12                   Find the country that any IP address or hostname originates from
ORBit2-2.14.19_2               High-performance CORBA ORB with support for the C language
OpenEXR-2.2.1_1                High dynamic-range (HDR) image file format
aalib-1.4.r5_12                ASCII art library
accountsservice-0.6.40         D-Bus interface for user account query and manipulation
adwaita-icon-theme-3.22.0      GNOME Symbolic Icons
alsa-lib-1.1.2_1               ALSA compatibility library
alsa-plugins-1.1.1_3           ALSA compatibility library plugins
appstream-glib-0.5.7           Library to help with AppStream metadata
apr-1.6.3.1.6.1_1              Apache Portability Library
argyllcms-1.9.2_3              ICC compatible color management system
aspell-0.60.6.1_7              Spelling checker with better suggestion logic than ispell
at-spi2-atk-2.24.0             Assisted Technology Provider module for GTK+
at-spi2-core-2.24.0            Assistive Technology Service Provider Interface
atk-2.24.0                     GNOME accessibility toolkit (ATK)
atkmm-2.24.2_2                 C++ wrapper for ATK API library
atril-1.20.1                   MATE multi-format document viewer
avahi-app-0.7_1                Service discovery on a local network
bamf-0.5.3_1                   BAMF Application Matching Framework
bash-4.4.23                    GNU Project's Bourne Again SHell
bind-tools-9.12.2P1_1          Command line tools from BIND: delv, dig, host, nslookup...
binutils-2.30_5,1              GNU binary tools
boehm-gc-7.6.8                 Garbage collection and memory leak detection for C and C++
boost-libs-1.68.0_1            Free portable C++ libraries (without Boost.Python)
brisk-menu-0.5.1               Brisk Menu is an efficient menu for the MATE Desktop
brotli-1.0.5_1,1               Generic-purpose lossless compression algorithm
ca_root_nss-3.39_1             Root certificate bundle from the Mozilla Project
cairo-1.14.8_2,2               Vector graphics library with cross-device output support
cairomm-1.12.2_2               C++ interface to cairo
caja-1.20.2                    File manager for the MATE desktop
caja-extensions-1.20.0         Set of extensions for Caja
cantarell-fonts-0.0.25         Cantarell, a Humanist sans-serif font family
cdrdao-1.2.4_1                 Record CD-R[W]s in disk-at-once mode
celt-0.11.3_3                  The CELT ultra-low delay audio codec
cheese-3.18.1_2                Photobooth-inspired app for taking pictures and videos from webcam
chromium-68.0.3440.106_3       Google web browser based on WebKit
clucene-2.3.3.4_15             CLucene is a C++ port of Lucene
clutter-1.26.2                 OpenGL based interactive canvas library
clutter-gst3-3.0.14_1          Clutter GStreamer integration
clutter-gtk3-1.8.2             GTK+ Integration library for Clutter
cmocka-1.1.1_1                 Unit testing framework for C with support for mock objects
cogl-1.22.2                    Clutter OpenGL abstraction library
colord-1.2.12                  Manage color profiles to accurately color input/output devices
consolekit2-1.2.0              Framework for defining and tracking users
crosextrafonts-caladea-20130214_1 Font created by Google for ChromeOS to replace MS Cambria
crosextrafonts-carlito-20130920_2 Font created by Google for ChromeOS to replace MS Calibri
cscope-15.8b                   Interactive C program browser
ctags-5.8                      Feature-filled tagfile generator for vi and emacs clones
cups-2.2.8_1                   Common UNIX Printing System
cups-filters-1.16.0_6          Additional backends, filters and other software for CUPS
cups-pk-helper-0.2.6           Helper that makes system-config-printer use PolicyKit
cups-smb-backend-1.0_11        CUPS backend for printing to Windows servers
curl-7.61.1                    Command line tool and library for transferring data with URLs
cursor-dmz-theme-0.4.5         DMZ style neutral scalable cursor theme
cuse4bsd-kmod-0.1.36           Cuse4BSD character device loopback driver for userspace
cvsps-2.1_2                    Create patchset information from CVS
db5-5.3.28_7                   Oracle Berkeley DB, revision 5.3
dbus-1.10.16_2                 Message bus system for inter-application communication
dbus-glib-0.108                GLib bindings for the D-BUS messaging system
dconf-0.26.1                   Configuration database system for GNOME
dconf-editor-3.22.1            Configuration database editor for GNOME
dejavu-2.37                    Bitstream Vera Fonts clone with a wider range of characters
desktop-file-utils-0.23        Couple of command line utilities for working with desktop entries
devcpu-data-1.20               Intel and AMD CPUs microcode updates
dhcpcd-7.0_4                   DHCP/IPv4LL/IPv6RS/DHCPv6 client
dialog4ports-0.1.6             Console Interface to configure ports
djvulibre-3.5.27_1             DjVu base libraries and utilities
dmidecode-3.1_1                Tool for dumping DMI (SMBIOS) contents in human-readable format
doas-6.0p2                     Simple sudo alternative to run commands as another user
docbook-1.5                    Meta-port for the different versions of the DocBook DTD
docbook-sgml-4.5_1             DocBook SGML DTD
docbook-xml-5.0_3              DocBook XML DTD
docbook-xsl-1.76.1,1           XSL DocBook stylesheets
dotconf-1.3_1                  Simple, powerful configuration-file parser
dpkg-1.18.25                   Debian package maintenance system
drm-next-kmod-4.11.g20180822   DRM modules for the linuxkpi-based KMS components
droid-fonts-ttf-20131024_3     The Droid typeface family
e2fsprogs-libuuid-1.44.4       UUID library from e2fsprogs package
emojione-color-font-ttf-1.4    Color emoji font using EmojiOne Unicode 9.0
en-aspell-7.1.0_1              Aspell English dictionaries
en-hunspell-2018.04.16         English hunspell dictionaries
enchant-1.6.0_8                Dictionary/spellchecking framework
enchant2-2.2.3_1               Dictionary/spellchecking framework
encodings-1.0.4_4,1            X.Org Encoding fonts
engrampa-1.20.0                Archive manager for zip files, tar, etc
eom-1.20.0                     Eye of MATE image viewer
espeak-1.48.04_5               Software speech synthesizer
evolution-data-server-3.24.2_11 Data backends for the Evolution integrated mail/PIM suite
exaile-3.4.5_1                 Full featured python-based music player for GTK+
exempi-2.2.2_1                 Port of Adobe XMP SDK to work on UNIX
exiv2-0.26,1                   Exif, IPTC, and XMP metadata manipulation library and tools
expat-2.2.6_1                  XML 1.0 parser written in C
faac-1.29.9.2_1                MPEG-2 and MPEG-4 AAC audio encoder
faad2-2.8.8,1                  MPEG-2 and MPEG-4 AAC audio decoder
farstream-0.2.7                Collection of GStreamer modules and libraries for videoconferencing
fbsdpkgupdate-0.2              Tool to create pkg update list
fbsdupdatecheck-0.2            Tool to install FreeBSD system Update.
ffmpeg-4.0.2_3,1               Realtime audio/video encoder/converter and streaming server
fftw3-3.3.8_1                  Fast C routines to compute the Discrete Fourier Transform
fftw3-float-3.3.8_1            Fast Discrete Fourier Transform (Single Precision C Routines)
firefox-62.0_1,1               Web browser based on the browser portion of Mozilla
firefox-i18n-62.0_1            Localized interface for Firefox
fish-2.7.0                     User friendly command line shell
flac-1.3.2                     Free lossless audio codec
flashplayer-30.0               Native wrapper around Linux Flash Player
fltk-1.3.4                     Cross-platform C++ graphical user interface toolkit
fluidsynth-1.1.11              Real-time software synthesizer based on the SoundFont 2 specifications
font-adobe-100dpi-1.0.3_3      X.Org Adobe 100dpi font
font-adobe-75dpi-1.0.3_3       X.Org Adobe 75dpi font
font-adobe-utopia-100dpi-1.0.4_3 X.Org Adobe Utopia 100dpi font
font-adobe-utopia-75dpi-1.0.4_3 X.Org Adobe Utopia 75dpi font
font-adobe-utopia-type1-1.0.4_3 X.Org Adobe Utopia Type1 font
font-alias-1.0.3_3             X.Org Font aliases
font-arabic-misc-1.0.3_3       X.Org miscellaneous Arabic fonts
font-bh-100dpi-1.0.3_3         X.Org Bigelow Holmes 100dpi font
font-bh-75dpi-1.0.3_3          X.Org Bigelow Holmes 75dpi font
font-bh-lucidatypewriter-100dpi-1.0.3_3 X.Org Bigelow Holmes Lucida TypeWriter 100dpi font
font-bh-lucidatypewriter-75dpi-1.0.3_3 X.Org Bigelow Holmes Lucida TypeWriter 75dpi font
font-bh-ttf-1.0.3_3            X.Org Bigelow & Holmes TTF font
font-bh-type1-1.0.3_3          X.Org Bigelow Holmes Type1 font
font-bitstream-100dpi-1.0.3_3  X.Org Bitstream Vera 100dpi font
font-bitstream-75dpi-1.0.3_3   X.Org Bitstream Vera 75dpi font
font-bitstream-type1-1.0.3_3   X.Org Bitstream Vera Type1 font
font-cronyx-cyrillic-1.0.3_3   X.Org Cronyx Cyrillic font
font-cursor-misc-1.0.3_3       X.Org miscellaneous Cursor fonts
font-daewoo-misc-1.0.3_3       X.Org miscellaneous Daewoo fonts
font-dec-misc-1.0.3_3          X.Org miscellaneous Dec fonts
font-ibm-type1-1.0.3_3         X.Org IBM Type1 font
font-isas-misc-1.0.3_3         X.Org miscellaneous ISAS fonts
font-jis-misc-1.0.3_3          X.Org miscellaneous JIS fonts
font-micro-misc-1.0.3_3        X.Org miscellaneous Micro fonts
font-misc-cyrillic-1.0.3_3     X.Org miscellaneous Cyrillic font
font-misc-ethiopic-1.0.3_3     X.Org miscellaneous Ethiopic font
font-misc-meltho-1.0.3_3       X.Org miscellaneous Meltho font
font-misc-misc-1.1.2_3         X.Org miscellaneous Misc fonts
font-mutt-misc-1.0.3_3         X.Org miscellaneous Mutt fonts
font-schumacher-misc-1.1.2_3   X.Org miscellaneous Schumacher fonts
font-screen-cyrillic-1.0.4_3   X.Org Screen Cyrillic font
font-sony-misc-1.0.3_3         X.Org miscellaneous Sony fonts
font-sun-misc-1.0.3_3          X.Org miscellaneous Sun fonts
font-util-1.3.1                Create an index of X font files in a directory
font-winitzki-cyrillic-1.0.3_3 X.Org Winitzki Cyrillic font
font-xfree86-type1-1.0.4_3     X.Org XFree86 Type1 font
fontconfig-2.12.6,1            XML-based font configuration API for X Windows
fonts-indic-2.1.5_3            The Lohit family of Indic fonts
foomatic-db-20180713           Database for integrating printer drivers with common spoolers
foomatic-db-engine-4.0.13,2    Foomatic database engine
foomatic-db-hpijs-1.4          Foomatic data for the HPIJS printer drivers
freebsd-release-manifests-20180627 FreeBSD release manifests
freedesktop-sound-theme-0.8    Sound theme based on the FreeDesktop specification
freeglut-3.0.0_1               open source implementation of the GLUT library
freetype2-2.9.1                Free and portable TrueType font rendering engine
fribidi-0.19.7                 Free Implementation of the Unicode Bidirectional Algorithm
fusefs-ext4fuse-0.1.3_1,1      Read-only ext4 implementation for FUSE
fusefs-libs-2.9.7              FUSE allows filesystem implementation in userspace
fusefs-ntfs-2017.3.23          Mount NTFS partitions (read/write) and disk images
fusefs-simple-mtpfs-0.3.0_3    Simple MTP fuse filesystem driver
gamin-0.1.10_9                 File and directory monitoring system
gawk-4.1.4_2                   GNU version of Awk
gbi-5.8                        GBI is the GhostBSD front end user interface for pc-sysinstall.
gcab-0.8                       GObject library to create cabinet files
gcc-ecj-4.5                    Eclipse Java Compiler used to build GCC Java
gcc6-6.4.0_8                   GNU Compiler Collection 6
gcc7-7.3.0_5                   GNU Compiler Collection 7
gconf2-3.2.6_5                 Configuration database system for GNOME
gcr-3.18.0                     Library for bits of crypto UI and parsing
gdbm-1.13_1                    GNU database manager
gdk-pixbuf2-2.36.11            Graphic library for GTK+
gdrive-2.1.0                   Google Drive CLI Client
geoclue-2.4.3                  D-Bus service that provides location information
geocode-glib-3.18.2            Convenience library for the geocoding and reverse geocoding
getopt-1.1.6                   Replacement for getopt(1) that supports GNU-style long options
gettext-runtime-0.19.8.1_1     GNU gettext runtime libraries and programs
gettext-tools-0.19.8.1         GNU gettext development and translation tools
gexiv2-0.10.8_1                GObject-based wrapper around Exiv2 library
ghostbsd-bug-report-1.1        GhostBSD bug report tool
ghostbsd-icons-1.7             GhostBSD icons for GTK DE
ghostbsd-installed-common-settings-4.5 GhostBSD common settings in installed mode
ghostbsd-irc-1.3               GhostBSD irc client
ghostbsd-mate-themes-1.6       GhostBSD themes for mate flavour
ghostbsd-slim-theme-1.3        GhostBSD theme for slim and autologin too
ghostbsd-wallpapers-18.08.0    GhostBSD 18 wallpaper colection
ghostscript9-agpl-base-9.24_2  PostScript and PDF interpreter
giflib-5.1.4                   Tools and library routines for working with GIF images
git-2.18.0_2                   Distributed source code management tool
gksu-2.0.2_7                   Graphical frontend to su
glew-2.1.0                     OpenGL Extension Wrangler Library
glib-2.50.3_5,1                Some useful routines of C programming (current stable version)
glib-networking-2.50.0_1       Network-related giomodules for glib
glibmm-2.50.1_2,1              C++ interfaces for glib2
gmime26-2.6.23                 Library (written in C) for parsing and creating messages using MIME
gmp-6.1.2                      Free library for arbitrary precision arithmetic
gmtk-1.0.9_1                   Library for gnome-mplayer and gecko-mediaplayer
gnome-cups-manager-0.31_21,1   Administration tool for cups
gnome-desktop-3.18.2_1         Additional UI API for GNOME 3
gnome-doc-utils-0.20.10_5      GNOME doc utils
gnome-icon-theme-3.12.0_1      Collection of icons for the GNOME desktop
gnome-icon-theme-symbolic-3.12.0 GNOME Symbolic Icons
gnome-keyring-3.18.3_5         Program that keeps passwords and other secrets
gnome-mime-data-2.18.0_5       MIME and Application database for GNOME
gnome-mount-0.8_13             Front-end to mount, umount, and eject using HAL
gnome-mplayer-1.0.9_3          GNOME frontend for MPlayer
gnome-online-accounts-3.24.1_3 Interface provider to access the user's online accounts
gnome-vfs-2.24.4_9             GNOME Virtual File System
gnome-video-effects-0.4.3      Collection of Gstreamer effects
gnome_subr-1.0_1               Common startup and shutdown subroutines used by GNOME scripts
gnupg-2.2.10_1                 Complete and free PGP implementation
gnutls-3.5.19                  GNU Transport Layer Security library
gobject-introspection-1.50.0_1,1 Generate interface introspection data for GObject libraries
gohugo-0.48                    Fast and flexible static site generator
gpgme-1.11.1                   Library to make access to GnuPG easier
gpu-firmware-kmod-g20180825    Firmware modules for the linuxkpi-based KMS components
graphene-1.6.0_2               Optimizations for speeding up vector operations
graphite2-1.3.12               Rendering capabilities for complex non-Roman writing systems
grub2-efi-2.02_19              Multiboot EFI boot loader
grub2-pcbsd-2.02q_13           Multiboot boot loader
gsettings-desktop-schemas-3.18.1 Collection of globally shared GSetting schemas
gsfonts-8.11_8                 Standard Fonts for Ghostscript
gsmartcontrol-1.1.3_1          Graphical user interface for smartmontools
gssdp-1.0.2                    Framework for UPnP devices
gstreamer-0.10.36_6            Development framework for creating media applications
gstreamer-plugins-0.10.36_9,3  GStreamer written collection of plugins handling several media types
gstreamer-plugins-bad-0.10.23_4,3 Bad gstreamer-plugins
gstreamer-plugins-faad-0.10.23_2,3 Gstreamer MPEG-2 and MPEG-4 AAC decoder plugin
gstreamer-plugins-good-0.10.31_3,3 Good gstreamer-plugins
gstreamer-plugins-neon-0.10.23_2,3 Gstreamer neon plugin
gstreamer-plugins-ogg-0.10.36_2,3 Gstreamer Ogg bitstream plugin
gstreamer-plugins-soup-0.10.31_2,3 Gstreamer soup http src plugin
gstreamer-plugins-theora-0.10.36_2,3 Gstreamer theora plugin
gstreamer-plugins-vorbis-0.10.36_2,3 Gstreamer vorbis encoder/decoder plugin
gstreamer-plugins-vp8-0.10.23_5,3 Gstreamer vp8 codec plugin
gstreamer1-1.12.3              Media applications framework
gstreamer1-libav-1.12.3_2      GStreamer plug-in with many audio/video decoders/encoders
gstreamer1-plugins-1.12.3_1    GStreamer written collection of plugins handling several media types
gstreamer1-plugins-a52dec-1.12.3 GStreamer ATSC A/52 stream aka AC-3 (dvd audio) plugin
gstreamer1-plugins-bad-1.12.3_2 GStreamer-plugins that need more quality, testing or documentation
gstreamer1-plugins-core-1.12   Core set of typical audio and video GStreamer plugins
gstreamer1-plugins-dts-1.12.3  GStreamer dts audio decode plugin
gstreamer1-plugins-dvdread-1.12.3 GStreamer DVD access plugin with libdvdread
gstreamer1-plugins-faac-1.12.3 GStreamer MPEG-2 and MPEG-4 AAC encoder plugin
gstreamer1-plugins-flac-1.12.3 GStreamer free lossless audio encoder/decoder plugin
gstreamer1-plugins-gl-1.12.3   GStreamer GL graphics plugin
gstreamer1-plugins-good-1.12.3 GStreamer-plugins good-quality plug-ins
gstreamer1-plugins-jpeg-1.12.3 GStreamer jpeg encoder/decoder plugin
gstreamer1-plugins-lame-1.12.3 GStreamer High-quality free mp3 encode plugin
gstreamer1-plugins-mpg123-1.12.3 GStreamer MPEG Layer 1, 2, and 3 plugin
gstreamer1-plugins-ogg-1.12.3  GStreamer Ogg bitstream plugin
gstreamer1-plugins-pango-1.12.3 GStreamer pango textoverlay plugin
gstreamer1-plugins-png-1.12.3  GStreamer png plugin
gstreamer1-plugins-resindvd-1.12.3 GStreamer resindvd DVD playback plugin
gstreamer1-plugins-theora-1.12.3 GStreamer theora plugin
gstreamer1-plugins-ugly-1.12.3 GStreamer-plugins set of good-quality plug-ins that might have distribution problems
gstreamer1-plugins-v4l2-1.12.3 GStreamer Video 4 Linux 2 source plugin
gstreamer1-plugins-vorbis-1.12.3 GStreamer vorbis encoder/decoder plugin
gstreamer1-plugins-vpx-1.12.3_1 GStreamer vp8 codec plugin
gstreamer1-plugins-wavpack-1.12.3 GStreamer wavpack encode/decode plugin
gtar-1.30                      GNU version of the traditional tape archiver
gtk-engines2-2.20.2_3          Theme engine for the GTK+-2.0 toolkit
gtk-murrine-engine-0.98.2_5    Murrine GTK+ 2.x cairo based engine
gtk-update-icon-cache-2.24.32  Gtk-update-icon-cache utility from the Gtk+ toolkit
gtk2-2.24.32                   Gimp Toolkit for X11 GUI (previous stable version)
gtk3-3.22.29_1                 Gimp Toolkit for X11 GUI (current stable version)
gtk3-unico-engine-1.0.2_2      Gtk+ 3.0 engine
gtkmm30-3.22.2                 C++ wrapper for Gtk+3
gtksourceview3-3.24.8_1        Text widget that adds syntax highlighting to the GtkTextView widget
gtkspell-2.0.16_6              GTK+ 2 spell checking component
gucharmap-11.0.1               Unicode/ISO10646 character map and font viewer
gupnp-1.0.3                    Framework for UPnP devices
gvfs-1.26.3_10                 GNOME virtual file system
hal-0.5.14_33                  Hardware Abstraction Layer for simplifying device access
hal-info-20091130              Additional FDI files to further classify HAL devices
harfbuzz-1.8.8                 OpenType text shaping engine
harfbuzz-icu-1.8.8             Harfbuzz ICU support
hexchat-2.14.2                 IRC chat program with GTK and Text Frontend
hicolor-icon-theme-0.15_1      High-color icon theme shell from the FreeDesktop project
htop-2.2.0                     Better top(1) - interactive process viewer
hunspell-1.6.2_1               Improved spell-checker for Hungarian and other languages
hyphen-2.8.8                   Library for high quality hyphenation and justification
icu-62.1_2,1                   International Components for Unicode (from IBM)
idnkit-1.0_7                   Library to handle internationalized domain names
ilmbase-2.2.1                  ILM Base libraries a.k.a. Half, IlmThread, Imath, and Iex
indexinfo-0.3.1                Utility to regenerate the GNU info page index
intel-backlight-20180303       Control backlight on various modern Intel(R) GPUs
inxi-2.2.31                    GhostBSD inxi console and irc script
iperf3-3.6                     Improved tool to measure TCP and UDP bandwidth
iso-codes-3.76                 Lists of the country, language, and currency iso names
iso8879-1986_3                 Character entity sets from ISO 8879:1986 (SGML)
jackit-0.125.0_4               Low latency audio server
jansson-2.11                   C library for encoding, decoding, and manipulating JSON data
jasper-1.900.1_17              Implementation of the codec specified in the JPEG-2000 standard
jbig2dec-0.15                  Decoder implementation of the JBIG2 image compression format
jbigkit-2.1_1                  Lossless compression for bi-level images such as scanned pages, faxes
jpeg-turbo-2.0.0               SIMD-accelerated JPEG codec which replaces libjpeg
json-c-0.13.1                  JSON (JavaScript Object Notation) implementation in C
json-glib-1.2.8                JSON (RFC 4627) interface for Glib
jsoncpp-1.8.1_4                JSON reader and writer library for C++
keepass-2.38                   Light-weight and easy-to-use password manager
ksh93-20120801_2               Official AT&T release of KornShell 93
lame-3.100_2                   Fast MP3 encoder kit
lcms-1.19_6,1                  Light Color Management System -- a color management library
lcms2-2.9                      Accurate, fast, and small-footprint color management engine
leptonica-1.76.0               C library for efficient image processing and image analysis operations
libGLU-9.0.0_3                 OpenGL utility library
libICE-1.0.9_2,1               Inter Client Exchange library for X11
libIDL-0.8.14_3                Library for creating trees of CORBA IDL files
libSM-1.2.2_4,1                Session Management library for X11
libX11-1.6.6,1                 X11 library
libXScrnSaver-1.2.3_1          The XScrnSaver library
libXau-1.0.8_4                 Authentication Protocol library for X11
libXaw-1.0.13_1,2              X Athena Widgets library
libXcomposite-0.4.4_4,1        X Composite extension library
libXcursor-1.1.15_1            X client-side cursor loading library
libXdamage-1.1.4_4             X Damage extension library
libXdmcp-1.1.2_1               X Display Manager Control Protocol library
libXext-1.3.3_2,1              X11 Extension library
libXfixes-5.0.3_1              X Fixes extension library
libXfont-1.5.4_1,2             X font library
libXfontcache-1.0.5_4          The Xfontcache library
libXft-2.3.2_2                 Client-sided font API for X applications
libXi-1.7.9_1,1                X Input extension library
libXinerama-1.1.4_1,1          X11 Xinerama library
libXmu-1.1.2_4,1               X Miscellaneous Utilities libraries
libXp-1.0.3_1,1                X print library
libXpm-3.5.12_1                X Pixmap library
libXrandr-1.5.1_1              X Resize and Rotate extension library
libXrender-0.9.10_1            X Render extension library
libXres-1.2.0_1                X Resource usage library
libXt-1.1.5_1,1                X Toolkit library
libXtst-1.2.3_1                X Test extension
libXv-1.0.11_1,1               X Video Extension library
libXvMC-1.0.10_1               X Video Extension Motion Compensation library
libXxf86dga-1.1.4_4            X DGA Extension
libXxf86misc-1.0.4_1           X XF86-Misc Extension
libXxf86vm-1.1.4_2             X Vidmode Extension
liba52-0.7.4_3                 Free library for decoding ATSC A/52 streams, aka AC-3
libabw-0.1.2_4                 Library providing ability to interpret Abiword documents
libao-1.2.0_3                  Portable audio output library
libarchive-3.3.2,1             Library to create and read several streaming archive formats
libart_lgpl-2.3.21_3,1         Library for high-performance 2D graphics
libass-0.14.0                  Portable ASS/SSA subtitle renderer
libassuan-2.5.1                IPC library used by GnuPG and gpgme
libbonobo-2.32.1               Component and compound document system for GNOME2
libbonoboui-2.24.5_1           GUI frontend to the libbonobo component of GNOME 2
libburn-1.4.8                  Libburnia library to read/write optical discs
libcanberra-0.30_4             Implementation of the Freedesktop sound theme spec
libcanberra-gtk3-0.30_4        Implementation of the Freedesktop sound theme spec
libcddb-1.3.2_4                Library to access data on a CDDB server
libcdio-2.0.0                  Compact Disc Input and Control Library
libcdio-paranoia-10.2+0.94+2   Read audio from the CDROM directly as data
libcdr01-0.1.4_10              Library and tools for parsing Corel Draw file format
libcmis-0.5.1_9                Client library for the CMIS interface
libcroco-0.6.12                CSS2 parsing library
libcue-2.1.0                   CUE Sheet Parser Library
libdaemon-0.14_1               Lightweight C library that eases the writing of UNIX daemons
libdca-0.0.6                   Free DTS Coherent Acoustics decoder
libdmx-1.1.4_1                 DMX extension library
libdrm-2.4.93,1                Userspace interface to kernel Direct Rendering Module services
libdvdnav-6.0.0                Videolan version of the libdvdnav project
libdvdread-6.0.0               Videolan version of the libdvdread project
libe-book-0.1.3_6              Library for import of reflowable e-book formats
libedit-3.1.20170329_2,1       Command line editor library
libepoxy-1.4.3                 Library to handle OpenGL function pointer management
libepubgen-0.1.0_3             Library for generating documents in ePub format
liberation-fonts-ttf-2.00.1,2  Liberation fonts from Red Hat to replace MS TTF fonts
libetonyek01-0.1.8_2,1         Library to interpret and import Apple Keynote presentations
libevent-2.1.8_2               API for executing callback functions on events or timeouts
libexif-0.6.21_4               Library to read digital camera file meta-data
libexo-0.12.2                  Application library for the Xfce desktop environment
libexttextcat-3.4.5            Language guessing by N-Gram-Based Text Categorization
libffi-3.2.1_2                 Foreign Function Interface
libfontenc-1.1.3_2             The fontenc Library
libfreehand-0.1.2_7            Library for interpreting and importing Adobe/Macromedia drawings
libgcrypt-1.8.3                General purpose cryptographic library based on the code from GnuPG
libgd-2.2.5,1                  Graphics library for fast creation of images
libgdata-0.17.8                GLib based implimentation of the GData protocol
libgdiplus-5.6                 GDI+ API for System.Windows.Forms in Mono
libgee-0.18.1                  GObject collection library
libgksu-2.0.12_4               Library providing su and sudo functionality
libglade2-2.6.4_9              GNOME glade library
libgltf-0.0.2_15               C++ Library for rendering OpenGL models stored in glTF format
libgnome-2.32.1                Libraries for GNOME, a GNU desktop environment
libgnome-keyring-3.12.0_2      Program that keeps passwords and other secrets
libgnomecanvas-2.30.3_4        Graphics library for GNOME
libgnomecups-0.2.3_8,1         Support library for gnome cups administration
libgnomeprint-2.18.8_4         Gnome print support library
libgnomeprintui-2.18.6_4       Gnome print support library
libgnomesu-1.0.0_13            Library and frontend for running commands as root
libgnomeui-2.24.5              Libraries for the GNOME GUI, a GNU desktop environment
libgpg-error-1.32              Common error values for all GnuPG components
libgphoto2-2.5.16              Universal digital camera control library
libgsf-1.14.41                 Extensible I/O abstraction for dealing with structured file formats
libgtop-2.32.0                 GNOME top library
libgweather-3.24.1             Library to access online weather information
libgxps-0.2.5                  GObject based library for rendering XPS documents
libical-2.0.0_6                Implementation of the IETF Calendaring and Scheduling protocols
libiconv-1.14_11               Character set conversion library
libid3tag-0.15.1b_1            ID3 tags library (part of MAD project)
libidn-1.34                    Internationalized Domain Names command line tool
libidn2-2.0.5                  Implementation of IDNA2008 internationalized domain names
libijs-0.35_5                  C library that supports plugin printer driver for Ghostscript
libinotify-20180201            Kevent based inotify compatible library
libisofs-1.4.8_1               Libburnia ISO9660 filesystem creation library
libjpeg-turbo-2.0.0            SIMD-accelerated JPEG codec library, provides libTurboJPEG
libksba-1.3.5                  KSBA is an X.509 Library
liblangtag-0.6.2               Interface library to access tags for identifying languages
libltdl-2.4.6                  System independent dlopen wrapper
liblz4-1.8.2,1                 LZ4 compression library, lossless and very fast
libmad-0.15.1b_6               Libmad library (part of MAD project)
libmatekbd-1.20.1              MATE keyboard shared library
libmatemixer-1.20.0            Mixer library for MATE desktop
libmateweather-1.20.0          Library to accessing online weather informations
libmediaart-1.9.1              Library for handling media art
libmng-1.0.10_3                Multiple-image Network Graphics (MNG) reference library
libmodplug-0.8.9.0             ModPlug mod-like music shared libraries
libmspub01-0.1.4_5             Library and tools for parsing Microsoft Publisher file format
libmtp-1.1.15                  Media Transfer Protocol (MTP) library
libmwaw03-0.3.14_2             Import library for some old mac text documents
libnghttp2-1.33.0              HTTP/2.0 C Library
libnice-0.1.13                 Library and transmitter that implements ICE-19
libnice-gst1-0.1.13            Library and transmitter that implements ICE-19
libnotify-0.7.7_1              Library for desktop notifications
liboauth-1.0.3_3               C library implementing the OAuth Core standard
libodfgen01-0.1.7_1            Library for generating documents in Open Document Format (ODF)
libogg-1.3.3,4                 Ogg bitstream library
liborcus-0.13.4_3              Standalone file import filter library for spreadsheet documents
libpagemaker-0.0.4_4           Library and tools for parsing Aldus/Adobe PageMaker documents
libpaper-1.1.24.4              Library providing routines for paper size management
libpci-3.6.2                   PCI configuration space I/O made easy
libpciaccess-0.13.5            Generic PCI access library
libpeas-1.20.0                 Next evolution of the Gedit plugins engine
libproxy-0.4.15                Library that provides automatic proxy configuration management
libpthread-stubs-0.4           This library provides weak aliases for pthread functions
libpurple-2.13.0               Backend library for the Pidgin multi-protocol messaging client
libquvi-scripts09-0.9.20131130_1 Embedded lua scripts for libquvi and utility scripts
libquvi09-0.9.4_4              Cross-platform library for parsing flash media stream URLs
libqxp-0.0.0_5                 Library for parsing QuarkXPress documents
libraw-0.18.13_1               Library for manipulating raw images
libreoffice-6.0.5_4            Full integrated office productivity suite
librevenge-0.0.4_9             Base library for writing document import filters
librsvg2-2.40.20               Library for parsing and rendering SVG vector-graphic files
libsamplerate-0.1.9            Secret Rabbit Code: a Sample Rate Converter for audio
libsecret-0.18.6               Library to access the secret service API
libsexy-0.1.11_10              Extension widgets for GTK+
libsigc++-2.10.0_2             Callback Framework for C++
libsigsegv-2.12                Handling page faults in user mode
libsndfile-1.0.28_1            Reading and writing files containing sampled sound (like WAV or AIFF)
libsodium-1.0.16               Library to build higher-level cryptographic tools
libsoup-2.54.1                 SOAP (Simple Object Access Protocol) implementation in C
libsoup-gnome-2.54.1           SOAP (Simple Object Access Protocol) implementation in C
libsoxr-0.1.2.20160529_7       High quality, one-dimensional sample-rate conversion library
libspectre-0.2.8               Small library for rendering Postscript documents
libstaroffice-0.0.6_2          Library to build a filter for old StarOffice's documents
libsunacl-1.0.1                Wrapper providing SunOS NFSv4 ACL API
libtasn1-4.13                  ASN.1 structure parser library
libtheora-1.1.1_7              Theora video codec for the Ogg multimedia streaming system
libtorrent-0.13.7_1            BitTorrent Library written in C++
libtorrent-rasterbar-1.1.9     C++ library implementing a BitTorrent client
libublio-20070103_2            User space caching library
libunique-3.0.2_3              Library for single instance applications
libunistring-0.9.10            Unicode string library
libunwind-20170615             Generic stack unwinding library
libv4l-1.6.3_2                 Video4Linux library
libva-2.2.0_1                  VAAPI wrapper and dummy driver
libvdpau-1.1.1_1               VDPAU wrapper and tracing library
libvisio01-0.1.6_7             Library and tools for parsing the visio file format structure
libvncserver-0.9.11_2          Provide an easy API to a custom vnc server
libvolume_id-0.81.1            Library to provide file system type information
libvorbis-1.3.6,3              Audio compression codec library
libvpx-1.7.0_1                 VP8/VP9 Codec SDK
libwmf-0.2.8.4_15              Tools and library for converting Microsoft WMF (windows metafile)
libwnck3-3.14.0                Library used for writing pagers and taskslists
libwpd010-0.10.2_3             Tools for importing and exporting WordPerfect(tm) documents
libwpg03-0.3.2_1               Library and tools to work with WordPerfect Graphics (WPG) files
libwps-0.4.10                  Microsoft file word processor format import filter library
libwww-5.4.2                   W3C Reference Library
libx264-0.155.2917             H.264/MPEG-4 AVC Video Encoding (Library)
libxcb-1.13                    The X protocol C-language Binding (XCB) library
libxfce4menu-4.12.1_1          Widgets library for the Xfce desktop environment
libxfce4util-4.12.1            Extension library for the Xfce desktop environment
libxkbcommon-0.8.0             Keymap handling library for toolkits and window systems
libxkbfile-1.0.9_1             XKB file library
libxklavier-5.3_1,1            Utility library to make XKB stuff easier
libxml++-2.34.2_2,1            XML API for C++
libxml2-2.9.7                  XML parser library for GNOME
libxshmfence-1.2_3             Shared memory 'SyncFence' synchronization primitive
libxslt-1.1.32                 The XSLT C library for GNOME
libyaml-0.1.6_2                YAML 1.1 parser and emitter written in C
libzmf-0.0.2_10                Library that parses the file format of Zoner Callisto/Draw documents
linux-c6-alsa-lib-1.1.0_3      Advanced Linux Sound Architecture libraries (Linux CentOS 6.9)
linux-c6-alsa-plugins-oss-1.1.0_3 OSS plugin for ALSA (Linux CentOS 6.9)
linux-c6-atk-1.30.0_2          Accessibility Toolkit (Linux CentOS 6.9)
linux-c6-cairo-1.8.8_8         Vector graphics library Cairo (Linux CentOS 6.9)
linux-c6-curl-7.19.7_9         Command line tool for transferring files with URL syntax (Linux CentOS 6.9)
linux-c6-cyrus-sasl-lib-2.1.23_5 RFC 2222 SASL (Simple Authentication and Security Layer) (Linux CentOS 6.9)
linux-c6-dri-11.0.7_5          Mesa libGL runtime libraries (Linux CentOS 6.9)
linux-c6-elfutils-libelf-0.164_2 ELF file handling library (CentOS 6.9)
linux-c6-expat-2.0.1_5         XML 1.0 parser written in C (Linux CentOS 6.9)
linux-c6-fontconfig-2.8.0_3    XML-based font configuration API for X Windows (Linux CentOS 6.9)
linux-c6-gdk-pixbuf2-2.24.1_5  Graphic library for GTK+ (Linux CentOS 6.9)
linux-c6-gtk2-2.24.23_7        GTK+ library, version 2.X (Linux CentOS 6.9)
linux-c6-jasper-libs-1.900.1_5 JPEG-2000 reference implementation (Linux CentOS 6.10)
linux-c6-jpeg-1.2.1_3          SIMD-accelerated JPEG codec (Linux CentOS 6.9)
linux-c6-libpciaccess-0.13.4_2 Generic PCI access library (CentOS 6.9)
linux-c6-libpng-1.2.49_5       Library for manipulating PNG images (Linux CentOS 6.9)
linux-c6-libssh2-1.4.2_6       Library implementing the SSH2 protocol (Linux CentOS 6.9)
linux-c6-libthai-0.1.12_1      Thai language support library (Linux CentOS 6.9)
linux-c6-libtiff-3.9.4_5       Tools and library routines for working with TIFF images (Linux CentOS 6.9)
linux-c6-nspr-4.19.0           Netscape Portable Runtime (Linux CentOS 6.10)
linux-c6-nss-3.36.0            Network Security Services (Linux CentOS 6.10)
linux-c6-openldap-2.4.40_5     Lightweight Directory Access Protocol libraries (Linux CentOS 6.9)
linux-c6-openssl-1.0.1e_15     OpenSSL toolkit (Linux CentOS 6.9)
linux-c6-pango-1.28.1_7        Pango library (Linux CentOS 6.9)
linux-c6-pixman-0.32.8_1       Low-level pixel manipulation library (Linux CentOS 6.9)
linux-c6-sqlite-3.6.20_4       Library that implements an embeddable SQL database engine (Linux CentOS 6.9)
linux-c6-xorg-libs-7.4_10      Xorg libraries (Linux CentOS 6.9)
linux-flashplayer-30.0.0.154   Adobe Flash Player NPAPI Plugin
linux-sublime3-3.1.76          Sophisticated text editor for code, markup and prose
linux_base-c6-6.10             Base set of packages needed in Linux mode (Linux CentOS 6.10)
linuxlibertine-g-20120116_1    Linux Libertine G and Linux Biolinum G fonts
llvm60-6.0.1_2                 LLVM and Clang
lp_solve-5.5.2.5               Linear Programming Solver
lsof-4.92.b,8                  Lists information about open files (similar to fstat(1))
lua52-5.2.4                    Small, compilable scripting language providing easy access to C code
lua52-bitop-1.0.2_1            Bitwise operations on numbers
lua52-json-1.3.4               JSON parser/creator for Lua
lua52-lpeg-1.0.1_1             PEG-based pattern-matching library for Lua
lua52-luaexpat-1.3.0_4         LuaExpat is a SAX XML parser based on the Expat library
lua52-luasocket-3.0.r1_3,1     IPv4 and IPv6 socket support for the Lua language
lzo2-2.10_1                    Portable speedy, lossless data compression library
marco-1.20.1                   Window manager for the adult in you
mate-1.20.0                    "meta-port" for the MATE integrated X11 desktop
mate-applets-1.20.2            Applets components for the MATE Desktop Environment
mate-backgrounds-1.20.0        Collection of backgrounds for MATE
mate-base-1.20.0               "meta-port" for the MATE base integrated X11 desktop
mate-calc-1.20.1               MATE calculator tool based on the old calctool for OpenWindows
mate-control-center-1.20.2     Control center for MATE project
mate-desktop-1.20.3            Additional UI API for MATE
mate-icon-theme-1.20.0         Collection of icons for the MATE desktop
mate-icon-theme-faenza-1.20.0  Collection of Faenza and Faience icons for the MATE desktop
mate-installed-settings-3.4    GhostBSD mate settings in installed mode
mate-media-1.20.0              Multimedia applications for the MATE desktop
mate-menus-1.20.0              Implementation of the FreeDesktop Desktop Menu Spec
mate-notification-daemon-1.20.0 Send small notifications to your desktop
mate-panel-1.20.3              Panel component for the MATE Desktop
mate-polkit-1.20.0             MATE frontend to the PolicKit framework
mate-power-manager-1.20.1_1    Power management system for the MATE Desktop
mate-screensaver-1.20.0        MATE screen saver and locker
mate-session-manager-1.20.0    Session component for the MATE desktop
mate-settings-daemon-1.20.1    MATE settings daemon
mate-system-monitor-1.20.0_2   MATE system monitor program
mate-terminal-1.20.0_1         Terminal component for the MATE Desktop
mate-themes-3.22.14            Collection of themes and icons for MATE
mate-utils-1.20.0              MATE support utilities
mesa-demos-8.4.0_1             OpenGL demos distributed with Mesa
mesa-dri-18.1.5                OpenGL hardware acceleration drivers for DRI2+
mesa-libs-18.1.5               OpenGL libraries that support GLX and EGL clients
minizip-1.2.11                 Zip library and programs from Zlib distribution
mkfontdir-1.0.7                Create an index of X font files in a directory
mkfontscale-1.1.3_1            Creates an index of scalable font files for X
mono-5.10.1.57                 Open source implementation of .NET Development Framework
montserrat-7.200               Sans-serif font inspired by the street signs of Montserrat
mozo-1.20.0                    Editor for the freedesktop.org menu specification
mpc-1.1.0_1                    Library of complex numbers with arbitrarily high precision
mpfr-4.0.1                     Library for multiple-precision floating-point computations
mpg123-1.25.10                 Command-line player for MPEG Layer 1, 2, and 3 audio files
mpg321-0.2.10_10               Command-line MP3 player, compatible with mpg123
mplayer-1.3.0.20180413_4       High performance media player supporting many formats
mplayer-skins-1.1.5            Skins for MPlayer's Graphical User Interface (GUI)
mtools-4.0.10_5                Collection of tools for manipulating MS-DOS files
mythes-1.2.4_4                 Simple thesaurus library
nano-2.9.8                     Nano's ANOther editor, an enhanced free Pico clone
nautilus-3.18.5_1              File manager for the GNOME desktop
neon-0.30.2_1                  HTTP and WebDAV client library for Unix systems
nettle-3.4                     Low-level cryptographic library
networkmgr-2.8                 FreeBSD/GhostBSD network conection manager
noto-lite-1.0.5_1              Google font family - lite version
npth-1.6                       New GNU Portable Threads
nspluginwrapper-1.4.4_7        Compatibility plugin for Mozilla NPAPI plugins
nspr-4.20                      Platform-neutral API for system level and libc like functions
nss-3.39                       Libraries to support development of security-enabled applications
nvidia-settings-396.24         Display Control Panel for X NVidia driver
nvidia-texture-tools-2.0.8.1_9 Texture Tools with support for DirectX 10 texture formats
nvidia-xconfig-396.24          Tool to manipulate X configuration files for the NVidia driver
o3read-0.0.4                   Standalone converter for the OpenOffice.org writer and scalc formats
octopkg-0.2.0_3                Graphical front-end to the FreeBSD pkg-ng package manager
openal-soft-1.18.2_3           Software implementation of the OpenAL specification
opencollada-1.6.63_1           Library for reading and writing COLLADA files
opencv-core-3.4.1_4            Open Source Computer Vision library
openh264-1.8.0,2               Cisco implementation of H.264 codec
openjpeg-2.3.0_1               Open-source JPEG 2000 codec
openldap-client-2.4.46         Open source LDAP client implementation
openssl-1.0.2p_1,1             SSL and crypto library
opus-1.2.1                     IETF audio codec
orc-0.4.25                     Library and toolset to operate arrays of data
p11-kit-0.23.14                Library for loading and enumerating of PKCS#11 modules
p5-Authen-SASL-2.16_1          Perl5 module for SASL authentication
p5-CGI-4.40                    Handle Common Gateway Interface requests and responses
p5-Digest-HMAC-1.03_1          Perl5 interface to HMAC Message-Digest Algorithms
p5-Error-0.17026               Error/exception handling in object-oriented programming style
p5-GSSAPI-0.28_1               Perl extension providing access to the GSSAPIv2 library
p5-HTML-Parser-3.72            Perl5 module for parsing HTML documents
p5-HTML-Tagset-3.20_1          Some useful data table in parsing HTML
p5-IO-Socket-INET6-2.72_1      Perl module with object interface to AF_INET6 domain sockets
p5-IO-Socket-SSL-2.059         Perl5 interface to SSL sockets
p5-Mozilla-CA-20180117         Perl extension for Mozilla CA cert bundle in PEM format
p5-Net-SSLeay-1.85             Perl5 interface to SSL
p5-Socket6-0.28                IPv6 related part of the C socket.h defines and structure manipulators
p5-URI-1.74                    Perl5 interface to Uniform Resource Identifier (URI) references
p7zip-16.02_2                  File archiver with high compression ratio
pam_helper-1.1                 Authenticate applications requiring PAM services
pango-1.42.0                   Open-source framework for the layout and rendering of i18n text
pangomm-2.40.1_2               C++ wrapper for Pango
patch-2.7.6                    GNU patch utility
pavucontrol-3.0_3              GTK mixer for PulseAudio
pciids-20180812                Database of all known IDs used in PCI devices
pcre-8.42                      Perl Compatible Regular Expressions library
pcre2-10.31                    Perl Compatible Regular Expressions library, version 2
perl5-5.26.2                   Practical Extraction and Report Language
pidgin-2.13.0                  Pidgin multi-protocol messaging client (GTK+ UI)
pinentry-1.1.0_1               Collection of simple PIN or passphrase entry dialogs
pinentry-gnome3-1.1.0          GNOME 3 version of the GnuPG password dialog
pinentry-tty-1.1.0             Console version of the GnuPG password dialog
pixman-0.34.0                  Low-level pixel manipulation library
pkg-1.10.5_2                   Package manager
plank-0.11.4                   Elegant, simple, and clean dock
pluma-1.20.1_1                 Small but powerful text editor for MATE Desktop Environment
png-1.6.35                     Library for manipulating PNG images
policykit-0.9_10               Framework for controlling access to system-wide components
policykit-gnome-0.9.2_8        GNOME frontend to the PolicyKit framework
polkit-0.114_1                 Framework for controlling access to system-wide components
poppler-0.57.0_1               PDF rendering library
poppler-data-0.4.9             Poppler encoding data
poppler-glib-0.57.0_1          GLib bindings to poppler
poppler-utils-0.57.0_1         Poppler's xpdf-workalike command line utilities
popt-1.16_2                    Getopt(3) like library with a number of enhancements, from Redhat
portaudio-19.6.0,1             Portable cross-platform Audio API
pot-0.5.7                      Container framework for FreeBSD
protobuf-3.5.2_1,1             Data interchange format library
pstree-2.39                    List processes as a tree
pulseaudio-11.1_1              Sound server for UNIX
pv-1.6.6                       Pipe throughput monitor
py27-cairo-1.14.1              Python 2 bindings for Cairo
py27-cddb-1.4_2                Python module to fetch information on audio CDs from CDDB
py27-dbus-1.2.0_1              Python2 bindings for the D-BUS messaging system
py27-dnspython-1.15.0          DNS toolkit for Python
py27-gobject-2.28.6_8          Python bindings for GObject
py27-gobject3-3.18.2           Common files for the Python bindings for GObject
py27-gstreamer-0.10.22_5       Python bindings for gstreamer
py27-gtk2-2.24.0_5             Set of Python bindings for GTK+
py27-iso8601-0.1.11            Simple module to parse ISO 8601 dates
py27-libxml2-2.9.7             Python interface for XML parser library for GNOME
py27-mutagen-1.41.1            Python-based audio metadata tag reader and writer
py27-notify-0.1.1_12           python bindings for libnotify
py27-pexpect-4.6.0             Pure Python Expect-like module
py27-pillow-5.0.0              Fork of the Python Imaging Library (PIL)
py27-ply-3.11                  Python Lex-Yacc
py27-ptyprocess-0.5.1          Run a subprocess in a pseudo terminal
py27-setuptools-40.0.0         Python packages installer
py27-sexy-0.1.9_8              Libsexy bindings for Python
py27-tkinter-2.7.15_6          Python bindings to the Tk widget set (Python 2.7)
py36-Babel-2.6.0               Collection of tools for internationalizing Python applications
py36-Jinja2-2.10               Fast and easy to use stand-alone template engine
py36-MarkupSafe-1.0            Implements XML/HTML/XHTML Markup safe string for Python
py36-ansible-2.6.3             Radically simple IT automation
py36-asn1crypto-0.22.0         ASN.1 library with a focus on performance and a pythonic API
py36-bcrypt-3.1.4_1            Modern password hashing for your software and your servers
py36-cairo-1.14.1              Python 2 bindings for Cairo
py36-certifi-2018.4.16         Mozilla SSL certificates
py36-cffi-1.11.5               Foreign Function Interface for Python calling C code
py36-click-6.7_1               Python package for creating command line interfaces
py36-cryptography-2.3          Cryptographic recipes and primitives for Python developers
py36-cython-0.28.2             Compiler for Writing C Extensions for the Python Language
py36-ecdsa-0.11_1              ECDSA cryptographic signature library (pure python)
py36-first-2.0.1               Return the first true value of an iterable
py36-gobject3-3.18.2           Common files for the Python bindings for GObject
py36-idna-2.7                  Internationalized Domain Names in Applications (IDNA)
py36-jmespath-0.9.3            JSON Matching Expressions
py36-netaddr-0.7.19            Manipulation of IPv4, IPv6, CIDR, EUI and MAC network addresses
py36-paramiko-2.4.0            Python SSH2 protocol library
py36-pip-9.0.3                 Tool for installing and managing Python packages
py36-pip-tools-2.0.2           Keep your pinned dependencies fresh
py36-pipenv-2018.7.1           Python Development Workflow for Humans
py36-pyasn1-0.4.2              ASN.1 toolkit for Python
py36-pycparser-2.18            C parser in Python
py36-pycrypto-2.6.1_3          Python Cryptography Toolkit
py36-pyinotify-0.9.6           Python interface to (lib)inotify
py36-pynacl-1.2.1_1            Python binding to the Networking and Cryptography library
py36-pytz-2018.5,1             World Timezone Definitions for Python
py36-setuptools-40.0.0         Python packages installer
py36-six-1.11.0                Python 2 and 3 compatibility utilities
py36-tkinter-3.6.6_6           Python bindings to the Tk widget set (Python 3.6)
py36-virtualenv-16.0.0         Tool for creating isolated Python environments
py36-virtualenv-clone-0.3.0    Python virtualenv cloning script
py36-yaml-3.13                 Python YAML parser
py37-setuptools-40.0.0         Python packages installer
py37-tkinter-3.7.0_6           Python bindings to the Tk widget set (Python 3.7)
pydbus-common-1.2.0_2          Common files for the Python bindings for the D-BUS messaging system
pygobject3-common-3.18.2       Common files for the Python bindings for GObject
pypy-6.0.0_1                   Fast, compliant implementation of the Python language
pypy-tkinter-6.0.0_1           PyPy bindings to the Tk widget set
python27-2.7.15                Interpreted object-oriented programming language
python36-3.6.6_1               Interpreted object-oriented programming language
python37-3.7.0_3               Interpreted object-oriented programming language
qbittorrent-4.1.2              Bittorrent client using Qt4/5 and libtorrent-rasterbar
qpdf-8.2.1                     Command-line tools for transforming and inspecting PDF documents
qt5-concurrent-5.11.1          Qt multi-threading module
qt5-core-5.11.1                Qt core non-graphical module
qt5-dbus-5.11.1                Qt D-Bus inter-process communication module
qt5-gui-5.11.1                 Qt graphical user interface module
qt5-imageformats-5.11.1        Qt plugins for additional image formats
qt5-network-5.11.1_1           Qt network module
qt5-opengl-5.11.1              Qt 5-compatible OpenGL support module
qt5-printsupport-5.11.1        Qt print support module
qt5-qml-5.11.1                 Qt QML and JavaScript language module
qt5-quick-5.11.1               Qt declarative framework for dynamic user interfaces
qt5-sql-5.11.1                 Qt SQL database integration module
qt5-svg-5.11.1                 Qt SVG support module
qt5-testlib-5.11.1             Qt unit testing module
qt5-widgets-5.11.1             Qt C++ widgets module
qt5-x11extras-5.11.1           Qt platform-specific features for X11-based systems
qt5-xml-5.11.1                 Qt SAX and DOM implementations
qt5-xmlpatterns-5.11.1         Qt support for XPath, XQuery, XSLT and XML Schema
qtchooser-39                   Qt tool wrapper
raptor-1.4.21_6                RDF Parser Toolkit for Redland
raptor2-2.0.15_9               RDF Parser Toolkit for Redland
rarian-0.8.1_4                 OMF help system based on the Freedesktop specification
rasqal-0.9.33_1                High-level interface for RDF
re2-20180801                   Fast C++ regex library
readline-7.0.3_1               Library for editing command lines as they are typed
recordmydesktop-0.3.8.1_7      Record desktop sessions to an Ogg-Theora-Vorbis file
redland-1.0.17_4               High-level interface for RDF
rest-0.7.93                    Easy access to RESTful web services
roboto-fonts-ttf-2.134,1       Roboto typeface family
rsync-3.1.3                    Network file distribution/synchronization utility
rtorrent-0.9.7_1               BitTorrent Client written in C++
ruby-2.4.4_2,1                 Object-oriented interpreted scripting language
samba47-4.7.10                 Free SMB/CIFS and AD/DC server and client for Unix
sdl-1.2.15_11,2                Cross-platform multimedia development API
sdl2-2.0.7                     Cross-platform multimedia development API
sdl2_image-2.0.2               Simple library to load images of various formats as SDL surfaces
sdl2_mixer-2.0.1_1             Sample multi-channel audio mixer library
sdl2_ttf-2.0.14_1              Library to use TrueType fonts to render text in SDL applications
sdocbook-xml-1.1_2,2           "Simplified" DocBook XML DTD
serf-1.3.9_3                   Serf HTTP client library
setxkbmap-1.3.1                Set the keyboard using the X Keyboard Extension
shared-mime-info-1.8           MIME types database from the freedesktop.org project
shotwell-0.28.4_1              Open source photo manager for GNOME
slim-1.3.6_16                  Graphical login manager for X11, derived from Login.app
smartmontools-6.6_2            S.M.A.R.T. disk monitoring tools
smpeg2-2.0.0_4                 Free MPEG1 video player library with sound support
snappy-1.1.6                   Fast compressor/decompressor library
speech-dispatcher-0.8.6        Common interface to speech synthesis
speex-1.2.0,1                  Audio compression format designed for speech
speexdsp-1.2.r3_1              Audio compression format designed for speech
spidermonkey52-52.8.0_1        Standalone JavaScript based from Mozilla 52-esr
sqlite3-3.24.0_1               SQL database engine in a C library
ssft-1.0                       GhostBSD ssft.sh script
startup-notification-0.12_4    Library that supports startup notification spec from freedesktop.org
station-tweak-0.3              Mate configuration system.
subversion-1.10.2_1            Version control system
sudo-1.8.25                    Allow others to run commands as root
taglib-1.11.1_1                Library for manipulating ID3 tags and Ogg comments
talloc-2.1.14                  Hierarchical pool based memory allocator
tcl86-8.6.8                    Tool Command Language
tdb-1.3.16,1                   Trivial Database
telegram-desktop-1.3.14_1      Telegram Desktop messaging app
telepathy-glib-0.24.1_1        GLib utility library for the Telepathy framework
tesseract-3.05.02_2            Commercial quality open source OCR engine
tesseract-data-3.04.00         Trained language data for the Tesseract OCR engine
tevent-0.9.37                  Talloc based event loop library
thunderbird-60.0_2             Mozilla Thunderbird is standalone mail and news that stands above
thunderbird-i18n-60.0_2        Localized interface for Thunderbird
tiff-4.0.9_1                   Tools and library routines for working with TIFF images
tk86-8.6.8_2                   Graphical toolkit for Tcl
totem-pl-parser-3.10.8         GObject-based library to parse a host of playlist formats
tpm-emulator-0.7.4_2           Trusted Platform Module (TPM) emulator
tracker-1.6.1_14               Object database, tag/metadata database, search tool and indexer
tree-1.7.0                     Display a tree-view of directories with optional color or HTML output
trousers-0.3.14_2              Open-source TCG Software Stack
unique-1.1.6_7                 Library for single instance applications
unzip-6.0_7                    List, test, and extract compressed files from a ZIP archive
update-station-1.6             Tool to update FreeBSD/GhostBSD software and system.
upower-0.99.4                  D-Bus daemon for simplifying power management tasks
utf8proc-2.1.0                 UTF-8 processing library
v4l_compat-1.6.3_1             Video4Linux IOCTL header files
vala-0.36.15_1,1               Programming language and compiler that converts Vala code into C code
vim-8.1.0342                   Improved version of the vi editor
virtualbox-ose-5.2.18          General-purpose full virtualizer for x86 hardware
virtualbox-ose-kmod-5.2.18     VirtualBox kernel module for FreeBSD
virtualgl-2.4.1_5              Redirects commands from an OpenGL app to another X server
vte3-0.50.3_1                  Terminal widget with improved accessibility and I18N support
w3m-0.5.3.20180520_1           Pager/text-based WWW browser
wavpack-5.1.0_1                Audio codec for lossless, lossy, and hybrid compression
webcamd-4.17.0.3               Port of Linux USB webcam and DVB drivers into userspace
webkit2-gtk3-2.20.3_1          Opensource browser engine using the GTK+ 3 toolkit
webp-1.0.0_1                   Google WebP image format conversion tool
wmctrl-1.07_7                  Command line tool to interact with an EWMH/NetWM compatible X managers
woff2-1.0.2_2                  Library and converter tools for the WOFF 2.0 web font format
wv-1.2.9_5                     Library and executables to access Microsoft Word files
x265-2.8_1                     H.265/High Efficiency Video Coding (HEVC) format
xauth-1.0.10                   X authority file utility
xcb-util-0.4.0_2,1             Module with libxcb/libX11 extension/replacement libraries
xcb-util-image-0.4.0_1         Port of Xlib's XImage and XShmImage functions
xcb-util-keysyms-0.4.0_1       Standard X key constants and conversion to/from keycodes
xcb-util-renderutil-0.3.9_1    Convenience functions for the Render extension
xcb-util-wm-0.4.1_3            Framework for window manager implementation
xdg-user-dirs-0.17             Tool to help manage personal user directories
xdg-utils-1.1.1                Tools to allow all applications to integrate with the free desktop
xdotool-3.20160805.1,1         Programmatically simulate keyboard input or mouse activity
xdpyinfo-1.3.2_1               Display information utility for X
xf86-input-joystick-1.6.3_1    X.Org joystick input driver
xf86-input-keyboard-1.9.0_2    X.Org keyboard input driver
xf86-input-mouse-1.9.3_1       X.Org mouse input driver
xf86-input-synaptics-1.9.1_1   X.Org synaptics input driver
xf86-input-vmmouse-13.1.0_2    X.Org vmmouse input driver
xf86-input-wacom-0.36.1_1      X.Org Wacom tablet driver
xf86-video-ati-7.9.0_2,1       X.Org ati display driver
xf86-video-intel-2.99.917.20180512_1 Driver for Intel integrated graphics chipsets
xf86-video-nv-2.1.21_2         X.Org nv display driver
xf86-video-scfb-0.0.4_6        X.Org syscons display driver
xf86-video-vesa-2.4.0_1        X.Org vesa display driver
xf86-video-vmware-13.3.0_2     X.Org vmware display driver
xfburn-0.5.5                   CD/DVD burning tool for Xfce
xfce4-conf-4.12.1              D-Bus-based configuration storage system
xinit-1.4.0,1                  X Window System initializer
xkbcomp-1.4.2                  Compile XKB keyboard description
xkeyboard-config-2.24          X Keyboard Configuration Database
xmlcatmgr-2.2_2                SGML and XML catalog manager
xmlcharent-0.3_2               XML character entities
xmlrpc-c-1.39.13_2             XML-RPC library for C and C++
xmlsec1-1.2.25                 XML Security Library
xorg-drivers-7.7_5             X.org drivers meta-port
xorg-fonts-7.7_1               X.org fonts meta-port
xorg-fonts-100dpi-7.7          X.Org 100dpi bitmap fonts
xorg-fonts-75dpi-7.7           X.Org 75dpi bitmap fonts
xorg-fonts-cyrillic-7.7        X.Org Cyrillic bitmap fonts
xorg-fonts-miscbitmaps-7.7     X.Org miscellaneous bitmap fonts
xorg-fonts-truetype-7.7_1      X.Org TrueType fonts
xorg-fonts-type1-7.7           X.Org Type1 fonts
xorg-minimal-7.5.2_2           X.Org minimal distribution metaport
xorg-server-1.18.4_9,1         X.Org X server and related programs
xorgproto-2018.4               xorg protocol headers
xorriso-1.4.8                  ISO image manipulation tool based on Libburnia
xpdf-4.00_1,1                  Display PDF files and convert them to other formats
xpi-quick-locale-switcher-1.7.8.5 Quickly change and apply a different locale from the tools menu
xprop-1.2.3                    Property displayer for X
xrandr-1.5.0                   Primitive command line interface to the RandR extension
xrdb-1.1.1                     X server resource database utility
xsel-conrad-1.2.0_1            Access X selection from command line
xset-1.2.4_1                   User preference utility for X
xterm-335                      Terminal emulator for the X Window System
xvid-1.3.5,1                   Opensource MPEG-4 codec, based on OpenDivx
yajl-2.1.0                     Portable JSON parsing and serialization library in ANSI C
zenity-3.18.0                  Display GNOME dialogs from the command line
zsh-5.6                        The Z shell
```


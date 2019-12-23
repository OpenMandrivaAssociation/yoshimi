%define debug_package %{nil}

Name:           yoshimi
Summary:        ZynAddSubFX with improved RT capacities

Version:        1.6.1
Release:        1

Source:         http://sourceforge.net/projects/yoshimi/files/1.2/%{name}-%{version}.tar.bz2
URL:            http://yoshimi.sourceforge.net
Patch0:         yoshimi-cflags.patch
License:        GPLv2
Group:          Sound
BuildRequires:  cmake libalsa-devel jackit-devel fltk-devel zlib-devel
BuildRequires:  fftw-devel mxml-devel sndfile-devel fontconfig-devel glu-devel
BuildRequires:  boost-devel
BuildRequires:  desktop-file-utils
BuildRequires:	pkgconfig(cairo)
BuildRequires:  fltk-devel

%description
Yoshimi is the legendary and powerful ZynAddSubFX multitimbral standalone
synthesizer, but with improved realtime capacities. Yoshimi can use
either ALSA or JACK for both Audio and MIDI, the default now being JACK

%build
cd src
%cmake \
	-DCMAKE_INSTALL_DATAROOTDIR=%{_datadir}
%make_build
popd

%install
%make_install -C src/build

%files
%doc %{_docdir}/%{name}/
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/pixmaps/%{name}.png
%{_iconsdir}/hicolor/*/apps/%{name}*.svg
%{_libdir}/lv2/yoshimi.lv2/
%{_mandir}/man1/%{name}.1.*






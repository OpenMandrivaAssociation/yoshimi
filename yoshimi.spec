%define debug_package %{nil}

Name:           yoshimi
Summary:        ZynAddSubFX with improved RT capacities
Version:        2.2.0
Release:        1
Source:         http://sourceforge.net/projects/yoshimi/files/2.2/%{name}-%{version}.tar.bz2
URL:            http://yoshimi.sourceforge.net
License:        GPLv2
Group:          Sound
BuildRequires:  cmake 
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(jack)
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(mxml)
BuildRequires:  sndfile-devel 
BuildRequires:  pkgconfig(fontconfig) 
BuildRequires:  pkgconfig(glu)
BuildRequires:  boost-devel
BuildRequires:	fltk-devel 
BuildRequires:	fltk-fluid 
BuildRequires:  desktop-file-utils
BuildRequires:	pkgconfig(cairo)
BuildRequires:  pkgconfig(lv2)
BuildRequires:  pkgconfig(readline)

%description
Yoshimi is the legendary and powerful ZynAddSubFX multitimbral standalone
synthesizer, but with improved realtime capacities. Yoshimi can use
either ALSA or JACK for both Audio and MIDI, the default now being JACK

%prep
%setup -q

%build
cd src
%cmake  \
        -DCMAKE_CXX_FLAGS="${RPM_OPT_FLAGS} -fPIC" \
        -DFLTK_INCLUDE_DIR=%{_includedir}/Fl \
        -DCMAKE_INSTALL_PREFIX=%{_prefix}
%make_build

%install
cd src
%make_install -C build

rm -f %{buildroot}%{_datadir}/%{name}/banks/chip/.bankdir
chmod -R 755 %{buildroot}%{_datadir}/%{name}/banks
chmod -R 755 %{buildroot}%{_datadir}/%{name}/presets
chmod a-X %{buildroot}%{_datadir}/%{name}/banks/*/*
chmod a-X %{buildroot}%{_datadir}/%{name}/presets/*

desktop-file-install \
    --remove-key="Version" \
    --add-category="X-MandrivaLinux-Sound" \
    --dir %{buildroot}%{_datadir}/applications \
%{buildroot}%{_datadir}/applications/%{name}.desktop

%clean

%files

%dir %{_datadir}/%{name}
%doc %{_datadir}/doc/yoshimi/
%{_bindir}/%{name}
%{_libdir}/lv2/yoshimi.lv2/
%{_datadir}/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/yoshimi.appdata.xml
%{_datadir}/pixmaps/%{name}.png
%{_iconsdir}/hicolor/scalable/apps/yoshimi.svg
%{_iconsdir}/hicolor/scalable/apps/yoshimi_alt.svg
%{_mandri}/man1/yoshimi.1.*






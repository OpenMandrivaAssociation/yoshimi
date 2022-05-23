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
BuildRequires:  libalsa-devel 
BuildRequires:  jackit-devel 
BuildRequires:  zlib-devel
BuildRequires:  fftw-devel 
BuildRequires:  mxml-devel 
BuildRequires:  sndfile-devel 
BuildRequires:  fontconfig-devel 
BuildRequires:  glu-devel
BuildRequires:  boost-devel
BuildRequires:	fltk-devel 
BuildRequires:	fltk-fluid 
BuildRequires:  desktop-file-utils
BuildRequires:	pkgconfig(cairo)
BuildRequires:  pkgconfig(readline)

%description
Yoshimi is the legendary and powerful ZynAddSubFX multitimbral standalone
synthesizer, but with improved realtime capacities. Yoshimi can use
either ALSA or JACK for both Audio and MIDI, the default now being JACK

%prep
%setup -q

%build
cd src
cmake . 	
%cmake -DCMAKE_CXX_FLAGS="${RPM_OPT_FLAGS} -fPIC" -DFLTK_INCLUDE_DIR=%{_includedir}/Fl -DCMAKE_INSTALL_PREFIX=%{_prefix}
%make

%install
cd src
%makeinstall_std

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
%{_bindir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop






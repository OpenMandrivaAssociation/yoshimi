%define debug_package %{nil}

Name:           yoshimi
Summary:        ZynAddSubFX with improved RT capacities

Version:        1.2.1
Release:        3

Source:         http://sourceforge.net/projects/yoshimi/files/1.2/%{name}-%{version}.tar.bz2
URL:            http://yoshimi.sourceforge.net
License:        GPLv2
Group:          Sound
BuildRequires:  cmake libalsa-devel jackit-devel fltk-devel zlib-devel
BuildRequires:  fftw-devel mxml-devel sndfile-devel fontconfig-devel glu-devel
BuildRequires:  boost-devel
BuildRequires:  desktop-file-utils

%description
Yoshimi is the legendary and powerful ZynAddSubFX multitimbral standalone
synthesizer, but with improved realtime capacities. Yoshimi can use
either ALSA or JACK for both Audio and MIDI, the default now being JACK

%prep
%setup -q

%build
cd src
cmake . -DCMAKE_INSTALL_PREFIX=%{_prefix}
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






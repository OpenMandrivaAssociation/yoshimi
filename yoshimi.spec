%global	debug_package %{nil}

Summary:	ZynAddSubFX with improved RT capacities
Name:		yoshimi
Version:	2.3.3.3
Release:	1
Url:		https://yoshimi.sourceforge.io/
License:	GPLv2
Group:          Sound
Source0:	https://github.com/Yoshimi/yoshimi/archive/%{name}-%{version}.tar.gz
Patch0:		yoshimi-2.3.3.3-fix-build-with-fltk14.patch
BuildRequires:	cmake 
BuildRequires:	desktop-file-utils
BuildRequires:	fltk-fluid
BuildRequires:	boost-devel
BuildRequires:	fltk-devel 
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(fontconfig) 
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(lv2)
# mxml4 not supported yet
BuildRequires:	pkgconfig(mxml)
BuildRequires:	pkgconfig(readline)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(zlib)

%description
Yoshimi is the legendary and powerful ZynAddSubFX multitimbral standalone
synthesizer, but with improved realtime capacities. Yoshimi can use
either ALSA or JACK for both Audio and MIDI, the default now being JACK.

%files
%doc %{_datadir}/doc/%{name}/
%{_bindir}/%{name}
%{_libdir}/lv2/%{name}.lv2/
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/%{name}.metainfo.xml
%{_datadir}/pixmaps/%{name}.png
%{_iconsdir}/hicolor/*/apps/%{name}.*
%{_iconsdir}/hicolor/scalable/apps/%{name}_alt.svg
%{_mandir}/man1/%{name}.1.*

#-----------------------------------------------------------------------------

%prep
%autosetup -p1


%build
cd src
%cmake  \
	-DCMAKE_CXX_FLAGS="%{optflags} -fPIC" \
	-DFLTK_INCLUDE_DIR=%{_includedir}/FL \
	-DCMAKE_INSTALL_PREFIX=%{_prefix}
%make_build


%install
cd src
%make_install -C build

# Drop hidden files
rm -f %{buildroot}%{_datadir}/%{name}/banks/*/.bankdir

# We pick the example files as doc: avoid a zillion of "files-duplicate" rpmllint warnings
rm -rf %{buildroot}%{_datadir}/%{name}/examples/*
rm -rf %{buildroot}%{_datadir}/doc/%{name}/Yoshimi_License_History.txt

# Fix perms
chmod -R 755 %{buildroot}%{_datadir}/%{name}/banks
chmod -R 755 %{buildroot}%{_datadir}/%{name}/presets
chmod a-X %{buildroot}%{_datadir}/%{name}/banks/*/*
chmod a-X %{buildroot}%{_datadir}/%{name}/presets/*

# Fix .desktop file
desktop-file-edit \
	--remove-key="Version" \
	--add-category="X-OpenMandriva-Sound" \
	%{buildroot}%{_datadir}/applications/%{name}.desktop

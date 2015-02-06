Summary:	Extra drum kits for the Hydrogen drum machine
Name:		hydrogen-drumkits
Version:	0.9.3.20070703
Release:	7
License:	GPLv2+
Group:		Sound
Url:		http://www.hydrogen-music.org
Source0:	http://ftp.de.debian.org/debian/pool/main/h/hydrogen-drumkits/%{name}_%{version}.orig.tar.gz
Source1:	Makefile.hydrogen-drumkits
BuildArch:	noarch

%description
Hydrogen is an advanced drum machine for GNU/Linux. It's main goal is to bring
professional yet simple and intuitive pattern-based drum programming.

%files
%{_datadir}/hydrogen/data/drumkits/*
%{_datadir}/hydrogen/data/demo_songs/*

#----------------------------------------------------------------------------

%prep
%setup -q
install -m 644 %{SOURCE1} ./Makefile
perl -pi -e 's,KITS_DIR=.*,KITS_DIR=%{buildroot}%{_datadir}/hydrogen/data/drumkits,g' ./Makefile
perl -pi -e 's,SONG_DIR=.*,SONG_DIR=%{buildroot}%{_datadir}/hydrogen/data/demo_songs,g' ./Makefile

%build

%install
make unpack
chmod 0755 %{buildroot}%{_datadir}/hydrogen/data/drumkits/*


%define name    hydrogen-drumkits
%define version 0.9.3.20070703
%define release %mkrel 4

Summary:	Extra drum kits for the Hydrogen drum machine
Name:           %{name}
Version:        %{version}
Release:        %{release}
License:	GPLv2+
Group:		Sound
URL:		http://www.hydrogen-music.org
Source0:	http://ftp.de.debian.org/debian/pool/main/h/hydrogen-drumkits/%{name}_%{version}.orig.tar.gz
Source1:	Makefile.hydrogen-drumkits
BuildRoot:	%_tmppath/%{name}-buildroot

%description
Hydrogen is an advanced drum machine for GNU/Linux. It's main goal is to bring
professional yet simple and intuitive pattern-based drum programming.

%prep
%setup -q
install -m 644 %{SOURCE1} ./Makefile
perl -pi -e 's,KITS_DIR=.*,KITS_DIR=%{buildroot}%{_datadir}/hydrogen/data/drumkits,g' ./Makefile
perl -pi -e 's,SONG_DIR=.*,SONG_DIR=%{buildroot}%{_datadir}/hydrogen/data/demo_songs,g' ./Makefile

%build

%install
%__rm -rf %{buildroot}
make unpack
chmod 0755 %{buildroot}%{_datadir}/hydrogen/data/drumkits/*

%clean
%__rm -rf %buildroot

%files
%defattr(-,root,root)
%{_datadir}/hydrogen/data/drumkits/*
%{_datadir}/hydrogen/data/demo_songs/*


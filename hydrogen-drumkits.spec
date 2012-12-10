%define name    hydrogen-drumkits
%define version 0.9.3.20070703
%define release %mkrel 5

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



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.3.20070703-5mdv2011.0
+ Revision: 619493
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.9.3.20070703-4mdv2010.0
+ Revision: 429482
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.9.3.20070703-3mdv2009.0
+ Revision: 247130
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Oct 17 2007 Adam Williamson <awilliamson@mandriva.org> 0.9.3.20070703-1mdv2008.1
+ Revision: 99479
- import hydrogen-drumkits



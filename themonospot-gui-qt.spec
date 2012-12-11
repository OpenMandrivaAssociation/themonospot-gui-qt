Summary: Qt application to use themonospot (multimedia files parser/editor)
Name: themonospot-gui-qt
Version: 0.1.3
Release: %mkrel 3
License: GPLv2
Group: Video
Source: http://www.integrazioneweb.com/repository/SOURCES/themonospot-gui-qt-%{version}.tar.gz
Patch0: themonospot-gui-qt-0.1.3-drop-invalide-desktop-entry.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL: http://www.integrazioneweb.com/themonospot

BuildRequires: mono-devel
BuildRequires: qyoto-devel
BuildRequires: themonospot-base-devel



%description
themonospot-gui-qt is a Mono framework application to create a
graphic frontend to use themonospot base component and his plugins.

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x
make

%install
rm -fr %{buildroot}
%makeinstall_std


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc copying.gpl
%{_bindir}/themonospot-qt
%{_libdir}/themonospot/%{name}.exe
%{_datadir}/pixmaps/themonospot-qt.png
%{_datadir}/applications/themonospot-qt.desktop


%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.3-3mdv2011.0
+ Revision: 615210
- the mass rebuild of 2010.1 packages

* Mon Apr 19 2010 Funda Wang <fwang@mandriva.org> 0.1.3-2mdv2010.1
+ Revision: 536568
- fix build
- drop invalid desktop entry

* Sat Jan 02 2010 Armando Basile <hman@mandriva.org> 0.1.3-1mdv2010.1
+ Revision: 485147
- removed GAC use
  This line, and following ones, will be ignored--
  file SPECS/themonospot-gui-qt.spec modified
  file SOURCES/themonospot-gui-qt-0.1.3.tar.gz addedC use

* Thu Dec 24 2009 Armando Basile <hman@mandriva.org> 0.1.2-1mdv2010.1
+ Revision: 482035
- first public release of Qt gui application for new Themonospot suite
- create themonospot-gui-qt


Summary: Qt application to use themonospot (multimedia files parser/editor)
Name: themonospot-gui-qt
Version: 0.1.3
Release: %mkrel 2
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

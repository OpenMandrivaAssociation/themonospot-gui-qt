# mono...
%define debug_package %{nil}

Summary: Qt application to use themonospot (multimedia files parser/editor)
Name:    themonospot-gui-qt
Version: 0.1.3
Release: 5
License: GPLv2
Group:   Video
Source:  http://www.integrazioneweb.com/repository/SOURCES/themonospot-gui-qt-%{version}.tar.gz
Patch0:  themonospot-gui-qt-0.1.3-drop-invalide-desktop-entry.patch
Url:     https://www.integrazioneweb.com/themonospot

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
%makeinstall_std

%files
%doc copying.gpl
%{_bindir}/themonospot-qt
%{_libdir}/themonospot/%{name}.exe
%{_datadir}/pixmaps/themonospot-qt.png
%{_datadir}/applications/themonospot-qt.desktop

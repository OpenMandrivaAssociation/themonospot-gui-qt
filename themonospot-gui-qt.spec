Summary   : Qt application to use themonospot (multimedia files parser/editor)
Name      : themonospot-gui-qt
Version   : 0.1.3
Release   : %mkrel 1
License   : GPLv2
Group     : Video
Source    : http://www.integrazioneweb.com/repository/SOURCES/themonospot-gui-qt-%{version}.tar.gz
BuildRoot : %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL       : http://www.integrazioneweb.com/themonospot

#BuildArch : noarch

BuildRequires: mono-devel
BuildRequires: qyoto-devel
BuildRequires: themonospot-base-devel



%description
themonospot-gui-qt is a Mono framework application to create a
graphic frontend to use themonospot base component and his plugins.

%prep
%setup -q

%build
%configure2_5x
%make

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
* Wed Dec 30 2009 Armando Basile <hmandevteam@gmail.com> 0.1.3-1mdv2010.1
- removed GAC use

* Mon Dec 14 2009 Armando Basile <hmandevteam@gmail.com> 0.1.2-1mdv2010.1
- first release of new Qt application to use themonospot
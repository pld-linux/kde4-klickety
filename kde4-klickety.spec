%define		_state		stable
%define		orgname		klickety
%define		qtver		4.8.0

Summary:	Klickety
Name:		kde4-%{orgname}
Version:	4.14.3
Release:	2
License:	GPL
Group:		X11/Applications/Games
Source0:	http://download.kde.org/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	6075fdc45807e7b475a3be7c96a10650
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-libkdegames-devel >= %{version}
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
Obsoletes:	kde4-kdegames-%{orgname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Klickety.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT/var/games
# remove locolor icons
rm -rf $RPM_BUILD_ROOT%{_iconsdir}/locolor

%find_lang %{orgname}	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/klickety
%{_desktopdir}/kde4/klickety.desktop
%{_desktopdir}/kde4/ksame.desktop
%{_datadir}/apps/kconf_update/klickety-2.0-inherit-ksame-highscore.pl
%{_datadir}/apps/kconf_update/klickety.upd
%{_datadir}/apps/klickety
%{_iconsdir}/hicolor/*x*/apps/klickety.png
%{_iconsdir}/hicolor/*x*/apps/ksame.png

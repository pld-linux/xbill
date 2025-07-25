Summary:	Stop Bill from loading his OS into all the computers
Summary(pl.UTF-8):	Powstrzymaj Billa przed instalowaniem jego systemu na wszystkich komputerach
Name:		xbill
Version:	2.0
Release:	21
License:	MIT
Group:		X11/Applications/Games
Source0:	ftp://ftp.x.org/contrib/games/%{name}-%{version}.tgz
# Source0-md5:	132e4b340618924b6a41ec5ec106ca32
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-c++.patch
Patch1:		%{name}-imake.patch
Patch2:		%{name}-FHS.patch
BuildRequires:	libstdc++-devel
BuildRequires:	xorg-cf-files
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xorg-util-imake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The xbill game tests your reflexes as you seek out and destroy all
forms of Bill, establish new operating systems and boldly go where no
geek has gone before. Xbill has become an increasingly attractive
option as the Linux Age progresses, and it is very popular at Red Hat.

%description -l pl.UTF-8
Gra xbill sprawdza refleks przy wyłapywaniu i niszczeniu wszelkich
form Billa, instalowaniu nowych systemów operacyjnych oraz docieraniu
tam, gdzie nikt wcześniej nie dotarł. Xbill stawał się ciągle coraz
bardziej przyciągający w miarę postępu Ery Linuksa, jest także bardzo
popularny w Red Hacie.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
xmkmf
%{__make} \
	CXX="%{__cxx}" \
	CXXDEBUGFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions -fno-implicit-templates" \
	XBILL_DIR=%{_datadir}/xbill/

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install install.man \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_bindir} \
	MANPATH=%{_mandir} \
	XBILL_DIR=%{_datadir}/xbill/

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README README.Ports ChangeLog
%attr(2755,root,games) %{_bindir}/xbill
%attr(775,root,games) %dir /var/games/xbill
%attr(664,root,games) %config(noreplace) %verify(not md5 mtime size) /var/games/xbill/scores
%{_mandir}/man1/xbill.1*
%{_datadir}/xbill
%{_desktopdir}/xbill.desktop
%{_pixmapsdir}/*

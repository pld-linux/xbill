Summary:	Stop Bill from loading his OS into all the computers
Summary(pl):	Powstrzymaj Billa przed instalowaniem jego systemu na wszystkich komputerach
Name:		xbill
Version:	2.0
Release:	17
License:	MIT
Group:		X11/Applications/Games
Group(cs):	X11/Aplikace/Hry
Group(da):	X11/Programmer/Spil
Group(de):	X11/Applikationen/Spiele
Group(es):	X11/Aplicaciones/Juegos
Group(fr):	X11/Applications/Jeux
Group(is):	X11/Forrit/Leikir
Group(it):	X11/Applicazioni/Giochi
Group(ja):	X11/•¢•◊•Í•±°º•∑•Á•Û/•≤°º•‡
Group(no):	X11/Applikasjoner/Spill
Group(pl):	X11/Aplikacje/Gry
Group(pt):	X11/AplicaÁıes/Jogos
Group(ru):	X11/“…Ãœ÷≈Œ…—/È«“Ÿ
Group(sl):	X11/Programi/Igre
Group(sv):	X11/Till‰mpningar/Spel
Group(uk):	X11/“…ÀÃ¡ƒŒ¶ “œ«“¡Õ…/∂«“…
Source0:	ftp://ftp.x.org/contrib/games/%{name}-%{version}.tgz
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-c++.patch
Patch1:		%{name}-imake.patch
Patch2:		%{name}-FHS.patch
Icon:		xbill.xpm
BuildRequires:	XFree86-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
The xbill game tests your reflexes as you seek out and destroy all
forms of Bill, establish new operating systems and boldly go where no
geek has gone before. Xbill has become an increasingly attractive
option as the Linux Age progresses, and it is very popular at Red Hat.

%description -l pl
Gra xbill sprawdza refleks przy wy≥apywaniu i niszczeniu wszelkich
form Billa, instalowaniu nowych systemÛw operacyjnych oraz docieraniu
tam, gdzie nikt wcze∂niej nie dotar≥. Xbill stawa≥ siÍ ci±gle coraz
bardziej przyci±gaj±cy w miarÍ postÍpu Ery Linuksa, jest takøe bardzo
popularny w Red Hacie.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
xmkmf
%{__make} \
	CXXDEBUGFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions -fno-implicit-templates"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Games,%{_pixmapsdir}}

%{__make} DESTDIR=$RPM_BUILD_ROOT install install.man

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

gzip -9nf README README.Ports ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(2755,root,games) %{_bindir}/xbill
%attr(775,root,games) %dir /var/games/xbill
%attr(664,root,games) %config(noreplace) %verify(not size mtime md5) /var/games/xbill/scores
%{_mandir}/man1/*
%{_libdir}/xbill
%{_applnkdir}/Games/xbill.desktop
%{_pixmapsdir}/*

Summary:	Stop Bill from loading his OS into all the computers
Name:		xbill
Version:	2.0
Release:	15
License:	MIT
Group:		X11/Applications/Games
Group(de):	X11/Applikationen/Spiele
Group(pl):	X11/Aplikacje/Gry
Source0:	ftp://ftp.x.org/contrib/games/%{name}-%{version}.tgz
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-c++.patch
Patch1:		%{name}-imake.patch
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

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
xmkmf
%{__make} \
	CXXDEBUGFLAGS="%{?debug:-g -O}%{!?debug:$RPM_OPT_FLAGS} \
	-fno-rtti -fno-exceptions -fno-implicit-templates"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Games,%{_pixmapsdir}}

%{__make} DESTDIR=$RPM_BUILD_ROOT install install.man

( cd $RPM_BUILD_ROOT
  install -d .%{_libdir}/xbill
  for i in bitmaps pixmaps
  do
	mv -f ./var/lib/games/xbill/$i .%{_libdir}/xbill/$i
	ln -s ../../../..%{_libdir}/xbill/$i ./var/lib/games/xbill/$i
  done
)

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

gzip -9nf README README.Ports ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(2755,root,games) %{_bindir}/xbill
%attr(775,root,games)  %dir /var/lib/games/xbill
%attr(664,root,games)  %config /var/lib/games/xbill/scores
/var/lib/games/xbill/bitmaps
/var/lib/games/xbill/pixmaps
%{_mandir}/man1/*
%{_libdir}/xbill
%{_applnkdir}/Games/xbill.desktop
%{_pixmapsdir}/*

Summary:	Stop Bill from loading his OS into all the computers
Name:		xbill
Version:	2.0
Release:	7
Copyright:	MIT
Group:		X11/Games
Group(pl):	X11/Gry
Source0:	ftp://ftp.x.org/contrib/games/%{name}-%{version}.tgz
Patch0:		xbill-2.0-rh.patch
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
%patch -p1

%build
xmkmf
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install install.man

( cd $RPM_BUILD_ROOT
  install -d .%{_libdir}/xbill
  for i in bitmaps pixmaps
  do
    mv ./var/lib/games/xbill/$i .%{_libdir}/xbill/$i
    ln -s ../../../..%{_libdir}/xbill/$i ./var/lib/games/xbill/$i
  done

install -d .%{_sysconfdir}/X11/wmconfig
cat > .%{_sysconfdir}/X11/wmconfig/xbill <<EOF
xbill name "xbill"
xbill description "Save the world"
xbill group Games/Video
xbill exec "xbill &"
EOF
)

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(2755,root,games) %{_prefix}/X11R6/bin/xbill
%attr(775,root,games)	%dir /var/lib/games/xbill
%attr(664,root,games)	%config /var/lib/games/xbill/scores
/var/lib/games/xbill/bitmaps
/var/lib/games/xbill/pixmaps
%{_libdir}/xbill
%config %{_sysconfdir}/X11/wmconfig/xbill

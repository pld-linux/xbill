Summary:	Stop Bill from loading his OS into all the computers.
Name:		xbill
Version:	2.0
Release:	6
Copyright:	MIT
Group:		Amusements/Games
Source:		ftp://ftp.x.org/contrib/games/%{name}-%{version}.tgz
Patch:		xbill-2.0-rh.patch
BuildRoot:	/tmp/%{name}-%{version}-root

%description
The xbill game tests your reflexes as you seek out and destroy all forms
of Bill, establish new operating systems and boldly go where no geek has
gone before.  Xbill has become an increasingly attractive option as the
Linux Age progresses, and it is very popular at Red Hat.

%prep
%setup -q
%patch -p1

%build
xmkmf
make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install install.man

( cd $RPM_BUILD_ROOT
  mkdir -p ./usr/lib/xbill
  for i in bitmaps pixmaps
  do
    mv ./var/lib/games/xbill/$i ./usr/lib/xbill/$i
    ln -s ../../../../usr/lib/xbill/$i ./var/lib/games/xbill/$i
  done

  mkdir -p ./etc/X11/wmconfig
  cat > ./etc/X11/wmconfig/xbill <<EOF
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
%attr(2755,root,games)	/usr/X11R6/bin/xbill
%attr(775,root,games)	%dir /var/state/games/xbill
%attr(664,root,games)	%config /var/state/games/xbill/scores
/var/state/games/xbill/bitmaps
/var/state/games/xbill/pixmaps
/usr/lib/xbill
%config /etc/X11/wmconfig/xbill

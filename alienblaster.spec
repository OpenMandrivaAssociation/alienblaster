%define	name	alienblaster
%define	version 1.1.0
%define release	10
%define	Summary	Action-loaded 2D arcade shooter game

Version:	%{version}
Summary:	%{Summary}
Name:		%{name}
Release:	%mkrel %{release}
License:	GPL
Group:		Games/Arcade
Source0:	http://www.informatik.uni-bremen.de/~schwardt/alienblaster/%{name}-%{version}.tar.bz2
Source11:	%{name}-16x16.png
Source12:	%{name}-32x32.png
Source13:	%{name}-48x48.png
URL:		http://www.schwardtnet.de/alienblaster/
BuildRequires:	SDL_mixer-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Alien Blaster is an action-loaded 2D arcade shooter game. Your mission in the 
game is simple: stop the invasion of the aliens by blasting them. 
Simultaneous two-player mode is available.

%prep
%setup -q -n %{name}

%build
%make OPTIMIZATION="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

install -m755 alienBlaster -D $RPM_BUILD_ROOT%{_gamesbindir}/alienBlaster.real

cat > $RPM_BUILD_ROOT%{_gamesbindir}/alienBlaster << EOF
#!/bin/bash
cd %{_gamesdatadir}/%{name}
%{_gamesbindir}/alienBlaster.real \$@
EOF
chmod 755 $RPM_BUILD_ROOT%{_gamesbindir}/alienBlaster

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Alien Blaster
Comment=%{Summary}
Exec=%{_gamesbindir}/alienBlaster
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;ArcadeGame;
EOF

mkdir -p $RPM_BUILD_ROOT%{_gamesdatadir}/%{name}
cp -R images sound cfg $RPM_BUILD_ROOT%{_gamesdatadir}/%{name}

install -m644 %{SOURCE11} -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

%if %mdkversion < 200900
%post
%update_menus
%endif
 
%if %mdkversion < 200900
%postun
%update_menus 
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
%doc README CHANGELOG AUTHORS VERSION
%attr(0755,root,games) %{_gamesbindir}/*
%{_gamesdatadir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png


%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-9mdv2011.0
+ Revision: 616559
- the mass rebuild of 2010.0 packages

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 1.1.0-8mdv2010.0
+ Revision: 436638
- rebuild

* Sun Apr 05 2009 Funda Wang <fwang@mandriva.org> 1.1.0-7mdv2009.1
+ Revision: 364137
- fix icon name

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 1.1.0-6mdv2009.0
+ Revision: 218435
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Thu Jan 03 2008 Thierry Vignaud <tv@mandriva.org> 1.1.0-6mdv2008.1
+ Revision: 141886
- drop X-MandrivaLinux-MoreApplications-Games-Arcade category
- drop old menu

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 1.1.0-5mdv2008.1
+ Revision: 135819
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import alienblaster


* Mon Sep 04 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.1.0-5mdv2007.0
- XDG

* Wed Jun 28 2006  Lenny Cartier <lenny@mandriva.com> 1.1.0-4mdv2007.0
- rebuild

* Fri Aug 19 2005 Per Ã˜yvind Karlsen <pkarlsen@mandriva.com> 1.1.0-3mdk
- buildrequires
- compile with $RPM_OPT_FLAGS
- add icons
- %%mkrel
- drop 'LICENSE' as package is GPL and 'INSTALL' as it just cointains
  some easy install instructions which really isn't very useful
  for a binary package..
- cosmetics

* Tue Aug 31 2004 Michael Scherer <misc@mandrake.org> 1.1.0-2mdk 
- fix inclusion of datafile

* Fri Aug 20 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.1.0-1mdk
- new

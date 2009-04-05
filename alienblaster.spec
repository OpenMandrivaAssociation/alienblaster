%define	name	alienblaster
%define	version 1.1.0
%define	release	7
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

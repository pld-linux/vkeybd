#
# Conditional build
%bcond_with	ladcca	# with LADCCA support
#
Summary:	Virtual Keyboard
Summary(pl.UTF-8):	Wirtualne klawisze
Name:		vkeybd
Version:	0.1.18b
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://ftp.suse.com/pub/people/tiwai/vkeybd/%{name}-%{version}.tar.bz2
# Source0-md5:	2b5c46e753aed2729147e8aa688b08c7
Source1:	%{name}rc
Source2:	%{name}.desktop
Patch0:		%{name}-Makefile.patch
URL:		http://www.alsa-project.org/~tiwai/alsa.html
BuildRequires:	alsa-lib-devel
%{?with_ladcca:BuildRequires:	ladcca-devel >= 0.4.0}
BuildRequires:	tk-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a virtual keyboard for AWE, MIDI and ALSA drivers. It's a
simple fake of a MIDI keyboard.

%description -l pl.UTF-8
Wirtualne klawisze dla sterowników AWE, MIDI i ALSA. Program "udaje"
klawisze syntezatora MIDI.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	COPTFLAGS="%{rpmcflags} -Wall" \
	XLIB="-lX11" \
	XINC= \
	%{?with_ladcca:USE_LADCCA=1}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install-all \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/vkeybd
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}
mv $RPM_BUILD_ROOT%{_pixmapsdir}/vkeybd_48x48.png $RPM_BUILD_ROOT%{_pixmapsdir}/vkeybd.png
rm -f $RPM_BUILD_ROOT%{_pixmapsdir}/vkeybd_*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/sftovkb
%attr(755,root,root) %{_bindir}/vkeybd
%{_mandir}/man1/vkeybd.1*
%{_datadir}/vkeybd
%{_desktopdir}/vkeybd.desktop
%{_pixmapsdir}/vkeybd.png
